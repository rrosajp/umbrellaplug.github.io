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
	name = params.get('tvshowtitle', params['title'])
	sysname = quote_plus(name)

	imdb = params.get('imdb', '')
	tvdb = params.get('tvdb', '')
	season = params.get('season', '')
	episode = params.get('episode', '')

	playcount = getInfoLabel('ListItem.Playcount')
	watched = (int(playcount) >= 1) if playcount else False

	path = f'RunPlugin({plugin}?action=tools_traktManager&name={sysname}&imdb={imdb}&tvdb={tvdb}&season={season}&episode={episode}&watched={watched})'

	executebuiltin(path)