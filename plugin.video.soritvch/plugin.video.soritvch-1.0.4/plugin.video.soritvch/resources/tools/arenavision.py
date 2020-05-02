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


def arenavision_playlists_agenda(params):
    plugintools.log("arenavision_playlists_agenda")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"])
    request_headers.append(["referrer","http://arenavision.in/iguide"])
    url = params.get("url")
    try:
        data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    except: data="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de:","\n"+url)

    #ret = xbmcgui.Dialog().select('Choose a playlist', ['Playlist #1', 'Playlist #2', 'Playlist #3'])
    #xbmcgui.Dialog().ok("Error",str(ret))

    if data:
        plugintools.log("url="+url)
        plugintools.log("data="+data)
        data = data.replace('<br />',' ')
        data = data.replace('[SPA]','[COLOR red][SPA][/COLOR]')
        date_data = plugintools.find_multiple_matches(data,'<td class="auto-style3" style="width: 230px">(.*?)</td>')
        time_data = plugintools.find_multiple_matches(data,'<td class="auto-style3" style="width: 215px">(.*?)</td>')
        type_data = plugintools.find_multiple_matches(data,'<td class="auto-style3" style="width: 291px">(.*?)</td>')
        liga_data = plugintools.find_multiple_matches(data,'<td class="auto-style3" style="width: 418px">(.*?)</td>')
        even_data = plugintools.find_multiple_matches(data,'<td class="auto-style3" style="width: 897px">(.*?)</td>')
        chnl_data = plugintools.find_multiple_matches(data,'<td class="auto-style3" style="width: 489px">(.*?)</td>')
        #plugintools.log("data="+data)
        #for i in range(1,21):
        #    a = 'AV'+str(i)
        #    data = data.replace(a+'/','[COLOR red]'+a+'[/COLOR]/')
        #data = data.replace('AV7','[COLOR red] AV7[/COLOR]')
        #data = data.replace('AV8','[COLOR red] AV8[/COLOR]')
        #data = data.replace('AV9','[COLOR red] AV9[/COLOR]')
        #data = data.replace('AV10','[COLOR red] AV10[/COLOR]')
        #data = data.replace('AV11','[COLOR red] AV11[/COLOR]')
        #data = data.replace('AV12','[COLOR red] AV12[/COLOR]')
        #data = data.replace('AV16','[COLOR red] AV16[/COLOR]')
        #data = data.replace('<br/>','')
        #dada = data.split('\n')
        for i in range(len(date_data)):
            #i = i.replace('<br/>','')
            #plugintools.log("dada="+i)
            #plugintools.add_item(title=i, folder=False)
            #matches = plugintools.find_multiple_matches(data,"<br/>(.*?)<br/>")
            title = date_data[i] + time_data[i]
            plugintools.add_item(action="arenavision_playlists_agenda_select", title=title, url="http://www.arenavision.in/", isPlayable=True, folder=False)


        #for entry in matches:
            #plugintools.log("entry="+entry)
            #plugintools.add_item(title=entry, folder=False)

