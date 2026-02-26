import sys

nb1 = float(sys.argv[1])
nb2 = float(sys.argv[3])
operateur = sys.argv[2]

if operateur == "+":
    print(nb1+nb2)
elif operateur == "-":
    print(nb1-nb2)
elif operateur == "*":
    if nb1 == int(nb1):
        resultat = 0
        for i in range (int(nb1)):
            resultat += nb2
        print(resultat)
    elif nb2 == int(nb2):
        resultat = 0
        for i in range (int(nb2)):
            resultat += nb1
        print(resultat)
    else:
        print(nb1*nb2)
    
    print(nb1*nb2)
elif operateur == "/":
    print(nb1/nb2)
else:
    print("Erreur dans l'opérande")