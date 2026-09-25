class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1

        while self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            i = i // 2

    def remove_smallest(self):
        if len(self.arreglo) == 1:
            return None

        menor = self.arreglo[1]
        self.arreglo[1] = self.arreglo[-1]
        self.arreglo.pop()

        if len(self.arreglo) > 1:
            self._sift_down(1)

        return menor

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + lista[:]
        i = (len(self.arreglo) - 1) // 2

        while i > 0:
            self._sift_down(i)
            i -= 1

    # auxiliares

    def _sift_down(self, i):
        while (i * 2) < len(self.arreglo):
            hijo_min = self._min_child(i)
            if self.arreglo[i] > self.arreglo[hijo_min]:
                self.arreglo[i], self.arreglo[hijo_min] = self.arreglo[hijo_min], self.arreglo[i]
            else:
                break
            i = hijo_min

    def _min_child(self, i):
        if i * 2 + 1 >= len(self.arreglo):
            return i * 2
        else:
            if self.arreglo[i * 2] <= self.arreglo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
