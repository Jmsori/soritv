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


def peppapig_playlists(params):
    plugintools.log("arenavision_playlists_agenda")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    #request_headers.append(["Referer","http://www.mimediacenter.info/"])
    url = params.get("url")
    try:
       #data = plugintools.read(url)
       data,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    except: data="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)

    #ret = xbmcgui.Dialog().select('Choose a playlist', ['Playlist #1', 'Playlist #2', 'Playlist #3'])
    #xbmcgui.Dialog().ok("Error",str(ret))

    if data:
        #plugintools.log("data="+data)
        data = plugintools.find_single_match(data,'</p>[^<]+<p>(.*?)</p>')
        plugintools.log("data="+data)
        data = data.replace('AV7','[COLOR red] AV7[/COLOR]')
        data = data.replace('AV8','[COLOR red] AV8[/COLOR]')
        data = data.replace('AV9','[COLOR red] AV9[/COLOR]')
        data = data.replace('AV10','[COLOR red] AV10[/COLOR]')
        data = data.replace('AV11','[COLOR red] AV11[/COLOR]')
        data = data.replace('AV12','[COLOR red] AV12[/COLOR]')
        data = data.replace('AV16','[COLOR red] AV16[/COLOR]')
        data = data.replace('<br/>','')
        dada = data.split('\n')
        for i in dada:
            #i = i.replace('<br/>','')
            plugintools.log("dada="+i)
            #plugintools.add_item(title=i, folder=False)
            #matches = plugintools.find_multiple_matches(data,"<br/>(.*?)<br/>")
            plugintools.add_item(action="arenavision_playlists_agenda_select", title=i, url="http://www.arenavision.in/", isPlayable=False, folder=True)


        #for entry in matches:
            #plugintools.log("entry="+entry)
            #plugintools.add_item(title=entry, folder=False)

def arenavision_playlists_agenda_select(params):
    plugintools.log("arenavision_playlists_agenda_select")
    #request_headers=[]
    #request_headers.append(["User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31"])
    url = params.get("url")
    data = params.get("title")
    #ch = []
    if data.find('AV7') != -1:
        #ch.append("AV7")
        link_sopcast(url + "arenavision7", "AV7")
        #lugintools.log(turl)
    if data.find('AV8') != -1:
        #ch.append("AV8")
        link_sopcast(url + "arenavision8", "AV8")
    if data.find('AV9') != -1:
        #ch.append("AV9")
        link_sopcast(url + "arenavision9", "AV9")
    if data.find('AV10') != -1:
        link_sopcast(url + "arenavision10", "AV10")
        #ch.append("AV10")
    if data.find('AV11') != -1:
        link_sopcast(url + "arenavision11", "AV11")
        #ch.append("AV11")
    if data.find('AV12') != -1:
        link_sopcast(url + "arenavision12", "AV12")
        #ch.append("AV12")
    if data.find('AV16') != -1:
        link_sopcast(url + "arenavision16", "AV16")
        #ch.append("AV16")

    #ret = -1
    #if len(ch) != 0:
        #ret = xbmcgui.Dialog().select('Choose a playlist', ch)
        #xbmcgui.Dialog().ok("Error",str(ret))

    #if ret != -1:
        #if ch[ret] == 'AV7': url = url + "arenavision7"
        #if ch[ret] == 'AV8': url = url + "arenavision8"
        #if ch[ret] == 'AV9': url = url + "arenavision9"
        #if ch[ret] == 'AV10': url = url + "arenavision10"
        #if ch[ret] == 'AV11': url = url + "arenavision11"
        #if ch[ret] == 'AV12': url = url + "arenavision12"
        #if ch[ret] == 'AV16': url = url + "arenavision16"
        #plugintools.log("ch="+ch[ret])

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
            dataurl = 'plugin://plugin.video.p2p-streams/?url=' + dataurl + '&mode=2&name='
            dataurl = dataurl.strip()
            plugintools.add_item( action="play" , title=title , plot=plot , url=dataurl , thumbnail=thumbnail , isPlayable=True, folder=False )
    except: dataurl="";xbmcgui.Dialog().ok("Error","\nFallo al obtener la información de","\n"+url)


def arenavision_playlists_canales(params):
    plugintools.log("arenavision_playlists_canales")
    url = params.get("url")
    data = params.get("title")
    link_sopcast(url + "arenavision7", "AV7")
    plugintools.log(url + "arenavision7")
    link_sopcast(url + "arenavision8", "AV8")
    link_sopcast(url + "arenavision9", "AV9")
    link_sopcast(url + "arenavision10", "AV10")
    link_sopcast(url + "arenavision11", "AV11")
    link_sopcast(url + "arenavision12", "AV12")
    link_sopcast(url + "arenavision16", "AV16")

