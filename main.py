import world

longcours=world.world()
print(len(longcours.map.zones[0].listeport),"port dans la zone 0")
print(len(longcours.map.zones[1].listeport),"port dans la zone 1")
print(len(longcours.map.zones[2].listeport),"port dans la zone 2")
print(len(longcours.map.zones[3].listeport),"port dans la zone 3")
print(len(longcours.map.zones[4].listeport),"port dans la zone 4")
print(len(longcours.map.zones[5].listeport),"port dans la zone 5")
print(len(longcours.map.zones),"zones")
longcours.jouerpartie()
#1| Corriger la baston (faire l'addition des puissance des cartes) / La refaire
#2| Créer la fonction d'achat au port
#3| Debug Achat puis vente
