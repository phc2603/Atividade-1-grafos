from topologicalSort import TopologicalSort
from breadthFirstSearch import BreathFirstSearch
from depthFirstSearch import DepthFirstSearch
from dijkstra import Dijkstra
import random

class DirectedMatriceGraph:
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
    
    def insertEdge(self, firstVertex, receptorVertex, weigth):
        self.matrix[firstVertex][receptorVertex] += 1
        self.weigthEdges[firstVertex][receptorVertex] += weigth
    
    def removeEdge(self, firstVertex, receptorVertex):
        if (self.matrix[firstVertex][receptorVertex] == 0):
            return
        amount = self.matrix[firstVertex][receptorVertex]
        self.weigthEdges[firstVertex][receptorVertex] -= (self.weigthEdges[firstVertex][receptorVertex]/amount)
        self.matrix[firstVertex][receptorVertex] -= 1

    def checkSuccessors(self, vertex):
        aux = []
        for i in range(len(self.matrix)):
            if (self.matrix[vertex][i] >= 1):
                aux.append(i)
        return aux
    
    def checkPredecessors(self, vertex):
        aux = []
        for i in range(len(self.matrix)):
            if (self.matrix[i][vertex] >= 1):
                aux.append(i)
        return aux
    
    def vertexDegree(self, vertex):
        print(f"Grau de entrada do vértice {vertex} é {len(self.checkPredecessors(vertex))} ")
        print(f"Grau de saída do vértice {vertex} é {len(self.checkSuccessors(vertex))} ")
    
    def isSimpleGraph(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if ((i == j and self.matrix[i][j]!=0) or (self.matrix[i][j] > 1)):
                    return False
        return True        

    def isRegularGraph(self):
        basePredecessor = len(self.checkPredecessors(0))
        baseSucessor = len(self.checkSuccessors(0))
        for i in range(1, len(self.matrix)):
            if ((len(self.checkPredecessors(i)) != basePredecessor) or (len(self.checkSuccessors(i) != baseSucessor))):
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
                    print(f"CORES DE {i}: {self.__colors[i]} | de {vertex}: {self.__colors[vertex]}")
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
    
    def breadthFirstSearch(self):
        search = BreathFirstSearch().matrixSearch(self.matrix)
        print(f"Iniciando a busca pelo vértice {search[0]}, tem-se a seguinte ordem dos vértices visitados: {search}")

    def depthFirstSearch(self):
        search = DepthFirstSearch().matrixSearch(self.matrix, random.randint(0, len(self.matrix)-1), False)
        print(f"Iniciando a busca pelo vértice {search[0]}, tem-se a seguinte ordem dos vértices visitados: {search}")
    
    def topologicalSort(self):
        topologicalSortStack = TopologicalSort().topologicalSortMatrix(self.matrix)
        print(f"Ordenação topológica para o grafo: {topologicalSortStack}")

    def isConnected(self):
        search = DepthFirstSearch()
        for i in range(len(self.matrix)):
            search.matrixSearch(self.matrix, i , True)
            if (not search.connected):
                return False 
        return True
    
    def minimumDistance(self, src, target):
        Dijkstra(self.matrix, self.weigthEdges, True, src, target)

graphSize = int(input("Digite o tamanho do grafo: "))

graph = DirectedMatriceGraph(graphSize)
choice = 0

while (choice != -1):
        print("----------------------------------------------------------")
        print("[1] Para adicionar aresta\n[2] Para remover aresta\n[3] Para identificar a vizinhaça do vértice")
        print("[4] Para identificar o grau do vértice")
        print("[5] Para verificar se o grafo é simples\n[6] Para verificar se o grafo é regular\n[7] Para identificar se o grafo é completo\n[8] Para identificar se o grafo é bipartido")
        print("[9] Para mostrar o grafo\n[10] Para realizar busca em largura\n[11] Para realizar busca em profundidade")
        print("[12] Para mostrar a ordenação topológica do grafo\n[13] Para verificar se o grafo é fortemente conexo\n[14] Para calcular o caminho mínimmo entre 2 vértices\n[-1] Para encerrar")
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
                vertex = int(input("Digite o vértice que deseja verificar os predecessores e sucessores: "))
                if (vertex >= graphSize or vertex < 0):
                    print("Vértice inválido")
                else:
                    print(f"Predecessores: {list(set(graph.checkPredecessors(vertex)))}")
                    print(f"Sucessores: {list(set(graph.checkSuccessors(vertex)))}")
            case 4:
                vertex = int(input("Digite o número do vértice que deseja identificar o grau: "))
                if (vertex >= graphSize or vertex < 0):
                    print("Vértice inválido")
                else:
                    graph.vertexDegree(vertex)
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
                graph.topologicalSort()
            case 13:
                if (graph.isConnected()):
                    print("Grafo é fortemente conexo")
                else:
                    print("Grafo não é fortemente conexo")
            case 14:
                source = int(input("Digite o vértice de origem: "))
                target = int(input("Digite o vértice que deseja alcançar: "))
                graph.minimumDistance(source, target)
            case -1:
                choice = -1
            case _:
                print("opção invalida")