# Capítulo 1 — "Loop Statements", p. 12.

product = 1
value = 1
while value <= 10:
    product *= value
    value += 1
print(product)

product = 1
for value in range(1, 11):
    product *= value
print(product)
