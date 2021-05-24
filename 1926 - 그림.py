from collections import deque

n,m = map(int, input().split())

image = [] 

for i in range(n) :
	pixel = list(map(int, input().split()))
	image.append(pixel)

visited = [ [False] * m for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs_all (xy) :
	que = deque([xy]) 
	visited[xy[0]][xy[1]] = True

	while que :
		pix = que.popleft()

		for i in range(4) :
			x = pix[0] + dx 
			y = pix[1] + dy

			if  x < 0 or y < 0 or x >= n or y >= m :
				continue

			visited[x][y] = True

			que.append((x,y))


def bfs_area (xy) :
	que = deque([xy]) 
	visited[xy[0]][xy[1]] = True

	while que :
		pix = que.popleft()

		for i in range(4) :
			x = pix[0] + dx 
			y = pix[1] + dy

			if  x < 0 or y < 0 or x >= n or y >= m :
				continue

			visited[x][y] = True

			que.append((x,y))			
