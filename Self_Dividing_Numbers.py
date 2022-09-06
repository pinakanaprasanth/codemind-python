def s_d(n):
    for i in str(n):
        if i=="0" or n%int(i)>0:
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if s_d(i):
        print(i,end=" ")
    
    
        
        

