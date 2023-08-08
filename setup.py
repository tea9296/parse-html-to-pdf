from setuptools import setup

setup(name='parsing_helper',
      version = '0.1',
      description = "using pypdf and BeautifulSoup to save contents into pdf file",
      author = 'chih chuan chang',
      author_email = 'tea9296@gmail.com',
      install_requires = ['pypdf==3.12.2','beautifulsoup4','fpdf'],
      packages=['parsing_helper']
      #py_modules = ['parsing_helper']
      )