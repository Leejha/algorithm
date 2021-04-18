N = int(input())

li = []

for j in range(N) :
  li.append(list(map(int, input().split())))

# 시작시간을 오름차순으로 정렬
li.sort() 
# 끝나는 시간을 오름차순으로 정렬
li.sort(key = lambda x : x[1]) 

# 정렬된 회의중에서 첫번째 회의를 배정 
pivot = li[0] 
del li[0]
sum = 1

# 리스트는 이미 잘 정렬된 상태이므로 시작시간과 끝나는 시간만 비교하여 
for i in li :
	if i[0] >= pivot[1] :
		pivot = i
		sum += 1

print(sum)
