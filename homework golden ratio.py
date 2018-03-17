n = int(input("enter number "))
for a in range(1, 100):
    for b in range(1, 100):
        c = a+b
        if  (a/b) == (b/c) and a/b <= 0.1:
            print("yes")
       #else:
       #    print("no golden ratio")