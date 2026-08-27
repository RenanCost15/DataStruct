# Capítulo 1 — "Reading and Writing Objects with pickle", p. 29–30.

import pickle

lyst = [60, "A string object", 1977]
fileObj = open("items.dat", "wb")
for item in lyst:
    pickle.dump(item, fileObj)
fileObj.close()

lyst = list()
fileObj = open("items.dat", "rb")
while True:
    try:
        item = pickle.load(fileObj)
        lyst.append(item)
    except EOFError:
        # Fim da entrada detectado aqui.
        fileObj.close()
        break
print(lyst)
