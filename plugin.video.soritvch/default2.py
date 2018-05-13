# -*- coding: utf-8 -*-
#------------------------------------------------------------
# XBMC Add-on for Disney Junior
# Version 1.0.0
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------
# Changelog:
# 1.0.0
# - First release
#---------------------------------------------------------------------------

import os, sys, urlparse, xbmcaddon
import plugintools
#import urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json


from resources.tools.seriesnovelas import *
from resources.tools.arenavision import *
from resources.tools.esport3 import *
from resources.tools.peppapig import *
from resources.tools.dbsowo import *
from resources.tools.ohpelis import *
from resources.tools.ororotv import *
from resources.tools.general import *
from resources.tools.gironatv import *
from resources.tools.channels import *
from resources.tools.vercanalestv import *
from resources.tools.pelismundo import *

# YouTube channel shown (preferences)
YOUTUBE_CHANNEL_ID = plugintools.get_setting("youtube_channel_id")

# Directory's addon
addonDir = xbmcaddon.Addon().getAddonInfo("path")

# Localized strings
T_OFFICIAL_WEBSITE=30002
T_YOUTUBE_CHANNEL=30003
T_SEARCH=30004
T_PREFERENCES=30005
T_LALIGATV=30008
T_SOPCASTLIST=30009
T_SERIESNOVELAS=30010
T_ARENAVISION=30011
T_ESPORT3=30012
T_DBSOWO=30013
T_OROROTV=30014

