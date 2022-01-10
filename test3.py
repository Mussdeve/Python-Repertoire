def affiche_menu():
    print("Menu :")
    print("* Action 1")
    print("* Action 2")

affiche_menu() #Appel à la fonction

def dire(texte):
    print('#' + texte)

dire('Bonjour')
dire('Au revoir')
dire('A demain')

def addition(a,b):
    return a + b

somme = addition(2,5)
print(somme)

def saluer (nom='Visiteur'):
    print('Bonjour' + nom)

saluer('Clem')
saluer ()