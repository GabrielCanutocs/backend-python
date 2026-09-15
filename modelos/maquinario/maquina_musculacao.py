from modelos.maquinario.equipamento import Equipamento

class MaquinaMusculacao(Equipamento):
    def __init__(self, nome, marca, grupamento, carga_maxima):
        super().__init__(nome, marca)
        self._grupamento = grupamento
        self._carga_maxima = carga_maxima

    def __str__(self):
        return self._nome