from datetime import date

class Date:
    def _init_(self, jour: int, mois: int, annee: int):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def to_string(self) -> str:
        return f"{self.jour:02d}/{self.mois:02d}/{self.annee}"

    def difference(self, autre) -> int:
        date1 = date(self.annee, self.mois, self.jour)
        date2 = date(autre.annee, autre.mois, autre.jour)
        return abs((date1 - date2).days)


