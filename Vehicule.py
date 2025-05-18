from abc import ABC, abstractmethod

class Vehicule(ABC):
    def _init_(self, marque, modele, annee):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._disponible = True  # Attribut pour suivre l'état de disponibilité


    @property 
    def marque(self):
        return self._marque
    @marque.setter 
    def marque(self, marque):
       self._marque = marque
    @property  
    def modele(self):
        return self._modele
    @modele.setter
    def modele(self, modele):
       self._modele = modele
    @property  
    def annee(self):
        return self._annee
    @annee.setter
    def annee(self, marque):
       self._marque = marque
    @property
    def disponible(self):
        return self._disponible(self)
    @annee.setter
    def annee(self, marque):
       self._marque = marque        
          
    @abstractmethod
    def afficher_info(self):
        pass

    def louer(self):
        if self._disponible:
            self._disponible = False
            print("Le véhicule a été loué.")
        else:
            print("Le véhicule n'est pas disponible.")

    def rendre(self):
        self._disponible = True
        print("Le véhicule a été rendu et est maintenant disponible.")

    def est_disponible(self):
        return self._disponible
class Voiture(Vehicule):
    def _init_(self, marque, modele, annee, nb_portes):
        super()._init_(marque, modele, annee)
        self._nb_portes = nb_portes  # Attribut spécifique à Voiture

    def afficher_info(self):
        print(f"Voiture : {self._marque} {self._modele} ({self._annee}), {self._nb_portes} portes")


class Camion(Vehicule):
    def _init_(self, marque, modele, annee, capacite_tonnes):
        super()._init_(marque, modele, annee)
        self._capacite_tonnes = capacite_tonnes  # Attribut spécifique à Camion

    def afficher_info(self):
        print(f"Camion : {self._marque} {self._modele} ({self._annee}), Capacité : {self._capacite_tonnes} tonnes")