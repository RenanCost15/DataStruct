"""Exemplo — captura de ValueError e nova tentativa de entrada."""
def ler_inteiro(mensagem):
    texto=input(mensagem)
    try: return int(texto)
    except ValueError:
        print('Erro no formato:',texto); return ler_inteiro(mensagem)
if __name__=='__main__': print(ler_inteiro('Digite um inteiro: '))
