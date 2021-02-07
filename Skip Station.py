# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:16:28 2021

@author: 91842
"""
T = int(input())
arr=[]
for i in range(T):
    x = int(input())
    arr.append(x)

def skip_station(n):
    if (n==0 or n==1):
        return 1
    elif (n==2):
        return 2
    else:
        return skip_station(n-1) + skip_station(n-2) + skip_station(n-3)

ans = []

for i in range(T):
    x = skip_station(arr[i]+1)
    ans.append(x)
    
i=0
for i in range(T):
    print(ans[i])