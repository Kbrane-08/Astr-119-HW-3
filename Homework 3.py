#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


x = np.linspace(0, 2*np.pi, 1000)  # creating a numpy array that has 1000 values between 0 and 2pi, evenly spaced
y1 = 5.5 * np.cos(2 * x) + 5.5  # defining each of the three functions listed, using numpy operations (to apply the function for all values of x to 
# create a new array)
y2 = 0.02 * np.exp(x)
y3 = 0.25 * np.square(x) + 0.1 * np.sin(10 * x)
plt.plot(x, y1)# plotting (a)
plt.plot(x, y2)# plotting (b)
plt.plot(x, y3)# plotting (c)


plt.xlim(0, 2 * np.pi) # changing x axis range to 0-2pi
plt.ylim(-1, 10) # y axis range to -1,10 (though -1,11 would be a better choice)

# setting axes labels
plt.ylabel('Measures of Awesomeness')
plt.xlabel('Time in ASTR 119')

plt.show() # displaying the plot


# In[4]:


np


# In[ ]:




