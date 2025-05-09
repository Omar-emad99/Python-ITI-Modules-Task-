def Triangle(x):
    try:
        x = int(x)
        if x <= 0:
            return False
        for i in range(1, x + 1):
            for j in range(1, i + 1):  
                print(f"{i}x{j}={i*j}", end=" ")
            print()
        return True
    except ValueError:
        print("Not a Valid entry")
        return False

def listed(x):
    table = []
    minitable = []
    try:        
        x=int(x)    
        for i in range(1, x + 1):
            for j in range(1, i + 1):  
                x= i*j
                minitable.append(x)  
    
            table.append (minitable)
            minitable = []       
            
        del minitable
        print(table)
        return True
    except ValueError:
        print("Not a Valid entry")
        return False

