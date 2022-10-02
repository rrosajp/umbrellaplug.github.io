# -*- coding: utf-8 -*-
"""
	Umbrella Add-on
"""

from resources.lib.modules.control import addonPath, addonId, getUmbrellaVersion, joinPath
from resources.lib.windows.textviewer import TextViewerXML


def get(file):
	umbrella_path = addonPath(addonId())
	umbrella_version = getUmbrellaVersion()
	helpFile = joinPath(umbrella_path, 'resources', 'help', f'{file}.txt')
	with open(helpFile, 'r', encoding='utf-8', errors='ignore') as f:
		text = f.read()
	heading = f'[B]Umbrella -  v{umbrella_version} - {file}[/B]'
	windows = TextViewerXML('textviewer.xml', umbrella_path, heading=heading, text=text)
	windows.run()
	del windows