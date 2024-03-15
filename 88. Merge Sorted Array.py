def merge(nums1, m, nums2, n):

    last_pointer = m + n -1 # getting the total length of nums1 and placing pointer to the last digit of the total array

    while m > 0 and n > 0: # while both m and n are greater than 0

        if nums1[m-1] > nums2[n-1]: # compares the last values of both nums1 and nums2
            nums1[last_pointer] = nums1[m-1] # initializes the last value (empty) with nums1 value
            m -= 1 # decreases nums1 counter by 1

        else:
            nums1[last_pointer] = nums2[n-1] # initializes the last value (empty) with nums2 value
            n -= 1 # decreases nums2 counter by 1

        last_pointer -= 1 # decreases last_pointer counter by 1

    while n > 0: # if nums2 still has values, add all to the start of nums1 since already sorted
        nums1[last_pointer] = nums2[n-1] 
        n -= 1
        last_pointer -= 1



    return nums1


print(merge([4,5,6,0,0,0], 3, [1,2,3], 3))


                