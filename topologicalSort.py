class TopologicalSort():
    def __init__(self):
        pass
    
    def __auxTopologicalSortList(self, vertex, visited, stack, graph):
        visited.append(vertex)
        for i in range(graph[vertex].length):
            adjacenteVertex = graph[vertex].get(i).value
            if (adjacenteVertex not in visited):
                self.__auxTopologicalSortList(adjacenteVertex, visited, stack, graph)
        stack.insert(0, vertex)

    def topologicalSortList(self, graph):
        visited = []
        stack = []
        for i in graph:
            if (i not in visited):
                self.__auxTopologicalSortList(i, visited, stack, graph)
        return stack
    

    def __auxTopologicalSortMatrix(self, vertex, visited, stack, matrix):
        visited.append(vertex)
        for i in range(len(matrix)):
            if (matrix[vertex][i] >= 1 and (i not in visited)):
                self.__auxTopologicalSortMatrix(i, visited, stack, matrix)
        stack.insert(0, vertex)

    def topologicalSortMatrix(self, matrix):
        visited = []
        stack = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (matrix[i][j] >= 1 and (i not in visited)):
                    self.__auxTopologicalSortMatrix(i, visited, stack, matrix)
        return stack

        
        
