#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct No {
    int valor;
    struct No* proximo;
} No;

typedef struct {
    int m;
    int n;
    No** nos;
} TabelaHash;

void inserir(TabelaHash* tabela, int valor);

No* criar_no(int valor) {
    No* novo_no = (No*)malloc(sizeof(No));

    novo_no->valor = valor;
    novo_no->proximo = NULL;

    return novo_no;
}

TabelaHash* criar_tabela_hash(int m) {
    TabelaHash* tabela = (TabelaHash*)malloc(sizeof(TabelaHash));

    tabela->m = m;
    tabela->n = 0;
    tabela->nos = (No**)malloc(sizeof(No*) * m);

    for (int i = 0; i < m; i++) {
        tabela->nos[i] = NULL;
    }

    return tabela;
}

int hash(int valor, int m) {
    return valor % m;
}

void rehash(TabelaHash* tabela, int valor) {
    int novo_m = tabela->m * 2;

    No** novos_nos = (No**)malloc(sizeof(No*) * novo_m);

    for (int i = 0; i < novo_m; i++) {
        novos_nos[i] = NULL;
    }

    for (int i = 0; i < tabela->m; i++) {
        No* no_atual = tabela->nos[i];

        while (no_atual != NULL) {
            No* proximo_no = no_atual->proximo;

            int novo_indice = hash(no_atual->valor, novo_m);

            no_atual->proximo = novos_nos[novo_indice];
            novos_nos[novo_indice] = no_atual;
            no_atual = proximo_no;
        }
    }

    free(tabela->nos);

    tabela->nos = novos_nos;
    tabela->m = novo_m;

    inserir(tabela, valor);
}

void inserir(TabelaHash* tabela, int valor) {
    int chave = hash(valor, tabela->m);

    if ((float)tabela->n / tabela->m >= 1.0) {
        rehash(tabela, valor);
    } else {
        int indice = hash(chave, tabela->m);

        No* novo_no = criar_no(valor);

        if (tabela->nos[indice] == NULL) {
            tabela->nos[indice] = novo_no;
        } else {
            No* no_atual = tabela->nos[indice];

            while (no_atual->proximo != NULL) {
                no_atual = no_atual->proximo;
            }

            no_atual->proximo = novo_no;
        }

        tabela->n++;
    }
}

int buscar(TabelaHash* tabela, int valor) {
    int indice = hash(valor, tabela->m);

    No* no_atual = tabela->nos[indice];

    while (no_atual != NULL) {
        if (no_atual->valor == valor) {
            return 1;
        }

        no_atual = no_atual->proximo;
    }

    return 0;
}

void imprimir_tabela_hash(TabelaHash* tabela) {
    for (int i = 0; i < tabela->m; i++) {
        printf("[%d]->", i);

        No* no_atual = tabela->nos[i];

        while (no_atual != NULL) {
            printf("[%d]->", no_atual->valor);
            no_atual = no_atual->proximo;
        }

        printf("\n");
    }
}

void destruir_tabela_hash(TabelaHash* tabela) {
    for (int i = 0; i < tabela->m; i++) {
        No* no_atual = tabela->nos[i];

        while (no_atual != NULL) {
            No* temp_no = no_atual;
            no_atual = no_atual->proximo;
            
            free(temp_no);
        }
    }

    free(tabela->nos);
    free(tabela);
}

int main(int argc, char **argv) {
    TabelaHash* tabela = criar_tabela_hash(1);

    struct timespec inicio, fim;
    unsigned int tempo, n;

    n = atoi(argv[1]);

    int aux;

    int *v = (int*)malloc(sizeof(int) * n);
    
    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        aux = rand();
        inserir(tabela, aux);
        v[i] = aux;
    }

    int valor_aleatorio = rand() % n;

    clock_gettime(CLOCK_MONOTONIC, &inicio);
    int encontrado = buscar(tabela, v[valor_aleatorio]);
    clock_gettime(CLOCK_MONOTONIC, &fim);

    destruir_tabela_hash(tabela);

    tempo = (fim.tv_sec * 1e9 + fim.tv_nsec) - (inicio.tv_sec * 1e9 + inicio.tv_nsec);

    printf("%u\n", tempo);

    return 0;
}

