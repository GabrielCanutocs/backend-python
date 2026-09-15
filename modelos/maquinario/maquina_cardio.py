from modelos.maquinario.equipamento import Equipamento

class MaquinaCardio(Equipamento):
    
    def __init__(self, nome, marca, velocidade_maxima):
        super().__init__(nome, marca)
        self._velocidade_maxima = velocidade_maxima

    def __str__(self):
        return self._nome