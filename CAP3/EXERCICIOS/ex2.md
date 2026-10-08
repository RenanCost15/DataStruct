# Capítulo 3 — segundo bloco de exercícios

## 1. Termo dominante e classificação

| Expressão | Termo dominante | Classificação |
|---|---:|---:|
| \(2^n - 4n^2 + 5n\) | \(2^n\) | \(O(2^n)\), exponencial |
| \(3n^2 + 6\) | \(3n^2\) | \(O(n^2)\), quadrática |
| \(n^3 + n^2 - n\) | \(n^3\) | \(O(n^3)\), cúbica |

Constantes multiplicativas e termos de menor ordem não alteram a classe
assintótica.

## 2. Comparação entre A e B

- A executa \(n^2\) instruções.
- B executa \(\frac{1}{2}n^2 + \frac{1}{2}n\) instruções.
- A diferença é \(\frac{1}{2}n(n-1)\). Portanto, para todo \(n>1\), A
  realiza mais trabalho; para \(n=1\), os dois realizam exatamente uma
  instrução.
- Para valores grandes de \(n\), B usa aproximadamente metade das instruções
  de A. Para valores muito pequenos, sobretudo \(n=1\) e \(n=2\), os totais
  são iguais ou próximos.
- Ambos continuam pertencendo a \(O(n^2)\).

## 3. Comparação entre \(n^4\) e \(2^n\)

Em \(n=16\), os valores são iguais:
\(16^4 = 65.536 = 2^{16}\). Em \(n=17\), \(17^4 = 83.521\), enquanto
\(2^{17} = 131.072\). Assim, a partir de **n = 17**, \(n^4\) passa a exigir
menos trabalho; daí em diante, \(2^n\) cresce cada vez mais rapidamente.
