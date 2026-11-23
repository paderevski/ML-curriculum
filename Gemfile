source "https://rubygems.org"

# Match the parent site's Jekyll version
gem "jekyll", "~> 4.3"

# No theme gem: the site ships its own layouts (_layouts/, _includes/theme/,
# _sass/theme/). The parent aet-cs site still uses minimal-mistakes-jekyll.

# Plugins (matching parent site)
gem "jekyll-remote-theme"
gem "jekyll-paginate"
gem "jekyll-sitemap"
gem "jekyll-gist"
gem "jekyll-feed"
gem "jekyll-include-cache"
gem "jekyll-redirect-from"
gem "jekyll-relative-links"
gem "jemoji"

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
