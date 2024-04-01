class DirectedMatriceGraph:
    def __init__(self, size):
        self.matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            self.matrix.append(row)
    
    def insertEdge(self, firstVertex, receptorVertex):
        self.matrix[firstVertex][receptorVertex] += 1
    
    def removeEdge(self, firstVertex, receptorVertex):
        self.matrix[firstVertex][receptorVertex] -= 1

    def checkSuccessors(self, vertex):
        aux = []
        for i in range(len(self.matrix)):
            if (self.matrix[vertex][i] != 0):
                aux.append(self.matrix[vertex][i])
        print(f"Sucessores de {vertex}: {aux}")
        return aux
    
    def checkPredecessors(self, vertex):
        aux = []
        for i in range(len(self.matrix)):
            if (self.matrix[i][vertex] != 0):
                aux.append(self.matrix[i][vertex])
        print(f"Antecessores de {vertex}: {aux}")
        return aux
    
    def vertexDegree(self, vertex):
        acc = 0
        for i in range(len(self.matrix)):
            acc += self.matrix[vertex][i]
        return acc
    
    def isSimpleGraph(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if ((i == j and self.matrix[i][j]!=0) or (self.matrix[i][j] > 1)):
                    return False
        return True        

    def isRegularGraph(self):
        firstVertexDegree = self.vertexDegree(0)
        for i in range(1, len(self.matrix)):
            if (self.vertexDegree(i) != firstVertexDegree):
                return False
        return True

    def isCompleteGraph(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if ((i==j and self.matrix[i][j] != 0) or (i!=j and self.matrix[i][j] != 1)):
                    return False
        return True
        
    def showMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(f"{self.matrix[i][j]} ", end="")
            print()    

    def isBipartiteGraph(self):
        self.__colors = [] #atributo auxiliar privado para definir a cor de cada vértice
        for i in range(len(self.matrix)):
            self.__colors.append(-1) #seta todas as cores como sendo -1. Em breve, significará azul e 1 rosa

        for i in range(len(self.matrix)):
            if (self.__colors[i] == -1 and len(self.__neighborhood(i))):
                self.__fillVertexWithColors(i)
        #verifica se existem dois vértices vizinhos com a mesma cor
        for i in range(len(self.matrix)):
            vertexNeighbor = self.__neighborhood(i)
            for j in range(len(vertexNeighbor)):
                vertex = vertexNeighbor[j]
                if (self.__colors[i] == self.__colors[vertex]):
                    print(f"CORES DE {i}: {self.__colors[i]} // de {vertex}: {self.__colors[vertex]}")
                    return False
        return True

    def __fillVertexWithColors(self, vertex):#método privado para 'colorir' os vértices
        self.__colors[vertex] = 0 #define a cor do vértice como 0, ou como dito antes, azul
        queue = []
        queue.append(vertex)
        position = 0

        while (position < len(queue)):
            currentVertex = queue[position]
            position += 1
            vertexNeighbor = self.__neighborhood(currentVertex)
            for i in range(len(vertexNeighbor)):
                neighborVertex = vertexNeighbor[i]
                if (self.__colors[neighborVertex] == -1):
                    self.__colors[neighborVertex] = 1 - self.__colors[currentVertex] #faz a cor do vértice vizinho ser oposta ao vértice atual
                    queue.append(neighborVertex)

    def __neighborhood(self, vertex):
        neighborVertices = []
        for i in range(len(self.matrix)):
            if (self.matrix[vertex][i] != 0):
                neighborVertices.append(i)
        return neighborVertices


graphSize = int(input("Digite o tamanho do grafo: "))

graph = DirectedMatriceGraph(graphSize)
choice = 0

while (choice != -1):
        print("----------------------------------------------------------")
        print("[1] Para adicionar aresta\n[2] Para remover aresta\n[3] Para identificar a vizinhaça do vértice")
        print("[4] Para identificar o grau do vértice")
        print("[5] Para verificar se o grafo é simples\n[6] Para verificar se o grafo é regular\n[7] Para identificar se o grafo é completo\n[8] Para identificar se o grafo é bipartido")
        print("[9] Para mostrar o grafo\n[-1] Para encerrar")
        choice = int(input())
        match choice:
            case 1:
                firstV = int(input("Digite o primeiro vértice que deseja criar a aresta: "))
                secondV = int(input("Digite o segundo vértice para montar a aresta: "))
                if (firstV >= graphSize or secondV > graphSize or firstV < 0 or secondV >= graphSize):
                    print("Vértice inválido")
                else:
                    graph.insertEdge(firstV, secondV)
            case 2:
                firstV = int(input("Digite o primeiro vértice que deseja remover a aresta: "))
                secondV = int(input("Digite o segundo vértice para remover a aresta: "))
                if (firstV >= graphSize or secondV > graphSize or firstV < 0 or secondV >= graphSize):
                    print("Vértice inválido")
                else:
                    graph.removeEdge(firstV, secondV)
            case 3:
                vertex = int(input("Digite o vértice que deseja verificar os predecessores e sucessores: "))
                if (vertex >= graphSize or vertex < 0):
                    print("Vértice inválido")
                else:
                    graph.checkPredecessors(vertex)
                    graph.checkSuccessors(vertex)
            case 4:
                vertex = int(input("Digite o número do vértice que deseja identificar o grau: "))
                if (vertex >= graphSize or vertex < 0):
                    print("Vértice inválido")
                else:
                    print(f"Grau do vértice {vertex} é: {graph.vertexDegree(vertex)}")
            case 5:
                if (graph.isSimpleGraph()):
                    print("O grafo é simples")
                else:
                    print("O grafo não é simples")
            case 6:
                if (graph.isRegularGraph()):
                    print("O grafo é regular")
                else:
                    print("O grafo não é regular")
            case 7:
                if (graph.isCompleteGraph()):
                    print("O grafo é completo")
                else:
                    print("O grafo não é completo")
            case 8:
                if (graph.isBipartiteGraph()):
                    print("O grafo é bipartido")
                else:
                    print("O grafo não é bipartido")
            case 9:
                graph.showMatrix()
            case -1:
                choice = -1
            case _:
                print("opção invalida")
