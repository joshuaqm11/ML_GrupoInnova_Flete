"""Preprocesadores (ColumnTransformer) — RESPONSABLE: Fabio.

Dos versiones, porque cada familia de modelos necesita algo distinto:
  * crear_preprocesador_lineal(): imputación + StandardScaler + One-Hot
    (Ridge/Lasso son sensibles a la escala y no entienden códigos ordinales).
  * crear_preprocesador_arboles(): imputación + OrdinalEncoder
    (los árboles no necesitan escalar y One-Hot de 70 categorías los vuelve lentos).

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
    # TODO (Fabio): revisar/justificar cada paso en notebooks/02_preprocesamiento.ipynb
    numericas = Pipeline([
        ("imputar", SimpleImputer(strategy="median")),   # mediana: decisión del Lab 4
        ("escalar", StandardScaler()),
    ])
    categoricas = Pipeline([
        ("imputar", SimpleImputer(strategy="constant", fill_value="sin_categoria")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])
    return ColumnTransformer([
        ("num", numericas, config.VARIABLES_NUMERICAS),
        ("cat", categoricas, config.VARIABLES_CATEGORICAS),
    ])


def crear_preprocesador_arboles() -> ColumnTransformer:
    # TODO (Fabio): revisar/justificar en notebooks/02_preprocesamiento.ipynb
    numericas = SimpleImputer(strategy="median")
    categoricas = Pipeline([
        ("imputar", SimpleImputer(strategy="constant", fill_value="sin_categoria")),
        ("ordinal", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)),
    ])
    return ColumnTransformer([
        ("num", numericas, config.VARIABLES_NUMERICAS),
        ("cat", categoricas, config.VARIABLES_CATEGORICAS),
    ])
