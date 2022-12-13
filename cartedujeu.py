import zone

class cartejeu:
    """Constructeur de base de la carte"""
    def __init__(self) -> None:

        self.zones : list[zone.zonedejeu]

        for i in range(6):
            self.zones.append(zone.zonedejeu(i))
    
