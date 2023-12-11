def maximumProfit(prices):
    # Write your code here.
    size=len(prices)
    max_profit=0
    profit=0
    buy=prices[0]
    for i in range(size):
        if prices[i]<buy:
            buy=prices[i]
        profit=prices[i]-buy
        max_profit=max(profit,max_profit)
    return max_profit 
