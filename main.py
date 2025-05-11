import math

def round_tax(tax):
    return math.ceil(tax * 20) / 20.0

def calculate_price(item):
    base_price = item['price']
    imported = item['imported']
    exempt = item['exempt']
    tax_rate = 0
    
    if not exempt:
        tax_rate += 0.10
    if imported:
        tax_rate += 0.05
    tax = round_tax(base_price * tax_rate)
    return round(base_price + tax, 2), round(tax, 2)

if __name__ == "__main__":
    menu = {
        1: {"name": "book", "price": 12.49, "imported": False, "exempt": True},
        2: {"name": "music CD", "price": 14.99, "imported": False, "exempt": False},
        3: {"name": "chocolate bar", "price": 0.85, "imported": False, "exempt": True},
        4: {"name": "bottle of perfume", "price": 18.99, "imported": False, "exempt": False},
        5: {"name": "imported bottle of perfume", "price": 27.99, "imported": True, "exempt": False},
        6: {"name": "imported box of chocolates", "price": 10.00, "imported": True, "exempt": True},
        7: {"name": "packet of headache pills", "price": 9.75, "imported": False, "exempt": True},
        8: {"name": "box of imported chocolates", "price": 11.25, "imported": True, "exempt": True}
    }
    
    print("============ MENU =============")
    for key, val in menu.items():
        print(f"{key}. {val['name'].title()}")
    print("===============================")
    
    basket = []
    while True:
        choice = input("Enter item number (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        try:
            item_id = int(choice)
            if item_id not in menu:
                print("Invalid item selected.")
                continue
            quantity = int(input("Enter quantity: "))
            item = menu[item_id]
            total_price, tax = calculate_price(item)
            
            basket.append({
                "quantity": quantity,
                "name": item['name'],
                "price_with_tax": round(total_price * quantity, 2),
                "tax": round(tax * quantity, 2)
            })
            
        except ValueError:
            print("Invalid input. Try again.")
            
    
    total_tax = sum(item['tax'] for item in basket)
    total_cost = sum(item['price_with_tax'] for item in basket)
    
    print("\n============ RECEIPT ============")
    for item in basket:
        print(f"{item['quantity']} {item['name']}: {item['price_with_tax']:.2f}")
    print(f"Sales Taxes: {total_tax:.2f}")
    print(f"Total: {total_cost:.2f}")
    print("==================================\n")

