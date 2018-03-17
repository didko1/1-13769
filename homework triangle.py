import math
n = int(input("input angle 36 or 108 "))
if n == 36:     #bedroto >osnovata
    a = math.cos(n)
    for b in range(0, 25):
        c = math.sqrt(2*b**2-2*(b**2)*a)
        print(b, c)
        if c > b:
            break
elif n == 108:    #osnova > bedroto
    cn = math.cos(n)
    for c in range(0, 25):
        b = math.sqrt((c**2)/2*(1-cn))
        print(b, c)
        if c > b:
            break



