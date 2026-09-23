"""Projeto 01 — Complexidade de == nas duas implementações de bag.

Casos rápidos: identidade, tipos/tamanhos incompatíveis -> O(1). Para duas bags
não ordenadas do mesmo tamanho, uma implementação que para cada item de uma faz
`item in outra` pode executar n buscas lineares -> O(n²) no pior e em geral na
análise assintótica. A estrutura interna (array ou links) não muda essa ordem.
"""
print("melhores testes O(1); comparação geral de bags não ordenadas O(n²)")