# Entry point
def run():
    #xbmc.log("### soritvch.run", xbmc.LOGNOTICE)
    plugintools.log("soritvch.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    #plugintools.log("soritvch.main_list "+repr(params))
    xbmc.log("### soritvch.main_list", xbmc.LOGNOTICE)

    plugintools.add_item(
        action="general_playlists",
        title=plugintools.get_localized_string(T_SEARCH),
        thumbnail="http://bioweb.biology.utah.edu/sekercioglu/image.png",
        #url="https://www.youtube.com/results?lclk=long&filters=long&search_query=",
        url = "https://www.youtube.com/results?filters=long%2Cvideo&lclk=video&search_query=",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="peppapig_playlists",
        title="Peppa Pig",
        thumbnail="http://s.sidereel.com/tv_shows/41155/giant_2x/79222-1.jpg",
        url="https://www.youtube.com/results?filters=long&search_query=peppa+pig+espa%C3%B1a&lclk=long",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="peppapig_playlists",
        title="Caillou",
        thumbnail="http://www.cartoonpics.net/data/media/86/caillou.jpg",
        url = "https://www.youtube.com/results?filters=long%2Cvideo&search_query=caillou+espanol&lclk=video",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="peppapig_playlists",
        title="Caillou English",
        thumbnail="https://i.ytimg.com/vi/u6VKXKzUySo/hqdefault.jpg",
        url = "https://www.youtube.com/results?search_query=caillou+cartoon+english",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="peppapig_playlists",
        title="Les tres Bessones",
        thumbnail="http://www.directe.cat/imatges/les-tres-bessones.jpg",
        url = "https://www.youtube.com/results?filters=long%2Cvideo&search_query=les+tres+bessones&lclk=video",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="peppapig_playlists",
        title="The Triplets",
        thumbnail="http://4.bp.blogspot.com/_zFz9LEUoW_8/R36FMS_iLRI/AAAAAAAAACQ/ayg9p4ULhIA/s320/The_Triplets.jpg",
        url = 'https://www.youtube.com/results?q="the+baby+triplets"+cartoon&sp=EgIQAQ%253D%253D',
        isPlayable=False,
        folder=True)

    #plugintools.add_item(
        #action="esport3_playlists",
        #title=plugintools.get_localized_string(T_ESPORT3),
        #thumbnail="https://pbs.twimg.com/profile_images/474564715943690241/p567uWNw_400x400.png",
        #url="http://www.ccma.cat/tv3/directe/esport3/",
        #isPlayable=True,
        #folder=False )

    #plugintools.add_item(
        #action="GiTV_playlists",
        #title="GironaTV",
        #thumbnail="http://www.catosfera.cat/2016/images/logos/tvgirona.jpg",
        #url="",
        #isPlayable=True,
        #folder=False)

    plugintools.add_item(
        action="Channels_playlists",
        title="Channels TV",
        thumbnail=os.path.join(addonDir, "resources", "images", "icon.png"),
        url="",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="JustinTV_playlists",
        title="Justin.tv",
        thumbnail="https://media.licdn.com/media/p/1/000/2ae/3a3/1c3a64d.png",
        url="http://es.justintvstyle.com/",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="VerCanalesTV_playlists",
        title="VerCanalesTV.com",
        thumbnail="http://www.vercanalestv.com/wp-content/uploads/2014/01/vercanalestv4.png",
        url="http://www.vercanalestv.com/ver-gol-tv-en-directo-y-online-las-24h-gratis/",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="ohpelis_playlists",
        title="Oh-Pelis",
        thumbnail="http://www.ohpelis.com/wp-content/uploads/2017/07/logo8.png",
        url="http://www.ohpelis.com",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="pelismundo_playlists",
        title="Pelismundo",
        thumbnail="http://www.pelismundo.com/wp-content/uploads/2015/08/logo.png",
        url="http://www.pelismundo.com/",
        isPlayable=False,
        folder=True)

    #plugintools.add_item( action="search",
    #    title=plugintools.get_localized_string(T_SEARCH) )

    plugintools.add_item(
        action="arenavision_playlists",
        title=plugintools.get_localized_string(T_ARENAVISION),
        thumbnail="http://arenavision.in/sites/default/files/FAVICON_AV2015.png",
        url="",
        isPlayable=False,
        folder=True)

    plugintools.add_item(
        action="dbsowo_playlists",
        title=plugintools.get_localized_string(T_DBSOWO),
        thumbnail="http://cm1.narvii.com/6545/9c98445673df95e56b6430d8c563a7a2a7a62524_120.jpg",
        url="",
        folder=True)

    plugintools.add_item(
        action="ororotv_playlists",
        title=plugintools.get_localized_string(T_OROROTV),
        thumbnail="https://pp.vk.me/c624919/v624919176/72f6/UuzaQbWLjbk.jpg",
        url="https://ororo.tv/es",
        folder=True)

    plugintools.add_item( 
        action="disneyweb", 
        title=plugintools.get_localized_string(T_OFFICIAL_WEBSITE),
        thumbnail="https://static-mh.content.disney.io/matterhorn/assets/logos/nav_logo-89193ebe6563.png",
        url="http://www.disney.es/disney-junior/contenido/video.jsp",
        folder=True)
    
    plugintools.add_item(
        action="youtube_playlists",
        title=plugintools.get_localized_string(T_YOUTUBE_CHANNEL),
        thumbnail="https://www.youtube.com/yts/img/yt_1200-vfl4C3T0K.png",
        url="http://gdata.youtube.com/feeds/api/users/"+YOUTUBE_CHANNEL_ID+"/playlists?v=2&start-index=1&max-results=30",
        folder=True)

    plugintools.add_item(
        action="laligatv_playlists",
        title=plugintools.get_localized_string(T_LALIGATV),
        thumbnail="http://files.laliga.es/201402/855x481_06172611noticia-la-liga-tv.es.jpg",
        url="http://www.lfp.es/laligatv",
        folder=True)
    
    plugintools.add_item(
        action="livefootballol_playlists",
        title=plugintools.get_localized_string(T_SOPCASTLIST),
        thumbnail="http://www.livefootballol.me/images/logo.png",
        url="http://www.livefootballol.com/sopcast-channel-list.html",
        folder=True)
        
    plugintools.add_item(
        action="seriesnovelas_playlists",
        title=plugintools.get_localized_string(T_SERIESNOVELAS),
        thumbnail="http://www.verseriesynovelas.com/wp-content/themes/maco/css/images/logo-verseriesynovelas.com.png",
        url="",
        folder=True)

    plugintools.add_item(
        action="preferences",
        title=plugintools.get_localized_string(T_PREFERENCES),
        thumbnail=os.path.join(addonDir, "resources", "images", "icon.png"),
        isPlayable=False,
        folder = False )


# Show all videos from the official website
def disneyweb(params):
    plugintools.log("soritvch.disneyweb "+repr(params))
    

    # Fetch video list from YouTube feed
    data = plugintools.read( params.get("url") )
    data = plugintools.find_single_match( data , '<div id="video_main_promos_inner">(.*?)<div id="content_index_navigation">')
    
    # Extract items from feed
    '''
    <div class="promo" style="background-image: url(/cms_res/disney-junior/images/promo_support/promo_holders/video.png);">
        <a href="/disney-junior/contenido/video/canta_con_dj_arcoiris.jsp " class="promoLinkTracking"><img src="/cms_res/disney-junior/images/video/canta_dj_arco_iris_164x104.jpg" class="promo_image" alt=""/></a>
        <div class="promo_title_3row"><p>Canta con DJ: La canción del arco iris</p></div>
        <a class="playlist_button_large"  href="" ref="canta_con_dj_arcoiris"><img src="/cms_res/disney-junior/images/promo_support/playlist_add_icon.png" alt="" /></a>
    </div>
    '''
    pattern  = '<div class="promo"[^<]+'
    pattern += '<a href="([^"]+)"[^<]+'
    pattern += '<img src="([^"]+)"[^<]+'
    pattern += '</a[^<]+'
    pattern += '<div[^<]+'
    pattern += '<p>([^<]+)</p>'
    matches = plugintools.find_multiple_matches(data,pattern)
    
    for scrapedurl, scrapedthumbnail, scrapedtitle in matches:
        # Not the better way to parse XML, but clean and easy
        title = scrapedtitle
        thumbnail = urlparse.urljoin( params.get("url") , scrapedthumbnail )
        url = urlparse.urljoin( params.get("url") , scrapedurl.strip() )
        plot = ""

        # Appends a new item to the xbmc item list
        plugintools.add_item( action="disneyweb_play" , title=title , plot=plot , url=url ,thumbnail=thumbnail , isPlayable=True, folder=False )

# Play one video from the official website
def disneyweb_play(params):
    plugintools.log("soritvch.disneyweb_play "+repr(params))

    # Fetch page
    data = plugintools.read( params.get("url") )

    url_start = plugintools.find_single_match( data , "config.rtmpeServer \= '([^']+)'")
    plugintools.log("soritvch.disneyweb_play url_start="+url_start)

    url_end = plugintools.find_single_match( data , "config.firstVideoSource \= '([^']+)'")
    plugintools.log("soritvch.disneyweb_play url_end="+url_end)
    
    url = url_start + url_end
    plugintools.log("soritvch.disneyweb_play url="+url)

    plugintools.play_resolved_url( url )

# Show all YouTube playlists for the selected channel
def youtube_playlists(params):
    plugintools.log("soritvch.youtube_playlists "+repr(params))

    # Fetch video list from YouTube feed
    data = plugintools.read( params.get("url") )
    plugintools.log("data="+data)
    
    # Extract items from feed
    pattern = ""
    matches = plugintools.find_multiple_matches(data,"<entry(.*?)</entry>")
    
    for entry in matches:
        plugintools.log("entry="+entry)
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,"<titl[^>]+>([^<]+)</title>")
        plot = plugintools.find_single_match(entry,"<media\:descriptio[^>]+>([^<]+)</media\:description>")
        thumbnail = plugintools.find_single_match(entry,"<media\:thumbnail url='([^']+)'")
        url = plugintools.find_single_match(entry,"<content type\='application/atom\+xml\;type\=feed' src='([^']+)'/>")

        # Appends a new item to the xbmc item list
        plugintools.add_item( action="youtube_videos" , title=title , plot=plot , url=url , thumbnail=thumbnail , folder=True)

