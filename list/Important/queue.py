Q=[]
while True:
    print("1. Adding")
    print("2. Removing")
    print("3. Display")
    print("4. Exit")
    opt=int(input("Enter your option "))
    if opt==1:
        value=int(input("Enter any value"))
        Q.append(value)
        print(f'{value} added inside Q')
    elif opt==2:
        if len(Q)==0:
            print("Queue is empty")
        else:
            value=Q[0]
            del Q[0]
            print(f'{value} deleted from Queue')
    elif opt==3:
        print(f'{Q}')
    elif opt==4:
        break
    else:
        print("invalid option")
