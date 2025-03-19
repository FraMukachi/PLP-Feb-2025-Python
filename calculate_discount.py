def calculate_discount(price, discount_percent):
    # Checking if the discount is 20% or higher
    if discount_percent >= 20:
        #Calculating discounted price
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Returns original price if discount is less than 20%
        return price
    
# User Input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the final price
final_price = calculate_discount(original_price, discount_percent)

# Printing results 
if discount_percent >= 20:
    print(f"Final price after applying {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: R{original_price:.2f}")