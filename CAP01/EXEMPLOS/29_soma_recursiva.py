"""Exemplo — soma de intervalo por definição recursiva."""
def nossa_soma(inferior,superior):
    if inferior>superior: return 0
    return inferior+nossa_soma(inferior+1,superior)
print(nossa_soma(1,4))
