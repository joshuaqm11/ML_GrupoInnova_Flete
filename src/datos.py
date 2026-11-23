"""Carga, variables derivadas y partición Train/Test compartida.

Uso en cualquier notebook:

    import sys; sys.path.append("..")
    from src.datos import cargar_datos, dividir_train_test
    df = cargar_datos()
    X_train, X_test, y_train, y_test = dividir_train_test(df)

Regla de oro: aquí NO se imputa, NO se escala y NO se codifica nada.
Todo lo que "aprende" de los datos (medianas, medias, categorías) va dentro de
un Pipeline que se ajusta SOLO con Train (ver src/preprocesamiento.py).
"""
import pandas as pd
from sklearn.model_selection import train_test_split

from src import config


def cargar_datos(ruta=config.DATA_RAW) -> pd.DataFrame:
    """Lee olist_ventas.csv (mismo origen que el Lab 4), traduce columnas,
    deja solo órdenes entregadas y crea las variables derivadas."""
    df = pd.read_csv(ruta).rename(columns=config.NOMBRES_ESPANOL)

    # Igual que en el Lab 4: sin fecha de entrega = orden no entregada (2.18 %).
    df = df[df["fecha_entrega"].notna()].copy()

    df = crear_variables(df)
    return df.reset_index(drop=True)


def crear_variables(df: pd.DataFrame) -> pd.DataFrame:
    """Variables derivadas fila por fila (no aprenden de otras filas, así que
    se pueden crear antes de dividir sin fuga de información)."""
    df = df.copy()
    df["volumen_cm3"] = df["largo_cm"] * df["alto_cm"] * df["ancho_cm"]
    df["mismo_estado"] = (df["estado_cliente"] == df["estado_vendedor"]).astype(int)
    return df


def dividir_train_test(df: pd.DataFrame):
    """Partición 80/20 reproducible. Es regresión, así que no se estratifica por
    clase; se usa la misma semilla en todo el proyecto."""
    X = df[config.VARIABLES_NUMERICAS + config.VARIABLES_CATEGORICAS]
    y = df[config.TARGET]
    return train_test_split(
        X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_STATE
    )
