def calculerVolume():
    hauteur = int (input("Entrez la hauteur :"))
    rayon = int (input("Entrez la rayon :"))
    pi = 3.14

    base = pi * pow(rayon,2)

    volume = base * hauteur / 3


    print ("Le volume est {}".format(volume)+ "cm3")

calculerVolume()