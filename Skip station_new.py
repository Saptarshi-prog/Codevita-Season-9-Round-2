# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:30:37 2021

@author: 91842
"""
T = int(input())
arr=[]
for i in range(T):
    x = int(input())
    arr.append(x)

def skip_station(n):
    a = [0] * (n + 2)
    a[0] = 1
    a[1] = 1
    a[2] = 2
     
    for i in range(3, n + 1) :
        a[i] = a[i - 1] + a[i - 2] + a[i - 3]
     
    return a[n]
    
ans = []

for i in range(T):
    x = skip_station(arr[i]+1)
    ans.append(x)
    
i=0
for i in range(T):
    print(ans[i])
    
