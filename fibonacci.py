def fibo():
    n = input("How many fibonacci numbers do you want? ")
    f = []
    if n == 0:
        print "Here is the series", f
        return
    for i in range(0,n):
        if i == 0 or i == 1:
            f.append(1)
        else:
            j = f[i-2] + f[i-1]
            f.append(j)
    print "Here is the series", f
fibo()
