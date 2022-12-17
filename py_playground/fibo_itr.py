
def fibo(n):

    f = [0,1]
    f0 = f[0]
    f1 = f[1]
    
    #0 1 2 3 4 5 6 7  
    #0,1,1,2,3,5,8,13
    
    fn=0 if n==0 else 1
    for i in range(2,n+1): 
        fn = f[0] + f[1]
        f[0]=f[1]
        f[1]=fn
                
    return fn

if __name__=='__main__':
    print ("Start...")
    res = fibo(n=6)
    print (res)
    print ('END')