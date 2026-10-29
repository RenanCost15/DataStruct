# Projeto 6 — Diagrama de classes para um conjunto ordenado

**Enunciado em PT-BR:** um conjunto ordenado comporta-se como um conjunto, mas permite percorrer itens em ordem crescente e oferece busca logarítmica. Desenhe onde uma nova classe de conjunto ordenado deve ser colocada no framework da Figura 6-4.

## Resolução

```text
AbstractCollection
        |
   AbstractBag
        |
     ArrayBag
        |
 ArraySortedBag
        |
 ArraySortedSet
```

`ArraySortedSet` deve ficar abaixo de `ArraySortedBag`: assim herda a ordem
crescente e a busca binária `O(log n)` e precisa especializar apenas a inclusão
para rejeitar duplicatas. Essa é também a posição mostrada no framework
profissional da Figura 6-5. O Projeto 7 implementa essa classe.
