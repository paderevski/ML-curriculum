source "https://rubygems.org"

# Match the parent site's Jekyll version
gem "jekyll", "~> 4.3"

# No theme gem: the site ships its own layouts (_layouts/, _includes/theme/,
# _sass/theme/). The parent aet-cs site still uses minimal-mistakes-jekyll.

# Plugins (only the ones the site uses)
gem "jekyll-sitemap"
gem "jekyll-redirect-from"   # index.md redirects /calendar/
gem "jekyll-relative-links"  # [text](./page.md) links in unit pages

# Server and parser
gem "webrick", "~> 1.8"
gem "kramdown-parser-gfm"

# Windows / JRuby zoneinfo
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Windows directory-watching booster
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
