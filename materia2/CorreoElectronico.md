# Def
  - Es la aplicacion distribuida que permite enviar mensajes electronicos por medio de sist informaticos
# Formato
  - RFC 822
  - Formado por: Cabecera -> Info Gral
  - Cuerpo   -> Mensaje a transmitir
# Campos
  - Originario(From)
  - Destinatario(To)
  - Destinatario de copia(Cc)
  - Destinatario de copia Ciega(Bcc)
  - Destinatario de Respuesta (Reply-To)
  - Asunto (Subject)
  - Fecha (Date)
  - Identificador del Mensaje (Message-ID)
  - 3 Obligatorios, Originario, fecha y (Copia ciega || Destinatario)

# Despues del +, para el servidor de correos no essiste
-Actua similar a casillas de correo
# Protocolos
- SMTP(simpel mail transfer protokol) ( Cliente-Servidor o Servidor-Servidor) 
- PoP(Post Oficce Porotcol) -> ENtrega y borra(copia del servidor)
- IMAP (Internet Message Access Protocol) -> Sincronizado con servidor
# Roles
- MTA (Agente de Transporte) -> Servidor de correo que lo hace viajar
- MUA (Agente de Usuario) -> Interactua con usuario (Outlook,thunderbird)
- MDA (Agente de Entrega) -> Redirige a usuario (hoy en dia MTA y MDA En el mismo, uno hace las 2 pegas)

