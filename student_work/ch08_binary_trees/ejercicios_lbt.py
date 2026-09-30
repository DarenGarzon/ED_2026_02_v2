from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True

    cola = [T.root()]
    hueco = False                   

    while len(cola) > 0:

        p = cola.pop(0)

        for hijo in [T.left(p), T.right(p)]:

            if hijo is None:
                hueco = True

            elif hueco:             
                return False

            else:
                cola.append(hijo)

    return True


def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""

    desde_p = []
    x = p
    while x is not None:
        desde_p.append(x)
        x = T.parent(x)

    desde_q = []
    y = q
    while y not in desde_p:
        desde_q.append(y)
        y = T.parent(y)


    subida = desde_p[:desde_p.index(y) + 1]
    desde_q.reverse()
    nodos = subida + desde_q

    textos = []

    for nodo in nodos:
        textos.append(str(nodo.element()))
    return " -> ".join(textos)


if __name__ == "__main__":
    pass
