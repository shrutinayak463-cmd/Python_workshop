products_set = {
    "Laptop", "Mobile", "Headphones", "Keyboard", "Mouse",
    "Charger", "Camera", "Smartwatch", "Tablet", "Speaker"
}

print("Original Set:", products_set)

products_set.add("Printer")
print("After add:", products_set)

products_set.discard("Camera")
print("After discard 'Camera':", products_set)

products_set.add("Printer")
print(products_set)

products_set.remove("Mouse")
print(products_set)

products_set.clear()
print(products_set)
