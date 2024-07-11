n = int(input())
nums = [1]*10

for i in range(1, n):
    temp_nums = [0]*10

    for j in range(10):
        for k in range(j, 10):
            temp_nums[k] += nums[j] % 10007

    nums = temp_nums[:]

print(sum(nums) % 10007)
