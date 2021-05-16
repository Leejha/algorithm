N = int(input())

li = []

for j in range(N) :
  li.append(list(map(int, input().split())))

li.sort() 
li.sort(key = lambda x : x[1]) 

pivot = li[0] 
del li[0]
sum = 1

for i in li :
	if i[0] >= pivot[1] :
		pivot = i
		sum += 1
    
print(sum)
