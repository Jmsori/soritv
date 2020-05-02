# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Pelismundo para SorichTV
# Version 0.1 (23/09/2017)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import plugintools
import xbmc
import xbmcaddon
import xbmcgui


#__addon__ = xbmcaddon.Addon()
#__addonname__ = __addon__.getAddonInfo('name')
#__icon__ = __addon__.getAddonInfo('icon')

def pelismundo_playlists(params):
    #xbmc.log("### ohpelis_playlists", xbmc.LOGNOTICE)
    plugintools.log("pelismundo_playlists")
    plugintools.add_item(
        action="estrenos_playlists",
        title="Últimos estrenos",
        thumbnail="http://www.pelismundo.com/wp-content/uploads/2015/08/logo.png",
        url="http://www.pelismundo.com/",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="castellano_playlists",
        title="Castellano",
        thumbnail="http://www.pelismundo.com/wp-content/uploads/2015/08/logo.png",
        url="http://www.pelismundo.com/lenguaje/castellano/",
        page="0",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="latino_playlists",
        title="Latino",
        thumbnail="http://www.pelismundo.com/wp-content/uploads/2015/08/logo.png",
        url="http://www.pelismundo.com/lenguaje/latino/",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="subtitulada_playlists",
        title="Subtitulada",
        thumbnail="http://www.pelismundo.com/wp-content/uploads/2015/08/logo.png",
        url="http://www.pelismundo.com/lenguaje/subtitulada/",
        isPlayable=False,
        folder=True)


def estrenos_playlists(params):
    #xbmc.log("### ohpelis_peliculas_playlists", xbmc.LOGNOTICE)
    plugintools.log("pelismundo_estrenos_playlists")
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
    matches = plugintools.find_single_match(data,'<div id="page-side-center">(.*?)<h2>Proximamente</h2>')
    #plugintools.log("data="+matches)
    movies = plugintools.find_multiple_matches(matches,'<a href="(.*?)</a>')
    for entry in movies:
        #plugintools.log("entry="+entry)
        url = plugintools.find_single_match(entry,'(.*?)" class')
        #plugintools.log("url="+url)
        thumbnail = plugintools.find_single_match(entry,'<img class="im2load toreflect" src="(.*?)" alt')
        #plugintools.log("thumbnail="+thumbnail)
        title = plugintools.find_single_match(entry,'<div class="label">(.*?)</div>')
        #plugintools.log("title="+title)
        plot = title
        #plugintools.log("plot="+plot)
        plugintools.add_item(
            action="estrenos_conectores_playlists",
            title=title,
            thumbnail=thumbnail,
            url=url,
            plot=plot,
            isPlayable=False,
            folder=True)

def estrenos_conectores_playlists(params):
    plugintools.log("estrenos_conectores_playlists")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    request_headers.append(["referrer","http://verdirectotv.com/tv/digitales2/plustoros.html"])
    url_main = params.get("url")
    #plugintools.log("url_main="+url_main)
    plot = params.get("plot")
    thumbnail = params.get("thumbnail")
    title = params.get("title")
    try:
       data,response_headers = plugintools.read_body_and_headers(url_main, headers=request_headers)
    except:
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+data)
        data=""
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url_main)
        return
        pass
    #https://my.mail.ru/video/embed/3641166504956794027
    movies = plugintools.find_multiple_matches(data,'<a id="op(.*?)clearfix')
    i = 0
    for entry in movies:
        i = i + 1
        plugintools.log("entry="+entry)
        url = plugintools.find_single_match(entry,'rel="(.*?)" class')
        plugintools.log("url="+url)
        plugintools.add_item(
            action="direct_play",
            title="Opción " + str(i) + " (" + url + ")",
            thumbnail=thumbnail,
            url=url,
            plot=plot,
            isPlayable=True,
            folder=False)

def direct_play(params):
    url = params.get("url")
    plugintools.play_resolved_url( url )
    #plugintools.direct_play( url )







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


def estrenos2222_playlists(params):
    #xbmc.log("### ohpelis_estrenos_playlists", xbmc.LOGNOTICE)
    plugintools.log("ohpelis_estrenos_playlists")

def num(s):
    try:
        return int(s)
    except ValueError:
        return 1

