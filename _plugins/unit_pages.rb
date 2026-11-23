# _plugins/unit_pages.rb
#
# Lets unit pages (layout: unit) be written as near-plain Markdown that
# previews well in VS Code. Just before Liquid renders the page, this hook
# rewrites the page's Markdown source:
#
#   ## Logistic Regression
#     -> numbered section heading "5.2 Logistic Regression", id "logistic-regression"
#        (add {.unnumbered} to the end of a heading to skip numbering)
#
#   #### Notes (draft)
#     -> "Notes" label with a draft tag
#
#   - **Homework** [Recognizing Digits](./digits-student.ipynb): Pick the best $k$.
#     -> a card: role badge, title, description, buttons.
#        Roles (and their colors, unit-map pills) are listed in
#        _data/unit_roles.yml.
#        The link decides the card type:
#          .ipynb            notebook   View / Download / Open in Colab
#          .md page          handout / notes / assignment page, plus a PDF
#                            button when a same-name .pdf sits next to it
#          .pdf              PDF
#          .csv .json ...    dataset    Download
#          .html             interactive
#          anything else     link
#        No link: "- **Homework** k-d tree packet: handed out in class."
#        A description starting "Coming soon" gives a dashed placeholder card.
#        With `show_keys: true` (set only in _config.local.yml), cards also get
#        a Key button when an answer key sits next to the file
#        (x_Key.ipynb, x-key.ipynb, x_teacher.ipynb, x_SOLUTIONS.ipynb,
#        x_Student -> x_Key, worksheet -> key, ...).
#
#   [text](./file.ipynb), [text](./data.csv), ![](./fig.png)
#     -> relative links resolved against the Markdown file's own folder
#        (.ipynb links go to the notebook's web view).
#
# It also inserts the unit map before the first section and fills
# page.unit_sections for _includes/unit-map.html.
#
# Cards themselves are rendered by _includes/unit-material.html, so their
# look is edited there, not here.

