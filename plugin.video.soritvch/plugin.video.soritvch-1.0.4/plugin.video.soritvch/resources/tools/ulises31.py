# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Parser de Ulises para SorichTV
# Version 0.1 (22/05/2015)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a las librerías de pelisalacarta de Jesús (www.mimediacenter.info)


import plugintools


def Ulises31_playlists(params):
    plugintools.log("soritvch.Ulises31_playlists ")
    Ulises31_name = []
    Ulises31_link = []
    Ulises31_name.append("Capítulo 1: Cíclope o la maldición de los dioses")
    Ulises31_link.append("https://www.youtube.com/watch?v=pS3p7Y1UZLQ")
    Ulises31_name.append("Capítulo 2: El planeta perdido")
    Ulises31_link.append("https://www.youtube.com/watch?v=2RhXvnt12Lc")
    Ulises31_name.append("Capítulo 3: Hératos")
    Ulises31_link.append("https://www.youtube.com/watch?v=QhT-uza0xko")
    Ulises31_name.append("Capítulo 4: Eolo o el cofrecillo de los vientos cósmicos")
    Ulises31_link.append("https://www.youtube.com/watch?v=df1GeIYY3zc")
    Ulises31_name.append("Capítulo 5: Sísifo o el eterno comienzo")
    Ulises31_link.append("https://www.youtube.com/watch?v=BgcXcXGyUcY")
    Ulises31_name.append("Capítulo 6: Las flores salvajes")
    Ulises31_link.append("https://www.youtube.com/watch?v=9E9HntUHF8M")
    Ulises31_name.append("Capítulo 7: La insurrección de los compañeros")
    Ulises31_link.append("https://www.youtube.com/watch?v=MnHRkbaIuTA")
    Ulises31_name.append("Capítulo 8: La Esfinge")
    Ulises31_link.append("https://www.youtube.com/watch?v=GgpyNFT4PwA")
    Ulises31_name.append("Capítulo 9: El Dios del tiempo")
    Ulises31_link.append("https://www.youtube.com/watch?v=P2uPxpTKcXk")
    Ulises31_name.append("Capítulo 10: Los Lestrígonos")
    Ulises31_link.append("https://www.youtube.com/watch?v=QyzHik5Xpkk")
    Ulises31_name.append("Capítulo 11: El sillón del olvido")
    Ulises31_link.append("https://www.youtube.com/watch?v=F7xxZc7qso8")
    Ulises31_name.append("Capítulo 12: Los planetas opuestos")
    Ulises31_link.append("https://www.youtube.com/watch?v=L9O9xZduvyw")
    Ulises31_name.append("Capítulo 13: La laguna de los dobles")
    Ulises31_link.append("https://www.youtube.com/watch?v=Ei3ip61kjNQ")
    Ulises31_name.append("Capítulo 14: El tesoro de las Sirenas")
    Ulises31_link.append("https://www.youtube.com/watch?v=Sv4_4-i-twI")
    Ulises31_name.append("Capítulo 15: La segunda Arca")
    Ulises31_link.append("https://www.youtube.com/watch?v=WDKs9i8t1pY")
    Ulises31_name.append("Capítulo 16: La maga Circe")
    Ulises31_link.append("https://www.youtube.com/watch?v=WNwiEORW5Qo")
    Ulises31_name.append("Capítulo 17: El laberinto del Minotauro")
    Ulises31_link.append("https://www.youtube.com/watch?v=xh3pwvzNs7w")
    Ulises31_name.append("Capítulo 18: Atlas")
    Ulises31_link.append("https://www.youtube.com/watch?v=a9T5MPyecnM")
    Ulises31_name.append("Capítulo 19: Nereo y la verdad oculta")
    Ulises31_link.append("https://www.youtube.com/watch?v=lYeJd0Mk6F4")
    Ulises31_name.append("Capítulo 20: El mago negro")
    Ulises31_link.append("https://www.youtube.com/watch?v=DOGMD_ntLvI")
    Ulises31_name.append("Capítulo 21: Los rebeldes de Lemnos")
    Ulises31_link.append("https://www.youtube.com/watch?v=AXRfH37aDMQ")
    Ulises31_name.append("Capítulo 22: La ciudad de Córtex")
    Ulises31_link.append("https://www.youtube.com/watch?v=N67DP9Tvj9M")
    Ulises31_name.append("Capítulo 23: Calypso")
    Ulises31_link.append("https://www.youtube.com/watch?v=ACYT7gl-f4Q")
    Ulises31_name.append("Capítulo 24: Ulises encuentra a Ulises")
    Ulises31_link.append("https://www.youtube.com/watch?v=1r26hVKGFh0")
    Ulises31_name.append("Capítulo 25: Los devoradores de Lotos")
    Ulises31_link.append("https://www.youtube.com/watch?v=eE-kHUhRrVI")
    Ulises31_name.append("Capítulo 26: El reino de Hades")
    Ulises31_link.append("https://www.youtube.com/watch?v=H_CpzVv8hZc")

    for i in range(len(Ulises31_name)):
        title = Ulises31_name[i]
        url =  Ulises31_link[i]
        video_id = plugintools.find_single_match(url, '[=](.+)')
        plugintools.log("video_id = " + video_id)
        plot = ""
        #thumbnail = ""
        thumbnail = "http://img.youtube.com/vi/"+video_id+"/0.jpg"
        #video_id = str(url.split("https://www.youtube.com/watch?v="))
        url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+video_id
        plugintools.add_item( action="play" , title=title , plot=plot , url=url , thumbnail=thumbnail , isPlayable=False, folder=False )

