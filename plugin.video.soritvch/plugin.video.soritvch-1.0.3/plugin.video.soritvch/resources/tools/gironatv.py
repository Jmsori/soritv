# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Arenavision para SorichTV
# Version 0.1 (22/05/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import plugintools


def GiTV_playlists(params):
    #url = 'rtmp://tvgirona.dnssw.net/live/<playpath>Icontouch <swfUrl>http://p.jwpcdn.com/6/12/jwplayer.flash.swf <pageUrl>http://www.tvgirona.cat/playertvgirona/playertvgirona.htm'
    url = "rtmp://tvgirona.dnssw.net/live/Icontouch"
    plugintools.play_resolved_url( url )
