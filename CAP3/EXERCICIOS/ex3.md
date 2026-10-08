# Capítulo 3 — terceiro bloco de exercícios

## 1. Rastreamento da busca binária

Lista: `20, 44, 48, 55, 62, 66, 74, 88, 93, 99`, com índices de 0 a 9.

### Alvo 90

| Passo | `left` | `right` | `midpoint` | Valor central | Decisão |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 9 | 4 | 62 | 90 > 62; `left = 5` |
| 2 | 5 | 9 | 7 | 88 | 90 > 88; `left = 8` |
| 3 | 8 | 9 | 8 | 93 | 90 < 93; `right = 7` |

Como `left` passa a 8 e `right` a 7, a busca termina sem encontrar 90.

### Alvo 44

| Passo | `left` | `right` | `midpoint` | Valor central | Decisão |
|---:|---:|---:|---:|---:|---|
| 1 | 0 | 9 | 4 | 62 | 44 < 62; `right = 3` |
| 2 | 0 | 3 | 1 | 44 | Alvo encontrado no índice 1 |

## 2. Estratégia semelhante à consulta de uma lista telefônica

Em vez de usar sempre `(left + right) // 2`, pode-se estimar uma posição pela
proporção alfabética do alvo no intervalo atual. Por exemplo, convertendo a
primeira letra em um valor de 0 (`A`) a 25 (`Z`), estima-se uma fração entre a
primeira e a última chave da sublista e consulta-se essa posição. Após a
comparação, os limites são atualizados como na busca binária. Essa técnica é
uma forma de **busca por interpolação**.

Ela pode ser mais rápida em média quando os nomes se distribuem de modo quase
uniforme, mas não possui melhor limite geral: distribuições irregulares podem
gerar estimativas ruins e levar a \(O(n)\) no pior caso. A busca binária mantém
o pior caso \(O(\log n)\). Portanto, sem uma hipótese forte sobre a distribuição,
sua complexidade não é melhor que a da busca binária padrão.
