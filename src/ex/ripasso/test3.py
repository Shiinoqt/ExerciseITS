def products(products: dict[str,int]) -> dict[str,int]:

    new_products: dict[str,int] = {}

    for key, value in products.items():
        if value < 50:
            value = (value * 110)/100
            new_products[key] = round(value, 2)
        
    return new_products