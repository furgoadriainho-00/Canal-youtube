# Lo que tienes que hacer tú

Todo esto lo tienes que hacer tú porque implica crear cuentas, contraseñas o datos personales, y eso yo no lo hago (sección 12). Va en orden de prioridad. Tiempo total: unos 60–90 minutos, repartidos en varios días.

Cuando termines cada paso, márcalo con `[x]` o dímelo en el chat.

---

## 1. Crear el canal (10 min) · urgente

- [ ] Entra en youtube.com con tu cuenta de Google → foto de perfil → **Crear un canal**.
- [ ] Elige **usar un nombre personalizado**. Así se crea una cuenta de marca y el canal no queda atado a tu nombre personal, que es lo que conviene si algún día lo vendes o lo compartes.
- [ ] Nombre. Propuestas, por orden:
  1. **Home Explained**
  2. **How Homes Work**
  3. **House Decoded**

  Si el nombre o el @ ya están cogidos, prueba el siguiente y dime cuál ha quedado.
- [ ] En YouTube Studio → **Configuración → Canal → Información básica**: país **Estados Unidos** si te deja; si no, el tuyo real. Idioma del canal: **inglés**.
- [ ] Logo y banner: déjalos vacíos. Te los preparo yo cuando me digas el nombre.

## 2. Verificar el canal con el teléfono (3 min) · urgente

Sin esto no se pueden subir vídeos de más de 15 minutos ni poner **miniaturas personalizadas**, y la miniatura es la mitad del éxito de un vídeo largo.

- [ ] Ve a **youtube.com/verify**, elige SMS, pon tu número y escribe el código.
- [ ] Compruébalo en YouTube Studio → **Configuración → Canal → Disponibilidad de funciones**. Las «funciones intermedias» deben aparecer como **habilitadas**.
- [ ] Las «funciones avanzadas» llegan solas con el tiempo y el historial del canal, o con una verificación de identidad si YouTube te la ofrece. Si te la ofrece, hazla.

Fuente: https://support.google.com/youtube/answer/9890437

## 3. Darte de alta en Amazon Afiliados (20 min) · esta semana

Es el único ingreso posible antes de la monetización. El público es de EE. UU., así que el programa es el de **amazon.com**, aunque vivas en España.

- [ ] Ve a **affiliate-program.amazon.com** → *Sign up*.
- [ ] En «sitios web y apps» pon la URL de tu canal de YouTube.
- [ ] Rellena la **entrevista fiscal** (formulario W-8BEN, para no residentes en EE. UU.). Así no te retienen el 30 %.
- [ ] Mándame tu **ID de afiliado** (algo como `homeexplained-20`). No me mandes la contraseña.
- **Ojo:** Amazon cierra la cuenta si en **180 días no hay 3 ventas** que cuenten. Tus propias compras no cuentan. Por eso no corre prisa darse de alta antes del primer vídeo, pero tampoco hay que esperar mucho: lo ideal es hacerlo cuando ya haya 4–6 vídeos publicados.
- Yo pondré en cada descripción con enlaces el aviso obligatorio: *"As an Amazon Associate I earn from qualifying purchases."*

## 4. Claves gratuitas de imágenes (10 min) · esta semana

- [ ] **Pexels:** crea una cuenta en pexels.com → **pexels.com/api** → pide una clave.
- [ ] **Pixabay:** crea una cuenta en pixabay.com → **pixabay.com/api/docs** → la clave aparece en la página cuando has iniciado sesión.
- [ ] Pásamelas de forma segura, **nunca pegándolas en el chat**. En Claude Code abre el menú del entorno en la barra de título de la sesión → **Editar** → apartado *Network secrets* (en versiones antiguas, *API credentials*). Si no aparece ese apartado, añádelas como variables de entorno. Los nombres son `PEXELS_API_KEY` y `PIXABAY_API_KEY`. Las sesiones nuevas las leerán solas.

Mientras tanto hago los visuales con gráficos y diagramas por código, así que esto no bloquea nada.

## 5. Proyecto de la API de YouTube (20 min + espera de semanas) · cuando puedas

Sirve para que algún día suba yo los vídeos solo. Mientras no esté auditado, cualquier vídeo subido por la API se queda **bloqueado en privado** y no se puede recurrir. Hasta entonces te dejo cada vídeo listo en `salida/` y lo subes tú desde YouTube Studio (unos 2 minutos).

- [ ] **console.cloud.google.com** → Crear proyecto → nombre, por ejemplo, `home-explained-uploader`.
- [ ] *APIs y servicios → Biblioteca* → activa **YouTube Data API v3**.
- [ ] *Pantalla de consentimiento de OAuth* → tipo **Externo** → rellena el nombre de la app y tu correo → añade tu propia cuenta como **usuario de prueba**.
- [ ] *Credenciales → Crear credenciales → ID de cliente de OAuth* → tipo **Aplicación de escritorio**. Descarga el JSON, pero **no me lo pegues en el chat**: lo configuraremos juntos cuando el proceso de producción funcione en tu ordenador.
- [ ] Pide la auditoría en el formulario **YouTube API Services – Audit and Quota Extension Form** (búscalo con ese nombre en Google). Motivo: subir tus propios vídeos a tu propio canal. Suele tardar varias semanas.

## 6. Decidir dónde se ejecuta todo · antes del paso 7 de la primera sesión

Esta sesión corre en un servidor temporal en la nube, no en tu ordenador. Para la producción diaria automática hay dos opciones:

- **A. Tu ordenador** (lo que dice `CLAUDE.md`): clonas el repositorio, ejecutas `./instalar.sh` y programamos una tarea diaria. Hace falta tener Claude Code instalado ahí.
- **B. En la nube:** una tarea programada abre una sesión como esta cada día, produce el vídeo y lo sube al repositorio, y tú lo descargas y lo subes a YouTube. Es más cómodo, pero los vídeos pesan y hay que moverlos.

**Ya está activa la B** (cada día a las 03:17, hora de Madrid). Si prefieres la A, dímelo y la cambio.
