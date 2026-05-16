# _plugins/notebook_metadata.rb
#
# Auto-generates _data/notebooks.json before Jekyll reads site data.
# This ensures {% include nb.html ... %} works whether you run
# `bundle exec jekyll serve` directly or via serve_with_notebooks.sh.
#
# Skips regeneration when notebooks.json is newer than all .ipynb files
# (same mtime logic used by export_notebooks.py).

require 'open3'

Jekyll::Hooks.register :site, :after_reset do |site|
  metadata_path = File.join(site.source, '_data', 'notebooks.json')
  notebooks_dir = File.join(site.source, 'notebooks')
  script        = File.join(site.source, 'scripts', 'generate_notebook_metadata.py')

  next unless File.exist?(script)

  # Skip if metadata is already fresh
  if File.exist?(metadata_path)
    metadata_mtime = File.mtime(metadata_path)
    notebooks      = Dir.glob("#{notebooks_dir}/**/*.ipynb").reject { |f| f.include?('/.') }
    newest         = notebooks.map { |f| File.mtime(f) }.max
    if newest.nil? || metadata_mtime >= newest
      Jekyll.logger.debug 'Notebooks:', 'Metadata is up to date, skipping generation'
      next
    end
  end

  Jekyll.logger.info 'Notebooks:', 'Generating metadata...'
  _out, err, status = Open3.capture3('python3', script, chdir: site.source)

  if status.success?
    Jekyll.logger.info 'Notebooks:', 'Metadata generated.'
  else
    Jekyll.logger.warn 'Notebooks:', "Metadata generation failed — {% include nb.html %} links will be broken.\n#{err}"
  end
end
