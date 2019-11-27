def substringcheck(string,sub):
    start = 0 #initialize start index for searching with 0 
    count = 0 #initialize counter with 0
    condition = True #initialize condition with True to make the searching going on as long as it still find substring inside string
    while condition :
        check = string.find(sub,start) """using str.find() method to find in which index it should start seeking,with a parameters of sub 
        and start values """
        if check == -1 : #return false if the substring not found in string
            condition = False
        else :
            count +=1 #adding 1 to count everytime the program encounter a substring searched in a string
            start = check+1 #start value will be changed based on which index the str.find() method found the substring
    return(count)

if __name__ == '__main__':
    string = input("Enter string : ").strip() #prompt input for string 
    sub = input("Enter substring to search for : ").strip() #prompt input for substring that will be searched and counted
    
    substringsum = substringcheck(string, sub)#call the substringcheck function and save the return value into substringsum variable
    print(substringsum)  
