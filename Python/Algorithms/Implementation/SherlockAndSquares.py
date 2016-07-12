import math
n = raw_input()

for i in range(int(n)):
    nums = raw_input().split()
    a = int(nums[0])
    b = int(nums[1])
    
    print int(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
