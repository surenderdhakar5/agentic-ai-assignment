from data import orders, products
from logger import log_tool


# Tool 1: Get Order Details
def get_order(order_id):

    log_tool("get_order", order_id)

    return orders.get(order_id)


# Tool 2: Get Product Details
def get_product(product_id):

    log_tool("get_product", product_id)

    return products.get(product_id)


# Tool 3: Search Products
def search_products(query):

    log_tool("search_products", query)

    results = []

    for product in products.values():

        if query.lower() in product["name"].lower():
            results.append(product)

    return results
    