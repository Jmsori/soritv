# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Canales Streaming para SorichTV
# Version 0.1 (14/08/2017)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import plugintools
import xbmc
import xbmcaddon
import xbmcgui
import urllib2
import scrapertools

T_ESPORT3 = plugintools.get_localized_string(30012)
T_PSWD = plugintools.get_localized_string(50004)

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')

def VerCanalesTV_playlists(params):
    xbmc.log("### Channels_playlists", xbmc.LOGNOTICE)

    plugintools.log("VerCanalesTV_playlists")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url_main = params.get("url")
    try:
       data,response_headers = plugintools.read_body_and_headers(url_main, headers=request_headers)
    except:
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+data)
        data=""
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url_main)
        return
        pass
    #plugintools.log("data="+data)
    #matches = plugintools.find_multiple_matches(data,'><img src="(*.?)" alt
    matches = plugintools.find_multiple_matches(data,'(<td>.*?<\/td>)')
    for entry in matches:
        title = plugintools.find_single_match(entry,'title="(.*?)">')
        thumbnail = plugintools.find_single_match(entry,'<img src="(.*?)"')
        url = plugintools.find_single_match(entry,'<a href="(.*?)"')
        #url = "http://edgoo1.telesport.pw/live/tve1/index.m3u8"
        #url = "http://cdn66.verliga.club/hls/live/syfy/index.m3u8"
        #url = "http://edgoo7.telesport.pw/live/axn/index.m3u8"
        #plugintools.log('TITLE='+title)
        if title: # Si el title no esta en blanco
            plugintools.add_item(
                action="Play_Channel",
                title=title,
                thumbnail=thumbnail,
                url=url,
               isPlayable=True,
               folder=False )

def Play_Channel(params):
    url = params.get("url")
    xbmc.log("### Play_Channel", xbmc.LOGNOTICE)
    plugintools.play_resolved_url(url)

