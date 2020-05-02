# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Arenavision para SorichTV
# Version 0.1 (22/05/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import plugintools


def esport3_playlists(params):
    url = 'http://ccma-tva-es-abertis-live.hls.adaptive.level3.net/es/ngrp:es3_web/playlist.m3u8'
    plugintools.play_resolved_url( url )
