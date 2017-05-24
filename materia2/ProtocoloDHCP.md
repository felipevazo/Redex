# DHCP
- Extensino de BOOTP, centraliza y administra la info de config tcpIP
- Cada vez que cliente parte, requiere info de direccionamiento a un servidor DHCP
- Cuando recibe peticion (request) selecciona una IP de una pool definida y la ofrece al cliente
- Si cliente acepta, la info de la ip es entregada al cliente por tiempo especificado
- Sin disponibilidad, no inicia tcp/ip 

# Procesos de 4 fases // PEDIDO DE IP A TRAVES DE BROADCAST
- Request
  - Solicita entrega de ip A través de BROADCAST
  - Como no conoce IP, pone origen 0.0.0.0 y como destino 255.255.255.255
  - El request es un mensaje DHCPDISCOVER, el cual tiene MAC y nombre de cliente
- Lease offer
  - Los serivodres que reciben el request, ofertan con la siguiente informacion: MAC del cliente, direccion IP, tiempo de entrega
    - Y LA IP DEL SERVIDOR 
  - Se envia a broadcast, a través de un mensaje DHCPOFFER y se reserva mientras guarda espera 
  - El cliente espera por un segundo una oferta, si no hay respuesta, hace rebroadcast, 3 veces, a intervalos de 9, 13 y 16
    - + un delta aleatorio, para evitar peleas
  - Si no recibe  ofertas despues de 4 request, el cliente reintenta cada 5 minutos
- Lease selection 
  - Despues que recibe oferta de al menos un servidor DHCP, hace broadcast  atodos los DHCP indicando que acepto oferta
  - El broacdast es enviado en un mensaje DHCPREQUEST que incluye IP del servidor cuya oferta ha aceptado
  - Otros servidores retiran ofertas
- Lease ACK
  - El servidor que fue aceptado, hace broadcast ACK hacia cliente con forma de mensaje DHCPACK que contiene:
    - IP Otorgada
	- Otra info de Configuración
  - Cuando cliente recibe ACK, obtiene TCP/IP y cliente es feliz en la red
# RENOVACION
- Despues de tiempo llega al 50%, trata de renovar con DHCPREQUEST, similar a fase 3
- Si esta disponible, lo renueva enviando DHCPACK similar a fase 4, con tiempo de arriendo igual o distinto y cambios de config
- Si servidor no puede renovar:
  - El cliente intenta contactar a cualquier DHCP cuando el 87.5% del tiempo se agota, haciendo Broadcast DHCPREQUEST
  - Cualquier servidor responde con DHCPACK
  - Si el tiempo del arriendo expira o se recibe DHCPNACK entonces el cliente DHCP debe discontinuar el uso de IP
    - y retornar proceso de obtener (4 fases)
