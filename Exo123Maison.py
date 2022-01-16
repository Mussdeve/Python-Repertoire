#Exercice n°1
"""
a = int(input('Entrez la première valeur : '))
b = int(input('Entrez la deuxième valeur : '))
c = int(input('Entrez la troisième valeur : '))

if (0 <a and b and c< 40000):
    print((a+b+c)/3)
"""
# Exercice n°2
"""
a = int(input("Entrez une valeur : "))

if a >= 0:
    print('Ce nombre est positif ou nul')
elif a<0:
    print('Ce nombre est négatif')
"""
# Exercice n°3
a = int(input('Ecrivez une valeur : '))
""" isAModulo3 = a % 3 == 0
isAModulo5 = a % 5 == 0

if isAModulo3:
    print('Ce nombre est un multiple de 3')
if isAModulo5:
    print('Ce nombre est un multiple de 5')
else:
    print('Ce n5ombre n\'est pas un multiple de 3 ou de 5') """

def isMultiple(tonChiffre, multiple):
    if(tonChiffre % multiple == 0):
        print('Ce nombre est un multiple de ' + multiple)

isMultiple(a,3)
isMultiple(a,5)

""" if a%3 == 0 and a%5 == 0:
    print('Ce nombre est un multiple de 3 et de 5')
elif a%3 == 0:
    print('Ce nombre est un multiple de 3')
elif a%5 ==0:
    print('Ce nombre est un multiple de 5')
else:
    print('Ce nombre n\'est pas un multiple de 3 ou de 5') """

