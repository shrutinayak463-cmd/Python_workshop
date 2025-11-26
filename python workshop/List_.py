products_list = [
    "Laptop", "Mobile", "Headphones", "Keyboard", "Mouse",
    "Charger", "Camera", "Smartwatch", "Tablet", "Speaker"
]

print("\nLIST EXAMPLE")
print("Original List:", products_list)

products_list.append("Printer")
print("After append:", products_list)

products_list.insert(2, "USB Cable")
print("After insert at index 2:", products_list)

products_list.remove("Mouse")
print("After remove 'Mouse':", products_list)

products_list.pop()
print("After pop():", products_list)

products_list.sort()
print("After sort():", products_list)

products_list.reverse()
print("After reverse():", products_list)
