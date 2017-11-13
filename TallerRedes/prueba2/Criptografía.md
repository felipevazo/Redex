# Cifrar Mensajes

# Realizado desde la antiguedad

# Basado en Aritmetica

# Utilizan Claves
- 2 Grupos
  - Simetricas
    - Clave unica para cifrar y descifrar
    - en 194 Calude Shannon dice que lamejor clave, tiene que tener minimo, el largo del mensaje cifrado
    - Desventaja: Distribuir clave privada
      - Para mas gente, debe crear N(N-1)/2 claves diferentes
  - Asimetricas
    - Clave publica y privada
    - Publica para cifrar
    - Privada para descifrar
    - 1976
    - Clave publica se deduce de clave privada
    - Ventajas
      - no necesidad de ponerse de acuerdo por clave unica
      - Cualquier tipo de distribucion
    - Desventajas
      - no hay forma de saber que corresponde a la clave publica que nosotros queremos, pq son aleatorias
# Decryption(descifrado) o analisis cryptonalisis o ripto analisis 
- Descifrar de forma ilegitima
- Utilizan Metodos Matemáticos
-  4 tipos
  - Ataque de solo texto cifrado -> Utilizando texto cifrado
  - Ataque de texto simple conocido
  - Ataque de texto simple elegido
  - Ataque de texto cifrado elegido
  
 
# Seguridad
  - Mas grande mejor (?)
  - 2 Sistemas NO COMPARABLES
  - Entre 128 a 256 bits en simetrico
  - para publica 1024 a 2048 es lo mejors
# Pretty Good Privacy (PGP)
  - Hibrido
  - TIpo de algoritmo RSA
  - Comprime tiempo de transmisión
  - Ahorra espacio en disco
  - Aumenta seguridad Criptografica
  - Antes de encriptar los mensajes, los comprime y luego encripta
  - Pasos
   -  Cifrado 
    - PGP crea clave con IDEA
    - Cifra con IDEA y la envia usando la clave publica RSA
   -  Descifrado
      - PGP descifra con RSA
      - PGP descifra los datos con clave IDEA
      
      
# Firmas Electronicas
  - Autenticidad de documentos
  - Utiliza Hash, para  asegurar de que el remitente diga quien dice ser
    - Hash es algoritmo matematico, que crea un resumen del texto
    - Representa huella digital del documento
    - SE usa MD5 y SHA
      - MD5 no se usa pq tamaño es muy bajo
      - SHA es la mooda
      
# Certificados
- Permite asociar clave publica a usuario
- Validado por una CA, con tiempo de validez especifico.
- Tipos
  - Firmados Localmente
    - Util en intranets
  - Firmados por entidad de certificación
    - Usados en cosas con plata
- Tipos de contextos
  - de Cliente, para autenticar al cliente
  - De Servidor, sistema de transacciones
  - De VPN, Permite conectarse a la vpn
- SSL (SECURE SOCKET LAYERS)
  - Valida servidores 
  - Valida toda transaccion a través de net
  - Netscape, con bancos
  - Crea llave privada instalada en el servidor y reparte llave publica entre los que se conectan
  
