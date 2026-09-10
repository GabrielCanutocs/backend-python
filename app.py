from modelos.academia import Academia

academia_movimento = Academia("Movimento", 130)
academia_corpos = Academia("Corpos", 140)
academia_contorno = Academia("Contorno", 150)

academia_movimento.ativa_academia()

academia_movimento.receber_avaliacao("Gabriel", 9)
academia_movimento.receber_avaliacao("Luiz", 10)
academia_movimento.receber_avaliacao("Davi", 6)

def main():
    Academia.lista_academias()


if __name__ == "__main__":
    main()