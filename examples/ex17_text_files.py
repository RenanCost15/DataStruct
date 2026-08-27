# Capítulo 1 — Saída e entrada de arquivos de texto, p. 26–28.

f = open("myfile.txt", "w")
f.write("First line.\nSecond line.\n")
f.close()

f = open("myfile.txt", "r")
text = f.read()
print(text)

f = open("myfile.txt", "r")
for line in f:
    print(line)

f = open("myfile.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    print(line)
