from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

DATA = ROOT/'data'

ORDERS_FILE = DATA/"olist_orders_dataset.csv"
ORDER_ITEMS_FILE = DATA/"olist_order_items_dataset.csv"
PAYMENTS_FILE = DATA/"olist_order_payments_dataset.csv"
REVIEWS_FILE = DATA/"olist_order_reviews_dataset.csv"
CUSTOMERS_FILE = DATA/"olist_customers_dataset.csv"
PRODUCTS_FILE = DATA/"olist_products_dataset.csv"
SELLERS_FILE = DATA/"olist_sellers_dataset.csv"
GEOLOCATION_FILE = DATA/"olist_geolocation_dataset.csv"
CATEGORY_TRANSLATION_FILE = DATA/"product_category_name_translation.csv"