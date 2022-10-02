# -*- coding: utf-8 -*-

import sys
import xbmc
try: #Py2
	from urlparse import parse_qsl
except ImportError: #Py3
	from urllib.parse import parse_qsl, quote_plus

if __name__ == '__main__':
	item = sys.listitem
	# message = item.getLabel()
	path = item.getPath()
	plugin = 'plugin://plugin.video.umbrella/'
	args = path.split(plugin, 1)
	params = dict(parse_qsl(args[1].replace('?', '')))
	imdb = params.get('imdb', '')
	tmdb = params.get('tmdb', '')
	tvdb = params.get('tvdb', '')
	season = params.get('season', '')
	episode = params.get('episode', '')
	tvshowtitle = params.get('tvshowtitle', '')
	title = params.get('title','')
	year = params.get('year', '')
	sysname = item.getLabel()
	systvshowtitle = quote_plus(tvshowtitle) if tvshowtitle else ''
	systitle = quote_plus(title) if title else ''
	action = 'tvshows' if 'tvshowtitle' in params else 'movies'
	if action == 'movies':
		xbmc.executebuiltin(
			f'RunPlugin({plugin}?action=library_movieToLibrary&name={sysname}&title={systitle}&year={year}&imdb={imdb}&tmdb={tmdb})'
		)

	elif action == 'tvshows':
		xbmc.executebuiltin(
			f'RunPlugin({plugin}?action=library_tvshowToLibrary&tvshowtitle={systvshowtitle}&year={year}&imdb={imdb}&tmdb={tmdb}&tvdb={tvdb})'
		)