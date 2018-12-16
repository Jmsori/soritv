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

def dbsowo_playlists(params):
    plugintools.add_item(
        action="dbsowo_playlists_sub",
        title="DBS [COLOR white]SUB ESPAÑOL[/COLOR]",
        thumbnail="http://dbsowo.com/wp-content/uploads/2016/01/sdssdds.png",
        url="http://dbsowo.com/category/dbs-sub-espanol/",
        folder=True)

    plugintools.add_item(
        action="dbsowo_playlists_sub",
        title="DBS [COLOR white]AUDIO LATINO[/COLOR]",
        thumbnail="http://dbsowo.com/wp-content/uploads/2016/01/sdssdds.png",
        url="http://dbsowo.com/category/dbs-audio-latino/",
        folder=True)

    #http://vaughnlive.tv/embed/video/wgg002?viewers=true&autoplay=true
    plugintools.add_item(
        action="dbsowo_play_ya",
        title="DBS [COLOR white]TV EN VIVO[/COLOR]",
        thumbnail="http://dbsowo.com/wp-content/uploads/2016/01/sdssdds.png",
        url = "plugin://plugin.stream.vaughnlive.tv/?sourcetype=auto&amp;img=http%3A%2F%2Fcdn.vaughnsoft.com%2Fvaughnsoft%2Fvaughn%2Fimg_profiles%2Fsherming7777_320.jpg&amp;title=sherming7777&amp;url=http%3A%2F%2Fvaughnlive.tv%2Fsherming7777&amp;section=&amp;site=&amp;mode=PlayLiveStream&amp;fimg=http%3A%2F%2Fcdn.vaughnsoft.com%2Fvaughnsoft%2Fvaughnlive%2Fimg_backgrounds%2Fsherming7777.jpg&amp;channel=sherming7777",
        folder=False)

    #https://www.youtube.com/watch?v=jGTTQqCpuuU
    #http://img.youtube.com/vi/jGTTQqCpuuU/0.jpg

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

def dbsowo_playlists_sub(params):
    plugintools.log("dbsowo_playlists")

    line1 = "This is a simple example of notifications"
    line1 = "Tenga paciencia puede durar varios segundos."
    time = 5000 #in miliseconds
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url = params.get("url")
    plugintools.log("URLURL: "+url)
    try:
       #data = plugintools.read(url)
       data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    except: data="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)

    matches = plugintools.find_multiple_matches(data,'<figure class=(.*?)</figure>')
    for entry in matches:
        plugintools.log("data="+entry)
        url = plugintools.find_single_match(entry,'href="(.*?)">')
        thumbnail = plugintools.find_single_match(entry,'src="(.*?)" class')
        title = plugintools.find_single_match(entry,'alt="(.*?)" />')
        plugintools.log("video_link="+url)
        #plugintools.log("video_img="+title)

        dataurl = dbsowo_play(url)

        plugintools.add_item(
            action="dbsowo_play_ya",
            title=title,
            #plot=plot,
            url=dataurl,
            thumbnail=thumbnail,
            isPlayable=True,
            folder=False )

    if "Next &#8594;" in data:
        url_next = plugintools.find_single_match(data,'page-numbers" href="(.*?)">Next')
        print "url_next: "+url_next
        plugintools.add_item(
            action="dbsowo_playlists_sub",
            title="Next Page",
            url=url_next,
            folder=True)


