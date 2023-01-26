


def fibonacci(n):
    
    if n==0:
        return 0
    if n==1:
        return 1

    fib=[0,0]

    fib[0]=0
    fib[1]=1
    fib2 = None

    for _ in range(2,n+1):
        fib2 = fib[0]+fib[1]
        fib[0] = fib[1]
        fib[1] = fib2
    
    return fib2



if __name__=='__main__':
    print ("start")

    ans = fibonacci(10)
    print ("ANS:=",ans)

    print ("END")