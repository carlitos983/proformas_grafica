#!/usr/bin/env python3
"""Descarga proformas de GitHub, usa membrete HD del acta y separa logos."""
import re
import shutil
import urllib.request
from pathlib import Path

ACTA_DIR = Path(__file__).resolve().parent.parent / "carta de conformidad"
OUT = Path(__file__).resolve().parent
URL = "https://raw.githubusercontent.com/carlitos983/proformas_grafica/main/index.html"


def main():
    html = urllib.request.urlopen(URL, timeout=120).read().decode("utf-8")
    print("Descargado:", len(html), "bytes")

    extra = ["// Iconos y bancos del pie (proforma original)"]
    for name in ("IMG_FOOTER_ICONS", "IMG_FOOTER_BANCOS"):
        m = re.search(r"var " + name + r"='([^']+)'", html)
        if not m:
            raise SystemExit(f"No se encontró {name}")
        extra.append(f"var {name} = '{m.group(1)}';")
    (OUT / "logos-pie-extra.js").write_text("\n".join(extra) + "\n", encoding="utf-8")

    html2 = html
    for name in ("IMG_LOGO", "IMG_FOTO", "IMG_FOOTER_ICONS", "IMG_FOOTER_BANCOS"):
        html2 = re.sub(r"var " + name + r"='[^']*';\s*", "", html2)

    insert = '<script src="logos.js"></script>\n<script src="logos-pie-extra.js"></script>\n'
    if 'src="logos.js"' not in html2:
        html2 = html2.replace(
            '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>',
            '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>\n' + insert,
            1,
        )

    (OUT / "index.html").write_text(html2, encoding="utf-8")
    shutil.copy2(ACTA_DIR / "logos.js", OUT / "logos.js")
    print("OK:", OUT)
    print("  index.html", (OUT / "index.html").stat().st_size)
    print("  logos.js", (OUT / "logos.js").stat().st_size)
    print("  logos-pie-extra.js", (OUT / "logos-pie-extra.js").stat().st_size)


if __name__ == "__main__":
    main()
