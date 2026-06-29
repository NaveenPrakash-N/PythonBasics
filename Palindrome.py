def pal(a):
    
    for i in range(0,len(a)//2):
        if a[i]!=a[len(a)-1-i]:
            return False
        
    return True
    

if pal("madam"):
    print("palindrome")
else:
    print("not")


                                                        