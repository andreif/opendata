# Swedish data references

## Area codes

```py
from BeautifulSoup import BeautifulSoup
import json
import requests

# land lines
html = requests.get('http://sv.wikipedia.org/wiki/Lista_%C3%B6ver_svenska_riktnummer').content
soup = BeautifulSoup(html)
area_codes = '{\n'
for table in soup.findAll('table', {'class':'wikitable sortable'}):
    for tr in table.findAll('tr'):
        td = tr.findAll('td')
        if len(td) > 1:
            towns = '", "'.join(td[1].text.split('-'))
            area_codes += '"%s": {"network": "fixed", "towns": ["%s"], "county": "%s"},\n' % (td[0].text, towns, td[2].text)

# mobile network
jsn = requests.get('http://directory.didww.com/area-prefixes/206.json').content
for row in json.loads(jsn):
    if row['area']['code']:
        area_codes += '"0%s": {"network": "mobile", "operator": "%s"},\n' % (row['area']['code'], row['area']['name'][7:-7])

with open('area_codes.json','w') as f:
    f.write((area_codes[:-2] + '\n}\n').encode('utf-8'))
```
