def calculate_discount(price,discount_percent):
    if discount_percent >= 20 :
        discount = (discount_percent/100)*price
        
        discounted_price = price-discount

        price=discounted_price

        return price

    else:
        
     return price

price = int(input("Enter the original price of the item: "))
discount = int(input("What percentage if discount were you given: "))

final_price = calculate_discount(price,discount)

print(f"The final price you will pay is KSHs.{final_price}")