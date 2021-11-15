graph = [[1,9],
         [0,8],
         [3],
         [2,4,5],
         [3],
         [3,6],
         [5,7],
         [3,6,8,10,11],
         [1,7,9],
         [0,8],
         [7,11],
         [7,10],
         []]
n = 13

graph = [ [1,3],
          [2],
          [],
          [2]
         ]

n = len(graph)
visited = [False]*n 
ordering= []   


def dfs(i,graph):
    visited[i] = True

    for j in graph[i]:
        if not visited[j]:
            dfs(j,graph)
    ordering.append(i)


def topSort(graph):
    
    for u in range(n):
        if not visited[u]:
            
            dfs(u,graph)      
    

    ordering.reverse()
    return  ordering     


print(topSort(graph))