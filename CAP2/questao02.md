# Capítulo 2 — Projeto 2

## Enunciado

Para comparar com Python, examine os tipos de coleção de Java no pacote
`java.util`, indicado pelo livro.

## Resposta

O Java Collections Framework separa **interfaces** de **implementações**. A
interface raiz `Collection<E>` representa grupos de elementos e se divide,
principalmente, em `List<E>`, `Set<E>` e `Queue<E>`. `Map<K,V>` faz parte do
framework, mas não herda de `Collection<E>`, pois armazena associações entre
chaves e valores.

| Necessidade | Python | Java (`java.util`) | Observação |
|---|---|---|---|
| Sequência textual imutável | `str` | `String` (em `java.lang`) | Ambos oferecem acesso posicional; não são coleções mutáveis. |
| Sequência mutável e ordenada | `list` | `List<E>`; por exemplo, `ArrayList<E>` ou `LinkedList<E>` | Permitem duplicatas e preservam posição. |
| Sequência imutável | `tuple` | Sem equivalente direto no Java 8 | Pode-se usar uma classe própria ou uma lista não modificável. |
| Conjunto sem duplicatas | `set` | `Set<E>`; por exemplo, `HashSet<E>`, `LinkedHashSet<E>` ou `TreeSet<E>` | `TreeSet` mantém ordenação; `HashSet` não garante ordem. |
| Mapeamento chave–valor | `dict` | `Map<K,V>`; por exemplo, `HashMap<K,V>`, `LinkedHashMap<K,V>` ou `TreeMap<K,V>` | As chaves são únicas. |
| Fila | Uso de `collections.deque` | `Queue<E>` | A operação típica é FIFO. |
| Fila de duas pontas/pilha | `collections.deque` | `Deque<E>`; por exemplo, `ArrayDeque<E>` | Admite inserção e remoção nas duas extremidades. |

Diferenças importantes:

1. Python usa tipagem dinâmica; Java usa tipos genéricos, como `List<String>`.
2. Em Java, escolhe-se uma implementação conforme o custo desejado das
   operações (`ArrayList`, `LinkedList`, `HashSet`, `TreeSet` etc.).
3. A classe utilitária `Collections` fornece algoritmos e adaptadores estáticos,
   como ordenação, busca e visualizações não modificáveis.
4. Tanto em Python quanto em Java, as coleções normalmente mantêm referências
   para objetos; copiar a coleção não implica copiar profundamente seus itens.

Fontes oficiais indicadas pelo enunciado:

- <https://docs.oracle.com/javase/8/docs/api/java/util/package-summary.html>
- <https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html>
- <https://docs.oracle.com/javase/tutorial/collections/interfaces/summary.html>
