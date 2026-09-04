#Problem 2: Simple Shopping Cart

customerName = input("Enter customer name: ")

productName1 = input("Enter product name: ")
productPrice1 = float(input("Enter product price: "))
productName2 = input("Enter product name: ")
productPrice2 = float(input("Enter product price: "))
productName3 = input("Enter product name: ")
productPrice3 = float(input("Enter product price: "))

subTotalCost = productPrice1+productPrice2+productPrice3

if subTotalCost >= 5000:
    discount = subTotalCost * 0.2
elif subTotalCost >= 3000:
    discount = subTotalCost * 0.1
elif subTotalCost >= 1000:
    discount = subTotalCost * 0.05
else:
    discount = 0

totalCost = subTotalCost - discount
print (f"Customer Name:{customerName}")
print (f"Subtotal Cost: {subTotalCost}")
print (f"Discount: {discount:.2f}")
print (f"Total Cost: {totalCost:.2f}")