# Show all YouTube videos for the selected playlist
def youtube_videos(params):
    plugintools.log("soritvch.youtube_videos "+repr(params))

    # Fetch video list from YouTube feed
    data = plugintools.read( params.get("url") )
    plugintools.log("data="+data)
    
    # Extract items from feed
    pattern = ""
    matches = plugintools.find_multiple_matches(data,"<entry(.*?)</entry>")
    
    for entry in matches:
        plugintools.log("entry="+entry)
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,"<titl[^>]+>([^<]+)</title>")
        title = title.replace("Disney Junior España | ","")
        plot = plugintools.find_single_match(entry,"<summa[^>]+>([^<]+)</summa")
        thumbnail = plugintools.find_single_match(entry,"<media\:thumbnail url='([^']+)'")
        video_id = plugintools.find_single_match(entry,"http\://www.youtube.com/watch\?v\=([0-9A-Za-z_-]{11})")
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id

        # Appends a new item to the xbmc item list
        plugintools.add_item( action="play" , title=title , plot=plot , url=url , thumbnail=thumbnail , isPlayable=True, folder=False )

def JustinTV_playlists(params):
    plugintools.log("JustinTV_playlists")
    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Mega Movies Accion",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/mega_movieshd.png",
        #url="https://vaughnlive.tv/mega_movieshd",
        url="mega_movieshd",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Zonafilms",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/zonafilmshd.png",
        url="zonafilmshd",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Morena",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/morena_channels12.png",
        #url="plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=morena_channels12",
        url="morena_channels12",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Cinestar",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/cine_star.png",
        url="cine_star",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Katy HD",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/katyhd.png",
        url="katyhd",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Crème",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/lcreme_staff.png",
        url="lcreme_staff",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Vitato TV",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/vitatotv.png",
        url="vitatotv",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Ochin",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/ochin1a.png",
        url="ochin1a",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Broad Movies",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/broadmovieshd.png",
        url="broadmovieshd",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Peliculas 300",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/300.png",
        url="300",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Mega Extremo",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/mega_extremo.png",
        url="mega_extremo",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Osvaldo",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/osvaldoquezada.png",
        url="osvaldoquezada",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="lcrememax",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/lcrememax.png",
        url="lcrememax",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Misterioso",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/misterioso777.png",
        url="misterioso777",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Chinomex",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/chinomex2.png",
        url="chinomex2",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Cine Calidad",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/cine_calidad.png",
        url="cine_calidad",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="Luis Lage TV",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/luislage.png",
        url="luislage",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="lcreme Dreams",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/lcreme_dreams.png",
        url="lcreme_dreams",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_Vaughn",
        title="lcreme Horror",
        thumbnail="http://thumbnails.vaughnsoft.com/1/fetch/live/lcreme_horror.png",
        url="lcreme_horror",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/fzn_VX_FLEc/default.jpg",
        url="fzn_VX_FLEc",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/oMRNGYZf9UE/default.jpg",
        url="oMRNGYZf9UE",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/CuKrmTSaNi4/default.jpg",
        url="CuKrmTSaNi4",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/rxGJU6i2_jo/default.jpg",
        url="rxGJU6i2_jo",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/DLAB0GSG2sE/default.jpg",
        url="DLAB0GSG2sE",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/652ayuYcGro/default.jpg",
        url="652ayuYcGro",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/LxXfondFXX8/default.jpg",
        url="LxXfondFXX8",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/wppqLAeWoM4/default.jpg",
        url="wppqLAeWoM4",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/-LafsvGL6tQ/default.jpg",
        url="-LafsvGL6tQ",
        isPlayable=True,
        folder=False)

    plugintools.add_item(
        action="JustinTV_playlists_YouTube",
        title="Peliculas",
        thumbnail="https://i.ytimg.com/vi/AwGRX2r-Xo8/default.jpg",
        url="AwGRX2r-Xo8",
        isPlayable=True,
        folder=False)

