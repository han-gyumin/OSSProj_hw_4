# 회의실 배정

num=int(input())
lst=[]
for i in range(num):
    lst.append(list(map(int,input().split())))




lst.sort()
min=lst[0][0]
max=lst[0][1]
for i in range(1,len(lst)):
    if lst[i][0]<min:
        min=lst[i][0]
    if lst[i][1]>max:
        max=lst[i][1]

for i in range(len(lst)):
    cnt=lst[i][0]
    lst[i][0]=lst[i][1]
    lst[i][1]=cnt
lst.sort()

for i in range(len(lst)):
    cnt=lst[i][0]
    lst[i][0]=lst[i][1]
    lst[i][1]=cnt

cnt=[lst[0][0],lst[0][1]]
count=1

for i in range(1,len(lst)):
    if lst[i][0]>=cnt[1]:
        count+=1
        cnt=[lst[i][0],lst[i][1]]

print(count)