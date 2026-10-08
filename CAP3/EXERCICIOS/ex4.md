# Capítulo 3 — quarto bloco de exercícios

## 1. Trocas na ordenação por seleção

A lista já ordenada em ordem crescente produz o menor número de trocas: zero,
pois o menor item de cada sublista já ocupa a posição correta. O máximo é
\(n-1\) trocas e ocorre quando, em cada passagem, o menor item restante está
fora da posição corrente. Um exemplo com cinco itens é `2, 3, 4, 5, 1`.

## 2. Papel das trocas e do tamanho dos objetos

A ordenação por seleção faz \(O(n^2)\) comparações, mas no máximo \(n-1\)
trocas. A ordenação por bolha também faz \(O(n^2)\) comparações e pode fazer
\(O(n^2)\) trocas. Assim, quando trocar dados custa caro, a seleção pode ter
vantagem prática. No modelo usual, cada troca custa tempo constante. Em Python,
trocam-se referências, de modo que o tamanho interno do objeto normalmente não
altera a ordem de complexidade; em um modelo que copie objetos inteiros, objetos
maiores aumentariam o custo de cada troca.

## 3. Caso médio da bolha modificada

O encerramento antecipado só evita passagens quando a lista já fica ordenada.
Uma permutação aleatória contém, em média, \(n(n-1)/4\) inversões, e cada troca
adjacente elimina apenas uma inversão. Portanto, ainda há uma quantidade
quadrática de trabalho em média: \(O(n^2)\).

## 4. Inserção em listas parcialmente ordenadas

O custo da ordenação por inserção acompanha a quantidade de deslocamentos, que
é proporcional ao número de inversões. Em uma lista parcialmente ordenada há
poucas inversões; a busca para inserir cada item percorre apenas uma pequena
distância para trás. Nesse cenário, o desempenho se aproxima de \(O(n)\).
