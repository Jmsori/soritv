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


def dbsuper_playlists(params):
    plugintools.log("dbsuper_playlists_dbsch")
    plugintools.add_item(
        action="dbsuper_playlists_dbsch",
        title="Capítulos DBS",
        thumbnail="http://cm1.narvii.com/6545/9c98445673df95e56b6430d8c563a7a2a7a62524_120.jpg",
        url="http://www.dragonballsuper.com.mx/2017/12/dragon-ball-super-hd.html",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="dbsuper_playlists_dblatin",
        title="DBS Latino",
        thumbnail="http://cm1.narvii.com/6545/9c98445673df95e56b6430d8c563a7a2a7a62524_120.jpg",
        url="http://www.dragonballsuper.com.mx/2017/12/dragon-ball-super-hd.html",
        isPlayable=False,
        folder=True)

# OPENINGS
    plugintools.add_item(
        action="dbsowo_play_ya",
        title="[COLOR blue]OPENING[/COLOR]",
        thumbnail = "http://img.youtube.com/vi/jGTTQqCpuuU/0.jpg",
        url="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=jGTTQqCpuuU",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="dbsowo_play_ya",
        title="[COLOR blue]OPENING 2[/COLOR]",
        thumbnail = "http://img.youtube.com/vi/oVI39Yr_yTs/0.jpg",
        url="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=oVI39Yr_yTs",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="dbsowo_play_ya",
        title="[COLOR blue]ENDING[/COLOR]",
        thumbnail = "http://img.youtube.com/vi/wNmtYqfjcIM/0.jpg",
        url="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=wNmtYqfjcIM",
        isPlayable=True,
        folder=False)


def dbsuper_playlists_dbsch(params):
    plugintools.log("dbsuper_playlists_dbsch")
    T_DBSUPER = 50005

    #line1 = "Tenga paciencia puede durar varios segundos."
    line1 = plugintools.get_localized_string(T_DBSUPER)
    time = 5000 #in miliseconds
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url = params.get("url")
    plugintools.log(url)
    try:
        data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    except:
        data="";
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)

    matches = plugintools.find_multiple_matches(data,'<!--INICIA LINK-->(.*?)<!--TERMINA LINK-->')
    for entry in matches:
        #plugintools.log("data="+entry)
        url2 = plugintools.find_single_match(entry,'href="(.*?)"')
        #thumbnail = "http://cm1.narvii.com/6545/9c98445673df95e56b6430d8c563a7a2a7a62524_120.jpg"
        title = plugintools.find_single_match(entry,'target="_blank">(.*?)<')
        title = replace_html(title)
        #plugintools.log("url="+url2)
        #plugintools.log("title="+title)

        data2,response_headers = plugintools.read_body_and_headers(url2, headers=request_headers)
        data2 = plugintools.find_single_match(data2,"<div class='cover'>(.*?)<div class='postbot'>")
        thumbnail = plugintools.find_single_match(data2,'src="(.*?)"')

        plugintools.add_item(
            action = "dbsowo_subplay",
            title = title,
            thumbnail = thumbnail,
            url = url2,
            isPlayable = False,
            folder = True)


def dbsowo_subplay(params):
    plugintools.log("dbsowo_subplay")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url = params.get("url")
    #plugintools.log(url)
    try:
        data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    except:
        data="";
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)

    matches = plugintools.find_single_match(data,"<div class='cover'>(.*?)<div class='postbot'>")
    thumbnail = plugintools.find_single_match(matches,'src="(.*?)"')
    plot = plugintools.find_single_match(matches,'100%;">(.*?)<')
    plot = replace_html(plot)
    matches = plugintools.find_single_match(matches,'class="item_Description">(.*?)clear: both;')
    #plugintools.log("matches="+matches)
    matches2 = plugintools.find_multiple_matches(matches,'[Ss][Rr][Cc]="(.*?)"')
    for entry in matches2:
        entry = replace_html(entry)
        #plugintools.log("data="+entry)
        dataurl = dbsuper(entry)
        #plugintools.log("dataurl="+dataurl)
        #url2 = plugintools.find_single_match(entry,' src="(.*?)"')
        plugintools.add_item(
            action = "dbsowo_play_ya",
            title = entry,
            plot = plot,
            thumbnail = thumbnail,
            url = dataurl,
            isPlayable = True,
            folder = False)


def dbsuper(params):
    plugintools.log("dbsuper")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    #url = params.get("url")
    url = params
    plugintools.log("dbsuper_url = " + url)
    try:
        data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    except:
        data="";
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)

    video_url = ""
    if "openload" in url:
        #plugintools.log("dbsuper_data = " + data)
        video_url = "https://oload.stream/embed/TApaOiDf8JY/3.mp4?mime=true"
        video_url = "https://1fjiw6c.oloadcdn.net/dl/l/izleOOPq6gPX6DD1/TApaOiDf8JY/3.mp4?mime=true"
        #https://1fjiw6c.oloadcdn.net/dl/l/KAiYPSPmYe4IpTL9/M9DPzGEnWAk/4.mp4?mime=true
        #plugintools.log("dbsowo_play_openload="+video_url)

    elif "ok" in url:
        video_url = ""
    elif "vidoza" in url:
        video_url = plugintools.find_single_match(data,'file:"(.*?)"')
    else:
        video_url = ""

    return video_url


def dbsowo_play_ya(params):
    url=params.get("url")
    plugintools.log("dbsowo_play_ya="+url)
    plugintools.play_resolved_url( url )
    #plugintools.direct_play( url )
    #plugin://program.plexus/?url=acestream://' + dataurl + '&mode=1&name='

def play(item):
    logger.info("[animelatino] play url="+item.url)
    itemlist = servertools.find_video_items(data=item.url)
    return itemlist

def replace_html(text=""):
    text = str(text)
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    text = text.replace("\r\n", " ")
    text = text.replace("&aacute;","á")
    text = text.replace("&eacute;","é")
    text = text.replace("&iacute;","í")
    text = text.replace("&oacute;","ó")
    text = text.replace("&uacute;","ú")
    text = text.replace("&iquest;","¿")
    text = text.replace("&ntilde;","ñ")
    text = text.replace("&Ntilde;","Ñ")
    text = text.replace("&ecirc;","ê")
    text = text.replace("&iexcl;","¡")
    text = text.replace("&‌nbsp;"," ")
    text = text.replace("&#161;","¡")
    text = text.replace("&#191;","¿")
    text = text.replace("&#8220;",'"')
    text = text.replace("//www",'www')
    text = re.sub("<.*?>", "", text)
    return text.strip()

