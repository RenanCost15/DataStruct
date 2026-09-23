"""Exercício 2.5 — Por que ArrayBag não precisa obrigatoriamente de __contains__?

Quando __contains__ não existe, Python pode testar pertinência percorrendo o objeto por seu protocolo de iteração. Como a busca da bag é sequencial de qualquer forma, um método especializado não é necessário nesta implementação básica."""
print(__doc__)