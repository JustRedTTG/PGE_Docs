project = 'Pygame Extra'
copyright = '2020, RedstoneHair'
author = 'RedstoneHair'
release = '1.6'
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]
master_doc = "contents"
templates_path = ['_templates']
html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}
source_suffix = '.rst'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
html_static_path = ['_static']
html_theme = 'groundwork'
