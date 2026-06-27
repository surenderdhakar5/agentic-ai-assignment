from agent import run_agent


def test_order_status():
    result = run_agent("Where is my order ORD-1001?")
    assert "Rahul" in result
    assert "Shipped" in result


def test_product_details():
    result = run_agent("P101")
    assert "Nike Shoes" in result
    assert "5000" in result


def test_product_search():
    result = run_agent("Search Shoes")
    assert "Nike Shoes" in result
    assert "Adidas Shoes" in result


def test_cheaper_alternative():
    result = run_agent("Cheaper P101")
    assert "Cheaper Alternative" in result


def test_invalid_product():
    result = run_agent("P999")
    assert "Product not found" in result