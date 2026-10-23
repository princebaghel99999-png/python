def hello(n):
    if n==0:
        return
    
    print("Start",n)

    hello(n-1)

    print("End",n)

hello(2)
