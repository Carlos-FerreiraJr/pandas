#!/usr/bin/env python
# coding: utf-8

# ### pandas

# ##### imports

# In[16]:


import pandas as pd


# In[5]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# <br>

# ##### series dict

# In[4]:


data = {'b':5,'c':6,'a':3}


# In[5]:


y = pd.Series(data)


# <br>

# ##### series ndarray

# In[6]:


x = pd.Series(np.random.randn(5))


# In[34]:


z = pd.Series([4,2,8],index = ['a','b','c'],name='myArray')


# ###### scalar value

# In[ ]:


a = pd.Series(6.,index = ['a','b','c','d','e','f'])


# <br>

# ##### DataFrame

# In[63]:


frame = np.zeros((3,), dtype=[('first','i4'),('Second','f4'),('third','a30')])


# In[65]:


frame[:] = [(1,2.,'Hello'),(2,3.,'world'),(3,4,('friday'))]


# <br>

# In[76]:


pd.DataFrame(frame)


# <br>

# In[82]:


pd.DataFrame(frame,index=['FColumn','SCColumn','TCColumn'])

