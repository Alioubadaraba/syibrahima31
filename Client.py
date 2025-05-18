from abc import ABC, abstractmethod

class Client(ABC):
    def __init__(self, nom, id):
        self.nom = nom
        self.id = id
    
    def info(self):
        return f"Client id: {self.id}, nom: {self.nom}" 