from linked_list import LinkedList
from topologicalSort import TopologicalSort
from breadthFirstSearch import BreathFirstSearch
from depthFirstSearch import DepthFirstSearch
import random
from dijkstra import Dijkstra

class DirectedGraphList:
    def __init__(self, size):
        self.graph =  {}
        self.weigthEdges = []
        for i in range(size):
            self.graph[i] = LinkedList()
            aux = []
            for j in range(size):
                aux.append(0)
            self.weigthEdges.append(aux)
    
    def insertEdge(self, vertex, linkedVertex, weigth):
        self.graph[vertex].insertElement(linkedVertex)
        self.weigthEdges[vertex][linkedVertex] += weigth
    
    def removeEdge(self, vertex, linkedVertex):
        amount = 0 #verifica a quantidade de arestas entre os vertices (se tem aresta paralela e quanto)
        for i in range(self.graph[vertex].length):
            if (self.graph[vertex].get(i).value == linkedVertex):
                amount += 1
        if (amount == 0): #se amount for zero, significa que não tem aresta entre os vértices parametrizados
            return
        self.weigthEdges[vertex][linkedVertex] -= (self.weigthEdges[vertex][linkedVertex]/amount)
        self.graph[vertex].removeElementbyValue(linkedVertex)

    def checkSuccessor(self, vertex):
        successors = []
        for i in range(self.graph[vertex].length):
            successors.append(self.graph[vertex].get(i).value)
        return successors

    def checkPredecessor(self, vertex):
        predecessors = []
        for i in range(len(self.graph)):
            for j in range(self.graph[i].length):
                if (self.graph[i].get(j).value == vertex):
                    predecessors.append(i)
                    break
        return predecessors

    def vertexDegree(self, vertex):
        print(f"Grau de entrada do vértice {vertex} é {len(self.checkPredecessor(vertex))} ")
        print(f"Grau de saída do vértice {vertex} é {len(self.checkSuccessor(vertex))} ")

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
        for i in range(len(self.graph)):
            if  (len(self.checkPredecessor(i)) != (len(self.checkSuccessor(i)))):
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

    def topologicalSort(self):
        topologicalSortStack = TopologicalSort().topologicalSortList(self.graph)
        print(f"A ordenação topológica do grafo é: {topologicalSortStack}")
    
    def isConnected(self):
        search = DepthFirstSearch()
        for i in range(len(self.graph)):
            search.graphListSearch(self.graph, i , True)
            if (not search.connected):
                return False 
        return True
    
    def minimumDistance(self, src, target):
        Dijkstra(self.graph, self.weigthEdges, False, src, target)

graphSize = int(input("Digite o tamanho do grafo: "))

graph = DirectedGraphList(graphSize)
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
                    print(f"Antecessores: {graph.checkPredecessor(vertex)}")
                    print(f"Sucessores: {graph.checkSuccessor(vertex)}")
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

