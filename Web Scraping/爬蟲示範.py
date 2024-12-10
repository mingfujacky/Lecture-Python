from urllib.request import urlopen
import re
import pprint

url = 'http://olympus.realpython.org/profiles/dionysus'
with urlopen(url) as page:
    html_bytes = page.read()
html = html_bytes.decode('utf-8')
title_regex = re.compile('<title.*?>.*?</title.*?>', re.IGNORECASE)
result = title_regex.search(html).group()
remove_title_regex = re.compile('<.*?>')
result = remove_title_regex.sub('', result)
pprint.pprint(html)
