def isPrime(n):
     
    if (n <= 1): 
        return False 
    if (n <= 3): 
        return True 
  
    if (n % 2 == 0 or n % 3 == 0): 
        return False 
    
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
    return True 
  

def isThreeDivisors(n): 
    import math
    sq = math.sqrt(n) 
  
    if (sq * sq != n): 
        return False 
  
    if isPrime(sq):
        return True 
    else:
        return False  

s = raw_input()
n, k = [int(i) for i in s.split()]

nums = raw_input()
n_arr = []
magic_array = []
n_arr.append([int(i) for i in nums.split()])
# print(n_arr[0])
operations = []

arr_len = len(n_arr[0])
output = 0

for i in n_arr[0]:
    ops = lops = rops = 0
    li = ri = i
    is_li = False
    if isThreeDivisors(i):
        if len(magic_array) < k:
            magic_array.append(i)
            output += 1
            continue
        else:
            break

    while (li > 0) and (not isThreeDivisors(li)):
        li -= 1
        lops += 1
        is_li = isThreeDivisors(li)
        # print('(li, lops):', li, lops)

    while not isThreeDivisors(ri):
        ri += 1
        rops += 1
        # print('(ri, rops):', ri, rops)
    
    mn = i
    if lops < rops and is_li:
        ops = lops
        mn = li
    elif lops > rops:
        ops = rops
        mn = ri
    else:
        ops = rops
        mn = ri

    if len(magic_array) < k:
        magic_array.append(mn)
        output += ops
    else:
        break     
    
    # operations.append((i, ops))

print(output, magic_array)
