# Domain name Server
- Relaciona ip con direccion
- En ARPANET existia hosts.txt (el primer DNS consultado)
- Invencion de esquema jerarquico 
- Inicialmente solo enviado en paquetes UDP
- ICANN -> big boss en dominio, creado en 1998
- Dominios de nivel superior (250) -> .cl .org. .com .com.ar
- subdominio = 63 caracteres
- TOTAL = 255 caracteres


# Registro de dominios
- 5tupla
- Nombre_Dominio Tiempo_de_Vida Clase Tipo Valor
  - Nombre_Dominio: ufro.cl, uct.cl etc etc etc
    - Clave Primaria
  
  - Tiempo_de_Vida
    - Cambios de forma periodica o no cambio alguno
    - Si no hay cambio, se registra 86400 (un dia)
    - De haber mucho, se registra 60 (un minuto)
    - Valor por Omision -> 3600 (una hora)
  
  - Clase
    - IN (internete)
  
  - Tipo
    - DNS,MX,A,AAAA, etc
    - Mas tipos en PPT
  
  - Valor
    - Ip, Alias, etc
    
# SIEMPRE DEFINIR ALIAS WWW
