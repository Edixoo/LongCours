import cartes

class paquetdecarte():
    def __init__(self) -> None:
        self.listecarte = []
        for i in range (12):
            if(i%2==0):
                carte=cartes.carte_mouvement(0,'mouvement direct')
                
            else:
                carte=cartes.carte_mouvement(1,'mouvement ordinaire')
            self.listecarte.append(carte)

        
#Dictionnaire de cartes pour visualisation:
{
    'carte_mouvement':[
        'mouvement direct',
        'mouvement ordinaire',
    ],
    'carte_tempete':[
        'Tempête',
    ],
    'carte_bras_de_fer':[
        'force 0',
        'force 1',
        'force 2',
        'force 3',
    ]
}
