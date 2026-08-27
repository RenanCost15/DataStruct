# Capítulo 1 — Escrita e leitura de números em arquivos, p. 26–29.

import random

f = open("integers.txt", "w")
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")
f.close()

f = open("integers.txt", "r")
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number
print("A soma é", theSum)

f = open("integers.txt", "r")
theSum = 0
for line in f:
    wordlist = line.split()
    for word in wordlist:
        number = int(word)
        theSum += number
print("A soma é", theSum)

f = open("integers.txt", "r")
print("A soma é", sum(map(int, f.read().split())))
