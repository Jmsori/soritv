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

T_ESPORT3 = plugintools.get_localized_string(30012)
T_PSWD = plugintools.get_localized_string(50004)

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')

def Channels_playlists(params):
    xbmc.log("### Channels_playlists", xbmc.LOGNOTICE)
    plugintools.add_item(
        action="Escalenc_playlists",
        title="L'Escala TV",
        thumbnail="http://www.canal10.cat/img/logofacebook_400x400.jpg",
        url="",
        isPlayable=True,
        folder=False )

    plugintools.add_item(
        action="GiTV_playlists",
        title="GironaTV",
        thumbnail="http://www.catosfera.cat/2016/images/logos/tvgirona.jpg",
        url="",
        isPlayable=True,
        folder=False )

    plugintools.add_item(
        action="esport3_playlists",
        title=T_ESPORT3,
        thumbnail="http://statics.ccma.cat/multimedia/png/8/6/1466523023568.png",
        url="http://www.ccma.cat/tv3/directe/esport3/",
        isPlayable=True,
        folder=False )

    plugintools.add_item(
        action="SyFy_playlists",
        title="SyFy",
        thumbnail="http://www.syfy.com/sites/syfy/files/tve_auth2/Syfylogo.png",
        url="http://163.172.52.83:8000/live/1024r1mN991908/19mQH9092JEs44/201.m3u8",
        isPlayable=True,
        folder=False )

    plugintools.add_item(
        action="MiamiTV_playlists",
        title="Dark",
        thumbnail="http://darktv.es/wp-content/uploads/2017/06/logoprincipal.png",
        #url="http://smartiptvspain1.mine.nu:980/live/Ronnie/Ronnie/53445.m3u8",
        url="http://xxedge61.livesports.pw/live/verdarkes07ff3fa6e4dc81d3/index.m3u8?token=iM8yghZDdFwnDs0UbeClyg&expires=1506281690",
        isPlayable=True,
        folder=False )

    plugintools.add_item(
        action="MiamiTV_playlists",
        title="MiamiTV",
        thumbnail="http://www.miamitvchannel.com/images/LOGOMIAMITVNEW300.png",
        url="http://usaserver.miamitvchannel.com/miamitv/smil:miamitv/chunklist_w1612796246_b2592000.m3u8",
        isPlayable=True,
        folder=False )

    plugintools.add_item(
        action="JustinTV_playlists",
        title="JustinTV",
        thumbnail="https://res.cloudinary.com/crunchbase-production/image/upload/v1398213955/ckpauuvnmyk5wg6h306y.jpg",
        url="",
        isPlayable=True,
        folder=False )


def Escalenc_playlists(params):
    plugintools.log("Escalenc_playlists")
    url = 'http://ventdelnord.tv:8080/escala/directe.m3u8'
    plugintools.play_resolved_url( url )

def esport3_playlists(params):
    url = 'http://ccma-tva-es-abertis-live.hls.adaptive.level3.net/es/ngrp:es3_web/playlist.m3u8'
    plugintools.play_resolved_url( url )


def GiTV_playlists(params):
    #url = 'rtmp://tvgirona.dnssw.net/live/<playpath>Icontouch <swfUrl>http://p.jwpcdn.com/6/12/jwplayer.flash.swf <pageUrl>http://www.tvgirona.cat/playertvgirona/playertvgirona.htm'
    url = "rtmp://tvgirona.dnssw.net/live/Icontouch"
    plugintools.play_resolved_url( url )


def SyFy_playlists(params):
    url = params.get("url")
    xbmc.log("### "+url, xbmc.LOGNOTICE)
    # http://www.vercanalestv.com/ver-syfy-hd-online-en-castellano-en-directo-gratis-24h-por-internet/
    #url = "http://cdn66.verliga.club/hls/live/syfy/index.m3u8"
    plugintools.play_resolved_url( url )


def MiamiTV_playlists(params):
    #url = plugintools.read( params.get("url") )
    url = params.get("url")

    texto = plugintools.keyboard_input("")
    num = strtoint(texto)
    if num == 9898:
        #url = 'http://usaserver.miamitvchannel.com/miamitv/smil:miamitv/chunklist_w1612796246_b2592000.m3u8'
        plugintools.play_resolved_url( url )
    else:
        #line1 = T_PSWD
        #time = 5000 #in miliseconds
        #xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
        cap1 = plugintools.get_localized_string(50001)
        cap2 = plugintools.get_localized_string(50004) # wrong password
        plugintools.message(cap1,cap2)
        return False


def JustinTV_playlists(params):
    url = "http://vaughnlive.tv/platinum_hd"
    plugintools.play_resolved_url( url )


def strtoint(s):
    try:
        return int(s)
    except:
        #return float(s)
        return 0

def Ver_playlists(params):
    xbmc.log("### Ver_playlists", xbmc.LOGNOTICE)
    plugintools.log("Ver_playlists")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url = params.get("url")
    try:
       data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
       xbmc.log("data= "+data, xbmc.LOGNOTICE)
    except:
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+data)
        data=""
        xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)
        return
        pass
    plugintools.play_resolved_url(url)

