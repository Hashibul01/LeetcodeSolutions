# Boyer-Moore Voting Algorithm

def majorityElement(nums): 

    candidate = None # Set candidate = None (Assumption: No Majority Element)
    count = 0 # If candidate found in array, increase count

    for num in nums:
        if count == 0: 
            candidate = num # Replace candidate with num
            count += 1 # Increment count

        elif num == candidate: # if num and candidate same
            count += 1 # increase count

        else:
            count -= 1 # if num not same as candidate, decrease count

    return candidate


print(majorityElement([2,2,1,1,1,2,2]))
        






