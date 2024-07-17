# Define o terminal de saída como pngcairo com tamanho 800x600 pixels
set terminal pngcairo size 800,600

# Define o nome do arquivo de saída para salvar o gráfico
set output 'graphics/selection/selection.png'

# Ativa a grade de fundo no gráfico
set grid   

# Define o título do gráfico
set title 'algorithm selection-sort execution time'

# Define o rótulo do eixo y (vertical) como "time in nanoseconds"
set ylabel "time in nanoseconds"

# Define o rótulo do eixo x (horizontal) como "problem instance size (n)"
set xlabel "problem instance size (n)"

# Comando de plotagem:
#   - 'graphics/selection/selection.txt': Especifica o arquivo de dados a ser plotado
#   - using 1:2: Usa a primeira coluna como dados para o eixo x e a segunda coluna como dados para o eixo y
#   - with lines: Plota os pontos com linhas conectando-os
#   - title 'title': Define o título da legenda para a série de dados como 'title'
plot 'graphics/selection/selection.txt' using 1:2 with lines title 'title'

