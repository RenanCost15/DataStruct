"""Capítulo 1 — Projeto 8: navegação pelas linhas de um arquivo."""


def carregar_linhas(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.readlines()


def linha_por_numero(linhas, numero):
    """Retorna a linha numerada a partir de 1."""
    if not 1 <= numero <= len(linhas):
        raise IndexError("Número de linha fora do intervalo")
    return linhas[numero - 1].rstrip("\n")


def main():
    nome_arquivo = input("Nome do arquivo: ")
    linhas = carregar_linhas(nome_arquivo)
    while True:
        print("Número de linhas no arquivo:", len(linhas))
        numero = int(input("Digite um número de linha (0 para sair): "))
        if numero == 0:
            break
        if 1 <= numero <= len(linhas):
            print(linha_por_numero(linhas, numero))
        else:
            print("Número de linha inválido.")


if __name__ == "__main__":
    main()
