def VowelsCount(x):
    a = e = i = o = u = 0
    for k in range(len(x)):
        if x[k].lower() == 'a':
            a += 1
        elif x[k].lower() == 'e':
            e += 1
        elif x[k].lower() == 'i':
            i += 1
        elif x[k].lower() == 'o':
            o += 1
        elif x[k].lower() == 'u':
            u += 1
    print(f"a = {a}, e = {e}, i = {i}, o = {o}, u = {u}")
    return True



def iCount(x):
    count = []
    for i in range(len(x)):
        if x[i].lower() == 'i':
            count.append(i)
        
    if count: 
        print(f"Positions of 'i':\n {count}")    
        return True
    else: 
        print("the letter 'i' is not found")    
        return False
    
    
    
