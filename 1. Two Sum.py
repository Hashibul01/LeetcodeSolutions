def twosums(nums, target):

    mydict = {} # Stores both index and values when result is subtracted by the instance of array for eg: 9-2. So 
                # stores the value and array index of '2'

    for index, value in enumerate(nums): # 'enumerate' function stores both the index and the value
        result = target - value # for example: 9-2 = 7
 
        if result in mydict: # checks if 7 is in our dictionary. initially dictionary is empty
            return(index, mydict[result]) # if 7 is found, returns the 'index' and results index from dictionary
        
        else:
           mydict[value] = index # if 7 is not found, adds the value and index in dictionary
                                 # if previously in dictionary (for duplicates), rewrites 7's index

    return None # if no match found.



print(twosums([2, 7, 11, 15],9))
