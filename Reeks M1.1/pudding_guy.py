units_purchased = int(input())
price_per_unit = float(input())
barcodes_per_coupon = int(input())
miles_per_coupon = int(input())

total_cost = units_purchased * price_per_unit
coupons = units_purchased // barcodes_per_coupon
miles = coupons * miles_per_coupon

print(f"Phillips spendeerde ${total_cost:.2f} voor {miles} frequent flyer mijlen.")
