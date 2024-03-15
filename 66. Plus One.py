def plusOne(digits):

    n = len(digits) # finding the length of 'digits' for eg: 3

    for i in range(n-1, -1, -1): # 'n-1' represents last value of digits array (eg: 2) [Starting Position]
                                 # '-1' represents first value of digits array (eg: 0) [Ending Position]
                                 # '-1' represents going backstep by 1 in our digits array
                                 
        if digits[i] != 9: # if last digit not equals to 9 (eg: position 2)
            digits[i] += 1 # add 1
            return digits, range(n-1, digits[-1]) # return array to stop loop

        else:
            digits[i] = 0 # else make last digit = 0

    digits.insert(0,1) # if all values are 9 (eg: 999), loop will not go to return and break. In this case, insert '1' in '0' position
    return digits, range(n-1, digits[-1]) # return array to break loop




print(plusOne([1,9,9]))