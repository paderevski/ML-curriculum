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
#     -> a notebook card (badge, title, description, View / Download / Colab)
#        Roles: Demo, In class (or Classwork), Homework (or HW), Demo + HW.
#        Links to .ipynb become notebook cards; .csv/.json/.zip/... become
#        datasets; .html becomes "interactive"; anything else is a plain link.
#        No link: "- **Homework** k-d tree packet: handed out in class."
#        A description starting "Coming soon" gives a dashed placeholder card.
#
#   [text](./file.ipynb), [text](./data.csv), ![](./fig.png)
#     -> relative links resolved against the Markdown file's own folder
#        (.ipynb links go to the notebook's web view). .md links are left to
#        jekyll-relative-links, which already handles them.
#
# It also inserts the unit map before the first section and fills
# page.unit_sections, which _includes/unit-map.html renders.
#
# Cards themselves are rendered by _includes/unit-material.html, so their
# look is edited there, not here.

module UnitPages
  ROLES = {
    "demo" => "demo",
    "in class" => "classwork",
    "classwork" => "classwork",
    "homework" => "hw",
    "hw" => "hw",
    "demo + hw" => "demo-hw",
    "demo+hw" => "demo-hw",
    "demo + homework" => "demo-hw",
  }.freeze

  DATA_EXTS = %w[.csv .tsv .json .zip .txt .xlsx .parquet .gz .pkl].freeze

  CARD_START = /\A\s{0,3}[-*]\s+\*\*(?<role>[^*]+)\*\*\s*(?<rest>.*)\z/

  module_function

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
  # "./file.ipynb" into that form before this hook runs.
  def resolve(target, source_dir, baseurl = "")
    path, frag = target.split("#", 2)
    if path.start_with?("/")
      path = path.delete_prefix(baseurl) unless baseurl.empty?
      return [path.sub(%r{\A/}, ""), frag]
    end
    full = File.expand_path(path, "/" + source_dir).sub(%r{\A/}, "")
    [full, frag]
  end

  def notebook_entry(site, repo_path)
    site.data.dig("notebooks", "by_path", repo_path)
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

  def liquid_str(s)
    s.to_s.gsub("\\", "\\\\\\\\").gsub('"', '\\"')
  end

  # One card list item -> capture/include Liquid line, plus its role.
  def card_line(site, source_dir, role, rest)
    label = rest
    target = nil
    blurb = ""
    if (m = rest.match(/\A\[(?<label>[^\]]+)\]\((?<target>[^)\s]+)\)\s*(?:[:–—-]\s*)?(?<blurb>.*)\z/m))
      label, target, blurb = m[:label], m[:target], m[:blurb]
    elsif (m = rest.match(/\A(?<label>[^:]+?)\s*:\s*(?<blurb>.*)\z/m))
      label, blurb = m[:label], m[:blurb]
    end

    params = { "role" => role }
    if target.nil?
      params["kind"] = blurb.match?(/\Acoming soon/i) ? "soon" : "item"
    elsif external?(target)
      params["kind"] = "link"
      params["url"] = target
    else
      repo_path, frag = resolve(target, source_dir, site.config["baseurl"].to_s)
      ext = File.extname(repo_path).downcase
      if ext == ".ipynb"
        params["kind"] = "notebook"
        params["path"] = repo_path
      else
        params["kind"] = DATA_EXTS.include?(ext) ? "dataset" : (ext == ".html" ? "interactive" : "link")
        params["url"] = url_for(site, repo_path, frag)
      end
    end
    params["kind"] = "soon" if blurb.match?(/\Acoming soon/i)

    attrs = params.map { |k, v| %(#{k}="#{liquid_str(v)}") }.join(" ")
    "{% capture uc_label %}#{label.strip}{% endcapture %}" \
      "{% capture uc_blurb %}#{blurb.strip}{% endcapture %}" \
      "{% include unit-material.html #{attrs} label=uc_label blurb=uc_blurb %}"
  end

  # Rewrite relative links/images in a line of prose.
  def rewrite_links(line, site, source_dir)
    baseurl = site.config["baseurl"].to_s
    line.gsub(/(\]\()([^)\s]+)(\))/) do
      open, target, close = $1, $2, $3
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
          current = { "num" => num, "id" => id, "title" => title,
                      "notes" => false, "demo" => 0, "classwork" => 0, "hw" => 0 }
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
      if (m = line.match(CARD_START)) && (role = ROLES[m[:role].strip.downcase])
        text = [m[:rest]]
        j = i + 1
        while j < lines.length && lines[j].match?(/\A\s+\S/) && !lines[j].match?(CARD_START)
          text << lines[j].strip
          j += 1
        end
        out << card_line(site, source_dir, role, text.join(" "))
        if current
          current["demo"] += 1 if %w[demo demo-hw].include?(role)
          current["hw"] += 1 if %w[hw demo-hw].include?(role)
          current["classwork"] += 1 if role == "classwork"
        end
        i = j
        next
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
