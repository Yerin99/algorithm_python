import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    maximum_prices = [prices[-1]]
    prices = prices[::-1]

    for i in range(1, n):
        maximum_price = max(maximum_prices[-1], prices[i])
        maximum_prices.append(maximum_price)

    maximum_profit = 0

    for i in range(n):
        maximum_profit += maximum_prices[i] - prices[i]

    print(maximum_profit)
