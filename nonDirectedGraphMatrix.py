from breadthFirstSearch import BreathFirstSearch
from depthFirstSearch import DepthFirstSearch
from AGMprim import Prim
from dijkstra import Dijkstra
import random

class NonDirectedMatriceGraph:
    def __init__(self, size):
        self.matrix = []
        self.weigthEdges = []
        for i in range(size):
            row = []
            auxEdges = []
            for j in range(size):
                row.append(0)
                auxEdges.append(0)
            self.matrix.append(row)
            self.weigthEdges.append(auxEdges)

    def insertEdge(self, firstVertex, secondVertex, weigth):
        self.matrix[firstVertex][secondVertex] += 1
        self.matrix[secondVertex][firstVertex] += 1
        self.weigthEdges[firstVertex][secondVertex] += weigth
        self.weigthEdges[secondVertex][firstVertex] += weigth
    
    def removeEdge(self, firstVertex, secondVertex):
        if (self.matrix[firstVertex][secondVertex] == 0):
            return
        amount = self.matrix[firstVertex][secondVertex]
        #desconta o valor do peso da aresta no array auxiliar de peso
        self.weigthEdges[firstVertex][secondVertex] -= (self.weigthEdges[firstVertex][secondVertex]/amount)
        self.weigthEdges[secondVertex][firstVertex] -= (self.weigthEdges[secondVertex][firstVertex]/amount)
        self.matrix[firstVertex][secondVertex] -= 1
        self.matrix[secondVertex][firstVertex] -= 1
        

    def showVertexNeighbourhood(self, vertex):
        aux = []
        for i in range(len(self.matrix)):
            if (self.matrix[vertex][i] >= 1):
                aux.append(i)
        print(f"Vizinhaças do vértice {vertex}: {aux}")
    
    def vertexDegree(self, vertex):
        acc = 0
        for i in range(0, len(self.matrix)):
            if (self.matrix[vertex][i] >= 1):
                acc += self.matrix[vertex][i]
        return acc
 
    def isSimpleGraph(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if ((self.matrix[i][j] > 1) or (i == j and self.matrix[i][j] > 0)):
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
                if ((i==j and self.matrix[i][j]!=0) or (i!=j and self.matrix[i][j]!=1)):
                    return False
        return True

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

    def showMatrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(f"{self.matrix[i][j]} ", end="")
            print()
    
    def breadthFirstSearch(self):
        search = BreathFirstSearch().matrixSearch(self.matrix)
        print(f"Iniciando a busca pelo vértice {search[0]}, tem-se a seguinte ordem dos vértices visitados: {search}")

    def depthFirstSearch(self):
        search = DepthFirstSearch().matrixSearch(self.matrix, random.randint(0, len(self.matrix)-1), False)
        print(f"Iniciando a busca pelo vértice {search[0]}, tem-se a seguinte ordem dos vértices visitados: {search}")

    def MST(self):
        if (self.isConnected is False):
            print("O grafo não é conexo")
            return 
        Prim().primMatrix(self.matrix, self.weigthEdges)

    def isConnected(self):
        search = DepthFirstSearch()
        search.matrixSearch(self.matrix, random.randint(0, len(self.matrix)-1), True)
        return search.connected

    def minimumDistanceVertex(self,source, target):
        Dijkstra(self.matrix, self.weigthEdges, True, source, target)

graphSize = int(input("Digite o tamanho do grafo: "))

graph = NonDirectedMatriceGraph(graphSize)
choice = 0

while (choice != -1):
        print("----------------------------------------------------------")
        print("[1] Para adicionar aresta\n[2] Para remover aresta\n[3] Para identificar a vizinhaça do vértice")
        print("[4] Para identificar o grau do vértice")
        print("[5] Para verificar se o grafo é simples\n[6] Para verificar se o grafo é regular\n[7] Para identificar se o grafo é completo\n[8] Para identificar se o grafo é bipartido")
        print("[9] Para mostrar o grafo\n[10] Para realizar uma busca em largura")
        print("[11] Para realizar busca em profundidade\n[12] Para mostrar a AGM")
        print("[13] Para verificar se é conexo\n[14] Para obter o menor caminho entre dois vértices\n[-1] Para encerrar")
        choice = int(input())
        match choice:
            case 1:
                firstV = int(input("Digite o primeiro vértice que deseja criar a aresta: "))
                secondV = int(input("Digite o segundo vértice para montar a aresta: "))
                weigth = int(input("Digite o peso da aresta: "))
                if (firstV >= graphSize or secondV > graphSize or firstV < 0 or secondV >= graphSize):
                    print("Vértice inválido")
                else:
                    graph.insertEdge(firstV, secondV, weigth)
            case 2:
                firstV = int(input("Digite o primeiro vértice que deseja remover a aresta: "))
                secondV = int(input("Digite o segundo vértice para remover a aresta: "))
                if (firstV >= graphSize or secondV > graphSize or firstV < 0 or secondV >= graphSize):
                    print("Vértice inválido")
                else:
                    graph.removeEdge(firstV, secondV)
            case 3:
                vertex = int(input("Digite o vértice que deseja verificar a vizinhaça: "))
                if (vertex >= graphSize or vertex < 0):
                    print("Vértice inválido")
                else:
                    graph.showVertexNeighbourhood(vertex)
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
            case 10:
                graph.breadthFirstSearch()
            case 11:
                graph.depthFirstSearch()
            case 12:
                graph.MST()
            case 13:
                result = graph.isConnected()
                if (result):
                    print("Grafo é conexo")
                else:
                    print("Grafo não é conexo")
            case 14:
                source = int(input("Digite o vértice de origem: "))
                target = int(input("Digite o vértice de destino: "))
                graph.minimumDistanceVertex(source, target)
            case -1:
                choice = -1
            case _:
                print("opção invalida")