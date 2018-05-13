# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Seriesadicto para PalcoTV
# Version 0.1 (22/05/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import os
import sys
import urlparse
#import urllib
#import urllib2
#import re
#import shutil
#import zipfile

#import xbmc
#import xbmcgui
#import xbmcaddon
#import xbmcplugin

import plugintools

#from resources.tools.resolvers import *


def seriesnovelas_lista_playlists(params):
    data = plugintools.read(params.get("url"))
    plugintools.log("data="+data)
    data = plugintools.find_single_match(data,'<ul class="listpage">(.*?)</ul>')

    # Extract items from feed
    matches = plugintools.find_multiple_matches(data,"<li>(.*?)</li>")

    for entry in matches:
        plugintools.log("entry="+entry)

        #<li><a target="_blank" href="http://www.verseriesynovelas.com/ver/100-code" title="ver 100 Code">100 Code</a></li>
        title = plugintools.find_single_match(entry,'">(.*?)</a>')
        url = plugintools.find_single_match(entry,'href="(.*?)">')
        plugintools.add_item(action="seriesnovelas_temp", title=title, url=url, folder=True)


def seriesnovelas_temp(params):
    data = plugintools.read(params.get("url"))
    pattern = '<div class="widget HTML" id="HTML1">(.*?)'
    pattern = pattern + "<div class='widget HTML' id='HTML2'>"
    data = plugintools.find_single_match(data, pattern)
    plugintools.log("data="+data)

    matches = plugintools.find_multiple_matches(data,'<div class="col_portadas">(.*?)<div class="clear">')

    for entry in matches:
        plugintools.log("entry="+entry)
        #<div style='position:absolute;margin-top:35px;margin-left:15px;'></div>
        #<h2 class="posttitle">
        #<a href="http://www.verseriesynovelas.com/2014/10/agents-of-shield-temporada-2.html">Agents of SHIELD Segunda Temporada (2014) online</a></h2>
        #<a href="http://www.verseriesynovelas.com/2014/10/agents-of-shield-temporada-2.html"><img class="portadas_img" title="Agents of S.H.I.E.L.D. Temporada 2 " alt="Agents of S.H.I.E.L.D. Temporada 2 " src="http://4.bp.blogspot.com/-81iWTXquqhA/VV0x0IEKtUI/AAAAAAAABII/_S41N87fn7w/s320/Agents-of-Shield_season_2.jpg">
        #</a>
        title = plugintools.find_single_match(entry,'html">(.*?)</a>')
        url = plugintools.find_single_match(entry,'href="(.*?)">')
        fanart = plugintools.find_single_match(entry,'src="(.*?)">')

        plugintools.add_item(action="seriesnovelas_cap", title=title, thumbnail=fanart, fanart=fanart, url=url, folder=True)


def seriesnovelas_cap(params):
    plugintools.log("SERIESNOVELAS_CAP")
    data = plugintools.read(params.get("url"))
    pattern = '<ul class="listpage">(.*?)<div align="center">'
    data = plugintools.find_single_match(data, pattern)
    plugintools.log("data="+data)

    matches = plugintools.find_multiple_matches(data,'<li>(.*?)</li>')

    for entry in matches:
        plugintools.log("entry="+entry)
        #<div style='position:absolute;margin-top:35px;margin-left:15px;'></div>
        #<h2 class="posttitle">
        #<a href="http://www.verseriesynovelas.com/2014/10/agents-of-shield-temporada-2.html">Agents of SHIELD Segunda Temporada (2014) online</a></h2>
        #<a href="http://www.verseriesynovelas.com/2014/10/agents-of-shield-temporada-2.html"><img class="portadas_img" title="Agents of S.H.I.E.L.D. Temporada 2 " alt="Agents of S.H.I.E.L.D. Temporada 2 " src="http://4.bp.blogspot.com/-81iWTXquqhA/VV0x0IEKtUI/AAAAAAAABII/_S41N87fn7w/s320/Agents-of-Shield_season_2.jpg">
        #</a>
        title = plugintools.find_single_match(entry,'blank">(.*?)</a>')
        if entry.find("SUB.") != -1:
           title = title + " [COLOR white](SUB)[/COLOR]"
        if entry.find("EN.") != -1:
           title = title + " [COLOR white](EN)[/COLOR]"
        if entry.find("ES.") != -1:
           title = title + " [COLOR white](ES)[/COLOR]"
        url = plugintools.find_single_match(entry,'href="(.*?)"')

        plugintools.add_item(action="seriesnovelas_geturl", title=title, url=url, isPlayable=True, folder=False)


def seriesnovelas_geturl(params):
    plugintools.log("SERIESNOVELAS_GETURL")
    data = plugintools.read(params.get("url"))
    #plugintools.log("data= "+data)
    pattern = 'ock"> <iframe src='
    pattern = pattern + "'(.*?)' width="
    url = plugintools.find_single_match(data, pattern)    
    plugintools.log("URL= "+url)
    plugintools.play_resolved_url(url)
    #url = 'plugin://plugin.video.p2p-streams/?url=' + url + '&mode=2&name='



