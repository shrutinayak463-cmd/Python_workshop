food_menu = {
    "idly": 30,
    "dosa": 50,
    "poori": 45,
    "pongal": 40,
    "biriyani": 120,
    "fried_rice": 90,
    "chapathi": 35,
    "parotta": 20,
    "pizza": 150,
    "burger": 80
}

# Taking user input
item = input("Enter a food item: ").lower()

# Checking and printing the price
if item in food_menu:
    print(f"Price of {item} is ₹{food_menu[item]}")
else:
    print("Sorry, this item is not available in the food menu.")