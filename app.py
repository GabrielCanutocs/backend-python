from modelos.academia import Academia
from modelos.maquinario.maquina_cardio import MaquinaCardio
from modelos.maquinario.maquina_musculacao import MaquinaMusculacao

academia_movimento = Academia("Movimento", 130)
supino_reto = MaquinaMusculacao("supino_reto", "titako", "peito", "100kg")
esteira = MaquinaCardio("esteira", "xlr8", "20km/h")

def main():
    print(supino_reto)
    print(esteira)

if __name__ == "__main__":
    main()