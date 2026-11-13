import matplotlib.pyplot as plt


class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1

        # upheap: sube mientras sea menor que su padre (el -INF de la posicion 0 lo detiene)
        while self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            i = i // 2

        if imagen:
            self.dibujar()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) == 1:
            return None

        menor = self.arreglo[1]
        self.arreglo[1] = self.arreglo[-1]
        self.arreglo.pop()

        if len(self.arreglo) > 1:
            self._sift_down(1)

        if imagen:
            self.dibujar()

        return menor

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + lista[:]
        i = (len(self.arreglo) - 1) // 2

        # downheap desde el ultimo padre hasta la raiz
        while i > 0:
            self._sift_down(i)
            i -= 1

        if imagen:
            self.dibujar()

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

    # imagen

    def _posicion(self, i):
        # nivel del nodo i: cuantas veces se puede dividir entre 2 hasta llegar a 1
        nivel = 0
        n = i
        while n > 1:
            n = n // 2
            nivel += 1

        nodos_en_nivel = 2 ** nivel
        k = i - nodos_en_nivel           # lugar del nodo dentro de su nivel (0, 1, 2, ...)
        x = (k + 0.5) / nodos_en_nivel   # reparte el nivel a lo ancho, de izquierda a derecha
        y = -nivel                       # cada nivel debajo del anterior
        return x, y

    def dibujar(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        n = len(self.arreglo)

        # aristas: de cada nodo i a sus hijos 2i y 2i+1 (si existen)
        for i in range(1, n):
            x, y = self._posicion(i)
            for hijo in (2 * i, 2 * i + 1):
                if hijo < n:
                    xh, yh = self._posicion(hijo)
                    ax.plot([x, xh], [y, yh], color='black', zorder=1)

        # nodos: se empieza en 1 para no dibujar el -INF
        for i in range(1, n):
            x, y = self._posicion(i)
            ax.text(x, y, str(self.arreglo[i]), ha='center', va='center', fontsize=12, zorder=2,
                    bbox=dict(boxstyle='circle', facecolor='lightblue', edgecolor='black'))

        # el ultimo nodo esta en el nivel mas bajo; si el heap esta vacio solo queda un nivel
        y_minimo = 0
        if n > 1:
            y_minimo = self._posicion(n - 1)[1]

        ax.set_xlim(0, 1)
        ax.set_ylim(y_minimo - 0.5, 0.5)
        ax.axis('off')
        plt.show()


if __name__ == "__main__":
    H = Heap()
    H.insert(10)
    H.insert(4)
    H.insert(7, imagen=True)
    H.remove_smallest(imagen=True)
    H.build_heap([31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
                  15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], imagen=True)
