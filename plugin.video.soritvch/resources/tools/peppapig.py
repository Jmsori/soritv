# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Arenavision para SorichTV
# Version 0.1 (22/05/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import plugintools


def peppapig_playlists(params):
    plugintools.log("soritvch.peppapig_playlists "+repr(params))
    data = plugintools.read( params.get("url") )
    plugintools.log("data="+data)
    pattern = '<h3 class="yt-lockup-title "><a href="(.*?)</h3>'
    plugintools.log("_________matches_________")
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
        #plot = plugintools.find_single_match(entry,"<summa[^>]+>([^<]+)</summa")
        plot = ""
        #thumbnail = plugintools.find_single_match(entry,"<media\:thumbnail url='([^']+)'")
        thumbnail = "http://img.youtube.com/vi/"+video_id+"/0.jpg"

        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id
        #plugintools.play_resolved_url( url )
        #if title.find("Pig") != -1: 
        plugintools.add_item( action="play" , title=title , plot=plot , url=url , thumbnail=thumbnail , isPlayable=False, folder=False )

def peppapig2_playlists(params):
    plugintools.log("soritvch.peppapig2_playlists "+repr(params))
    #url=params.get("url")
    #video_id = url.split("https://www.youtube.com/watch?v=")
    video_id = "AqOyWr9tI28&list=PL3_jGbziVMuEQlNiTD8MUO9zTUinTOiQI"
    url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id
    #url = "https://www.youtube.com/watch?v=Z1VZAsE7SS8"
    plugintools.log("url= "+url)
    plugintools.play_resolved_url( url )
    
