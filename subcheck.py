def substringcheck(string,sub):
    start = 0
    count = 0
    condition = True
    while condition :
        check = string.find(sub,start)
        if check == -1 :
            condition = False
        else :
            count +=1
            start = check+1
    return(count)

if __name__ == '__main__':
    string = input("Enter string : ").strip()
    sub = input("Enter substring to search for : ").strip()
    
    count = substringcheck(string, sub)
    print(count)