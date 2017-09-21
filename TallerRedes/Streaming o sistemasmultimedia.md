# Multimedia
- Multimedia= Multiples medios
- Sistema:: Equipos informaticos capaces degestionar todo tipo de informacion audivisual
- Interaccion con usuario = Multimedia
- 3 disciplinas -> telematico, audiovisual, informatica

- Multimedia Interactiva: Todo lo que hace interaccion con un sujeto X, y este sujeto es capaz de entregar lo mismo a los demas


# Sistema Multimedia
- Definicion Arriba
- bit, byte, paquete, objeto 
- Medio
  - Discreto : texto,imagen,grafico
  - Continuo : videos, audio, animaciones
- Stream: Secuencia temporal de paquetes pertenecientes a un medio.
- Relacion de flujos, requerimientos de sincronizacion entre flujos, video conferencias
- Varian segun tipos de componentes
  - Aislados: Pc personal
  - Comunicacion entre iguales: P2P, 2 o mas usuarios en diferentes puuntos
  - Clientes servidor: Modelo cliente serviors
  
- Varian segun uso
  - Presentacion multimedia: ppt
  - Conferencia: skaip, llamadas de voz de wasap, tiempo real
- App multimedia
- Caracteristicas
  - Multiples flujos de medios
  - Relacion temporal entre los flujos
  - Calidad de servicio exigida a la red
- AAM= (Lista de flijos, relacion, calidad de servicio)
- Calidad de servicio se traduce en parametros tales como ancho de banda, retardo de transmision, perdida de paquetes, etc.

- Tipos de aplicaciones
- En funcion de modo de generacion de informacio
  - Orquestadas = Youtube, con su BD
  - Directo = Directamente con dispositivo de captura
- En funcion de utilidad
  - Comunicacion = Skaip wasap
  - Interactivas sobre internet = Juegos
  - Entretenimiento =  NO hay mayor interaccion con usuarios
  
  
- Servicios Multimedia
  - Servicio = Aplicacion accesible de forma no local
  - Se suministran desde servidores a través de redes de comunicacion
  
- Arquitectura Basica
  - Aplicacion 
  - Gestion de medios
  - Control de la calidad de servicio
  - Subsistema de red
  
- Entorno de Acceso
  - Usuario domestico, pasa a su ISP, de ahi a la WAN, y luego pasa la las LAN
  - El profesional  necesita internet mejor
  
- Tipos de servicios
  - Simetricos: Velocidad de transmicsion de datos es similar al proveedor
  - Asimetricos: Velocidad de transmision de datos es mayor que la velocidad de retorno
  - MIRAR PPT CON ESPECIFICACIONES
  
  
  
  
# Multimedia Quality of Service
- La red provee a las aplicaciones con nivel de desempeño requerido para funcionamiento
  - Principios
    - Clasificar app multimedia
    - Identificar servicios de red que apps requeieren
    PPT
    
    
 - MM En red
  - Streaming de audio/video almacenado, en vivo o tiempo real e interactivo
  
- Jitter: Variabilidad del retardo de paquetes dentro del mismo flujo de paquetes

- Cuando se envia el paquete, el jitter tiene que v er en el delta entre un paquete y otro

- hay apps de streaming tolerante a perdidas. Y otros intolerante a perdidas, pero tolerante al retardo.

- Streaming multimedia Almacenadoa
  - Almacenado en fuente
  - Transmitido al cliente
  - Reproduccion antes de que todos los datos lleguen
  - Restriccion de tiempo para datos por ser transmitido
  - Tiene interactividad con apps, tipo VCR = pausa, rebobinar, avanzar, etc.
  - 10 sg de retardo ok, 1-2 hasta que comando actua estamos bien
  - RTSP usado a menudo
  - Restricciones : Datos deben ser transmitidos a tiempo para reproducirse
  
- Streaming en vivo
  - Buffer de reproduccion, puede retrasarse decenas de segundso
  - HAy restricciones de tiempo
  
- Podemos rebobinar y pausar.
- audio <150 ms bueno, <400 ms OK
- Retardo en capa aplicacion y red
- Retardos mayores notorios, impide interactividad
- Inicia sesion a través de sockettt


- Multimedia hoy en día
  - Best Effort TCP/UDP
  - no hay garantias de retardo o perdidas
  
- Como deberia evolucionar internet para mejorar soporte multimedia
  - Filosofia de servicios integrados
    - Cambios fundamentales en internet, asi apps pueden reservar ancho de banda extremo a extremo
    - Requiere nuevo y complejo software en router y hosts
    - Crear sistemas mas complejos, reformulando el internet actual, con el fin de lograr lo de arriba
  - Dejar hacer dejar pasar
    - mas ancho de banda cuando se necesite
    - Distribucion de contenidos multicast a nivel de app
  - Servicios diferensiados
    - Menores cambios a internet, pero proveer clases de servicio de las categorias anteriores
# Streaming multimedia almacenada
  - Se trabaja a nivel de aplicacion utilizando UDP (best effort)
  - Tareas de reproductor:
    - Remover Jitter (taza de demora)
    - Servicio de descompresion
    - Acomodo a errores
    - INterfaces graficas con interactividad.
    
# Multimedia en internet: Caso simple
  - Web browser con webserver, y luego a media player.
  - Idealmente debe estar audio y video en mismo archivo
  - Se transmite como http, para luego pasado al reproductor
# Audio/Video no continuo, tipo tcp

# Via Streaming
  - PPT
  - Tanto navegador como servidor conectan con servidor
  - Navegador conecta con metafile al reproductor
  
# Buffering 
- LAnzar a una taza desde el servidor de streaming el archivo
- Hay un retardo, que significa que en el cliente se almacena el archivo mientras almacena un par de segundos, se lanza el reproductor.
- Si o si la taza de entradda debe ser igual a la taza de salida. para evitar problemas en streaming

# TCP  O UDP EN STREAMING?
  - UDP
    - Servidor envia a tasa apropiada para ciliente( evitando congestion)
      - tasa envio=taasa de codigficacion= tasa cte
      - tasa llegada=tasa cte - tasa llegada
      
    -  REtardo en reproduccion pequeño para compensar variaciones de retardo
    - Recuperacion de errores, lo que alcance 
    
  - TCP
    - ENviar a tasa maxima posible bajo tcp
    - Llegada de paquetes fluctua debido a control de gonestion TCP
    - Retardo de reproduccion mayor: taza envio de tcp estable
    - PASA MAS FACIL POR LOS FIREWALLS
# Tasas de cliente
  - Con condificacion de 1.5 Mbps vs 28.8 kbps
  - El servidor transmite multiples copias de videos, codificadas a distinta tasa, para menejar capacidades diferentes de recepcion
