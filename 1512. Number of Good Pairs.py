def numIdenticalPairs(nums):

    index = 0 # count number of good pairs
    
    for x in range(len(nums)): # range of total digits starting from 0 to end
        for y in range(x+1, len(nums)): # range of total digits starting from 1 more than x to end

            if nums[x] == nums[y]: # if similar found
                index += 1 # index + 1

    return index
    



print(numIdenticalPairs([1,2,3,1,1,3]))

            

    
    
