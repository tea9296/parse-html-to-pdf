# parse-html-to-pdf
using pypdf and BeautifulSoup to save content into pdf file


## parse to pdf example 

``` python
import parsing_helper as ph
ph.convert_url_to_pdf("https://beautiful-soup-4.readthedocs.io/en/latest/", "bf4.pdf",tag="p",language='en')

```


## get url links example
``` python
import parsing_helper as ph

print(ph.get_links("https://beautiful-soup-4.readthedocs.io/en/latest/", set()))

```
``` python
['http://www.crummy.com/software/BeautifulSoup/', 'http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html', 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/', 'http://kondou.com/BS4/', 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/', 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/', 'https://groups.google.com/forum/?fromgroups#!forum/beautifulsoup', 'http://www.crummy.com/software/BeautifulSoup/download/4.x/', 'http://lxml.de/', 'http://code.google.com/p/html5lib/', 'https://facelessuser.github.io/soupsieve/', 'http://www.w3.org/TR/html5/syntax.html#syntax', 'http://wiki.python.org/moin/PrintFails', 'http://pypi.python.org/pypi/cchardet/', 'http://www.crummy.com/software/BeautifulSoup/bs3/download/3.x/BeautifulSoup-3.2.0.tar.gz', 'http://www.python.org/dev/peps/pep-0008/', 'http://sphinx-doc.org/', 'https://github.com/rtfd/sphinx_rtd_theme', 'https://readthedocs.org', 'http://www.readthedocs.org']

```