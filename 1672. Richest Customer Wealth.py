def maximumWealth(accounts):

    return max(sum(amount) for amount in accounts)






print(maximumWealth([[1,5],[7,3],[3,5]]))