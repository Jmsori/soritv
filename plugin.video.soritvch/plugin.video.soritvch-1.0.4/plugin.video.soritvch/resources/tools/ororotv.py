# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Arenavision para SorichTV
# Version 0.1 (22/05/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import re
import os
import sys
import urlparse
import urllib
import urllib2

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

import plugintools
#import openload
#from resources.tools.openload import *

 
__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')

def ororotv_playlists(params):
    plugintools.log("ororotv_playlists")

    #line1 = "This is a simple example of notifications"
    #line1 = "Tenga paciencia puede durar varios segundos."
    #time = 5000 #in miliseconds
    #xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url_main = params.get("url")
    try:
       #data = plugintools.read(url)
       data,response_headers = plugintools.read_body_and_headers(url_main, headers=request_headers)
    except: 
        data=""
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url_main)
        return
        pass

    matches = plugintools.find_multiple_matches(data,"<div class='index show'(.*?)</a><a class=")
    for entry in matches:
        plugintools.log("data="+entry)
        url = "https://ororo.tv"+plugintools.find_single_match(entry,'href="(.*?)">')
        #thumbnail = "https://ororo.tv/uploads"+plugintools.find_single_match(entry,'uploads(.*?)"')
        thumbnail = "https"+plugintools.find_single_match(entry,'https(.*?)jpg')+"jpg"
        title = plugintools.find_single_match(entry,"'title'>\n(.*?)\n<")
        plot = plugintools.find_single_match(entry,"<p>(.*?)<")
        #plugintools.log("url="+url)
        #plugintools.log("thumbnail="+thumbnail)
        #plugintools.log("title="+title)
        #plugintools.log("plot="+plot)

        #dataurl = ororotv_play(url)

        plugintools.add_item(
            action="ororotv_play",
            #action="",
            title=title,
            plot=plot,
            #url=url,
            url="https://ororo.tv/es/shows/younger#1-1",
            thumbnail=thumbnail,
            isPlayable=True,
            folder=False )

#<iframe width="960" height="520" src="https://openload.co/embed/riGW6Zud4eo/" frameborder="0" allowfullscreen=""></iframe>


def ororotv_play(params):
    plugintools.log("ororotv_play")

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
    plugintools.log("data="+data)

    matches = plugintools.find_single_match(data,'<iframe[^c]+c="([^"]+)')
    if not "http" in matches:
        matches = "http:"+matches
    plugintools.log("dbsowo_play="+matches)
    video_mp4 = ""
    try:
        data,response_headers = plugintools.read_body_and_headers(matches, headers=request_headers)
    except: data="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+matches)

    #plugintools.log("video_mp4="+video_mp4)
    return video_mp4

def ororotv_play_ya(params):
    url=params.get("url")
    plugintools.log("ororotv_play_ya="+url)
    plugintools.play_resolved_url( url )
    #plugintools.direct_play( url )

def play(item):
   logger.info("[animelatino] play url="+item.url)
   
   itemlist = servertools.find_video_items(data=item.url)
    
   return itemlist

def test_video_exists(page_url):
    logger.info("[openload.py] test_video_exists(page_url='%s')" % page_url)

    data = scrapertools.cache_page(page_url, headers=headers)

    if 'We are sorry!' in data:
        return False, 'File Not Found or Removed.'

    return True, ""

