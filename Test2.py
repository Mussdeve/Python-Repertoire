a = int(input("a:"))
b = int(input("b:"))
while b !=0:
    a, b = b, a%b
print(a)