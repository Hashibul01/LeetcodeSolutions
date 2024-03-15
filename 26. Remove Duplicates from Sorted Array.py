def removeDuplicates(nums):

    left_pointer = 1 # Initially stays on first index for example: 0

    for right_pointer in range(1, len(nums)): # right pointer to loop through the list and compare with left pointer

        if nums[right_pointer] != nums[right_pointer-1]: # checking for instances where left and right pointer values are different
            nums[left_pointer] = nums[right_pointer] # when different, left pointer value replaces with right pointer
            left_pointer += 1 # increments left pointer by 1

        else:
            continue # if left and right pointer values are same, loop continues

    return left_pointer


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        
    
