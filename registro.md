# Registro

- 2026-10-29 · Paso 1 (sección 13): comprobado el entorno. Ya había Python 3.13, ffmpeg 6.1 (libx264, aac, loudnorm, subtitles, drawtext), Node 22 y Pillow.
- 2026-10-29 · Instalado en `.venv`: MoviePy 2.2.1, faster-whisper 1.2.1, kokoro-onnx 0.6.1 y el modelo de voz Kokoro v1.0 (338 MB, en `modelos/`). Todo gratis y en local.
- 2026-10-29 · Decisión: uso faster-whisper en lugar de openai-whisper porque va más rápido en CPU y no necesita PyTorch. He fijado `av<16` porque la versión 19 rompe faster-whisper.
- 2026-10-29 · Prueba completa correcta: voz Kokoro → transcripción con Whisper exacta → clip 1080×1920 H.264/AAC a −14 LUFS.
- 2026-10-29 · Creados `requirements.txt` e `instalar.sh` para reproducir el entorno en cualquier máquina.
