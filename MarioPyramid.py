
def strin(x):
        try:
                x = abs(int(x))
                y = range(x)[-1]
                for i in range (1,x+1):
                        print (' '*y ,'*'*i)
                        y-=1
                return True        
        except ValueError:
                print("Not a Valid entry")
                return False

def listed(x):
        try:
                x=int(x)       
                L = [" "]*x
                for i in range(len(L)):
                        L.append("*")
                        L.pop(0)
                        print(L)
                return True
        except ValueError:
                print("Not a valid entry")
                return False        