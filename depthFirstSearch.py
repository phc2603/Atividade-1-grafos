import random

class DepthFirstSearch():
    def __init__(self):
        self.connected = True

    def graphListSearch(self,graph, starterVertex, shouldReturn):
        self.connected = True
        visited = []
        stack = [starterVertex]
        while(len(visited) != len(graph)): #enquanto todos os vertices não forem visitados
            if (not stack):
                self.connected = False #caso em algum momento a pilha fique vazia, mas ainda haja vértice para visitar, significa que temos mais de uma componente e o grafo não é conexo
                if(shouldReturn):#se a busca for para verificar apenas se o grafo é conexo, quando chegamos aqui, já sabemos que ele não é 
                    return 
                for i in graph:
                    if (i not in visited):#busca os vértices que ainda não foram visitados
                        stack.insert(0, i)#inserindo o vertice no topo da pilha
                        visited.append(i)
                        break 
            while stack:
                lastStackVertex = stack.pop(0) #remove atual vértice da pilha
                if (lastStackVertex not in visited):
                    visited.append(lastStackVertex)
                currentVertexAdjacentList = graph[lastStackVertex]
                for i in range(currentVertexAdjacentList.length):
                    adjacentVertex = currentVertexAdjacentList.get(i).value
                    if (adjacentVertex not in visited):
                        stack.insert(0, adjacentVertex) #acrescenta o vertice no topo da pilha
        return visited

    def matrixSearch(self,matrix, starterVertex, shouldReturn):
        self.connected = True
        visited = []
        stack = [starterVertex]
        while (len(visited) != len(matrix)):
            if (not stack):
                self.connected = False #caso em algum momento a pilha fique vazia, mas ainda haja vértice para visitar, significa que temos mais de uma componente e o grafo não é conexo
                if (shouldReturn): #se a busca for para verificar apenas se o grafo é conexo, quando chegamos aqui, já sabemos que ele não é 
                    return
                for i in range(len(matrix)):
                    if (i not in visited):
                        visited.append(i)
                        stack.append(i)
                        break  
            while stack:
                lastStackVertex = stack.pop(0) #remove o último vértice da pilha
                if (lastStackVertex not in visited):
                    visited.append(lastStackVertex)
                for i in range(len(matrix)):
                    if (matrix[lastStackVertex][i] >= 1):
                        adjacentVertex = i
                        if (adjacentVertex not in visited):
                            stack.insert(0, adjacentVertex) #acrescenta o vertice adjacente na fila 
        
        return visited