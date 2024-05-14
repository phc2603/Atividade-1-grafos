from linked_list import LinkedList
from breadthFirstSearch import BreathFirstSearch
from depthFirstSearch import DepthFirstSearch
from AGMprim import Prim
from dijkstra import Dijkstra
import random

class NonDirectedGraphList:
    def __init__(self, size):
        self.graph = {}
        self.weigthEdges = []
        for i in range(size):
            self.graph[i] = LinkedList()
            aux = []
            for j in range(size):
                aux.append(0)
            self.weigthEdges.append(aux)
    
    def insertEdge(self, firstVertex, secondVertex, weigth):
        self.graph[firstVertex].insertElement(secondVertex)
        self.graph[secondVertex].insertElement(firstVertex)
        self.weigthEdges[firstVertex][secondVertex] += weigth
        self.weigthEdges[secondVertex][firstVertex] += weigth

    def removeEdge(self, firstVertex, secondVertex):
        amount = 0 #verifica a quantidade de arestas entre os vertices (se tem aresta paralela e quanto)
        for i in range(self.graph[firstVertex].length):
            if (self.graph[firstVertex].get(i).value == secondVertex):
                amount += 1
        if (amount == 0): #se amount for zero, significa que não tem aresta entre os vértices parametrizados
            return
        #desconta o valor do peso da aresta no array auxiliar de peso
        self.weigthEdges[firstVertex][secondVertex] -= (self.weigthEdges[firstVertex][secondVertex]/amount)
        self.weigthEdges[secondVertex][firstVertex] -= (self.weigthEdges[secondVertex][firstVertex]/amount)
        self.graph[firstVertex].removeElementbyValue(secondVertex)
        self.graph[secondVertex].removeElementbyValue(firstVertex)

    def showVertexNeighbourhood(self, vertex):
        aux = []   
        for i in range(self.graph[vertex].length):
            aux.append(self.graph[vertex].get(i).value)
        
        print(f"Vizinhaças do vértice {vertex}: {list(set(aux))}")

    def vertexDegree(self, vertex):
        print(f"Grau do vértice {vertex}: {self.graph[vertex].length}")
        return self.graph[vertex].length

    def isSimpleGraph(self):
        for i in self.graph:
            for j in range (self.graph[i].length):
                #verifica se tem laço
                if (i == self.graph[i].get(j).value):
                    return False
                for k in  range (j+1, self.graph[i].length):
                    #busca por aresta múltipla
                    if (self.graph[i].get(j).value == self.graph[i].get(k).value):
                        return False
        
        return True 

    def isRegularGraph(self):
        auxDegree = self.graph[0].length
        for i in self.graph:
            if self.graph[i].length != auxDegree:
                return False
        
        return True
    
    def isCompleteGraph(self):
        if (not(self.isRegularGraph() and self.isSimpleGraph())):
            return False
        for vertex in self.graph:
            if self.graph[vertex].length != len(self.graph) - 1:
                return False
        return True

    def isBipartiteGraph(self):
        self.__colors = [] #atributo auxiliar privado para definir a cor de cada vértice
        for i in range(len(self.graph)):
            self.__colors.append(-1) #seta todas as cores como sendo -1. Em breve, significará azul e 1 rosa

        for i in range(len(self.graph)):
            if (self.__colors[i] == -1):
                self.__fillVertexWithColors(i)
        #verifica se existem dois vértices vizinhos com a mesma cor
        for i in range(len(self.graph)):
            for j in range(self.graph[i].length):
                vertex = self.graph[i].get(j).value
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
            
            for i in range(self.graph[currentVertex].length):
                neighborVertex = self.graph[currentVertex].get(i).value
                if (self.__colors[neighborVertex] == -1):
                    self.__colors[neighborVertex] = 1 - self.__colors[currentVertex] #faz a cor do vértice vizinho ser oposta ao vértice atual
                    queue.append(neighborVertex)
     
    def showGraph(self):    
        for i in self.graph:
            aux = []
            for j in range(self.graph[i].length):
                aux.append(self.graph[i].get(j).value)
            print(f"{i}: {aux}")

    def breadthFirstSearch(self):
        search = BreathFirstSearch().graphListSearch(self.graph)
        print(f"Iniciando a busca pelo vértice {search[0]}, tem-se a seguinte ordem dos vértices visitados: {search}")

    def depthFirstSearch(self):
        search = DepthFirstSearch().graphListSearch(self.graph, random.randint(0, len(self.graph)-1), False)
        print(f"Iniciando a busca pelo vértice {search[0]}, tem-se a seguinte ordem dos vértices visitados: {search}")

    def MST(self):
        if (self.isConnected is False):
            print("O grafo não é conexo")
            return 
        Prim().primList(self.graph, self.weigthEdges)

    def isConnected(self):
        search = DepthFirstSearch()
        search.graphListSearch(self.graph, random.randint(0, len(self.graph)-1), True)
        return search.connected

    def minimumDistance(self, src, target):
        Dijkstra(self.graph, self.weigthEdges, False, src, target)

graphSize = int(input("Digite o tamanho do grafo: "))

graph = NonDirectedGraphList(graphSize)
choice = 0

while (choice != -1):
        print("----------------------------------------------------------")
        print("[1] Para adicionar aresta\n[2] Para remover aresta\n[3] Para identificar a vizinhaça do vértice")
        print("[4] Para identificar o grau do vértice")
        print("[5] Para verificar se o grafo é simples\n[6] Para verificar se o grafo é regular\n[7] Para identificar se o grafo é completo\n[8] Para identificar se o grafo é bipartido")
        print("[9] Para mostrar o grafo\n[10] Para realizar busca em largura")
        print("[11] Para realizar busca em profundidade\n[12] Para mostrar a AGM\n[13] Para testar se é conexo\n[14] Para identificar o menor caminho entre dois vértices\n[-1] Para encerrar")
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
                graph.showGraph()
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
                graph.minimumDistance(0, 7)
            case -1:
                choice = -1
            case _:
                print("opção invalida")
