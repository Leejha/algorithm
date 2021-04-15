from collections import deque

n = int(input())
fair = int(input())

net = [[] for _ in range(n+1)] 

for i in range(fair) :
  a,b = map(int, input().split())
  net[a].append(b)
  net[b].append(a)

visited = [False] * (n+1)


def bfs(x) :
  visited[x] = True
  queue = deque([x]) 
  sum = 0

  while(queue) :
    v = queue.popleft()
    for i in net[v] :
      if not visited[i] :
        queue.append(i)
        visited[i] = True
        sum += 1
  print(sum)

bfs(1)
