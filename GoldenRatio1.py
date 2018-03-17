n = int(input("enter number"))
for a in range(1, n):
    for b in range(1, n):
        c = a+b
        if round(a/b, 1) == round(b/c, 1):
            print(a, b)
