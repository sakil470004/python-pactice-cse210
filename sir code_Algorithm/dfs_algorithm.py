n = 13

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

visited = [False]*n

def dfs(i):
    if visited[i]:
        return

    print('Visiting node ',i)
    visited[i] = True

    for j in graph[i]:
        dfs(j)

    print('Backtracking node ',i)

for node in range(n):
    dfs(node)

