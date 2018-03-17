a=int(input("Please enter a: "))
b=int(input("Please enter b: "))
c=a+b
d=a+c
if round(a/b, 1) == round(b/c, 1):
    print("[a,b]: Golden ratio- yes.")
else:
    print("[a,b]: No golden ratio.")

if round(a/c, 1) == round(c/d, 1):
    print("[a,c]: Golden ratio- yes.")
else:
    print("[a,c]: No golden ratio.")