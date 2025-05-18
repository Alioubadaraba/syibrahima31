from datetime import date
from Location import Voiture, Camion, ParcAuto, Date, Client, Location  

class ClientStandard(Client):
    def __init__(self, nom, id):
        super().__init__(nom, id)


voiture1 = Voiture("Toyota", "Corolla", 2020, 4)
voiture2 = Voiture("Peugeot", "208", 2022, 5)
camion1 = Camion("Mercedes", "Actros", 2019, 10)

client1 = ClientStandard("Alice Dupont", 1)
client2 = ClientStandard("Bob Martin", 2)

date_debut1 = date(2025, 5, 10)
date_fin1 = date(2025, 5, 15)

date_debut2 = date(2025, 5, 18)
date_fin2 = date(2025, 5, 20)

parc = ParcAuto()
parc.ajouter_vehicule(voiture1)
parc.ajouter_vehicule(voiture2)
parc.ajouter_vehicule(camion1)

modele_recherche = "Corolla"
print(f"\n🔍 Recherche des véhicules modèle '{modele_recherche}':")
resultats = parc.rechercher(modele_recherche)
for v in resultats:
    v.afficher_info()


if voiture1.est_disponible():
    voiture1.louer()
    location1 = Location(date_debut1, date_fin1, voiture1.modele, client1.nom)
    print("\n📄 Détails de la Location 1 :")
    location1.afficher()
    prix1 = Location.calcul_prix(location1.duree())
    print(f"💰 Prix total de la location : {prix1} €")
else:
    print("🚫 La voiture n'est pas disponible.")

if camion1.est_disponible():
    camion1.louer()
    location2 = Location(date_debut2, date_fin2, camion1.modele, client2.nom)
    print("\n📄 Détails de la Location 2 :")
    location2.afficher()
    prix2 = Location.calcul_prix(location2.duree())
    print(f"💰 Prix total de la location : {prix2} €")
else:
    print("🚫 Le camion n'est pas disponible.")

voiture1.rendre()
camion1.rendre()
