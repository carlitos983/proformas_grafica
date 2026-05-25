#!/usr/bin/env python3
"""Copia logos.js HD desde carta de conformidad y opcionalmente re-extrae del PDF."""
import shutil
import subprocess
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent
ACTA = DIR.parent / "carta de conformidad"
SRC = ACTA / "logos.js"
DST = DIR / "logos.js"

if __name__ == "__main__":
    extraer = ACTA / "extraer-assets-acta.py"
    pdf = Path(r"C:\Users\User\Downloads\ACTA DE CONFORMIDAD GRAFICA SILVESTRE.pdf")
    if extraer.is_file() and pdf.is_file():
        print("Regenerando membrete desde PDF del acta...")
        subprocess.check_call([sys.executable, str(extraer)], cwd=str(ACTA))
    if not SRC.is_file():
        raise SystemExit(f"No existe {SRC}\nEjecute extraer-assets-acta.py en carta de conformidad.")
    shutil.copy2(SRC, DST)
    print("OK:", DST, "bytes:", DST.stat().st_size)
