from setuptools import setup

setup(name='parsing_helper',
      version = '0.1',
      description = "using pypdf and BeautifulSoup to save texts in the url into pdf file",
      author = 'chih chuan chang',
      author_email = 'tea9296@gmail.com',
      install_requires = ['pypdf==3.12.2','beautifulsoup4','fpdf'],
      packages=['parsing_helper'],
      package_data={'parsing_helper':['fonts/arial.ttf','fonts/SIMYOU.TTF']}
      ,include_package_data=True
      #py_modules = ['parsing_helper']
      )