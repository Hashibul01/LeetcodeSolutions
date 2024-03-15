def runningSum(nums):

    output = 0
    arr = []

    for num in nums:
        output += num
        arr.append(output)

    return arr






print(runningSum([1,2,3,4]))
