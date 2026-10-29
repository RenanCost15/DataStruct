# Projeto 4 — Diagrama de classes para `ArraySet` e `LinkedSet`

**Enunciado em PT-BR:** um conjunto comporta-se como uma bag, exceto por não permitir itens duplicados. Considerando `ArraySet` e `LinkedSet`, desenhe um diagrama que mostre onde essas classes entram no framework apresentado na Figura 6-4.

## Resolução

```text
AbstractCollection
        |
   AbstractBag
    /       \
ArrayBag  LinkedBag
   |          |
ArraySet   LinkedSet
```

A colocação preserva o reuso das implementações baseadas em array e em nós; as subclasses de conjunto especializam a operação `add` para impedir duplicatas. O Projeto 5 pede a implementação correspondente.
