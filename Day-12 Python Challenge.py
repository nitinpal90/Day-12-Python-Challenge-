#!/usr/bin/env python
# coding: utf-8

# # Day-12 Python Challenge

# # NumPy Open Source Library in Python

# # Creating a Array

# In[3]:


import numpy as np


# In[4]:


a = np.array([1,2,3,4,5]) ## Use the list to make nd.array
print(a)
print(type(a))


# In[5]:


a = np.array((1,2,3,4,5)) ## Use the Tuple to make nd.array
print(a)
print(type(a))


# # Dimension in Array

# In[7]:


arr = np.array((90)) 
print(arr)
print(type(arr))
print(arr.ndim)


# # 1 Dimension Array

# In[10]:


arr = np.array([1,2,3,4,5])
print(arr)
print(arr.ndim)


# # 2 Dimension Array

# In[13]:


a = np.array([[1,2,3],[1,2,4]])
print(a)
print(a.ndim)


# # 3 Dimension Array

# In[14]:


arr = np.array([[[1],[2]]])
print(arr)
print(arr.ndim)


# # Check Number of Dimension

# In[15]:


import numpy as np

a = np.array(10)
b = np.array([1])
c = np.array([[10]])
d = np.array([[[10]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# # Indexing in Array

# In[16]:


import numpy as np

a = np.array([1,2,3,5])
print(a[0])


# In[17]:


import numpy as np

a = np.array([1,2,3,5])
print(a[3])


# # Get the 6th, 7th and 8th Element from the following Array 

# In[19]:


import numpy as np
a = np.array([1,1.2,23,45,2,3,4,5,67,8.7,65,54,])

print("The 6th Element is: ",a[6])
print("The 7th Element is: ",a[7])
print("The 8th Element is: ",a[8])


# # Access the Element from the 2d Array

# In[22]:


import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("In 1st Row 3rd Element is: ",a[0,3])


# In[23]:


import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("In 2st Row 3rd Element is: ",a[1,3])


# # Add the 1st Element in 1st Row and Last Element in 2nd Row 

# In[27]:


import numpy as np

a = np.array([[1,2,3,4,5],[7,8,9,10,20]])

print("1st Element in 1st Row Is: ",a[0,0])
print("2nd Element in 2nd Row Is: ",a[1,4])
print("The Sum Is: ",a[0,0]+a[1,4])

