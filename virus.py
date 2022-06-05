# 백준 2606번 [바이러스]
n = int(input()) # 컴퓨터의 수 
m = int(input()) # 연결된 컴퓨터 쌍의 수

# 2차원 인접리스트 선언 
graph = [[] for i in range(n+1)]

x, y = map(int, input().split())
graph[x].append(y)
graph[y].append(x)

visited = [0] * (n+1)

def dfs(graph, v, visited):
  visited[v] = 1ㅗ
  for i in graph[v]:
    if visited[v] == 0:
      dfs(graph, i, visited)

dfs(graph, 1, visited)
print(sum(visited)-1)

  

