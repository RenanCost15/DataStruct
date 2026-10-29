"""Exercício 1.4 — Por que ArraySortedBag.add chama ArrayBag.add?

Nos casos em que o novo item pode ser anexado ao final, a lógica de redimensionamento e atualização de tamanho do pai já está correta. Delegar evita duplicação; usar explicitamente a implementação do pai também evita chamar novamente a própria versão sobrescrita."""
print(__doc__)