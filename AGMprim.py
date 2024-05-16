import sys

class Prim:
    def __init__(self):
        self.__matrixMST = []

    def primList(self, graph, weigthEdges):
        self.__matrixMST = []
        visited = [0]*len(graph)
        visitedEdges = 0
        visited[0] = True
        while visitedEdges < len(graph)-1:
            min = sys.maxsize #seta o peso do vértice como infinito
            for i in graph: #itera por todos vértices do grafo
                if visited[i]: #seta o vértice atual para verificar as arestas adj
                    for j in range(graph[i].length): #itera na lista adj
                        adjacentVertex = graph[i].get(j).value
                        if (not visited[adjacentVertex]):#se o vertice adj ao vertice atual não estiver visitado (isso corta a possibilidade de criar ciclos)
                            if (min > weigthEdges[i][adjacentVertex]):#se o valor do peso vértice adj for menor que o peso da aresta 
                                min = weigthEdges[i][adjacentVertex] #peso do vértice adjacente é o valor da aresta
                                sourceVertex = i #vértice de origem/atual
                                smallerAdjacentVertex = adjacentVertex #vértice adjancente de menor aresta
            visitedEdges += 1
            visited[smallerAdjacentVertex] = True #marca o vértice adjacente cuja aresta tem menor peso como visitado
            self.__matrixMST.append([sourceVertex, smallerAdjacentVertex, weigthEdges[sourceVertex][smallerAdjacentVertex]])
        self.showMST()
    
    def primMatrix(self, matrix, weigthEdges):
        self.__matrixMST = [] #reseta a árvore geradora
        visited = [0]*len(matrix)#lista auxiliar para setar os vértices visitados
        visitedEdges = 0
        visited[0] = True #pega um vértice ao acaso
        while visitedEdges < len(matrix)-1:
            min = sys.maxsize #define o peso do vértice como infinito
            for i in range(len(matrix)):
                if visited[i]: #verifica se estamos no vértice atual
                    for j in range(len(matrix)):#visita os vértices adjacentes ao vértice atual
                        if ((not visited[j]) and (matrix[i][j] >= 1)):
                            if (min > weigthEdges[i][j]):#verifica se o peso do vértice é maior que o peso da aresta
                                min = weigthEdges[i][j]#peso do vértice adjacente é o valor da aresta
                                sourceVertex = i #vértice de origem/atual
                                smallerAdjacentVertex = j #vértice de adjacência de menor aresta
            visitedEdges += 1
            visited[smallerAdjacentVertex] = True
            self.__matrixMST.append([sourceVertex, smallerAdjacentVertex, weigthEdges[sourceVertex][smallerAdjacentVertex]])
        self.showMST()
    
    def showMST(self):
        totalWeigth = 0
        print("ARESTA - PESO")
        for source, adjacent, weigth in self.__matrixMST:
            totalWeigth += weigth
            print(f"{source} -> {adjacent}: {weigth}")
        print(f"Peso total: {totalWeigth}")
