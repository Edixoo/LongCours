import zone

class cartejeu:
    """Constructeur de base de la carte"""
    def __init__(self) -> None:

        self.zones = [zone.zonedejeu]

        for i in range(6):
            ajout=zone.zonedejeu
            self.zones.append(ajout)
    
