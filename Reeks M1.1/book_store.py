book_price = 24.95
discount = 0.4

shipping_cost_first = 3
shipping_cost = 0.75

total_shipping = 0

total = (book_price * 60) * (1 - discount)

for x in range(60):
    if x == 1:
        total_shipping = total_shipping + shipping_cost_first
    else:
        total_shipping = total_shipping + shipping_cost

total = total + total_shipping

print(total)