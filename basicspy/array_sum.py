# Given an array A[] and a number x, check for pair in A[] with sum as x

arr = [10, 20, 30, 40, 70, 48, 12]
x = 60

# 20, 40
# 48, 12

# approach 1
output = []
for i, v in enumerate(arr):
    for j in range(i + 1, len(arr)):
        if (v + arr[j]) == x:
            output.append((v, arr[j]))

# approach 2
dic = {}
for v in arr:
    y = x - v
    if (y in arr) and (y not in dic.values()) and (y != v):
        dic.update({y: v})

print(dic)
