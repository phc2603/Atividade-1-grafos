import sys
import heapq

class Edge:
    def __init__(self, weigth, startVertex, targetVertex):
        self.weigth = weigth
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node:
    def __init__(self, num):
        self.num = num
        self.visited = False
        self.predecessor = None #processor do nosso vertice atual
        self.neighbors = [] #vertices adjacentes ao atual
        self.minimumDist = sys.maxsize #distancia do vertice que, inicialmente, vale infinito

    def __lt__(self, otherNode): #método __lt__ que serve para comparar atributos de um objeto. No caso, objetos da classe Node (vértice)
        return self.minimumDist < otherNode.minimumDist # compara as distâncias de dois vértices para saber se devemos ou não atualizar o valor de menor distância do vértice
    
    def addEdge(self, weigth, destinationVertex):
        edge = Edge(weigth, self, destinationVertex)
        self.neighbors.append(edge)

class Dijkstra:
    def __init__(self, dataStruct, weigthEdges, isMatrix, starter, target):
        #heap que contém os vértices com os respectivos valores. Devemos acrescetar vértice no heap caso ele não esteja, 
        #atualizá-lo caso o vértice  seja de menor valor que o já existente, ou excluí-lo após ser usado
        self.heap = []
        self.bulidGraph(dataStruct, weigthEdges, isMatrix, starter, target)
    
    def bulidGraph(self, dataStruct, weigthEdges, isMatrix, starter, target):
        vertexAuxList = []
        for i in range(len(dataStruct)):
            vertexAuxList.append(Node(i)) # [NÓ 0, NÓ 1, NÓ 2, NÓ 3...]
        if (isMatrix):
            for i in range(len(dataStruct)):
                for j in range(len(dataStruct)):
                    if (weigthEdges[i][j] and dataStruct[i][j] >= 1):
                        vertexAuxList[i].addEdge(weigthEdges[i][j], vertexAuxList[j])
        else:
            for i in range(len(dataStruct)):
                for j in range(dataStruct[i].length):
                    adjacentElement = dataStruct[i].get(j).value
                    if (weigthEdges[i][adjacentElement]):
                        vertexAuxList[i].addEdge(weigthEdges[i][adjacentElement], vertexAuxList[adjacentElement])
        self.calculate(vertexAuxList[starter])
        self.getShortestPath(vertexAuxList[target])

    
    def calculate(self, startVertex):
        startVertex.minimumDist = 0
        heapq.heappush(self.heap, startVertex)
        while self.heap:
            #remove o vértice de menor distância do heap
            currentVertex = heapq.heappop(self.heap)
            if (not currentVertex.visited):
                #itera pelos vértices adjacentes do vértice atual
                for edge in currentVertex.neighbors:
                    start = edge.startVertex #vértice atual que estamos
                    target = edge.targetVertex #vértice adjancente ao atual
                    newDistance = start.minimumDist + edge.weigth #a distância é a do vértice atual + a aresta que liga o vértice atual e o adjacente
                    if (newDistance < target.minimumDist):#caso essa distância seja menor que a distância mínimma que está representada no vértice atual
                        target.minimumDist = newDistance #atualiza a distância
                        target.predecessor = start #o predecessor do vértice adjacente vira o nosso atual
                        heapq.heappush(self.heap, target)
            
            currentVertex.visited = True
    
    def getShortestPath(self, vertex):
        if (vertex.minimumDist == sys.maxsize):
            print("Não existe um caminho partido do vértice de origem até o desejado")
            return
        print(f"O menor caminho do vértice é: {vertex.minimumDist}")
        aux = []
        currentVertex = vertex
        while currentVertex is not None:
            aux.append(currentVertex.num)
            currentVertex = currentVertex.predecessor
        aux.reverse()
        for i in aux:
            print(f"{i}",end=" ")
        print()