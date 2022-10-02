# -*- coding: utf-8 -*-

import xbmc

if __name__ == '__main__':
	plugin = 'plugin://plugin.video.umbrella/'
	path = f'RunPlugin({plugin}?action=cache_clearSources&opensettings=false)'
	xbmc.executebuiltin(path)