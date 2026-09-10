"""Capítulo 3 — Estudo de caso: Um Profiler de Algoritmos, p. 83–84 (PDF p. 101–102).
Define uma classe para perfilar algoritmos de ordenação.
"""
import time
import random

class Profiler(object):
    def test(self, function, lyst=None, size=10,
             unique=True, comp=True, exch=True, trace=False):
        """Executa a função com as opções pedidas pelo estudo de caso e imprime o perfil."""
        self.comp = comp
        self.exch = exch
        self.trace = trace
        if lyst is not None:
            self.lyst = lyst
        elif unique:
            self.lyst = list(range(1, size + 1))
            random.shuffle(self.lyst)
        else:
            self.lyst = []
            for count in range(size):
                self.lyst.append(random.randint(1, size))
        self.exchCount = 0
        self.cmpCount = 0
        self.startClock()
        function(self.lyst, self)
        self.stopClock()
        print(self)

    def exchange(self):
        """Conta trocas quando essa opção está habilitada."""
        if self.exch:
            self.exchCount += 1
        if self.trace:
            print(self.lyst)

    def comparison(self):
        """Conta comparações quando essa opção está habilitada."""
        if self.comp:
            self.cmpCount += 1

    def startClock(self):
        """Registra o instante inicial."""
        self.start = time.time()

    def stopClock(self):
        """Para o relógio e calcula segundos decorridos, arredondados a milissegundos."""
        self.elapsedTime = round(time.time() - self.start, 3)

    def __str__(self):
        """Retorna os resultados como string."""
        result = "Tamanho do problema: " + str(len(self.lyst)) + "\n"
        result += "Tempo decorrido: " + str(self.elapsedTime) + "\n"
        if self.comp:
            result += "Comparações: " + str(self.cmpCount) + "\n"
        if self.exch:
            result += "Trocas: " + str(self.exchCount) + "\n"
        return result
