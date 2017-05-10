# Sukats
# Repaso
  - PPT
# Concepto
  - 2 programas pueden intercambiar flujos de datos de manera fiable y ordenada
# Histopaja
  - 1971
  - 1983 -> Estandar -> API BSD en berkeley sockets
  - Winsock -> Api de socket windows -> Basada en Berkeley sockets
# Clasificacion
  - Segun Conexion
    - Socket de flujo
      - Utiliza TCP
      - Orientado a la conexion
    - Socket de datagramas
      - Utiliza UDP
      
   - Según Familia
      - Unix Domain Socket (IPC)
        - Se encuentran especificados en la norma POSIX
        - Tinen como proposito la intercomunicacion entre programa dentro del mismo pc
      - Internet Sockets
        - Tiene proposito la intercomunicación entre programas a través de la red
# Visualizacion de sockets
  - Netstat
  - Workflow
     - Socket()-> Se crea socket
        - Pasan 2 cosas: 
          - Obtiene IP( Maquina)
          - Asociado a puerto( depende socket si tcp o udp)
     - Bind() -> Metodo-> asociar a direccion puerto
     
