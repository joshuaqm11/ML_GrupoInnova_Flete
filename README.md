# ML Grupo Innova · Predicción del costo de envío (flete)

**Proyecto 3 · ISW-911 Minería de Datos · UTN 3C2026**
Rol: Consultores Senior de Machine Learning para **Grupo Innova S.A.**

| Integrante | Responsabilidad principal |
|---|---|
| **Joshua Quesada** (coordinador) | Estructura del repo, análisis estructural y target (`00`), evaluación comparativa y selección (`05`), notebook final integrado |
| **Fernanda Sibaja** | Nulos, atípicos, correlación y multicolinealidad (`01`), traducción a negocio y recomendaciones (`06`) |
| **Jose Fabio Oconitrillo** | Ingeniería de variables, preprocesamiento y partición (`02`), Modelo 1: Ridge/Lasso (`03`) |
| **Joseph Salazar** | Modelo 2: Árbol de decisión + Random Forest (`04`), Feature Importance (`06`) |

Kanban: tablero de Trello **"ML Grupo Innova · Proyecto 3 (Minería de Datos)"**.

## Problema

- **Dataset:** ventas de Olist (el mismo del Lab/Workshop 4, `data/raw/olist_ventas.csv`): una fila = un ítem vendido.
- **Target:** `flete` (costo de envío del ítem) → **regresión**.
- **Métricas obligatorias:** RMSE, MAE y R², sobre un **Test independiente** (20 %, `random_state=42`).
- **Predictores:** solo lo que se conoce al momento de la compra (peso, medidas, volumen, precio, categoría, estado del cliente y del vendedor, si están en el mismo estado). Se excluyen `valor_pago`, fechas de entrega y reseña por **fuga de información**.

> Diferencia clave con el Lab 4: allí el escalado se ajustó con todo el conjunto antes de dividir (data leakage). Aquí todo lo que aprende de los datos (imputación, escalado, encoding) va dentro de un `Pipeline` que se ajusta solo con Train.

## Estructura

```
data/raw/olist_ventas.csv        dataset original del Lab 4
src/config.py                    semilla, rutas, target y listas de variables (compartido)
src/datos.py                     carga + variables derivadas + split Train/Test (compartido)
src/preprocesamiento.py          ColumnTransformer lineal y de árboles  (Fabio)
src/evaluacion.py                métricas y registro en reports/metricas_modelos.csv
notebooks/00_estructura_y_target.ipynb        Joshua
notebooks/01_eda_limpieza.ipynb               Fernanda
notebooks/02_preprocesamiento.ipynb           Fabio
notebooks/03_modelo_lineal.ipynb              Fabio
notebooks/04_modelos_arboles.ipynb            Joseph
notebooks/05_evaluacion_comparativa.ipynb     Joshua
notebooks/06_interpretabilidad_y_negocio.ipynb Joseph + Fernanda
notebooks/Proyecto3_GrupoInnova.ipynb         ENTREGABLE FINAL (Joshua integra)
reports/                         métricas y figuras
presentacion/                    diapositivas (12–15 láminas, 20 min)
```

## Cómo ejecutar

```bash
pip install -r requirements.txt
jupyter notebook   # abrir los notebooks desde la carpeta notebooks/
```

En Google Colab: clonar el repo (`!git clone <url>`), `%cd` a `notebooks/` y ejecutar.

## Flujo de trabajo

Ver [`docs/flujo_trabajo.md`](docs/flujo_trabajo.md). Resumen: una rama por tarea, PR a `main`, cada uno trabaja **en su propio notebook** (no editar notebooks ajenos para evitar conflictos de merge en `.ipynb`).
