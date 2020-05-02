# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Arenavision para SorichTV
# Version 0.1 (22/05/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


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


def general_playlists(params):
    plugintools.log("soritvch.general_playlists "+repr(params))
    #data2 = xbmcgui.Dialog().input("Search to youtube")
    last_search = plugintools.get_setting("last_search")
    data2 = plugintools.keyboard_input(last_search)
    if not data2:
        cap1 = plugintools.get_localized_string(50001)
        cap2 = plugintools.get_localized_string(50002) # Canceled
        plugintools.message(cap1,cap2)
        exit=sys.exit()
        return exit
    data2 = data2.strip()
    plugintools.set_setting("last_search",data2)
    data2 = data2.replace(" ","+")
    sch_lng = plugintools.get_setting("sch_lng")
    #plugintools.message("-",sch_lng)
    url = params.get("url") + data2 + "+" + sch_lng
    #xbmcgui.Dialog().ok("Search to youtube", url)

    try:
        data = plugintools.read( url )
    except:
        cap1 = plugintools.get_localized_string(50001)
        cap2 = plugintools.get_localized_string(50003) # 0 Results
        plugintools.message(cap1,cap2)
        exit=sys.exit()
        return exit

    plugintools.log("data="+data)
    pattern = '<h3 class="yt-lockup-title "><a href="(.*?)</h3>'
    matches = plugintools.find_multiple_matches(data,pattern)

    for entry in matches:
        plugintools.log("=====================================")
        plugintools.log("entry="+entry)
        video_id = plugintools.find_single_match(entry,'v=(.*?)" class')
        plugintools.log("video_id="+video_id)
        title = plugintools.find_single_match(entry,'dir="ltr">(.*?)</a>')
        title2 = plugintools.find_single_match(entry,'"> -(.*?).</span>')
        title = title + "[COLOR yellow]-" + title2 + "[/COLOR]"
        title = title.replace('&quot;','"')
        title = title.strip()
        plot = ""
        thumbnail = "http://img.youtube.com/vi/"+video_id+"/0.jpg"
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id
        plugintools.add_item( action="play" , title=title , plot=plot , url=url , thumbnail=thumbnail , isPlayable=False, folder=False )

