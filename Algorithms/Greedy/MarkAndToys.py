def max_toys(prices, rupees):
    toys=0
    prices.sort()
    
    while rupees >= prices[0]:
        toys+=1
        rupees-=prices[0]
        prices = prices[1:]
    return toys

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
