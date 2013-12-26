from setuptools import setup

requires = ['pelican>=3.3.0', 'Markdown', 'typogrify'] 

setup(name='Pelican Website',
      version='1.0',
      description='My personal site and blog',
      author='Darrel Clute',
      author_email='darrel@darrelclute.net',
      url='https://github.com/darrelclute/pelican-opneshift',
      install_requires=requires,
     )
