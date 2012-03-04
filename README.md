# Collection of open data

```py
>>> import opendata
>>> area_codes = opendata.load('se/sv_SE/area_codes')
>>> area_codes.get('0980')
{u'county': u'Norrbottens l\xe4n', u'towns': [u'Kiruna'], u'network': u'fixed'}
>>> area_codes.get('07018')
{u'operator': u'Telia', u'network': u'mobile'}
```
