# 백준 7576 토마토

from collections import deque

M,N = map(int, input().split())

box = [] 

for i in range(N) :
	tomato = list(map(int, input().split()))
	box.append(tomato)

visited = [ [False] * M for _ in range(N)]
ripe = []

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs (a, b) : # x = x,y 좌표가 담긴 list
	queue = deque([(a,b)])
	#visited[x, y] = True
	while queue : 
		x, y = queue.popleft()
		if box[x][y] == 1 : 
			ripe.append((x,y))
			print(x, y)
		for i in range(4) :
			nx = x + dx[i] 
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= N or ny >= M :
				  continue
			if not visited[nx][ny] : 
				queue.append((nx, ny))
				visited[nx][ny] = True
bfs(0, 0)
print(ripe)


		if (x+1 < M) and (not visited[x+1 , y]) : 
			queue.append((x+1, -1))
		if (x-1 > 0) and (not visited[x-1, y]) : 
			queue.append((x-1, y))
		if (y+1 < N) and (not visited[x, y+1]) :
			queue.append((x, y+1)) 
		if (y-1 > 0) and not visited[x, y-1] :
			queue.append((x, y-1)) 
		
 # bfs로 탐색 후 노가다로 세는 방법?