def JustinTV_playlists_Vaughn(params):
    ch = params.get("url")
    url = "plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel="+ch
    plugintools.play_resolved_url(url)
    #plugintools.log("url="+url)
    #plugintools.play_resolved_url(url)

def JustinTV_playlists_YouTube(params):
    ch = params.get("url")
    url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+ch
    plugintools.play_resolved_url(url)

# Show all laligatv playlists for the oficial page
def laligatv_playlists(params):
    plugintools.log("soritvch.laligatv_playlists "+repr(params))

    # Fetch video list from laligatv feed
    data = plugintools.read(params.get("url"))
    plugintools.log("data="+data)
    
    thumbnail = params.get("thumbnail")
    plugintools.log("thumbnail= "+thumbnail)
    
    plugintools.add_item(action="", title = '[B][I][COLOR darkviolet]LALIGATV.ES[/B][/I][/COLOR]', url = "", thumbnail = 'http://files.lfp.es/201402/640x360_06172611noticia-la-liga-tv.es.jpg' , fanart = 'https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash3/556377_550288405007723_1790184113_n.jpg' , folder = False, isPlayable = False)
    plugintools.add_item(action="", title = '[B][I][COLOR white]Las emisiones comenzarán 15 minutos antes de cada partido[/B][/I][/COLOR]', url = "", thumbnail = 'http://files.lfp.es/201402/640x360_06172611noticia-la-liga-tv.es.jpg' , fanart = 'https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash3/556377_550288405007723_1790184113_n.jpg' , folder = False, isPlayable = False)
    plugintools.add_item(action="", title = "", url = "", thumbnail = 'http://files.lfp.es/201402/640x360_06172611noticia-la-liga-tv.es.jpg' , fanart = 'https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash3/556377_550288405007723_1790184113_n.jpg' , folder = False, isPlayable = False)
    
    match_total = plugintools.find_single_match(data, 'id=\"coming-soon\"(.*?)fb-root')
    plugintools.log("match_total= "+match_total)
    
    matches_dia = plugintools.find_single_match(data, 'id=\"coming-soon\"(.*?)</div></div>')
    plugintools.log("matches_dia= "+matches_dia) 
    
    jornada = plugintools.find_multiple_matches(match_total, 'class=\"title_jornada\">(.*?)</div>')
    print 'jornada',jornada
    
    matches = plugintools.find_multiple_matches(matches_dia, '<a href="(.*?)</a>')
    plugintools.add_item(action="" , title = '[COLOR lavender][B]' + jornada[0] + '[/B][/COLOR]' , thumbnail = thumbnail , folder = False , isPlayable = False)

    
    # Extract items from feed
    for entry in matches:
        plugintools.log("entry= "+entry)
        url_partido = entry.split('"')
        url_partido = url_partido[0]
        url_partido = url_partido.strip()
        plugintools.log("url_partido= "+url_partido)
        hora = plugintools.find_single_match(entry, 'hora_partido_otras_competiciones\">(.*?)</span>')
        plugintools.log("hora= "+hora)
        local = plugintools.find_single_match(entry, 'equipo_local_otras_competiciones\">(.*?)</span>')
        visitante = plugintools.find_single_match(entry, 'equipo_visitante_otras_competiciones\">(.*?)</span>')
        plugintools.log("local= "+local)
        plugintools.log("visitante= "+visitante)
        thum = "http://files.lfp.es/apps/laligatv/infografias/2014/c2_j21_"+local+"_"+visitante+"_19082014.jpg"
        thum = thum.replace("á","a")
        thum = thum.replace("é","e")
        thum = thum.replace("í","i")
        thum = thum.replace("ó","o")
        thum = thum.replace("ú","u")
        thum = thum.replace(" ","-")
        thum = thum.lower()
        print 'thumbnail = ',thum
        #plugintools.add_item(action="adelante_geturl" , title = '[COLOR lightyellow][B](' + hora + ')[/B][/COLOR][COLOR white] ' + local + ' - ' + visitante + ' [/COLOR]' , url = url_partido , thumbnail = params.get("thumbnail") , folder = False , isPlayable = True)
        plugintools.add_item(action="adelante_geturl" , title = '[COLOR lightyellow][B](' + hora + ')[/B][/COLOR][COLOR white] ' + local + ' - ' + visitante + ' [/COLOR]' , url = url_partido , thumbnail = thum , folder = False , isPlayable = True)

    if len(jornada) >= 2:
        plugintools.add_item(action="" , title = '[COLOR lavender][B]' + jornada[1] + '[/B][/COLOR]' , thumbnail = thumbnail , folder = False , isPlayable = False)
        matches_dia = plugintools.find_single_match(match_total, jornada[1]+'(.*?)</div></div>')
        plugintools.log("matches_dia= "+matches_dia)
        matches = plugintools.find_multiple_matches(matches_dia, '<a href="(.*?)</a>')
        for entry in matches:
            plugintools.log("entry= "+entry)
            url_partido = entry.split('"')
            url_partido = url_partido[0]
            url_partido = url_partido.strip()
            plugintools.log("url_partido= "+url_partido)
            hora = plugintools.find_single_match(entry, 'hora_partido_otras_competiciones\">(.*?)</span>')
            plugintools.log("hora= "+hora)
            local = plugintools.find_single_match(entry, 'equipo_local_otras_competiciones\">(.*?)</span>')
            visitante = plugintools.find_single_match(entry, 'equipo_visitante_otras_competiciones\">(.*?)</span>')
            plugintools.log("local= "+local)
            plugintools.log("visitante= "+visitante)
            thum = "http://files.lfp.es/apps/laligatv/infografias/2014/c2_j21_"+local+"_"+visitante+"_19082014.jpg"
            thum = thum.replace("á","a")
            thum = thum.replace("é","e")
            thum = thum.replace("í","i")
            thum = thum.replace("ó","o")
            thum = thum.replace("ú","u")
            thum = thum.replace(" ","-")
            thum = thum.lower()
            print 'thumbnail = ',thum
            plugintools.add_item(action="adelante_geturl" , title = '[COLOR lightyellow][B](' + hora + ')[/B][/COLOR][COLOR white] ' + local + ' - ' + visitante + ' [/COLOR]' , url = url_partido , thumbnail = thum, folder = False , isPlayable = True)
            #plugintools.add_item(action="adelante_geturl" , title = '[COLOR lightyellow][B](' + hora + ')[/B][/COLOR][COLOR white] ' + local + ' - ' + visitante + ' [/COLOR]' , url = url_partido , thumbnail = params.get("thumbnail") , folder = False , isPlayable = True)

