def removeElement(nums, val):

    k = 0 # left pointer stays where value of k and val are same

    for i in nums: # loops through nums
        if i != val: # if i not equal to val
            nums[k] = i # left pointer replaces k position with the value of i
            k += 1 # k pointer increases

    return k


print(removeElement([3,2,2,3], 3))