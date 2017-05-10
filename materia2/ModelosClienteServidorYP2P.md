# Aplicacion Distribuida
  - Formada por varios programas que se ejecutan en pcs diferentes y que se comunican por medio de la red que los une.
  - Cooperacion de trozos de codigo que la forman, deben seguir un protocolo.
  - La existencia de protocolo estandar garantiza posibilidad de interactuar entre productos de diferentes aplicasounds.
# Modelo CLiente-Servidor
  - Aplicacion se divide en dos partes Asimetricas
    - CLiente
    - Servidor-> Sistema potente que ofrece servicios a maquinas mas sencillas
  - Por lo gral, usuarios acceden a app por medio de cliente (Ej: Si usuario persona y quiere usar fb, cliente es navegador)
  - Diseño incluye dos elementos
    - Especificacion de los servicios que ofrece servidor
    - Especificacion de protocolo de acceso, como se piden y como retorna.(ej, fb se puide por protocolo HTTP)
# Modelo Peer To Peer
  - Usado en comparticion de archivos o mensajeria instantanea
  - No es incompatible con modelo cliente-servidor
  - Implica simetria
  - Caracteristicas
    - Escalabilidad
    - Robustez
    - Descentralización
    - Distribucion de costes
    - Anonimato
    - Seguridad
  - Problemas
    - Encontrear nodo que ya este conectado a red P2P
       - R: Mezclar modelos, tener servidor, pasa por ahi primero y luego a p2p
    - conectar a los nodos sin ip publica entre ellos
       - R: Intermediario (proxy) entre nodos
  