def livefootballol_playlists(params):
    
    T_UPDATED=39001
    tupdated=plugintools.get_localized_string(T_UPDATED)
    
    plugintools.log("soritvch.livefootballol_playlists "+repr(params))

    # Fetch video list from livefootballol feed
    data = plugintools.read( params.get("url") )
    data = data.replace('\r', '')
    data = data.replace('\n', '')
    
    # Actualizado.....
    ldate = plugintools.find_single_match(data,'<div class="modifydate">Checked weekly. Last Check: (.*?)</div>') 
    plugintools.log("ldate="+ldate)
    plugintools.log("---------------------------------------------")
    plugintools.add_item(action="", title = "[COLOR yellow][B]"+tupdated+" "+ldate+"[/B][/COLOR]", url = "", thumbnail = "", fanart = "", folder = False, isPlayable = False)
    
    # Simplificar XML
    data = plugintools.find_single_match(data,'<table(.*?)</table>')
    plugintools.log("data="+data)
    plugintools.log("---------------------------------------------")
    
    # Extract items from feed
    pattern = "<td><a href=(.*?)</tr>"
    plugintools.log("pattern="+pattern)
    matches = plugintools.find_multiple_matches(data, pattern)
    plugintools.log("---------------------------------------------")
    
    plugintools.log("gen entries")
    for entry in matches:
        #plugintools.log("entry="+entry)
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,"><strong>(.*?)</strong>")
        plot = ""
        thumbnail = ""
        url = plugintools.find_single_match(entry,"</a></td><td>(.*?)</td>")
        url = 'plugin://plugin.video.p2p-streams/?url=' + url + '&mode=2&name='
        url = url.strip()

        # Appends a new item to the xbmc item list
        plugintools.add_item( action="play" , title=title , plot=plot , url=url , thumbnail=thumbnail , isPlayable=True, folder=False )

