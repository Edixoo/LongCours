class marchandises:
    def __init__(self, ticket: int, nom: str, couleur: str):
        self.ticket_max:  int = ticket
        self.nom: str = nom
        self.couleur: str = couleur
        self.valeurachat: int


class tresort (marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'or', 'jaune')


class textiles(marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'textile', '')


class petrole(marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'petrole', 'bleu')


class cereales(marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'cereales', '')


class bois(marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'bois', 'marron')


class machines_outils(marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'machines-outils', '')



