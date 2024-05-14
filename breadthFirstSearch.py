import random

class BreathFirstSearch:
    def __init__(self):
        pass
    def graphListSearch(self, graph):
        randomVertex = random.choice(list(graph)) #pegando um vértice ao acaso para iniciar a busca
        
        visited = []
        visited.append(randomVertex)
        queue = [randomVertex]
        while(len(visited) != len(graph)): #enquanto todos os vertices não forem visitados
            if (not queue):
                for i in graph:
                    if (i not in visited):#busca os vértices que ainda não foram visitados
                        queue.append(i)
                        visited.append(i)
                        break 
            while queue:
                currentVertexAdjacentList = graph[queue[0]]
                for i in range(currentVertexAdjacentList.length):
                    adjacentVertex = currentVertexAdjacentList.get(i).value
                    if (adjacentVertex not in visited):
                        queue.append(adjacentVertex) #acrescenta o vertice adjacente na fila 
                        visited.append(adjacentVertex) #marca o vértice como visitado
                queue.pop(0) #remove atual vértice da fila
        return visited
    
    def matrixSearch(self, matrix):
        randomVertex = random.randint(0, len(matrix)-1) #pegando um vértice ao acaso para iniciar a busca
        visited = []
        visited.append(randomVertex)
        queue = [randomVertex]
        while (len(visited) != len(matrix)):
            if (not queue):
                for i in range(len(matrix)):
                    if (i not in visited):
                        visited.append(i)
                        queue.append(i)
                        break  
            while queue:
                currentVertexAdjacentList = queue[0]
                for i in range(len(matrix)):
                    if (matrix[currentVertexAdjacentList][i] >= 1):
                        adjacentVertex = i
                        if (adjacentVertex not in visited):
                            queue.append(adjacentVertex) #acrescenta o vertice adjacente na fila 
                            visited.append(adjacentVertex) #marca o vértice como visitado
                queue.pop(0) #remove atual vértice da fila
        return visited

    

