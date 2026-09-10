from modelos.avaliacao import Avaliacao


class Academia: 
    academias = []

    def __init__(self, nome, preco):
        self._nome =  nome.title()
        self._preco = preco
        self._ativo = False
        self._avaliacao = []
        Academia.academias.append(self)

    def __str__(self):
        return f"{self._nome} | {self._preco}"

    def ativa_academia(self):
            self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        self._avaliacao.append(Avaliacao(cliente, nota))


    @classmethod
    def lista_academias(cls):
        print(f"{'Nome da academia'.ljust(25)} | {'Preco'.ljust(25)} |  {'Avaliacao'.ljust(25)} |  {'Status'.ljust(25)}")
        for academia in cls.academias:
            print(f"{academia._nome.ljust(25)} | {str(academia._preco).ljust(25)} | {str(academia.media_avaliacoes).ljust(25)} | {academia.ativo}")

    @property
    def ativo(self):
        return "⌧" if self._ativo else "☐"

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        
        return round(sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao), 1)
