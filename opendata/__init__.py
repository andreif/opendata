# -*- coding: utf-8 -*-
import json
from os.path import join, dirname, exists

VERSION = (0,0,1)
__version__ = '.'.join([str(i) for i in VERSION])

DEFAULT_LOCALE = 'sv_SE'

CACHED_DATA = {}

class NotFound(Exception): pass

def load(path):
    if CACHED_DATA.has_key(path): return CACHED_DATA[path]
    full_path = join(dirname(__file__), 'data', path if path.endswith('.json') else path + '.json')
    data = CACHED_DATA[path] = json.loads(open(full_path).read())
    return data

class LocaleAware(object):
    def __init__(self, locale=None):
        self.set_locale(locale)

    def set_locale(self, locale):
        self._locale = locale or getattr(self, '_locale', DEFAULT_LOCALE)  # TODO: implement fallback
        return self

    @property
    def locale(self):
        return self._locale

    def __call__(self, locale=None, *args, **kwargs):
        return self.set_locale(locale)

class OpenDataLoader(LocaleAware):
    def __init__(self, country, locale=None):
        super(OpenDataLoader, self).__init__(locale=locale)
        self._country_code = country
        self._cache = {}

    def __getattr__(self, name):
        if name.startswith('_'): return object.__getattr__(self, name)
        dic = self._cache[name] = self._cache.get(name) or self._load(name)
        return dic

    def _load(self, name):
        path = join(dirname(__file__), 'data', self._country_code, self._locale, name) + '.json'
        if exists(path):
            return json.loads(open(path).read()) # TODO: later support different data formats  # TODO: implement fallback to existing locales
        else:
            raise Exception('Dataset "%s" for contry "%s" with locale "%s" is not available' % (name, self._country_code, self._locale))

class OpenDataManager(LocaleAware):
    """
    from opendata import OpenData
    print OpenData.se.area_codes
    print OpenData.SE('sv_SE').area_codes

    TODO:
    OpenData('sv_SE,en_US,*').SE.area_codes
    with OpenData.locale('sv_SE'):
        print OpenData.se.area_codes
    """
    def __init__(self, *args, **kwargs):
        super(OpenDataManager, self).__init__(*args, **kwargs)
        self._cache = {}

    def __getattr__(self, name):
        if name.startswith('_'): return object.__getattr__(self, name)
        country = name.lower()
        loader = self._cache[country] = self._cache.get(country) or OpenDataLoader(country=country)
        loader.set_locale(self._locale)
        return loader

OpenData = OpenDataManager()

#print OpenData.se.area_codes
#print OpenData('sv_SE').se('sv_SE').area_codes
#print OpenData.SE('sv_SE').area_codes
#area_codes = opendata.load('SE/sv_SE/area_codes')
#area_codes.get('08')