import zone

class cartejeu:
    """Constructeur de base de la carte(map)"""
    def __init__(self) -> None:

        self.zones : list[zone.zonedejeu]
        self.zones=[]

        for i in range(6):
            self.zones.append(zone.zonedejeu(i))
    
