from collections import deque 

N, M, V = map(int, input().split()) 

graph = [ [] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, input().split()) 
    graph[a].append(b) 
    graph[b].append(a)
    
for j in range(N) :
    graph[j].sort()
    
visited = [False] * (N+1)
visited_1 = [False] * (N+1)


def dfs (v) :
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v] :
        if not visited[i] :
            dfs(i)
        
def bfs (v) :
    queue = deque([v]) 
    visited_1[v] = True
    
    while queue :
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v] :
            if not visited_1[i] :
                queue.append(i)
                visited_1[i] = True
                
dfs(V)
print()
bfs(V)
