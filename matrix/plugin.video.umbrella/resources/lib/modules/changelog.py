# -*- coding: utf-8 -*-
"""
	Umbrella Add-on
"""

from resources.lib.modules.control import addonPath, addonVersion, joinPath, existsPath
from resources.lib.windows.textviewer import TextViewerXML


def get(name):
	nameDict = {'Umbrella': 'plugin.video.umbrella'}
	addon_path = addonPath(nameDict[name])
	addon_version = addonVersion(nameDict[name])
	changelog_file = joinPath(addon_path, 'changelog.txt')
	if not existsPath(changelog_file):
		from resources.lib.modules.control import notification
		return notification(message='ChangeLog File not found.')
	with open(changelog_file, 'r', encoding='utf-8', errors='ignore') as f:
		text = f.read()
	heading = f'[B]{name} -  v{addon_version} - ChangeLog[/B]'
	windows = TextViewerXML('textviewer.xml', addonPath('plugin.video.umbrella'), heading=heading, text=text)
	windows.run()
	del windows