class Pila:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def extract(self):
        try: #intenta devolver el ultimo elemento de la pila
            return self.items.pop()
        except IndexError: #si la pila esta vacía mandara una excepcion
            raise ValueError("La pila esta vacía")
    
    def include(self, item):
        self.items.append(item)

    def length(self):
        return len(self.items)
    
    def lastElement(self):
        return self.items[len(self.items)-1]
    
    def inspect(self):
        for i in range(0,len(self.items)):
            print(self.items[i])