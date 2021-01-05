#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(0,10)
print(arr)
arr.reshape(2,5)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[3]:


import numpy as np


# In[4]:


arr1 = np.arange(10).reshape(2,5)
arr2 = np.ones(10, dtype= int).reshape(2,5)
print(arr1,arr2)
np.vstack((arr1,arr2))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[5]:


import numpy as np


# In[8]:


arr1 = np.arange(10).reshape(2,5)
arr2 = np.ones(10, dtype = int).reshape(2,5)
print(arr1,arr2)
np.hstack((arr1,arr2))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[9]:


import numpy as np


# In[10]:


arr = np.array([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]])
print(arr)
arr.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[11]:


import numpy as np


# In[12]:


arr = np.arange(15).reshape(1,3,5)
print(arr.ndim,"Dimension")
print(arr)
arr = arr.flatten()
print(arr.ndim,"Dimension")
arr


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[13]:


import numpy as np


# In[14]:


arr = np.arange(15).reshape(-1,3)
arr


# In[ ]:





# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[15]:


import numpy as np


# In[16]:


arr = np.arange(25).reshape(5,5)
print(arr)
np.square(arr)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[17]:


import numpy as np


# In[18]:


np.random.seed(123)
arr = np.random.randint(30, size = (5,6))
print(arr)
arr.mean()


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[19]:


import numpy as np


# In[20]:


np.random.seed(123)
arr = np.random.randint(30, size = (5,6))
print(arr)


# In[21]:


np.std(arr)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[22]:


import numpy as np


# In[23]:


np.random.seed(123)
arr = np.random.randint(60,size = (5,6))
print(arr)
np.median(arr)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[24]:


import numpy as np


# In[25]:


np.random.seed(123)
arr = np.random.randint(30, size = (5,6))
arr


# In[26]:


arr.T


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[27]:


import numpy as np


# In[28]:


arr = np.arange(16).reshape(4,4)
print(arr)
np.diagonal(arr)


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[29]:


import numpy as np


# In[30]:


arr = np.arange(16).reshape(4,4)
print(arr)
np.linalg.det(arr)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[31]:


import numpy as np


# In[32]:


arr = np.arange(10)
print(arr)
print(np.percentile(arr,5))
print(np.percentile(arr,95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[33]:


import numpy as np


# In[45]:


print("Original array:")
nums = np.random.randint([1,2,3,4])
print(nums)
print("\nTest whether the said array has null values or not:")
print(nums.any(0).any())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




