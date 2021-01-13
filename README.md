# mic_control
Muestra un icono en el toolbar para saber si el micro esta mute o no

# Instalación
Solo esta operativo para sistemas Linux y probado en Ubuntu 18.04
Necesitas python y el GTK3 de python para que funcione, la vesión de python es la 2

mic_notificaciones.py "Nombre del dispositivo que vas a usar como micro"

mic_control.sh "Nombre del dispositivo que vas a usar como micro"

Para saber el nombre del dispositivo usa el comando

arecord -l

ejemplo de mi salida

**** Lista de CAPTURE dispositivos hardware ****
tarjeta 0: Webcam [AF FULL HD 1080P Webcam], dispositivo 0: USB Audio [USB Audio]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0
tarjeta 1: Device [USB PnP Audio Device], dispositivo 0: USB Audio [USB Audio]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0
tarjeta 2: PCH [HDA Intel PCH], dispositivo 0: ALC1150 Analog [ALC1150 Analog]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0
tarjeta 2: PCH [HDA Intel PCH], dispositivo 2: ALC1150 Alt Analog [ALC1150 Alt Analog]
  Subdispositivos: 1/1
  Subdispositivo #0: subdevice #0

Para ejecutar el programa sería

mic_notificaciones.py "USB PnP Audio"

mic_control.sh "USB PnP Audio"

Las dos imágenes las puedas cambiar por lo que quieras, o bien sustituyes por otra usando el mismo nombre o lo cambias en el mic_notificaciones.py


Ejecutando el programa de notificaciones en el inicio del sistema lo tendras ya funcionando, si ademas asocias el arranque del script mic_control con una tecla del sistema tendras el muted y el unmuted en ese boton con el cambio en las notificaciones



