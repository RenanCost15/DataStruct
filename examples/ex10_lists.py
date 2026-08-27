# Capítulo 1 — "Lists", p. 16–17.

print([])
print(["greater"])
print(["greater", "less"])
print(["greater", "less", 10])
print(["greater", ["less", 10]])

testList = []
testList.append(34)
testList.append(22)
testList.sort()
print(testList.pop())
testList.insert(0, 22)
testList.insert(1, 55)
print(testList.pop(1))
testList.remove(22)

print("Python is cool".split())
print(" ".join(["Python", "is", "cool"]))

# O livro usa esta chamada para demonstrar ValueError.
# testList.remove(55)
