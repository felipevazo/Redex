# Fiabilidad de servicio y mantener servicio el mayor tiempo posible

# Intro
- Fiabilidad -> Cuanto lo pueden usar los usuarios en condiciones optimas
- Desde usuario
  - Apropiado -> Satisface
  - Inapropiado -> No Satisface
- No todos los errores conducen a falla en el servicio, existen varias maneras de limitar las fallas 
  - Prevención de errores
  - Tolerancia a errores
  - Eliminacion de errores
  - Prredicción de errores, anticipar sus posibles impactos en el servicio.
- Alta Disponibilidad
  - Medidas tendientes a garantizar la disponibilida de servicio
  - fiabilidad -> Prob de que un sistema funcione durante un tiempo dado -> Continuidad de servicio
- Indice de disponibilidad
  - Tiempo de servicio activo, partido en tiempo total.
- Evaluación de riesgos
  - Debemos ser capaces de evaluar todos los riegos que pueden llevar a falla los sistemas
  - Esto puede producir distinto tipo de perdidas.
  - Causas de fallas:
    - Causas fisicas (de origen natural o delictivo)
      - CIELO FALSO ES CACA EN SERVIDORES
    - Causas Humanas (intencionales o accidentales)
      - Desarrolladores son la principal causa de errores, dado mentalidad del mismo.
    - Causas Operativas (vinculados al estado del sistema en un momento dado)
- Tolerancia a errores
  - En gral, necesitamos redundancia duplicando nuestros recursos
  - Capacidad de que un sistema funcione pese a que un componente falle
  - Cuando alguno de los recursos falla, los otros siguen funcionando.
  
- Copias de seguridad
  - Importante!
  - Idealmente un datacenter secundario, en el mejor de los casos.
  - Tipos
    - Completa -> Nombre lo dice
    - Diferencial -> Parecida a Incremental,  pero guarda todo lo modificado desde la ultima copia total
    - Incremental -> Parte con copia total, luuego se respaldan solo los archivos modificados desde la ultima copia incr.
      - De utilizarlo, cada cierti tiempo es recomendado un respaldo total.
    - Delta -> Incremental de los DATOS MODIFICADOS EN UN ARCHIVO
      - divide los archivos en distintos bloques, y va haciendo respaldo de las modificaciones de los archivos.
- Recomendación sobre tipo
  - Menor a 4 GB -> TOTAL
  - Volumen de datos modificados no es alto (4 GB) ->DIferenciales
  - Si volumen de datos alto y programa grande -> Incrementales o Delta
  
- Balanceadores de Carga/ Equilibrio de carga
  - Distribuir tareas en conjunto de servidores
  - Asegurar disponibilidad de equipos enviando datos solo a aquellos que puedan manejarlos
  - DOS tipos
    - Switch de nivel 4 (permiten implementar filtros de capa 4 o superior)
    - Por medio de servidor que utiliza round robin
- CLUSTER
  - Arquitectura constituida por varaios equipos donde cada nodo funciona de forma independiente
  - Tipos
    - Alta Disponibilidad -> Distribuyen carga de trabajo sobre servidores  de forma equitativa, solo un nodo activo de BD a la vez
    - Informáticos -> Distribuyen carga en gran cantidad de servidores con el fin de utilizar rendimineto acumulativo ( Mega computadores y cosas)
  - NAS, Almacenamiento conectado a red -> Gran servidor con hartos discos duros
  - SAN, Storage Area Network!
    - Relacionado con tipo de red que se utiliza, necesita wena red
    - Permite compartir datos entre varios equipos sin afectar el rendimiento
    - El SAN ES carisimo al lado del NAS 
- Sistemas RAID
  - Conjunto redundante de discos de bajo costo
  - Permite hacer un disco duro desde varios discos duros, capacidad maxima es la del disco duro de menor tamaño, permitiendo mayor tolerancia dado a un respaldo brigido
  - Gana en velocidad, gana en seguridad
  - 7 niveles de raid
    - 0 -> Striping " Caracterizar tamaño relativo de los fragmentos  almacenados en cada unidad fisica"
      - Utiliza al menos 2 DD
      - En este caso suman, pero si falla 1 disco es gg no re
      - Duplica velocidad de acceso a info
    - 1 -> Replica
      - Se replica la info, por lo tanto no suman los discos
      - Aumenta seguridad de datos
      - Aumenta velocidad de lectura mas rapida
      - Si uno se cae no GG 
      - Problema? Costoso
    - 0+1 -> wot
      - Combina ambos anteriores
      - Carisimo
    - 2 -> Bandas con paridad (obsoleto)
      - Utiliza codigo raro para conversion de errores
      - dado que codigo esta en controladores de discos actualmente, meh para ellos
      - Que hacía codigo raro?(hamming) -> Cuenta si cantidad de 1 de archivos en almacenamiento es par o impar
    - 3 -> Enladaos entre bits
      - Almacena datos en  bytes de cada unidad y luego maneja bit de paridad
    - 4 -> Entrelazados entre bloques
      - Igual que raid 3, diferencia en raid de paridad
    - 5 -> Conjunto de discos con paridad distribuida de entrelazado de bloques
      - SImilar al 4, pero la paridadse guarda en todos los discos, en anteriores habia uno o dos discos para eso
    - 6 -> configuracion que usa alguno de los de atras
    - 10 -> mezcla raid 1 con raid 0
      - Al reves de raid 0+1
   -  Que raid utilizar?
      - Segun rendimiento, costo y acceso a discos 
        - Seguridad -> Raid1 = Raid 5
        - Rendimiento Raid1 >>Raid5
        - Costo -> Raid5 >>Raid1
- Implementar Raid
  - Software : con dirver en el nivel del sistema operativo del ordenador que sea capaz de crear un volumen logico con varias unidades.
  -  Hardware: Con DASD o contorladores RAID
-  Fuente de alumentación
  - Fuente de alimentación ininterrumplible (UPS) -> CUALQUIER ENERGía
    - TIPOS DE UPS
      - Fuera de linea. se conectan por un relé electrico
      - En linea -> van en serie
      - Interactivos en linea-> Hibrido
    