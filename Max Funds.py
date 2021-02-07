# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:36:45 2021

@author: 91842
"""
N = int(input())  #no. of members

mega_list = []
new_list = []
ans = []

arr = list(map(int,input().split()))    # amount collected by each member
P = int(input())                        # No. of pairs
for i in range(P):
    grp = list(map(int,input().split())) 
    mega_list.append(grp)

if N==0:
    print(0)
    
combined_list = [item for sublist in mega_list for item in sublist]
combined_list1 = list(set(combined_list))

for i in range(1,N+1):
    if i not in combined_list1:
        new_list.append(i)


new = []
while len(mega_list)>0:
    first, *rest = mega_list
    first = set(first)

    lf = -1
    while len(first)>lf:
        lf = len(first)

        rest2 = []
        for r in rest:
            if len(first.intersection(set(r)))>0:
                first |= set(r)
            else:
                rest2.append(r)     
        rest = rest2

    new.append(first)
    mega_list = rest

sum = 0


x = len(new)
for i in range(x):
    
    for j in new[i]:
        sum = sum+arr[j-1]
    ans.append(sum)
    sum=0
    
i=0
y = len(new_list)

if y>0:
    for i in range(y):
        z = new_list[i]
        ans.append(arr[z-1])

ans.sort(reverse=True)

print(ans[0])        
        