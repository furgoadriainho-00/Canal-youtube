# Registro

- 2026-10-29 · Paso 1 (sección 13): comprobado el entorno. Ya había Python 3.13, ffmpeg 6.1 (libx264, aac, loudnorm, subtitles, drawtext), Node 22 y Pillow.
- 2026-10-29 · Instalado en `.venv`: MoviePy 2.2.1, faster-whisper 1.2.1, kokoro-onnx 0.6.1 y el modelo de voz Kokoro v1.0 (338 MB, en `modelos/`). Todo gratis y en local.
- 2026-10-29 · Decisión: uso faster-whisper en lugar de openai-whisper porque va más rápido en CPU y no necesita PyTorch. He fijado `av<16` porque la versión 19 rompe faster-whisper.
- 2026-10-29 · Prueba completa correcta: voz Kokoro → transcripción con Whisper exacta → clip 1080×1920 H.264/AAC a −14 LUFS.
- 2026-10-29 · Creados `requirements.txt` e `instalar.sh` para reproducir el entorno en cualquier máquina.
- 2026-10-29 · Paso 2: creada la estructura de carpetas (informes/, salida/, canales/), gastos.md, aprendizajes.md y una plantilla de canal en canales/_plantilla con las cabeceras de los CSV. Añado publicados.csv con estructura, miniatura y frase de inicio para poder comprobar la regla de no repetir.
- 2026-10-29 · Paso 3: investigados 3 nichos en inglés (A cosas cotidianas 7,25 · B tu casa 7,45 · C geografía 6,25). Recomiendo B. Plazo para que el humano elija: 2026-10-30; si no responde, B. Informe en informes/2026-10-29_propuesta-nichos.md.
- 2026-10-29 · Paso 4: propuesta de herramientas. Seguimos a 0 € con Kokoro. ElevenLabs Creator (22 $) queda como opción solo si la retención es baja. Hacen falta claves gratuitas de Pexels y Pixabay. Informe en informes/2026-10-29_propuesta-herramientas.md.
- 2026-10-29 · El humano elige el nicho B. Cancelado el aviso automático de las 24 h. Creada canales/how-your-home-works con nicho.md, estilo.md (voz Kokoro am_michael, paleta naranja/azul) y las 20 primeras ideas en ideas.csv.
- 2026-10-29 · Paso 5: escritas las instrucciones para el humano en PASOS_HUMANO.md (canal, verificación por teléfono, Amazon.com Afiliados, claves de Pexels y Pixabay, proyecto de la API y dónde ejecutar la producción diaria).
