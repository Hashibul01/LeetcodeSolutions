def searchInsert(nums, target):

    counter = 0 # to hold the index value of where a match is found or the index value becomes higher than the target

    for i in range(0, len(nums)): # loops through the nums array
        if nums[i] == target or nums[i] > target: # checks if match found or index value higher than target
            counter = i # in both cases, stores the index value
            break # breaks out of loop to stop looking further

        else:
            counter = len(nums) # if none of the above conditions match, collects the entire length of nums

    return counter


print(searchInsert([1,3,5,6], 5))