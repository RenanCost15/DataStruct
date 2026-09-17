"""Capítulo 4 — sessão com Array, p. 92 (PDF p. 110)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module
Array = import_module('01_arrays').Array

a = Array(5)
print(len(a))
print(a)
for i in range(len(a)):
    a[i] = i + 1
print(a[0])
for item in a:
    print(item)
