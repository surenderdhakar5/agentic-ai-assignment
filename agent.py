from tools import get_order, get_product, search_products
from llm import general_chat


def run_agent(question):
    

    original_question = question
    question = question.upper()

    # ---------------- CHEAPER ALTERNATIVE ----------------
    if "CHEAPER" in question:

        words = question.split()
        product_id = None

        for word in words:
            clean = word.replace("?", "").replace(".", "").replace(",", "")
            if clean.startswith("P"):
                product_id = clean
                break

        if product_id is None:
            return "Please provide a Product ID."

        product = get_product(product_id)

        if product is None:
            return "Sorry! Product not found."

        alternatives = search_products("Shoes")

        cheaper_products = []

        for item in alternatives:
            if item["price"] < product["price"]:
                cheaper_products.append(item)

        if len(cheaper_products) == 0:
            return "No cheaper alternative available."

        best = cheaper_products[0]

        return (
            f"The product you selected is {product['name']} (₹{product['price']}).\n"
            f"Cheaper Alternative:\n"
            f"{best['name']} - ₹{best['price']}"
        )

    # ---------------- ORDER STATUS ----------------
    if "ORD-" in question:  

        words = question.split()
        order_id = None

        for word in words:
            clean = word.replace("?", "").replace(".", "").replace(",", "")

            if clean.startswith("ORD-"):
                order_id = clean
                break

        if order_id is None:
            return "Please provide a valid Order ID."

        order = get_order(order_id)

        if order is None:
            return "Order not found."

        product = get_product(order["product_id"])

        return (
            f"Order ID : {order_id}\n"
            f"Customer : {order['customer']}\n"
            f"Product : {product['name']}\n"
            f"Status : {order['status']}"
        )

    # ---------------- PRODUCT DETAILS ----------------
    words = question.split()

    product_id = None

    for word in words:
        clean = word.replace("?", "").replace(".", "").replace(",", "")

        if clean.startswith("P") and len(clean) > 1 and clean[1:].isdigit():
            product_id = clean
            break

    if product_id:

        product = get_product(product_id)

        if product is None:
            return "Sorry! Product not found."

        return (
            f"Product Details\n\n"
            f"Product ID : {product_id}\n"
            f"Product Name : {product['name']}\n"
            f"Price : ₹{product['price']}"
        )

    # ---------------- SEARCH PRODUCTS ----------------
    if (
        "SEARCH" in question
        or "SHOW" in question
        or "LIST" in question
    ):

        query = (
            original_question.replace("search", "")
            .replace("Search", "")
            .replace("show", "")
            .replace("Show", "")
            .replace("list", "")
            .replace("List", "")
            .strip()
        )

        found_products = search_products(query)

        if len(found_products) == 0:
            return "Sorry! No matching products found."

        response = "Available Products:\n\n"

        for product in found_products:
            response += f"• {product['name']} - ₹{product['price']}\n"

        return response

    # ---------------- GENERAL QUESTIONS ----------------
    # If no rule matches, ask Gemini
    return general_chat(original_question)

   