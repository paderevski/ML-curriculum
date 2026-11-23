# _plugins/pandoc_pages.rb
#
# Some pages (handouts, a few notes) are written for pandoc -> PDF: their
# front matter has `geometry:` or `header-includes:`, and the body mixes in
# print-only LaTeX. For the web version of those pages only, this hook:
#
#   - turns on MathJax (math: true)
#   - drops ```{=latex} ... ``` blocks; a block that held a table or other
#     content becomes a short "see the PDF" note, and a big bold title inside
#     one (\Large\bfseries ...) becomes the page title if it has none
#   - drops print-only layout: \vspace{..}, \newpage, \hfill, centering,
#     and the "Name: ____ Date: ____" line
#   - gives a line that is only $$...$$ its own paragraph, so it shows as
#     display math the way pandoc prints it
#
# The source file is untouched, so the PDF build is unaffected.

module PandocPages
  LAYOUT_ONLY = /\A\s*(?:\\(?:vspace\*?|hspace\*?)\{[^}]*\}|\\(?:newpage|clearpage|pagebreak|hfill|vfill|medskip|bigskip|smallskip|noindent|centering)|\\(?:begin|end)\{center\}|\s)*\s*\z/
  NAME_LINE = /\A\s*Name:\s*\\underline/
  TITLE_IN_LATEX = /\\(?:Large|LARGE|large|huge|Huge)\s*\\bfseries\s+([^}\\]+)\}/

  module_function

  def pandoc_page?(page)
    page.data.key?("geometry") || page.data.key?("header-includes")
  end

  def transform(page, payload)
    lines = page.content.split("\n", -1)
    out = []
    title = nil
    i = 0
    while i < lines.length
      line = lines[i]
      if line.match?(/\A\s*```+\s*\{=latex\}\s*\z/)
        block = []
        i += 1
        while i < lines.length && !lines[i].match?(/\A\s*```+\s*\z/)
          block << lines[i]
          i += 1
        end
        i += 1 # closing fence
        text = block.join("\n")
        title ||= text[TITLE_IN_LATEX, 1]&.strip
        leftover = block.reject do |l|
          l.match?(LAYOUT_ONLY) || l.match?(NAME_LINE) || l.match?(TITLE_IN_LATEX)
        end
        unless leftover.join.strip.empty?
          what = text.include?("tabular") ? "This table" : "This part"
          out << "" << "*(#{what} is on the printed worksheet; see the PDF version.)*" << ""
        end
        next
      end
      if line.match?(NAME_LINE) || (line.match?(/\\[a-z]/) && line.match?(LAYOUT_ONLY))
        i += 1
        next
      end
      cleaned = line.gsub(/\\vspace\*?\{[^}]*\}/, "").gsub(/\\(?:newpage|clearpage)\b/, "")
      if cleaned.strip.match?(/\A\$\$.+\$\$\z/)
        # pandoc treats a line of $$...$$ as display math; kramdown only does
        # when it's its own paragraph.
        out << "" << cleaned.strip << ""
      else
        out << cleaned
      end
      i += 1
    end
    page.content = out.join("\n")

    extra = { "math" => true }
    extra["title"] = title if title && !page.data["title"]
    page.data.merge!(extra)
    payload["page"].merge!(extra) if payload["page"].respond_to?(:merge!)
  end
end

Jekyll::Hooks.register :pages, :pre_render do |page, payload|
  next unless PandocPages.pandoc_page?(page)
  PandocPages.transform(page, payload)
end
