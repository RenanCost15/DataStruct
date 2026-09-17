"""Exercício 4.2 — Acessar campos quando o ponteiro vale None.

Tentar `probe.data` quando probe é None gera AttributeError. Deve-se testar `probe is not None` antes de acessar seus campos, normalmente na condição do while/if."""
probe=None
print("seguro?",probe is not None)