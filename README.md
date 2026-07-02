# Proformas – Gráfica Silvestre

Generador de proformas en PDF (GitHub Pages).

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `index.html` | Formulario y generador PDF |
| `logos.js` | Membrete y pie HD (mismo que acta de conformidad) |
| `migrar-proformas.py` | Vuelve a descargar `index.html` de GitHub y regenera logos |

## Membrete nítido (importante)

El encabezado y pie en alta resolución vienen de la carpeta **carta de conformidad**:

```bash
cd "../carta de conformidad"
python extraer-assets-acta.py
```

Luego copie o vuelva a ejecutar `migrar-proformas.py` en esta carpeta (copia `logos.js` automáticamente).

## Uso local

Abra `index.html` en Chrome o Edge.

## Publicar en GitHub Pages

Suba: `index.html` y `logos.js` (el pie claro va dentro de `logos.js`, sin bloque de bancos).

URL: `https://carlitos983.github.io/proformas_grafica/`

## Precios

- Los precios ingresados **incluyen IGV** (se desglosa en sub total / IGV / total).
- Precio unitario en PDF: conserva todos los decimales que escriba (ej. `0.4144`).
