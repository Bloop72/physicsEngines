#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pip', 'install vpython')


# In[ ]:


from vpython import*
floor=box(pos=vector(0,0,0),length=30,height=0.5,width=4,color=color.blue)
ball=sphere(pos=vector(0,4,0),radius=1,color=color.red)
ball.velocity=vector(0,0,0)

g=9.8
dt=0.01

while 1:
    rate(15)
    ball.pos=ball.pos+ball.velocity
    if ball.pos.y<=ball.radius+0.25:
        ball.velocity.y=0.95*abs(ball.velocity.y)
    else:
        ball.velocity.y=ball.velocity.y-g*dt
    if ball.velocity.x==0:
        ball.velocity.x=0.5
    if ball.pos.x<-15 or ball.pos.x>15:
        ball.velocity.x=ball.velocity.x*-1


# In[ ]:




