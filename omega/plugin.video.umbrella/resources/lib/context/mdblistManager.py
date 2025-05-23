# -*- coding: utf-8 -*-

import sys
from xbmc import getInfoLabel, executebuiltin
try: #Py2
	from urlparse import parse_qsl
	from urllib import quote_plus
except ImportError: #Py3
	from urllib.parse import parse_qsl, quote_plus

if __name__ == '__main__':
	item = sys.listitem
	# message = item.getLabel()
	path = item.getPath()

	plugin = 'plugin://plugin.video.umbrella/'
	args = path.split(plugin, 1)
	params = dict(parse_qsl(args[1].replace('?', '')))
	name = params['tvshowtitle'] if 'tvshowtitle' in params else params['title']
	sysname = quote_plus(name)

	imdb = params.get('imdb', '')
	tvdb = params.get('tvdb', '')
	tmdb = params.get('tmdb', '')

	playcount = getInfoLabel('ListItem.Playcount')

	path = 'RunPlugin(%s?action=tools_mdbWatchlist&name=%s&imdb=%s&tvdb=%s&tmdb=%s)' % (
				plugin, sysname, imdb, tvdb, tmdb)
	executebuiltin(path)