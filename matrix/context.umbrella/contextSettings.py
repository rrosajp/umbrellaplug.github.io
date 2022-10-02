# -*- coding: utf-8 -*-

import xbmc

if __name__ == '__main__':
	plugin = 'plugin://plugin.video.umbrella/'
	path = f'RunPlugin({plugin}?action=tools_contextUmbrellaSettings&opensettings=false)'

	xbmc.executebuiltin(path)
	# xbmc.executebuiltin('RunPlugin(%s?action=widgetRefresh)' % plugin) #now part of "tools_contextUmbrellaSettings" action