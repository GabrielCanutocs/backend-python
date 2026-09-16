from abc import ABC, abstractmethod

class Equipamento(ABC):
    def __init__(self, nome, marca):
        self._nome = nome
        self._marca = marca

    @abstractmethod
    def realizar_manutencao(self):
        pass