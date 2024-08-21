#include <stdlib.h>
#include <stdio.h>
#include <time.h>

struct no_arvore {
    int valor;
    struct no_arvore* filho_esquerdo;
    struct no_arvore* filho_direito;
    unsigned int altura;
};

int obter_altura(struct no_arvore* no) {
    if (no == NULL) {
        return 0;
    }

    return no->altura;
}

int obter_diferenca(struct no_arvore* no) {
    if (no == NULL) {
        return 0;
    }

    return obter_altura(no->filho_esquerdo) - obter_altura(no->filho_direito);
}

void atualizar_altura(struct no_arvore* no) {
    if (no == NULL) {
        return;
    }

    int altura_esquerda = obter_altura(no->filho_esquerdo);
    int altura_direita = obter_altura(no->filho_direito);

    no->altura = (altura_esquerda > altura_direita ? altura_esquerda : altura_direita) + 1;
}

struct no_arvore* rotacionar_esquerda(struct no_arvore* no) {
    struct no_arvore* nova_raiz = no->filho_direito;

    no->filho_direito = nova_raiz->filho_esquerdo;

    nova_raiz->filho_esquerdo = no;

    atualizar_altura(no);
    atualizar_altura(nova_raiz);

    return nova_raiz;
}

struct no_arvore* rotacionar_direita(struct no_arvore* no) {
    struct no_arvore* nova_raiz = no->filho_esquerdo;

    no->filho_esquerdo = nova_raiz->filho_direito;

    nova_raiz->filho_direito = no;

    atualizar_altura(no);
    atualizar_altura(nova_raiz);
    
    return nova_raiz;
}

struct no_arvore* inserir(struct no_arvore* raiz, int valor) {
    if (raiz == NULL) {
        raiz = malloc(sizeof(struct no_arvore));
        raiz->valor = valor;
        raiz->filho_esquerdo = NULL;
        raiz->filho_direito = NULL;
        raiz->altura = 1;
    } else if (valor < raiz->valor) {
        raiz->filho_esquerdo = inserir(raiz->filho_esquerdo, valor);
    } else if (valor > raiz->valor) {
        raiz->filho_direito = inserir(raiz->filho_direito, valor);
    } else {
        return raiz;
    }

    atualizar_altura(raiz);

    int diferenca = obter_diferenca(raiz);

    if (diferenca > 1 && valor < raiz->filho_esquerdo->valor) {
        return rotacionar_direita(raiz);
    }
    if (diferenca < -1 && valor > raiz->filho_direito->valor) {
        return rotacionar_esquerda(raiz);
    }
    if (diferenca > 1 && valor > raiz->filho_esquerdo->valor) {
        raiz->filho_esquerdo = rotacionar_esquerda(raiz->filho_esquerdo);
        return rotacionar_direita(raiz);
    }
    if (diferenca < -1 && valor < raiz->filho_direito->valor) {
        raiz->filho_direito = rotacionar_direita(raiz->filho_direito);
        return rotacionar_esquerda(raiz);
    }

    return raiz;
}

struct no_arvore *buscar(struct no_arvore *raiz, int valor) {
    if (raiz != NULL) {
        if (raiz->valor == valor) {
            return raiz;
        }

        if (raiz->valor < valor) {
            return buscar(raiz->filho_direito, valor);
        }

        return buscar(raiz->filho_esquerdo, valor);
    }

    return NULL;
}

int main(int argc, char **argv) {
    struct no_arvore* raiz = NULL;

    struct timespec inicio, fim;
    unsigned int tempo, n;

    int i, aux, *arr;

    n = atoi(argv[1]);

    arr = malloc(n * sizeof(int));
    
    srand(time(NULL));

    for (i = 0; i < n; i++) {
        aux = rand();
        raiz = inserir(raiz, aux);
        arr[i] = aux;
    }

    int valor_busca = raiz->valor;

    clock_gettime(CLOCK_MONOTONIC, &inicio);
    struct no_arvore *no = buscar(raiz, valor_busca);
    clock_gettime(CLOCK_MONOTONIC, &fim);

    tempo = (fim.tv_sec * 1e9 + fim.tv_nsec) - (inicio.tv_sec * 1e9 + inicio.tv_nsec);

    printf("%u\n", tempo);

    return 0;
}

