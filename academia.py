
class Academia: 
    academias = []

    def __init__(self, nome, preco):
        self._nome =  nome.title()
        self._preco = preco
        self._ativo = False
        Academia.academias.append(self)

    def __str__(self):
        return f"{self._nome} | {self._preco}"

    @classmethod
    def lista_academias(cls):
        print(f"{'Nome da academia'.ljust(25)} | {'Preco'.ljust(25)} | {'Status'.ljust(25)}")
        for academia in cls.academias:
            print(f"{academia._nome.ljust(25)} | {str(academia._preco).ljust(25)} | {academia._ativo}")

    @property
    def ativo(self):
        return "⌧" if self._ativo else "☐"


academia_movimento = Academia("Movimento", 130)
academia_contorno = Academia("Contorno", 150)

Academia.lista_academias()

