def read_input() -> (int, int):
    n, m = map(int, input().split())

    one_prices = []
    six_prices = []

    for _ in range(m):
        six_price, one_price = map(int, input().split())
        one_prices.append(one_price)
        six_prices.append(six_price)

    return n, m, one_prices, six_prices


def solve(n, one_prices, six_prices):
    one_prices.sort()
    six_prices.sort()

    one_price = one_prices[0]
    six_price = six_prices[0]

    if one_price * 6 > six_price:
        return n // 6 * six_price + min(n % 6 * one_price, six_price)
    else:
        return n * one_price


def main():
    n, m, one_prices, six_prices = read_input()
    result = solve(n, one_prices, six_prices)
    print(result)


main()
