# Necesidades
- Necesarias de definir en toda empresa, entidad, etc
- realizar inventario, evaluar riesgos y amenazas
# Riesgo= (Amenazas*Vulnerabilidades)/ContraMedidas

# 3 etapas
  - Identificacion de necesidades
    - Inventario:
      - Personas (permisos, nivel jerarquico, jefes o no jefes)
      - Materiales
      - Esquematizacion de la red (topologias fisicas y logicas, rangos de ip)
      - Lista de nombres de domino de la empresa
      - INfraestuctura de comunicacion (routers, computadores, switchs, etc etc)
      - Información delicada
      
  - Analisis de los riesgos
    - A partir de necesidades
    - Evaluar riesgos que conllevan
    - Prob de que ocurra, impacto, daño que pueden causar
    - "Cuanto puede valer un ataque"
    - Importante confeccionar tabla  con potencialidades, con escalas definidas
      - Infundado
      - Debil
      - Moderada
      - Alta
  - DEFINICION DE POLITICA -> LO MAS IMPORTANTE
    - Documento que define objetivos de seguridad
    - Contiene todos los elementos, medidas, filtros, perfiles, TODO!
    - Proyecto a LARGO PLAZO
    - Si hay elementos humanos que no pueden seguirlas, las politicas no valen nah
    
    -  MEtodos para realizar politicas
      - MARION
      - MEHARI
      - EBIOS
      - ESTANDAR ISO 17799
    - Implementación
      - Añadir metodos o sistemas para seguridad
      - Establecer reglas en ellos
        - Firewall
          - Tipos
            - Stateless -> Lee encabezados
            - Dinamico (Statefull) -> Opera sobre capa 3 y 4 de OSI
              - Con el fin de enfocarse en Servicio 
            - De Apps -> Trabaja en capa 7, se denomina proxy
              - Requiere conocimiento de aplicaciones
          - Funciones
            - Autorizar (permitir)
            - Bloquear (denegar)
            - Rechazar sin informar al remitente (negar)
            - Subdividido
              - Autorizar solo explicito
              - rechazo solo explicito
          - Ordenador o Red que permite evitar intrusiones
          - Implementable a nivel hardware o software
          - Es necesario para el equipo que quiera ser firewall
            - ALta taza de procesamiento
            - Sistema debe ser seguro
            - Que no se ejeccute nada mas que el filtrado
          - Filtra todo el trafico de red interna a externa
          - TODA MAQUINA CONECTADA A NET ES PROPENSA A ATAQUES
          
        - Algoritmos Criptografico
        - VPN
        
  # Proxy
    - Intermediario entre LAN y el internete
    -  Regularmente son http
    - Establece una comunicación, pc no se conecta directamente sin pasar por el
    - Hoy en día todos los equipos lo traen por omision, pero se sigue implementando en grande
    -  Caracteristicas:
      - Almacenamiento en Caché -> si otro equipo quiere entrar a la pagina, proxy agiliza el ingreso con la cache
      - Filtrado -> a partir de los logs, permite filtrado
      - Autenticación -> Permite utilizar usuario y contraseña
        - Permite conocer todo el movimiento 
      - Proxy Inverso
        - Todo lo externo pasa por proxy
        - Interno nunca conocerá ip del remitente
    - Softwrae para proxy
      - Squid! libre y gratuito
      - Pagado: Wingate, Jana, Microsoft proxy server
  
