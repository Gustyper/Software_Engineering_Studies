class Iterator:
    """
    Essa classe aqui não faz mt né. Basta usar o for comum do python, 
    mas, por exemplo, se seu fizesse um Iterator pra uma árvore pode ser uma boa criar um Iterador, 
    já que eu posso ter a BFS a busca em profundidade sla
    """
    def __init__(self, data):
        self._index = 0
        self.data = data
        self.len = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= self.len:
            print("Acabei de iterar por tudo")
            raise StopIteration 
        item = self.data[self._index]
        self._index += 1
        return item 