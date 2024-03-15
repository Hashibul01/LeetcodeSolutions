def isPalindrome(x):

    str_x = str(x) # Convert integer to string

    if str_x == str_x[::-1]: # If string == reverse of the string
        return True # Return True
    
    return False # Return False
        
    

print(isPalindrome(-121))