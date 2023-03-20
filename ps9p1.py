def comptotal(qty, price):
    total = price * qty
    if total > 1000:
        total = total * 0.9
    
    return total

# Main
print("enter the number of items purchased: ")
qty = int(input())
print("what was the price per unit?")
price = int(input())
comptotal(qty, price)
total = comptotal(qty, price)
print("you ordered" + str(qty) + "number of items. each item costs $" + str(price) + ". this gives you a final total of $" + str(total))
