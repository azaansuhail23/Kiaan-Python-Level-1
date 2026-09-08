for row in range(1,11):
    for col in range(1,6):
        if row==1 or row==10:
            print("*",end='')
        
        elif col==1 or col==5:
            print("*",end='')
        
        else:
            print(" ",end='')
    
    print()