def arenavision_playlists_agenda_select(params):
    plugintools.log("arenavision_playlists_agenda_select")
    #request_headers=[]
    #request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url = params.get("url")
    data = params.get("title")
    ch = []
    #if data.find('AV7') != -1:
        #ch.append("AV7")
        #link_sopcast(url + "arenavision7", "AV7")
        #lugintools.log(turl)
    #if data.find('AV8') != -1:
        #ch.append("AV8")
        #link_sopcast(url + "arenavision8", "AV8")
    #if data.find('AV9') != -1:
        #ch.append("AV9")
        #link_sopcast(url + "arenavision9", "AV9")
    #if data.find('AV10') != -1:
        #link_sopcast(url + "arenavision10", "AV10")
        #ch.append("AV10")
    #if data.find('AV11') != -1:
        #link_sopcast(url + "arenavision11", "AV11")
        #ch.append("AV11")
    #if data.find('AV12') != -1:
        #link_sopcast(url + "arenavision12", "AV12")
        #ch.append("AV12")
    #if data.find('AV16') != -1:
        #link_sopcast(url + "arenavision16", "AV16")
        #ch.append("AV16")

    for i in range(1,35):
        a = '/AV'+str(i)+'/'
        data = data.replace("[COLOR red]","")
        data = data.replace("[/COLOR]","")
        if data.find(a) != -1:
            if (i<20):
                a = ' [COLOR green](Acestream)[/COLOR]'
            else:
                a = ' [COLOR yellow](Sopcast)[/COLOR]'
            ch.append('AV'+str(i)+a)

    ret = -1
    if len(ch) != 0:
        ret = xbmcgui.Dialog().select('Choose a playlist', ch)
        #xbmcgui.Dialog().ok("Error", str(ret))

    if ret != -1:
        txt = ""
        sopcast = False
        #for i in range(1,35):
        #plugintools.log(str(i)+"-"+ch[ret])
        #if ch[ret] == 'av'+str(i):
        txt = ch[ret]
        if '[COLOR yellow](Sopcast)[/COLOR]' in txt:
            sopcast = True
        txt = txt.replace(' [COLOR green](Acestream)[/COLOR]','')
        txt = txt.replace(' [COLOR yellow](Sopcast)[/COLOR]','')
        txt = txt.lower()
        txt = txt.strip()
        url = url + txt
        #texto = "txt="+txt+"\nurl="+url
        #xbmcgui.Dialog().ok("Error", texto)
        #if ch[ret] == 'AV7': url = url + "arenavision7"
        #if ch[ret] == 'AV8': url = url + "arenavision8"
        #if ch[ret] == 'AV9': url = url + "arenavision9"
        #if ch[ret] == 'AV10': url = url + "arenavision10"
        #if ch[ret] == 'AV11': url = url + "arenavision11"
        #if ch[ret] == 'AV12': url = url + "arenavision12"
        #if ch[ret] == 'AV16': url = url + "arenavision16"
        plugintools.log("url="+url)
        if sopcast == True:
            link_sopcast(url, txt)
        else:
            link_plexus(url, txt)
    #exit=sys.exit()
    #return exit

def link_sopcast(url,title):
    plugintools.log("link_sopcast")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    try:
        dataurl,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
        plugintools.log("data="+dataurl)
        dataurl = plugintools.find_single_match(dataurl,'name="SopAddress" value="(.*?)" /><param')
        plugintools.log("data="+dataurl)
        if dataurl != "":
            plot = ""
            thumbnail = ""
            #dataurl = 'plugin://plugin.video.p2p-streams/?url=' + dataurl + '&mode=2&name='
            dataurl = 'plugin://program.plexus/?url=' + dataurl + '&mode=2&name='
            dataurl = dataurl.strip()
            plugintools.log("data="+dataurl)
            plugintools.add_item( action="play" , title=title , plot=plot , url=dataurl , thumbnail=thumbnail , isPlayable=True, folder=False )
    except: dataurl="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)

def link_plexus(url,title):
    plugintools.log("link_plexus")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    try:
        dataurl,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
        plugintools.log("data="+dataurl)
        dataurl = plugintools.find_single_match(dataurl,'loadPlayer[^"]+"([^"]+)"')
        plugintools.log("data="+dataurl)
        if dataurl != "":
            plot = ""
            thumbnail = ""
            dataurl = 'plugin://program.plexus/?url=acestream://' + dataurl + '&mode=1&name='
            dataurl = dataurl.strip()
            plugintools.log("data="+dataurl)
            plugintools.add_item( action="play" , title=title , plot=plot , url=dataurl , thumbnail=thumbnail , isPlayable=True, folder=False )
    except: dataurl="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)


def arenavision_playlists_canales_ace(params):
    plugintools.log("arenavision_playlists_canales_ace")
    url = params.get("url")
    data = params.get("title")
    for i in range(1,21):
        txt = 'av'+str(i)
        link_plexus(url+txt, txt)


def arenavision_playlists_canales_sop(params):
    plugintools.log("arenavision_playlists_canales_sop")
    url = params.get("url")
    data = params.get("title")
    for i in range(21,35):
        if i < 0:
            txt = '0'+str(i)
        else:
            txt = str(i)
        link_sopcast(url+txt, txt)
    #link_sopcast(url + "arenavision7", "AV7")
    #plugintools.log(url + "arenavision7")
    #link_sopcast(url + "arenavision8", "AV8")
    #link_sopcast(url + "arenavision9", "AV9")
    #link_sopcast(url + "arenavision10", "AV10")
    #link_sopcast(url + "arenavision11", "AV11")
    #link_sopcast(url + "arenavision12", "AV12")
    #link_sopcast(url + "arenavision16", "AV16")

