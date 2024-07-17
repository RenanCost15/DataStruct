#!/bin/sh
chmod +x iterate.sh

help="
SYNTAX:
$0 <executions> <size-start> <size-pass> <size-end> <program> <name>

  <executions> - number of program execution iterations
  <size-start> - initial value of 'n' (size of the problem instance)
  <size-pass>  - increment value of 'n' (size of the problem instance)
  <size-end>   - final value of 'n' (size of the problem instance)
  <program>    - program string (name plus additional arguments)
  <name>       - base string used to create filenames
"

# Verifica se o número de argumentos é igual a 6
if [ $# -eq 6 ]; then

    # Cria uma pasta com o nome baseado no sexto argumento, se não existir
    mkdir -p $6

    # Nome do arquivo de resultado baseado no sexto argumento, dentro da pasta criada
    result=graphics/$6/$6.txt
    # Limpa o conteúdo do arquivo de resultado
    echo -n > $result

    # Loop através dos tamanhos de problema, de size-start até size-end com incrementos de size-pass
    for n in `seq $2 $3 $4`;
    do
        # Nome do arquivo específico para o tamanho atual, dentro da pasta criada
        file=graphics/$6/$6-$1-$n.txt
        # Limpa o conteúdo do arquivo específico
        echo -n > $file

        # Loop para executar o programa o número especificado de vezes
        for i in `seq $1`;
        do
            # Executa o programa com o tamanho atual e redireciona a saída para o arquivo específico
            $5 $n >> $file
        done

        # Calcula o valor máximo do tempo de execução
        max=$(awk 'BEGIN{s=0} {if ($1>s) s=$1} END{printf "%.2f", s}' $file)
        # Calcula o valor mínimo do tempo de execução
        min=$(awk 'BEGIN{s='$max'} {if ($1<s) s=$1} END{printf "%.2f", s}' $file)
        # Calcula a média dos tempos de execução
        mean=$(awk '{s+=$1} END{printf "%.2f", s/NR}' $file)
        # Calcula o erro quadrático médio
        maer=$(awk -v mean=$mean '{s+=($1-mean)^2} END{printf "%.2f", sqrt(s/NR)}' $file)

        # Escreve os resultados para o tamanho atual no arquivo de resultados
        echo "$n $mean $maer $max $min $1 $file" >> $result
    done
else
    # Exibe a ajuda se o número de argumentos não for igual a 6
    echo "$help"
fi
