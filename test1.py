class Node:
    def __init__(self, valor):
        self.valor = valor
        self.direita = None
        self.esquerda = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = Node(10)
        self.raiz.esquerda = Node(5)
        self.raiz.direita = Node(15)
        self.raiz.esquerda = Node(15)
        #filhos do nó 5
        
        self.raiz.esquerda.esquerda = Node(3)
        self.raiz.esquerda.direita = Node(7)
        #filhos do nó 15
        self.raiz.direita.esquerda = Node(13)
        self.raiz.direita.direita = Node(18)
        
        #filhos do nó 3
        self.raiz.esquerda.esquerda.direita = Node(1)
        self.raiz.esquerda.esquerda.esquerda = Node(4)
        
        #filho do nó 7
        self.raiz.esquerda.direita.esquerda = Node(6)
        self.raiz.esquerda.direita.direita = Node(8)
        #filho do nó 13
        
        self.raiz.direita.esquerda.direita = Node(12)
        
        #filho do nó 12
        self.raiz.direita.esquerda.direita.esquerda = Node(11)
        
        #filho do nó 11
        self.raiz.direita.esquerda.direita.esquerda.esquerda = Node(10)
        
        #filho do nó 18
        self.raiz.direita.direita.direita = Node(19)
        
        #filho do nó 19
        self.raiz.direita.direita.direita.direita = Node(21)
        
        #filho do nó 21
        self.raiz.direita.direita.direita.direita.direita = Node(20)
        
        #filho do nó 21
        self.raiz.direita.direita.direita.direita.esquerda = Node(22)
        
        
    def inserir(self, valor):
        novo_no = Node(valor)
        if self.raiz is None:
            self.raiz = novo_no
            return True

        def _inserir_nivel(no, nivel_alvo, nivel_atual):
            if nivel_atual == nivel_alvo - 1:
                if no.esquerda is None:
                    no.esquerda = novo_no
                    return True
                if no.direita is None:
                    no.direita = novo_no
                    return True
                return False
            
            inserido = False
            if no.esquerda and _inserir_nivel(no.esquerda, nivel_alvo, nivel_atual + 1):
                inserido = True
            if not inserido and no.direita and _inserir_nivel(no.direita, nivel_alvo, nivel_atual + 1):
                inserido = True
            return inserido
        
        nivel = 1
        while True:
            if _inserir_nivel(self.raiz, nivel, 0):
                break
            nivel += 1

    def imprimir_arvore(self):
      """Imprime os valores a=da árvore sem percursus especificos."""
      print("Raiz: ", self.raiz.valor)
      print("filho esquerdo dar raiz: ", self.raiz.esquerda.valor)
      print("filho direito da raiz: ", self.raiz.direita.valor)
      print("filho esquerdo de 5: ", self.raiz.esquerda.esquerda.valor)
      print("filho direito de 5: ", self.raiz.esquerda.direita.valor)
      print("filho esquerdo de 15: ", self.raiz.direita.esquerda.valor)
      print("filho direito de 15: ", self.raiz.direita.direita.valor)
      print("filho esquerdo de 3: ", self.raiz.esquerda.esquerda.direita.valor)
      print("filho direito de 3: ", self.raiz.esquerda.esquerda.esquerda.valor)
      print("filho esquerdo de 7: ", self.raiz.esquerda.direita.esquerda.valor)
      print("filho direito de 7: ", self.raiz.esquerda.direita.direita.valor)
      print("filho esquerdo de 13: ", self.raiz.direita.esquerda.direita.valor)
      print("filho esquerdo de 12: ", self.raiz.direita.esquerda.direita.esquerda.valor)
      print("filho esquerdo de 11: ", self.raiz.direita.esquerda.direita.esquerda.esquerda.valor)
      print("filho esquerdo de 18: ", self.raiz.direita.direita.direita.valor)
      print("filho esquerdo de 19: ", self.raiz.direita.direita.direita.direita.valor)
      print("filho esquerdo de 21: ", self.raiz.direita.direita.direita.direita.direita.valor)
      print("filho esquerdo de 21: ", self.raiz.direita.direita.direita.direita.esquerda.valor)


arvore = ArvoreBinaria()
arvore.imprimir_arvore()
arvore.inserir(2)
