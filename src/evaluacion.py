"""Métricas comunes — todos los modelos se evalúan con ESTA función.

Cada notebook de modelos (03 y 04) llama a registrar_metricas(...) y así
reports/metricas_modelos.csv se va llenando para la tabla comparativa (notebook 05).
"""
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src import config


def calcular_metricas(y_real, y_pred) -> dict:
    return {
        "RMSE": float(np.sqrt(mean_squared_error(y_real, y_pred))),
        "MAE": float(mean_absolute_error(y_real, y_pred)),
        "R2": float(r2_score(y_real, y_pred)),
    }


def registrar_metricas(nombre_modelo, responsable, modelo, X_train, y_train, X_test, y_test,
                       mejores_parametros=None):
    """Calcula métricas en Train y Test (para detectar overfitting) y las guarda
    en reports/metricas_modelos.csv, reemplazando la fila previa del mismo modelo."""
    tr = calcular_metricas(y_train, modelo.predict(X_train))
    te = calcular_metricas(y_test, modelo.predict(X_test))
    fila = {
        "modelo": nombre_modelo,
        "responsable": responsable,
        "RMSE_train": tr["RMSE"], "MAE_train": tr["MAE"], "R2_train": tr["R2"],
        "RMSE_test": te["RMSE"], "MAE_test": te["MAE"], "R2_test": te["R2"],
        "mejores_parametros": str(mejores_parametros or {}),
    }
    config.REPORTS.mkdir(exist_ok=True)
    if config.METRICAS_CSV.exists():
        tabla = pd.read_csv(config.METRICAS_CSV)
        tabla = tabla[tabla["modelo"] != nombre_modelo]
        tabla = pd.concat([tabla, pd.DataFrame([fila])], ignore_index=True)
    else:
        tabla = pd.DataFrame([fila])
    tabla.to_csv(config.METRICAS_CSV, index=False)
    return pd.DataFrame([fila]).round(3)
