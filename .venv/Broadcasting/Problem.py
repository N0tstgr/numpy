prices = [122,34,56]

discount = 10

final_prices = []
# taking the one element from the prices and storing in the prices
for price in prices:
    final_price = price - (price * discount/100)
    final_prices.append(final_price)

print(final_prices)