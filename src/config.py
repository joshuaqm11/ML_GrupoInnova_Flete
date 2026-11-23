"""Configuración compartida del Proyecto 3 (Grupo Innova S.A.).

TODOS los notebooks importan de aquí la semilla, el tamaño de Test y las listas
de variables. Si alguien necesita cambiar algo, se discute en el equipo y se
cambia SOLO aquí, para que todos los modelos se comparen sobre el mismo Test.
"""
from pathlib import Path

# ---------------------------------------------------------------- rutas
RAIZ = Path(__file__).resolve().parents[1]
DATA_RAW = RAIZ / "data" / "raw" / "olist_ventas.csv"
REPORTS = RAIZ / "reports"
FIGURAS = REPORTS / "figuras"
METRICAS_CSV = REPORTS / "metricas_modelos.csv"

# ------------------------------------------------------- reproducibilidad
RANDOM_STATE = 42
TEST_SIZE = 0.20
CV_FOLDS = 5

# ---------------------------------------------------------------- target
# Decidido en el Lab 4 y confirmado en notebooks/00: costo de envío por ítem.
TARGET = "flete"

# Nombres en español (mismos del Lab 4)
NOMBRES_ESPANOL = {
    "order_item_id": "numero_item",
    "price": "precio",
    "freight_value": "flete",
    "order_status": "estado_orden",
    "order_purchase_timestamp": "fecha_compra",
    "order_delivered_customer_date": "fecha_entrega",
    "order_estimated_delivery_date": "fecha_entrega_estimada",
    "product_name_lenght": "largo_nombre_producto",
    "product_description_lenght": "largo_descripcion_producto",
    "product_photos_qty": "cantidad_fotos",
    "product_weight_g": "peso_g",
    "product_length_cm": "largo_cm",
    "product_height_cm": "alto_cm",
    "product_width_cm": "ancho_cm",
    "product_category_name_english": "categoria_producto",
    "customer_zip_code_prefix": "codigo_postal_cliente",
    "customer_city": "ciudad_cliente",
    "customer_state": "estado_cliente",
    "seller_zip_code_prefix": "codigo_postal_vendedor",
    "seller_city": "ciudad_vendedor",
    "seller_state": "estado_vendedor",
    "review_score": "calificacion_resena",
    "payment_type": "tipo_pago",
    "payment_installments": "cuotas_pago",
    "payment_value": "valor_pago",
}

# ------------------------------------------------------------ predictores
# Solo variables que se conocen AL MOMENTO DE LA COMPRA (cuando se cotiza el flete).
VARIABLES_NUMERICAS = [
    "peso_g", "largo_cm", "alto_cm", "ancho_cm",
    "volumen_cm3",      # creada: largo * alto * ancho
    "precio",
    "numero_item",
    "mismo_estado",     # creada: 1 si cliente y vendedor están en el mismo estado
]
VARIABLES_CATEGORICAS = ["categoria_producto", "estado_cliente", "estado_vendedor"]

# Excluidas a propósito (fuga de información / no se conocen al comprar):
EXCLUIDAS_POR_FUGA = [
    "valor_pago",           # el pago ya incluye el flete
    "fecha_entrega", "dias_entrega", "entregado_a_tiempo",  # pasan después de la compra
    "calificacion_resena",  # la reseña llega después de la entrega
]
