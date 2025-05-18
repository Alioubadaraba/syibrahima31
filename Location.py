class Location:
    def _init_(self, date_debut, date_fin, vehicule, client):
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.vehicule = vehicule
        self.client = client
    
    def duree(self):
        delta = self.date_fin - self.date_debut
        return delta.days
    
    def presentation_client(self):
        
        return f"Client: {self.client}"
    
    def afficher(self):
       
        print("Détails de la location:")
        print(f"Date de début: {self.date_debut}")
        print(f"Date de fin: {self.date_fin}")
        print(f"Véhicule: {self.vehicule}")
        print(f"Durée: {self.duree()} jours")
        print(self.presentation_client())
    
    @staticmethod
    def calcul_prix(nb_jours, prix_journalier=50):
        """Calcule le prix total de la location"""
        return nb_jours * prix_journalier
class Voiture():
    def _init_(self, marque, modele, annee, nb_portes):
        super()._init_(marque, modele, annee)
        self._nb_portes = nb_portes  # Attribut spécifique à Voiture

    def afficher_info(self):
        print(f"Voiture : {self._marque} {self._modele} ({self._annee}), {self._nb_portes} portes")


class Camion():
    def _init_(self, marque, modele, annee, capacite_tonnes):
        super()._init_(marque, modele, annee)
        self._capacite_tonnes = capacite_tonnes  # Attribut spécifique à Camion

    def afficher_info(self):
        print(f"Camion : {self._marque} {self._modele} ({self._annee}), Capacité : {self._capacite_tonnes} tonnes")
class ParcAuto:
    def _init_(self):
        self.vehicules = []

    def ajouter_vehicule(self, v):
        self.vehicules.append(v)

    def lister_disponibles(self):
        return [v for v in self.vehicules if v.disponible]

    def rechercher(self, modele: str):
        return [v for v in self.vehicules if v.modele.lower() == modele.lower()]
class Date:
    def _init_(self, jour: int, mois: int, annee: int):
        self.jour = jour
        self.mois = mois
        self.annee = annee

class Client():
    def __init__(self, nom, id):
        self.nom = nom
        self.id = id
    
    def info(self):
        return f"Client id: {self.id}, nom: {self.nom}" 
