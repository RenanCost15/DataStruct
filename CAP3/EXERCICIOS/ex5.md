# Capítulo 3 — quinto bloco de exercícios

## 1. Estratégia e ganho do quicksort

O quicksort escolhe um pivô, particiona a sublista em itens menores e itens
maiores ou iguais ao pivô e repete o processo nas duas partes. Quando as
partições ficam aproximadamente equilibradas, há \(O(\log n)\) níveis; cada
nível examina, ao todo, \(O(n)\) itens. O resultado é \(O(n\log n)\), em vez
dos \(O(n^2)\) dos algoritmos básicos.

## 2. Pior caso

O quicksort não é sempre \(O(n\log n)\) porque o pivô pode gerar repetidamente
uma parte vazia e outra com \(n-1\) itens. Nesse caso, o trabalho é
\((n-1)+(n-2)+\cdots+1 = O(n^2)\).

Para a implementação do livro, que escolhe a **posição central** e usa o
particionamento nela mostrado, a lista
`[3, 9, 4, 7, 1, 10, 6, 8, 5, 2]` produz sublistas sucessivas de tamanhos
10, 9, 8, ..., 2 e, portanto, o pior comportamento quadrático. A lista exata
de pior caso depende da regra de particionamento.

## 3. Duas outras escolhas de pivô

1. Escolher uma posição aleatória da sublista.
2. Usar a mediana entre o primeiro, o central e o último item (“mediana de
   três”).

## 4. Inserção para sublistas pequenas

Chamadas recursivas e particionamentos têm custos fixos relevantes em sublistas
pequenas. A ordenação por inserção é simples, tem constantes baixas e trabalha
bem quando a sublista já está parcialmente ordenada. O método híbrido reduz a
sobrecarga sem alterar a complexidade média \(O(n\log n)\).

## 5. Pior caso do merge sort

Em cada nível, a intercalação visita ao todo \(O(n)\) itens. As divisões ao meio
produzem \(O(\log n)\) níveis, independentemente da ordem inicial dos dados.
Logo, até no pior caso, o tempo é \(O(n\log n)\).
