n = int(input("Enter range:"))

def fibonacci(n):
    l = []
    a,b = 0,1
    while(a<n):
        l.append(a)
        a,b = b,a+b
    return l

l1 = fibonacci(n)
for x in l1:
    print(x)