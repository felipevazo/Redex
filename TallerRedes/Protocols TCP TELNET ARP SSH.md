# INTERNET SOLO DEBERIA ESCUCHAR PUERTOS 80 y 443 DE UN SERVIDOR
# Putty, para windows








# ARP
- Traduce IP a MAC
- ARP request a Broadcast MAC para obtener direcciones IP
- Almacenadas en Tablas ARP
- SOLO FUNCIONA SI TODAS LAS MAQUINAS LO SOPORTAN
# REVERSE ARP (RARP)
- Protocolo para obtener Direccion IP perteneciente a un derterminado hardware electronico. Reemplazado por BOOTP (Protocolo usado para obtener direccion ip de servidor)
- Finalmente reemplazado por DHCP
# ARP Proxy: Consiste en que host responde a peticiones ARP destinadas a un host que se encuentra fuera de la red local
- SIMILAR A NAT POR PUERTO 

# Telnet
- Permite conectar con otro host remotamente
- Tambien es el nombre del software que implementa el cliente
-puerto 23
- SOLO PERMTIE MODO TERMINAL, SIN GRAFICOS, util para fallos a distancia, transferencia baja, antiguamente muy utilizado
- Actualmente se utiliza para detectar puertos abiertos en servidores
- PROBLEMA DE SEGURIDAD; TEXTO PLANO Y NO ENCRIPTACION
- HOY EN DIA SSH REINA
- RAZONES PARA NO USARLO
  - Muchas vulnerabilidades descubiertas
  - No Cifra nada
  - No hay sistema de autentificación.
# SSH
- Secure Shell
- Administrar maquinas remotas, a traves de programas graficos, a dierencia de Telnet
- SSH Permite copiar datos de forma segura,  tanto archivos sueltos simulando FTP(SFTP)
- SSH Permite Gestionar claves RSA para no escribir claves al conectar los dispositivos
- Seguridad:
  - Trabaja como Telnet, pero usando tecnicas de cifrado
  - La version uno hace uso de algoritmos patentados, pero no se usa mucho hoy en día
