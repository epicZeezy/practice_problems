
# Find out what's the most candy you can buy given an array of candy prices and limited money

# Input: candy prices: [5, 6, 7, 8], pocket money: $10
# Output: 2 candies


def get_neighbors(candy_prices, current_price, current_depth):
    neighbors = []
    for candy_price in candy_prices:
        difference = current_price - candy_price
        if difference >= 0:
            neighbors.append((difference, current_depth + 1))

    return neighbors


def get_max_candies(candy_prices, pocket_money):
    stack = [(pocket_money, 0)]
    num_candies_bought = 0
    while stack != []:
        print(stack)
        price, depth = stack.pop()
        if price == 0:
            if depth > num_candies_bought:
                num_candies_bought = depth
        else:
            neighbors = get_neighbors(candy_prices, price, depth)
            stack.extend(neighbors)

    return num_candies_bought


candy_prices = []
n = int(input("Enter number of elements:"))
for i in range(0, n):
    element = int(input())
    candy_prices.append(element)

pocket_money = int(input("How much money do you have?"))
print(get_max_candies(candy_prices, pocket_money))
