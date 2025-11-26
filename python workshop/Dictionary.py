products_dict = {1: "Laptop",
    2: "Mobile",
    3: "Headphones",
    4: "Keyboard",
    5: "Mouse",
    6: "Charger",
    7: "Camera",
    8: "Smartwatch",
    9: "Tablet",
    10: "Speaker"
}


print(products_dict)


print("Keys:", products_dict.keys())
print("Values:", products_dict.values())

products_dict.update({11: "Printer"})
print("After update:", products_dict)

products_dict.pop(5)
print("After pop key 5:", products_dict)
