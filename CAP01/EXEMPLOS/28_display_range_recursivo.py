"""Exemplo — mesma tarefa implementada recursivamente."""
def exibir_intervalo(inferior,superior):
    if inferior<=superior:
        print(inferior); exibir_intervalo(inferior+1,superior)
exibir_intervalo(1,4)
