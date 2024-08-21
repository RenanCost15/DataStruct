#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct no_arvore {
    int valor;
    struct no_arvore *filho_esquerdo;
    struct no_arvore *filho_direito;
};

void inserir(struct no_arvore **raiz, int valor) {
    if (*raiz == NULL) {
        *raiz = malloc(sizeof(struct no_arvore));
        (*raiz)->valor = valor;
        (*raiz)->filho_esquerdo = NULL;
        (*raiz)->filho_direito = NULL;
    } else {
        if ((*raiz)->valor < valor) {
            inserir(&(*raiz)->filho_direito, valor);
        } else {
            inserir(&(*raiz)->filho_esquerdo, valor);
        }
    }
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
    struct no_arvore *raiz = NULL;

    struct timespec inicio, fim;
    unsigned int tempo, n;
    
    int i, aux;

    n = atoi(argv[1]);

    int *arr = malloc(n * sizeof(int));

    srand(time(NULL));
    
    for (i = 0; i < n; i++) {
        aux = rand();
        inserir(&raiz, aux);
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

