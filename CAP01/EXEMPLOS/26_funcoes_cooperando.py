"""Exemplo — uma função chama outra definida no módulo."""
def primeira():
    print('Chamando primeira'); segunda()
def segunda(): print('Chamando segunda')
primeira()
