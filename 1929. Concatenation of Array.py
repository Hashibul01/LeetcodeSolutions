def getConcatenation(nums):

    ans = []

    for _ in range(2): # loop through the list 2 times 
        for num in nums: 

            ans.append(num) # append digits to ans array        

    return ans


print(getConcatenation([1,2,1]))