module UnitPages
  DEFAULT_ROLES = [
    { "key" => "demo", "label" => "Demo", "aliases" => ["demo"] },
    { "key" => "classwork", "label" => "In class", "aliases" => ["in class", "classwork"] },
    { "key" => "hw", "label" => "Homework", "aliases" => ["homework", "hw"] },
    { "key" => "demo-hw", "label" => "Demo + HW", "aliases" => ["demo + hw"], "counts_as" => %w[demo hw] },
  ].freeze

  DATA_EXTS = %w[.csv .tsv .json .zip .txt .xlsx .parquet .gz .pkl].freeze
  PAGE_KINDS = { "handouts" => "Handout", "notes" => "Notes", "assignments" => "Assignment" }.freeze

  CARD_START = /\A\s{0,3}[-*]\s+\*\*(?<role>[^*]+)\*\*\s*(?<rest>.*)\z/

  module_function

  def roles(site)
    list = site.data["unit_roles"]
    list.is_a?(Array) && !list.empty? ? list : DEFAULT_ROLES
  end

  # "homework" -> role hash, for every alias (and label) of every role.
  def alias_map(site)
    roles(site).each_with_object({}) do |r, h|
      (Array(r["aliases"]) + [r["label"].to_s]).each { |a| h[a.to_s.strip.downcase] = r }
    end
  end

  # GitHub-style heading slug (what VS Code uses for #anchor completion).
  def slug(text)
    text.downcase.gsub(/<[^>]+>/, "").gsub(/[^\p{Alnum}\s-]/u, "").strip.gsub(/\s/, "-")
  end

  # Links that point off-site or within the page: left alone.
  def external?(target)
    target.match?(%r{\A(?:[a-z][a-z0-9+.-]*:|//|#|\{\{)}i)
  end

  # Repo-relative path for a link target. Relative targets resolve against the
  # page's source folder. Site-absolute targets ("/notebooks/...", possibly with
  # the baseurl in front) are already repo paths; jekyll-relative-links turns
  # "./file.ipynb" and "./page.md" into that form before this hook runs.
  def resolve(target, source_dir, baseurl = "")
    path, frag = target.split("#", 2)
    if path.start_with?("/")
      path = path.delete_prefix(baseurl) unless baseurl.empty?
      return [path.sub(%r{\A/}, ""), frag]
    end
    full = File.expand_path(path, "/" + source_dir).sub(%r{\A/}, "")
    full += "/" if path.end_with?("/") && !full.end_with?("/")
    [full, frag]
  end

  def notebook_entry(site, repo_path)
    site.data.dig("notebooks", "by_path", repo_path)
  end

  # Exact-case file check (macOS file systems ignore case, Linux doesn't).
  def exists?(site, repo_path)
    full = site.in_source_dir(repo_path)
    File.file?(full) && Dir.children(File.dirname(full)).include?(File.basename(full))
  rescue Errno::ENOENT
    false
  end

  # Site URL (without baseurl) for a resolved repo path.
  def url_for(site, repo_path, frag = nil)
    url =
      if repo_path.end_with?(".ipynb") && (nb = notebook_entry(site, repo_path))
        "/" + nb["html_path"]
      else
        "/" + repo_path
      end
    frag ? "#{url}##{frag}" : url
  end

  # A rendered page (handout, notes, ...) by its URL or its source path.
  def page_for(site, repo_path)
    @pages_by_url = nil if @pages_site != site.object_id || @pages_count != site.pages.size
    @pages_site, @pages_count = site.object_id, site.pages.size
    @pages_by_url ||= site.pages.each_with_object({}) do |p, h|
      h[p.url] = p
      h[p.relative_path] = p
    end
    @pages_by_url["/" + repo_path] || @pages_by_url[repo_path] ||
      @pages_by_url["/" + repo_path.chomp("/") + "/"]
  end

  # Answer key next to a file, if any: repo path of the key, or nil.
  def key_for(site, repo_path, exts)
    dir = File.dirname(repo_path)
    base = File.basename(repo_path, File.extname(repo_path))
    candidates = [
      "#{base}_Key", "#{base}-Key", "#{base}_key", "#{base}-key", "#{base}_teacher",
      "#{base}_SOLUTIONS", "#{base}_solutions",
      base.sub(/student/i) { |s| s == "student" ? "key" : "Key" },
      base.sub(/([_-]?)student.*\z/i) { "#{Regexp.last_match(1)}Key" },
      base.sub(/worksheet/i, "key"),
      base.sub(/[_-]?student\z/i, ""),
    ].uniq - [base, ""]
    candidates.each do |c|
      exts.each do |ext|
        path = dir == "." ? "#{c}#{ext}" : "#{dir}/#{c}#{ext}"
        return path if exists?(site, path)
      end
    end
    nil
  end

  # Levenshtein distance, for "did you mean" on misspelled roles.
  def edit_distance(a, b)
    prev = (0..b.length).to_a
    a.each_char.with_index(1) do |ca, i|
      cur = [i]
      b.each_char.with_index(1) do |cb, j|
        cur << [prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca == cb ? 0 : 1)].min
      end
      prev = cur
    end
    prev.last
  end

  # Lines taken by the front matter, so warnings can give real file line numbers.
  def front_matter_lines(page)
    src = File.read(page.site.in_source_dir(page.relative_path))
    m = src.match(/\A---\s*\n.*?\n?^(?:---|\.\.\.)\s*$\n?/m)
    m ? m[0].count("\n") : 0
  rescue StandardError
    0
  end

  def liquid_str(s)
    s.to_s.gsub("\\", "\\\\\\\\").gsub('"', '\\"')
  end

  # One card list item -> capture/include Liquid line.
  def card_line(site, source_dir, role_key, rest)
    label = rest
    target = nil
    blurb = ""
    if (m = rest.match(/\A\[(?<label>[^\]]+)\]\((?<target>[^)\s]+)\)\s*(?:[:–—-]\s*)?(?<blurb>.*)\z/m))
      label, target, blurb = m[:label], m[:target], m[:blurb]
    elsif (m = rest.match(/\A(?<label>[^:]+?)\s*:\s*(?<blurb>.*)\z/m))
      label, blurb = m[:label], m[:blurb]
    end

    baseurl = site.config["baseurl"].to_s
    show_keys = site.config["show_keys"]
    params = { "role" => role_key }
    key_path = nil

    if target.nil?
      params["kind"] = "item"
    elsif external?(target)
      params["kind"] = "link"
      params["url"] = target
    else
      repo_path, frag = resolve(target, source_dir, baseurl)
      ext = File.extname(repo_path).downcase
      pg = (ext.empty? || ext == ".md") ? page_for(site, repo_path) : nil
      if ext == ".ipynb"
        params["kind"] = "notebook"
        params["path"] = repo_path
        key_path = key_for(site, repo_path, [".ipynb"]) if show_keys
      elsif pg
        src = pg.relative_path
        params["kind"] = "page"
        params["kind_label"] = PAGE_KINDS.fetch(src.split("/").first, "Page")
        params["url"] = frag ? "#{pg.url}##{frag}" : pg.url
        pdf = src.sub(/\.md\z/, ".pdf")
        params["pdf"] = "/" + pdf if pdf != src && exists?(site, pdf)
        key_path = key_for(site, src, [".pdf", ".md"]) if show_keys
      elsif ext == ".pdf"
        params["kind"] = "pdf"
        params["url"] = url_for(site, repo_path, frag)
        key_path = key_for(site, repo_path, [".pdf"]) if show_keys
      else
        params["kind"] = DATA_EXTS.include?(ext) ? "dataset" : (ext == ".html" ? "interactive" : "link")
        params["url"] = url_for(site, repo_path, frag)
      end
    end
    params["kind"] = "soon" if blurb.match?(/\Acoming soon/i)
    params["key_url"] = url_for(site, key_path) if key_path

    attrs = params.map { |k, v| %(#{k}="#{liquid_str(v)}") }.join(" ")
    "{% capture uc_label %}#{label.strip}{% endcapture %}" \
      "{% capture uc_blurb %}#{blurb.strip}{% endcapture %}" \
      "{% include unit-material.html #{attrs} label=uc_label blurb=uc_blurb %}"
  end

  # Rewrite relative links/images in a line of prose.
  def rewrite_links(line, site, source_dir)
    baseurl = site.config["baseurl"].to_s
    line.gsub(/(\]\()([^)\s]+)(\))/) do
      open, target, close = Regexp.last_match(1), Regexp.last_match(2), Regexp.last_match(3)
      if external?(target) || target.end_with?(".md") || target.include?(".md#")
        "#{open}#{target}#{close}"
      elsif target.start_with?("/") && !target.split("#").first.end_with?(".ipynb")
        "#{open}#{target}#{close}"   # already a site URL (e.g. from jekyll-relative-links)
      else
        repo_path, frag = resolve(target, source_dir, baseurl)
        "#{open}#{baseurl}#{url_for(site, repo_path, frag)}#{close}"
      end
    end
  end

  def transform(page, payload)
    site = page.site
    role_by_alias = alias_map(site)
    role_names = roles(site).map { |r| r["label"] }.join(", ")
    source_dir = File.dirname(page.relative_path)
    unit_no = page.data["unit_number"] ||
              File.basename(source_dir)[/\A(\d+)-/, 1].to_i
    lines = page.content.split("\n", -1)
    out = []
    sections = []
    current = nil
    in_fence = false
    map_inserted = false
    i = 0

    while i < lines.length
      line = lines[i]

      if line.match?(/\A\s*(```|~~~)/)
        in_fence = !in_fence
        out << line
        i += 1
        next
      end
      if in_fence
        out << line
        i += 1
        next
      end

      # Section heading
      if (m = line.match(/\A##\s+(?<title>[^#].*?)\s*\z/))
        title = m[:title]
        unnumbered = title.sub!(/\s*\{\s*\.unnumbered\s*\}\z/, "")
        id = slug(title)
        unless map_inserted
          out << "{% include unit-map.html %}" << ""
          map_inserted = true
        end
        if unnumbered
          out << "## #{title} {##{id}}"
          current = nil
        else
          num = "#{unit_no}.#{sections.length + 1}"
          current = { "num" => num, "id" => id, "title" => title, "notes" => false, "counts" => {} }
          sections << current
          out << %(## <span class="unit-section__num">#{num}</span> #{title} {##{id}})
        end
        i += 1
        next
      end

      # "#### Notes" / "#### Notes (draft)"
      if (m = line.match(/\A####\s+Notes\s*(?<draft>\(draft\))?\s*\z/i))
        current["notes"] = true if current
        out << (m[:draft] ? %(#### Notes <span class="draft-tag">draft</span>) : "#### Notes")
        i += 1
        next
      end

      # Card list item (+ indented continuation lines)
      if (m = line.match(CARD_START)) && (role = role_by_alias[m[:role].strip.downcase])
        text = [m[:rest]]
        j = i + 1
        while j < lines.length && lines[j].match?(/\A\s+\S/) && !lines[j].match?(CARD_START)
          text << lines[j].strip
          j += 1
        end
        out << card_line(site, source_dir, role["key"], text.join(" "))
        Array(role["counts_as"] || role["key"]).each do |k|
          current["counts"][k] = current["counts"].fetch(k, 0) + 1 if current
        end
        i = j
        next
      end

      # Bold-first bullet that isn't a known role: warn if it looks like a card.
      if (m = line.match(CARD_START))
        word = m[:role].strip
        links_a_file = m[:rest].match?(/\A\[[^\]]+\]\((?!#|https?:)[^)\s]+\)/)
        close_call = role_by_alias.keys.find { |r| (1..2).cover?(edit_distance(word.downcase, r)) }
        if links_a_file || close_call
          hint = close_call ? %( Did you mean "#{role_by_alias[close_call]['label']}"?) : ""
          Jekyll.logger.warn "Unit pages:",
            %(#{page.relative_path}:#{i + 1 + front_matter_lines(page)}: "**#{word}**" is not a card role, ) +
            %(so this line stays a plain bullet.#{hint} Roles: #{role_names}.)
        end
      end

      out << rewrite_links(line, site, source_dir)
      i += 1
    end

    page.content = out.join("\n")

    # Page settings every unit page wants; visible to layouts via payload.
    extra = {
      "unit_number" => unit_no,
      "unit_sections" => sections,
      "toc" => false,
      "math" => true,
      "classes" => (Array(page.data["classes"]) | ["unit-page"]),
    }
    page.data.merge!(extra)
    payload["page"].merge!(extra) if payload["page"].respond_to?(:merge!)
  end
end

Jekyll::Hooks.register :pages, :pre_render do |page, payload|
  next unless page.data["layout"] == "unit"
  UnitPages.transform(page, payload)
end
