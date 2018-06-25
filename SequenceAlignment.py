
# coding: utf-8

# In[41]:


import time
import random
import pdb
import matplotlib.pyplot as plt 
import numpy as np


# In[42]:


# Algorithm 1 based on Divide-and Conquer
def opt1(x,y):
    m=len(x)
    n=len(y)
    def opt(a,b):
        if a==m:
            return 2*(n-b)
        elif b==n:
            return 2*(m-a)
        else:
            if x[a]==y[b]:
                penalty=0
            else:
                penalty=1
            return min(opt(a+1,b+1)+penalty, opt(a+1,b)+2, opt(a,b+1)+2)
    return opt(0,0)


# In[50]:


# Algorithm 2 based on DB
def opt2(x,y):
    m=len(x)
    n=len(y)
    
    class cell:
        def __init__(self, cost, pointer, x, y):
            self.cost=cost
            self.pointer=pointer
            self.x=x
            self.y=y
    
    # initialization
    A = [[cell(0,None,y,x) for x in range(n+1)] for y in range(m+1)]
    A1 = ""
    A2 = ""
    for i in range(m-1,-1,-1):
        A[i][n].cost=2*(m-i)
        A[i][n].pointer=A[i+1][n]
    for j in range(n-1,-1,-1):
        A[m][j].cost=2*(n-j)
        A[m][j].pointer=A[m][j+1]
    
    # fill the table A
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            penalty=0
            # pdb.set_trace()
            if x[i]!=y[j]:
                penalty=1
            below = A[i+1][j].cost + 2
            right = A[i][j+1].cost + 2
            diagonal = A[i+1][j+1].cost + penalty
            if below <= right and below <= diagonal:
                A[i][j].cost = below
                A[i][j].pointer = A[i+1][j]
            elif right <= below and right <= diagonal:
                A[i][j].cost = right
                A[i][j].pointer = A[i][j+1]
            else:
                A[i][j].cost = diagonal
                A[i][j].pointer = A[i+1][j+1]
            
    # find the way
    nextcell = A[0][0]
    while nextcell.pointer != None:
        nextcell_next_x = nextcell.pointer.x;
        nextcell_next_y = nextcell.pointer.y;
        if nextcell.x == nextcell_next_x:
            A1 = A1 + '-'
            A2 = A2 + y[nextcell.y]
        elif nextcell.y == nextcell_next_y:
            A1 = A1 + x[nextcell.x]
            A2 = A2 + '-'
        else:
            A1 = A1 + x[nextcell.x]
            A2 = A2 + y[nextcell.y]
        nextcell = nextcell.pointer
    return A[0][0].cost, A1, A2


# In[ ]:


# sequence alignment using two algorithms

print("请输入x: ")
x=input()
print("请输入y: ")
y=input()
i=0
j=0
m=len(x)
n=len(y)

start = time.time()
cost = opt1(x,y)
end = time.time()
print("Sequence length of X: " + str(m) + "   Sequence length of Y: " + str(n)+ "   Runtime of Algorithm 1(s): " + str(end-start) + "   cost: "+ str(cost))

start = time.time()
cost,A1,A2 = opt2(x,y)
end = time.time()
t2.append(end-start)
print("Sequence length of X: " + str(m) + "   Sequence length of Y: " + str(n) + "   Runtime of Algorithm 2(s): " + str(end-start)+ "   cost: "+ str(cost))
print("the optimal alignment of the two sequences is: ")
print(A1)
print(A2)


# In[11]:


# compare Algorithm 2 with Algorithm 1

'''
s = ['A','T','C','G']
n = [3,4,5,6,7,8,9,10,11,12,13,14]
t1=[]
t2=[]
for i in range(len(n)):
    X = ""
    Y = ""
    for j in range(n[i]):
        X = X + s[random.randint(0,3)]
        Y = Y + s[random.randint(0,3)]
    
    start = time.time()
    cost = opt1(X,Y)
    end = time.time()
    t1.append(end-start)
    print("Sequence length: " + str(n[i]) + "   Runtime of Algorithm 1(s): " + str(end-start) + "   cost: "+ str(cost))
    
    
    start = time.time()
    (cost,A1,A2) = opt2(X,Y)
    end = time.time()
    t2.append(end-start)
    print("Sequence length: " + str(n[i]) + "   Runtime of Algorithm 2(s): " + str(end-start)+ "   cost: "+ str(cost))
    
    print()


max_value = max(max(t1),max(t2))
t1_o=[i*100/max_value for i in t1]
t2_o=[i*100/max_value for i in t2]
plot1=plt.plot(n,t1_o,color="red",linewidth=0.5, label='Algorithm 1')
plot2=plt.plot(n,t2_o,color="blue", linewidth=0.5, label='Algorithm 2')
plt.xlabel("length of sequences") 
plt.ylabel("runtime")
plt.legend(loc='upper left') 
plt.show()
'''

