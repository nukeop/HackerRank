def lonelyinteger(a):
    for i in range(len(a)):
        if a.count(a[i]) == 1:
            return a[i]

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
