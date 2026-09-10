"""Capítulo 3 — sessão de uso mostrada no estudo de caso, p. 80–81 (PDF p. 98–99).
Executa chamadas equivalentes às da sessão do livro.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from profiler import Profiler
from algorithms import selectionSort

p = Profiler()
p.test(selectionSort)
p.test(selectionSort, size=5, trace=True)
p.test(selectionSort, size=100)
p.test(selectionSort, size=1000)
# O livro também demonstra size=10000 com comp=False e exch=False; fica comentado
# para não impor uma execução longa ao abrir este arquivo.
# p.test(selectionSort, size=10000, exch=False, comp=False)
