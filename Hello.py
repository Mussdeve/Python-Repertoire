#msg="Hello world
#print(msg)

a=7
print(a+3)
b=3
print(a+b) 
# afficher le résultat des valeurs respectives des variables a et b 

# print(a)
# a = b + 1
# print(a)
# print(a+b)

# a += b #a = a + b
print(a)

a,b =11, 4
c=a//b
d=a%b
print('la division de '+ str(a)+ ' par ' + str(b) + ' est égale à ' +str(c)+'. Il reste '+ str(d))
print(d)

chaine = 'Et voilà du texte'
chaine1 = 'Nous l\'avons'
chaine2 = "\"réparée\""
print(chaine1 + " " + chaine2)

reponse = input () #une ligne vide apparait et attend que l'utilisateur entre une information

age = int(input ("Quel est vôtre âge ?"))
print("Vous avez " + str(age)+ " ans")

if age > 16 and age < 100 :
    print("Vous avez plus de 16 ans")
elif age > 100 or age < 0:
    print("Tu te moquerais pas de moi ?")
else :
    print("Tu es encore un peu jeune")

a=3
print(type(a))

b=8.2
print(type(b))

chaine="Au revoir"
print(type(chaine))
vrai= False 
print(type(vrai))

print(7 > 5 > 2)
print(b<a)

