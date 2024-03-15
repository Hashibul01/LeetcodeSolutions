def containsDuplicate(nums):

    seen = set() # Create an empty set to hold values

    for num in nums:
        if num in seen: # if num is present in 'seen' 
            return True # return True
        else:
            seen.add(num) # else add num to 'seen'

    return False # if num is not present in 'seen' return False

print(containsDuplicate([1,2,3,1]))
