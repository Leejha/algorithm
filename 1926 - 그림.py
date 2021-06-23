from collections import deque

def bfs(y, x) : 

	sum = 0

	que = deque([[y, x]])
	visited[y][x] = True

	while que :
		v = que.popleft() 
		sum += 1

		for i in range(4) :
			ny = v[0] + dy[i]
			nx = v[1] + dx[i] 

			if nx < 0 or nx >= m or ny < 0 or ny >= n :
				continue

			if drawing[ny][nx] == 1 and visited[ny][nx] == False :
				que.append([ny, nx])
				visited[ny][nx] = True

	draw_pix.append(sum)

n,m = map(int, input().split())

drawing = [] 

draw_pix = []


for i in range(n) :
	pixel = list(map(int, input().split()))
	drawing.append(pixel)

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]



for y in range(n) :
	for x in range(m) : 
		if drawing[y][x] == 1 and visited[y][x] == False :
			bfs(y,x) 


print(len(draw_pix))
print(max(draw_pix))
