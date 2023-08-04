#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install vpython')


# In[ ]:


from vpython import*

M=6.0e24
R=6.378e6
G=6.676e-11

Earth=sphere(pos=vector(0,0,0), radius=R, color=color.green)

m=M/36
h=3.6e7
x=R+h
y=0
rocket_pos0=vector(R,y,0)

rocket=sphere(pos=rocket_pos0, radius=R/5, make_trail=True, trail_type="points", interval=10)
r=rocket.pos-Earth.pos #vector!!

v_esc=sqrt(2*G*M/R)
#v0=1.1*v_esc
#v0=sqrt(G*M/x)
v=vector(0,v0,0)

F=vector(0,0,0)
p=m*v

T_circ=2*pi*(R+h)/v0
dt=0.001*T_circ

t=0
while t<20*T_circ:
    rate(100)
    F=-norm(r)*(G*M*m/mag(r)**2)
    p=p+F*dt
    v=p/m
    rocket.pos=rocket.pos+v*dt
    r=rocket.pos-Earth.pos
    t=t+dt


# In[ ]:




