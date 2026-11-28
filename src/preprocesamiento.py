"""Preprocesadores (ColumnTransformer) — RESPONSABLE: Fabio.

Dos versiones, porque cada familia de modelos necesita algo distinto:
  * crear_preprocesador_lineal(): imputación + StandardScaler + One-Hot
    (Ridge/Lasso son sensibles a la escala y no entienden códigos ordinales).
  * crear_preprocesador_arboles(): imputación + OrdinalEncoder
    (los árboles no necesitan escalar y One-Hot de ~120 columnas los vuelve lentos).

Se usan SIEMPRE dentro de un Pipeline: Pipeline([("prep", ...), ("modelo", ...)])
para que el fit ocurra solo con Train (evita el data leakage del Lab 4, donde el
StandardScaler se ajustó con todo el conjunto antes de dividir).
"""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

from src import config


def crear_preprocesador_lineal() -> ColumnTransformer:
    # Justificación completa en notebooks/02_preprocesamiento.ipynb (sección 3).
    numericas = Pipeline([
        ("imputar", SimpleImputer(strategy="median")),   # mediana: decisión del Lab 4
        ("escalar", StandardScaler()),
    ])
    categoricas = Pipeline([
        ("imputar", SimpleImputer(strategy="constant", fill_value="sin_categoria")),  # no tener categoría también es información
        ("onehot", OneHotEncoder(handle_unknown="ignore")),  # categoría nueva en Test -> todo ceros, no falla
    ])
    return ColumnTransformer([
        ("num", numericas, config.VARIABLES_NUMERICAS),
        ("cat", categoricas, config.VARIABLES_CATEGORICAS),
    ])


def crear_preprocesador_arboles() -> ColumnTransformer:
    # Justificación completa en notebooks/02_preprocesamiento.ipynb (sección 3).
    numericas = SimpleImputer(strategy="median")  # sin escalar: los árboles cortan por umbrales
    categoricas = Pipeline([
        ("imputar", SimpleImputer(strategy="constant", fill_value="sin_categoria")),
        ("ordinal", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)),
    ])
    return ColumnTransformer([
        ("num", numericas, config.VARIABLES_NUMERICAS),
        ("cat", categoricas, config.VARIABLES_CATEGORICAS),
    ])
