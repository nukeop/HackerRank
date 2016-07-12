N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
    C.append( int(number) )
    i = i+1

bought = [0 for x in range(K)]
sum = 0

for flower in range(len(C)):
    C.sort()
    C=list(reversed(C))
    
    bought.sort()
    
    sum += (bought[0]+1)*C[0]
    bought[0] += 1
    C = C[1:]
    
print sum