def seriesnovelas_playlists(params):
    plugintools.add_item(
        action="livefootballol_playlists",
        title="Series en Estreno",
        url="http://www.verseriesynovelas.com/genero/estrenos",
        folder=True)
    
    plugintools.add_item(
        action="seriesnovelas_lista_playlists",
        title="Lista de Series",
        url="http://www.verseriesynovelas.com/lista-de-series",
        folder=True)

    plugintools.add_item(
        action="livefootballol_playlists",
        title="Nuevos Episodios",
        url="http://www.verseriesynovelas.com/archivos/nuevo",
        folder=True)

def arenavision_playlists(params):
    plugintools.add_item(
        action="arenavision_playlists_agenda",
        title="Agenda de Eventos",
        thumbnail="http://arenavision.in/sites/default/files/FAVICON_AV2015.png",
        url="http://arenavision.in/iguide/",
        folder=True)

    plugintools.add_item(
        action="arenavision_playlists_canales_ace",
        title="Canales AceStream",
        thumbnail="http://arenavision.in/sites/default/files/FAVICON_AV2015.png",
        url="http://arenavision.in/",
        folder=True)

    plugintools.add_item(
        action="arenavision_playlists_canales_sop",
        title="Canales SopCast",
        thumbnail="http://arenavision.in/sites/default/files/FAVICON_AV2015.png",
        url="http://arenavision.in/",
        folder=True)

