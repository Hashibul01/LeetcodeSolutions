def singleNumber(nums):

    seen = set() # create empty set

    for num in nums:

        if num not in seen: # if num is not in 'seen'
            seen.add(num) # add num to 'seen'

        else: # if num is in 'seen'
            seen.remove(num) # remove num from 'seen'

    return seen.pop() # only one unique value remains in the end. Pop that and return the popped value



        

print(singleNumber([4, 1,2,1,2]))