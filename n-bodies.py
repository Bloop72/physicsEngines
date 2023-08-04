#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install vpython')


# In[ ]:


from vpython import*

#Initializing variables
N=50
AU=1.5e11
xmax=4*AU
ymax=4*AU
M=[]
Mmax=6.5e24
Mmin=5.5e24
R=xmax/50
G=3.37e-11

bodylist=[]
xlist,ylist,zlist=[],[],[]

r=[]
F=[vector(0,0,0)]*N
p=[vector(0,0,0)]*N
v=[vector(0,0,0)]*N

#Define mass
for d in range(N):
    M.append(Mmin+Mmax*random())

#Defining inital position
for b in range(N):
    xlist.append(xmax*random())
    ylist.append(ymax*random())
    zlist.append(0*random())

#Creating bodies
for a in range(N):
    body=sphere(pos=vector(xlist[a],ylist[a],zlist[a]), radius=R)
    bodylist.append(body)
for c in range(N):
    bodylist[c]

#Changing positions
dt=10000
rmin=0.5*AU
while 1:
    rate(100)
    for j in range(N):
        F[j]=vector(0,0,0)
        for i in range(N):
            r=bodylist[i].pos-bodylist[j].pos
            if i!=j:
                F[j]=F[j]+norm(r)*(G*M[j]*M[i]/mag(r)**2)
        p[j]=p[j]+F[j]*dt
        v[j]=p[j]/M[j]
        bodylist[j].pos=bodylist[j].pos+v[j]*dt


# In[ ]:




