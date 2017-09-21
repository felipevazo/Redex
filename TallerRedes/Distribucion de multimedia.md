# Distribucion de servicio (CDN)
  -  EVita que el envio de un gran archivo se haga desde un unico servidor
  -  Replicando el ontenido en cientos de servidores en el internete
  -  Contenido bajado con anticipacion
  - Se pone el contenido "cerca" del usuario
  - Cdn escribe un "mapa" 
    - Mapa es una especie de cache, con ip, distancia y cdn mas cercano
# Mas alla del Bes efor
  - Hasta aqui: Hacer lo mejor con best effort
  - Futuro: Proxima internet con garantias de QoS, a través de  
    - RSVP: Reservas, pero que no cumplen para todos! (ftp vs VOIP)
    - Servicios diferenciados el aislamiento obliga a "perder ancho de banda" en algunos casos, con el fin de cumplir siempre las asignaciones
    - Servicios integrados
  - PPT, enredado T_T
  - 4 principios feos T_T
  
  
  
  
  -  Mecanismo de Iteneracion y Politicas
    - Itineracion: eleccion del proximo paquete a enviar
    - Itineracion FIFO: enviar en orden de llegada a cola
      - Politica de descarte, si el paquete llega a cola llena, cual descartamos?
        - Tail drop
        - PPT
      - Colas de prioridad!
      - Itineracion round robin : Ciclo por clase, un paquete por clase, NO PRIORIDAD
      - Weighteid Fair QUeuing (WFQ)
        - Round robbin generalizado
        - Cada clase obtiene cantidad ponderada de servicio por ciclo
        - Ejemplo de la vida real?
 - Objetivo: Limitar trafico para no exceder parametro declarado
 - Como?
    - Tasa promedio (de largo plazo):  cuantos paquetes pueden ser enviados por unidad de tiempo
    - Tasa Peak: maximo alcanzado
    - Tamaño de rafaga: Max numero de paquetes enviados consecutivamente
    
 - Como limitar estos criterios/Politicas
  -  Balde de fichas/Tocken Bucket
    - Limita entrada a tamaño de rafaga y tasa promedio especificada
    - Numero de paquetes/fichas admitidos <=(rt+b) rafaga*tiempo + tamañobucket
  - Mezcla de tocken bucket con WFQ
    -  se va de balde en balde