def adelante_geturl(params):
    plugintools.log("soritvch.LaLigatv.es getURL: "+repr(params))

    data = plugintools.read(params.get("url"))
    plugintools.log("data= "+data)
    url = plugintools.find_single_match(data, 'src: escape\(\"(.*?)\"')    
    plugintools.log("URL= "+url)
    plugintools.play_resolved_url(url)


# Play selected video
def play(params):
    plugintools.play_resolved_url( params.get("url") )
    data = plugintools.find_single_match(data,'<table(.*?)</table>')

# Open preferences dialog
def preferences(params):
    plugintools.log("soritvch.configuracion "+repr(params))

    plugintools.open_settings_dialog()

# Open a popup dialog for input search terms, then call the result function
def search(params):
    plugintools.log("soritvch.search "+repr(params))

    last_search = plugintools.get_setting("last_search")
    texto = plugintools.keyboard_input(last_search)
    plugintools.set_setting("last_search",texto)

    params["texto"]=texto
    
    youtube_search(params)

# Show first 50 videos from YouTube that matches a search string
def youtube_search(params):
    plugintools.log("soritvch.search "+repr(params))

    # Fetch video list from YouTube feed
    data = plugintools.read( "https://gdata.youtube.com/feeds/api/videos?q="+params.get("texto").replace(" ","+")+"&orderby=published&start-index=1&max-results=50&v=2&lr="+plugintools.get_setting("youtube_language") )
    plugintools.log("data="+data)
    
    # Extract items from feed
    pattern = ""
    matches = plugintools.find_multiple_matches(data,"<entry(.*?)</entry>")
    
    for entry in matches:
        plugintools.log("entry="+entry)
        
        # Not the better way to parse XML, but clean and easy
        title = plugintools.find_single_match(entry,"<titl[^>]+>([^<]+)</title>")
        plot = plugintools.find_single_match(entry,"<summa[^>]+>([^<]+)</summa")
        thumbnail = plugintools.find_single_match(entry,"<media\:thumbnail url='([^']+)'")
        video_id = plugintools.find_single_match(entry,"http\://www.youtube.com/watch\?v\=([0-9A-Za-z_-]{11})")
        if video_id=="":
            video_id = plugintools.find_single_match(entry,"https\://www.youtube.com/watch\?v\=([0-9A-Za-z_-]{11})")
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id

        # Appends a new item to the xbmc item list
        plugintools.add_item( action="play" , title=title , plot=plot , url=url , thumbnail=thumbnail , isPlayable=True, folder=False )


run()
