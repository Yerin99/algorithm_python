n = int(input())  # 도시의 개수
roads = list(map(int, input().split()))  # 도로 길이
oil_price = list(map(int, input().split()))  # 오일의 리터당 가격
result = 0
cheaper_oil = oil_price[0]

for i in range(n-1):
    # result += roads[i]*min(oil_price[:i+1])
    if cheaper_oil > oil_price[i]:
        cheaper_oil = oil_price[i]
    result += roads[i]*cheaper_oil
print(result)