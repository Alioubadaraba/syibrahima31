class Vehicule:
    def _init_(self, modele: str, disponible: bool = True):
        self.modele = modele
        self.disponible = disponible

    def _str_(self):
        return f"Véhicule: {self.modele}, Disponible: {'Oui' if self.disponible else 'Non'}"


class ParcAuto:
    def _init_(self):
        self.vehicules = []

    def ajouter_vehicule(self, v: Vehicule):
        self.vehicules.append(v)

    def lister_disponibles(self):
        return [v for v in self.vehicules if v.disponible]

    def rechercher(self, modele: str):
        return [v for v in self.vehicules if v.modele.lower() == modele.lower()]


