#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <linux/time.h>

struct noArv {
    int valor;
    struct noArv* galhoEsq;
    struct noArv* galhoDir;
    unsigned int altura;
};

int obterAlt(struct noArv* no) {
    if (no != NULL) {
        return no->altura;
    }

    return 0;
}

int obterDif(struct noArv* no) {
    if (no != NULL) {
        return obterAlt(no->galhoEsq) - obterAlt(no->galhoDir);
    }

    return 0;
}

void attAltura(struct noArv* no) {
    if (no == NULL) {
        return;
    }

    int altEsq = obterAlt(no->galhoEsq);
    int altDir = obterAlt(no->galhoDir);

    no->altura = (altEsq > altDir ? altEsq : altDir) + 1;
}

struct noArv* rotEsq(struct noArv* no) {
    struct noArv* nvRaiz = no->galhoDir;

    no->galhoDir = nvRaiz->galhoEsq;

    nvRaiz->galhoEsq = no;

    attAltura(no);
    attAltura(nvRaiz);

    return nvRaiz;
}

struct noArv* rotDir(struct noArv* no) {
    struct noArv* nvRaiz = no->galhoEsq;

    no->galhoEsq = nvRaiz->galhoDir;

    nvRaiz->galhoDir = no;

    attAltura(no);
    attAltura(nvRaiz);
    
    return nvRaiz;
}

struct noArv* inserir(struct noArv* raiz, int valor) {
    if (raiz == NULL) {
        raiz = malloc(sizeof(struct noArv));
        raiz->valor = valor;
        raiz->galhoEsq = NULL;
        raiz->galhoDir = NULL;
        raiz->altura = 1;
    } else if (valor < raiz->valor) {
        raiz->galhoEsq = inserir(raiz->galhoEsq, valor);
    } else if (valor > raiz->valor) {
        raiz->galhoDir = inserir(raiz->galhoDir, valor);
    } else {
        return raiz;
    }

    attAltura(raiz);

    int dif = obterDif(raiz);

    if (dif > 1 && valor < raiz->galhoEsq->valor) {
        return rotDir(raiz);
    }
    if (dif < -1 && valor > raiz->galhoDir->valor) {
        return rotEsq(raiz);
    }
    if (dif > 1 && valor > raiz->galhoEsq->valor) {
        raiz->galhoEsq = rotEsq(raiz->galhoEsq);
        return rotDir(raiz);
    }
    if (dif < -1 && valor < raiz->galhoDir->valor) {
        raiz->galhoDir = rotDir(raiz->galhoDir);
        return rotEsq(raiz);
    }

    return raiz;
}

struct noArv *buscar(struct noArv *raiz, int valor) {
    if (raiz != NULL) {
        if (raiz->valor == valor) {
            return raiz;
        }

        if (raiz->valor < valor) {
            return buscar(raiz->galhoDir, valor);
        }

        return buscar(raiz->galhoEsq, valor);
    }

    return NULL;
}

int main(int argc, char **argv) {
    struct noArv* raiz = NULL;

    struct timespec ini, f;
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

    clock_gettime(CLOCK_MONOTONIC, &ini);
    struct noArv *no = buscar(raiz, valor_busca);
    clock_gettime(CLOCK_MONOTONIC, &f);

    tempo = (f.tv_sec * 1e9 + f.tv_nsec) - (ini.tv_sec * 1e9 + ini.tv_nsec);

    printf("%u\n", tempo);

    return 0;
}

