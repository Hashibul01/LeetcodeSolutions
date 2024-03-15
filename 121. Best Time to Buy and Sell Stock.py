def maxProfit(prices):

    buying = prices[0] # Initially putting buying as the first element
                       # and comparing all values with it to find the lowest
    profit = 0 # profit initially 0. 

    for price in prices[1:]: # Starting from prices[1] as prices[0] = buying
        buying = min(buying, price) # Taking min of prices[0] and each iteration of
                                    # prices as new buying 
        
        profit = max(profit, price - buying) # Taking max between profit and price - buying
                                             # as new profit

    return profit

    

print(maxProfit([7,1,5,3,6,4]))
