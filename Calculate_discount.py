def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to apply.

  Returns:
    The final price after applying the discount.
  """

  if discount_percent >= 20:
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
  else:
    final_price = price

  return final_price

# Prompt the user to enter the price and discount percentage.
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function.
final_price = calculate_discount(price, discount_percent)

# Print the final price.
print("The final price after applying the discount is:", final_price)
