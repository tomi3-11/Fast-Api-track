def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name, item_price)


prices = {
        "Book": 500.0,
        "pens": 105.90
    }
process_items(prices)
