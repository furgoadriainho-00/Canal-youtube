#!/usr/bin/env bash
# Prepara el entorno: comprueba herramientas del sistema, crea .venv y descarga el modelo de voz.
set -euo pipefail
cd "$(dirname "$0")"
for c in python3 ffmpeg ffprobe node; do
  command -v "$c" >/dev/null || { echo "Falta $c: instálalo antes de seguir"; exit 1; }
done
[ -d .venv ] || python3 -m venv .venv
. .venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt
mkdir -p modelos
base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -f "modelos/$f" ] || curl -sSL -o "modelos/$f" "$base/$f"
done
echo "Entorno listo."
