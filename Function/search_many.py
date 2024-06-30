def searchmany(x,y,z):
    count = 0 
    for i in x:
        if i ==y:
            count = count +1
        if count == z:
            return True
        else:
            return False
        
    print(searchmany([10,17,15,12],15,1))