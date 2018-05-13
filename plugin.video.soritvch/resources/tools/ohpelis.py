# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Oh-Pelis para SorichTV
# Version 0.1 (11/08/2017)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import plugintools
import xbmc
import xbmcaddon
import xbmcgui
#from core import logger
#import openload

#__addon__ = xbmcaddon.Addon()
#__addonname__ = __addon__.getAddonInfo('name')
#__icon__ = __addon__.getAddonInfo('icon')

def ohpelis_playlists(params):
    #xbmc.log("### ohpelis_playlists", xbmc.LOGNOTICE)
    plugintools.log("ohpelis_playlists")
    plugintools.add_item(
        action="peliculas_playlists",
        title="Películas",
        thumbnail="http://www.ohpelis.com/wp-content/uploads/2017/07/logo8.png",
        url="http://www.ohpelis.com/peliculas/",
        page="0",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="series_playlists",
        title="Series",
        thumbnail="http://www.ohpelis.com/wp-content/uploads/2017/07/logo8.png",
        url="http://www.ohpelis.com/series/",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="infantil_playlists",
        title="Infantil",
        thumbnail="http://www.ohpelis.com/wp-content/uploads/2017/07/logo8.png",
        url="http://www.ohpelis.com/genero/infantil/",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="estrenos_playlists",
        title="Últimos estrenos",
        thumbnail="http://www.ohpelis.com/wp-content/uploads/2017/07/logo8.png",
        url="http://www.ohpelis.com/release/2017/",
        isPlayable=False,
        folder=True)


def peliculas_playlists(params):
    #xbmc.log("### ohpelis_peliculas_playlists", xbmc.LOGNOTICE)
    plugintools.log("ohpelis_peliculas_playlists")
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
    #matches = plugintools.find_single_match(data,'<iframe[^c]+c="([^"]+)')
    matches = plugintools.find_multiple_matches(data,'item movies">(.*?)</article>')
    for entry in matches:
        #plugintools.log("entry="+entry)
        url = plugintools.find_single_match(entry,'<a href="(.*?)">')
        #plugintools.log("url="+url)
        thumbnail = plugintools.find_single_match(entry,'<img src="(.*?)" alt')
        #plugintools.log("thumbnail="+thumbnail)
        title = plugintools.find_single_match(entry,'alt="(.*?)"></a>')
        #plugintools.log("title="+title)
        plot = plugintools.find_single_match(entry,'class="texto">(.*?)"><div')
        #plugintools.log("plot="+plot)
        plugintools.add_item(
            action="play_peliculas_playlists",
            title=title,
            thumbnail=thumbnail,
            url=url,
            plot=plot,
            isPlayable=True,
            folder=False)
    line = plugintools.find_single_match(data,'pagination"><span>(.*?)</span>')
    actpage = plugintools.find_single_match(line,'Página (.*?) de')
    pageurl=params.get("page")
    #plugintools.log("maxpage1="+pageurl)
    if pageurl == "0":
        maxpage = plugintools.find_single_match(data,actpage+' de (.*?)</span>')
    else:
        maxpage = pageurl
    #plugintools.log("line="+str(line))
    #plugintools.log("actpage="+actpage)
    #plugintools.log("maxpage="+maxpage)
    nactpage = num(actpage)
    nmaxpage = num(maxpage)
    if nactpage < nmaxpage:
        actpage = str(nactpage + 1)
        #plugintools.log("actpage="+actpage)
        url="http://www.ohpelis.com/peliculas/page/" + actpage + "/"
        #plugintools.log("url="+url)
        plugintools.add_item(
            action="peliculas_playlists",
            title=line,
            thumbnail="http://www.ohpelis.com/wp-content/uploads/2017/07/logo8.png",
            url="http://www.ohpelis.com/peliculas/page/" + actpage + "/",
            plot="",
            page=maxpage,
            isPlayable=False,
            folder=True)

def play_peliculas_playlists(params):
    plugintools.log("ohpelis_play_peliculas_series_playlists")
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
    url = plugintools.find_single_match(data,'rptss" src="(.*?)" frameborder')
    plugintools.log("url="+url)
    #plugintools.log(test_video_exists(url))

    uurl = "plugin://plugin.video.alfa/?"+url
    xbmc.executebuiltin("xbmc.PlayMedia("+uurl+")")



    #plugintools.play_resolved_url( url )
    #plugintools.direct_play( url )





def series_playlists(params):
    #xbmc.log("### ohpelis_series_playlists", xbmc.LOGNOTICE)
    plugintools.log("ohpelis_series_playlists")


def infantil_playlists(params):
    #xbmc.log("### ohpelis_infantil_playlists", xbmc.LOGNOTICE)
    plugintools.log("ohpelis_infantil_playlists")


def estrenos_playlists(params):
    #xbmc.log("### ohpelis_estrenos_playlists", xbmc.LOGNOTICE)
    plugintools.log("ohpelis_estrenos_playlists")

def num(s):
    try:
        return int(s)
    except ValueError:
        return 1

