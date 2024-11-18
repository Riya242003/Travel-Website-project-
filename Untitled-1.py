def rev(s):
    

    j=len(s)-1
   
    r=""
   
    while j<=0:
        r+=s[j]
        j-=1 
        
    return r  
    
print(rev("hello"))