def dbsowo_play(params):
    plugintools.log("dbsowo_play")
    request_headers=[]

    '''headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}'''

    #request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    request_headers.append(["User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"])
    request_headers.append(["Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"])
    request_headers.append(["Accept-Charset","ISO-8859-1,utf-8;q=0.7,*;q=0.3"])
    request_headers.append(["Accept-Encoding","none"])
    request_headers.append(["Accept-Language","en-US,en;q=0.8"])
    request_headers.append(["Connection","keep-alive"])

    url = params
    try:
       data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    except: data="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)
    #plugintools.log("data="+data)
    matches = plugintools.find_single_match(data,'<iframe[^c]+c="([^"]+)')
    if not "http" in matches:
        matches = "http:"+matches
    plugintools.log("dbsowo_play="+matches)
    video_mp4 = ""
    try:
        data,response_headers = plugintools.read_body_and_headers(matches, headers=request_headers)
    except: data="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+matches)

    # SENDVID
    if "sendvid" in matches:
        video_mp4 = plugintools.find_single_match(data,'"og:video"[ ]content="([^"]+)')
        plugintools.log("dbsowo_play_sendvid="+video_mp4)

    # OPENLOAD
    if "openload" in matches:
        if 'We are sorry!' in data:
             matches = ""
        test = []
        test = get_video_url(matches)
        #plugintools.log("dbsowo_play_openload="+test[0])
        video_url = decodeOpenLoad(data)
        video_mp4 = matches
        plugintools.log("dbsowo_play_openload="+video_url)

    # DAILYMOTION  http://www.dailymotion.com/embed/video/k6w8Ts2VTXFMs4gKJSP?autoPlay=1
    if "dailymotion" in matches:
        video_id = matches.replace("http://www.dailymotion.com/embed/video/", "")
        video_id = video_id.replace("?autoPlay=1", "")
        video_mp4 = "plugin://plugin.video.dailymotion/?url="+video_id+"&mode=playVideo"
        plugintools.log("dbsowo_play_dailymotion="+video_mp4)

    #plugintools.log("video_mp4="+video_mp4)
    return video_mp4

def dbsowo_play_ya(params):
    url=params.get("url")
    plugintools.log("dbsowo_play_ya="+url)
    plugintools.play_resolved_url( url )
    #plugintools.direct_play( url )

def play(item):
   logger.info("[animelatino] play url="+item.url)
   
   itemlist = servertools.find_video_items(data=item.url)
    
   return itemlist

#### OPENLOAD
def decodeOpenLoad(html):
    #aastring = plugintools.find_single_match(html,r'<video(?:.|\s)*?<script\s[^>]*?>((?:.|\s)*?)</script')
    aastring = re.search(r"<video(?:.|\s)*?<script\s[^>]*?>((?:.|\s)*?)</script", html, re.DOTALL | re.IGNORECASE).group(1)
    aastring = aastring.replace("((ﾟｰﾟ) + (ﾟｰﾟ) + (ﾟΘﾟ))", "9")
    aastring = aastring.replace("((ﾟｰﾟ) + (ﾟｰﾟ))","8")
    aastring = aastring.replace("((ﾟｰﾟ) + (o^_^o))","7")
    aastring = aastring.replace("((o^_^o) +(o^_^o))","6")
    aastring = aastring.replace("((ﾟｰﾟ) + (ﾟΘﾟ))","5")
    aastring = aastring.replace("(ﾟｰﾟ)","4")
    aastring = aastring.replace("((o^_^o) - (ﾟΘﾟ))","2")
    aastring = aastring.replace("(o^_^o)","3")
    aastring = aastring.replace("(ﾟΘﾟ)","1")
    aastring = aastring.replace("(c^_^o)","0")
    aastring = aastring.replace("(ﾟДﾟ)[ﾟεﾟ]","\\")
    aastring = aastring.replace("(3 +3 +0)","6")
    aastring = aastring.replace("(3 - 1 +0)","2")
    aastring = aastring.replace("(1 -0)","1")
    aastring = aastring.replace("(4 -0)","4")
    #decodestring = plugintools.find_single_match(aastring,r'\\\+([^(]+)')
    decodestring = re.search(r"\\\+([^(]+)", aastring, re.DOTALL | re.IGNORECASE).group(1)
    decodestring = "\\+"+ decodestring
    decodestring = decodestring.replace("+","")
    decodestring = decodestring.replace(" ","")
    decodestring = decode(decodestring)
    decodestring = decodestring.replace("\\/","/")
    #videourl = plugintools.find_single_match(decodestring,r'="([^"]+)')
    videourl = re.search(r'="([^"]+)', decodestring, re.DOTALL | re.IGNORECASE).group(1)
    plugintools.log("dbsowo_play_openload="+videourl)
    #video_urls = []
    #video_urls.append([".mp4" + " [Openload]", videourl])

    return videourl

def decode(encoded):
    for octc in (c for c in re.findall(r'\\(\d{2,3})', encoded)):
        encoded = encoded.replace(r'\%s' % octc, chr(int(octc, 8)))
    return encoded.decode('utf8')

def test_video_exists(page_url):
    logger.info("[openload.py] test_video_exists(page_url='%s')" % page_url)

    data = scrapertools.cache_page(page_url, headers=headers)

    if 'We are sorry!' in data:
        return False, 'File Not Found or Removed.'

    return True, ""


