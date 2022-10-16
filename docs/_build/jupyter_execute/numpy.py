#!/usr/bin/env python
# coding: utf-8

# # `NumPy` 
# 
# ## What is Numpy?
# Package
# 
# ## Differences between NumPy arrays and standard Python sequences (e.g., lists)
# Table on column numpy the other lists
# https://numpy.org/devdocs/user/whatisnumpy.html
# - Numpy can only contain the same type of data items e.g. you cannot have one item int and another str
# - 
# 
# 
# ### Advantages over lists
# 
# * Efficient - uses less memory to data items than Python lists
# * NumPy uses a **vectorised** code system for arrays so no need to use loops to apply operations on each data item. It facilitates mathematical and other operations on data structures:
#     * Fewer lines of code
#     * Easier to read, resembles mathematical notation.
# 
# `````{tab-set}
# ````{tab-item} Standard Python
# ```{code-block}
# c = []
# for i in range(len(a)):
#     c.append(a[i]*b[i])
# ```
# 
# ````
# 
# ````{tab-item} NumPy
# ```{code-block}
# c = a * b
# ```
# ````
# `````
# 
# * Fast
# benchmark example above>
# 
# 
# 
# [//]: # (#```{admonition})
# 
# [//]: # (#:class: tip)
# 
# [//]: # ()
# [//]: # (#Timing of numpy versus normal list)
# 
# [//]: # ()
# [//]: # (#`````)
# 
# 
# Because we are using the Anaconda distribution, numpy should be already installed in our system.  You can check this in the Python Packages tab
# in PyCharm.  
# However to use numpy functions we need to import it in the code.  The widely adopted convention is as follows:

# In[1]:


import numpy as np


# ## Creating NumPy arrays
# A numpy array is the main datastructure of NumPy.  
# 
# We can create a numpy array from a Python list eg.
# 
# l = [55, 92, 110, 66, 75, 45, 40, 57, 55, 62]
# 
# a = np.array[l]
# 
# This creates an array of type **`ndarray`** in memory as we can see from PyCharm's variable pane.  `ndarray` is short for N-dimensional array 
# which means any number of dimensions.  
# * 1-D (one-dimensional) array is also called a **vector** and is similar to a Python list.
# * 2-D (two-dimensional) array is also called a **matrix**.
# * 3-D or higher dimensional arrays are also known as **tensor**.
# In this practical we will focus at vectors (1-D arrays) only.  
# 
# 
# Creating an array of vectors filled with zeros or ones
# `np.zeros()` method >> [Documentation to np.zeros() method](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
# 
# `np.ones()` method >> [Documentation to np.ones() method](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)
# 
# `np.arange()` method >> [Documentation to np.arange()](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
# We can also call the `np.arange()` method to initialise the ndarray with a sequential range of data items.  The np.arange() method 
# takes also as an argument a start, stop and step arguments that can be handy if you have a specific range in mind.
# 
# 
# `np.linspace()` method >> [Documentation to np.linspace()](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
# Generates num evenly spaced sequence of numbers from start to stop.  The default value of num is 50, if you
# want to change this you have to specify this new value in num.  for example, 
# np.linspace(start, stop, number of samples to generate (default is 50))
# 
# <maybe draw rectangle visuals of contents of the below and transform all these into a table:
# method, description, example>

# In[2]:


#create an array of 3 zeros
print(np.zeros(3))

#create an array of 3 ones
print(np.ones(3))


np.arange(3)
np.arange(start=1,stop=8,step=2)
or 
np.arange(1,8,2)

np.linspace(-5, 5, 11)


# a.ndim # get the number of dimensions of the array (returns 1) - we are only working with 1D arrays here but it could be more.
# a.size #returns 3 - returns the total number of data items in the ndarray.
# 
# 
# 
# 
# 
# ## NumPy data types
# NumPy is built from a low level language, C, because of this it inherits some features that are normally associated with low level languages.
# 
# While the size of Python data types we have seen so far offer flexibility, that is, they can grow to accommodate numbers of different sizes
# (within the machine's memory constraints), NumPy datatypes are have fixed sizes.
# Python data types are equivalent to the corresponding numpy equivalent
# 
# int np.int_
# bool np.bool_
# float np.float_
# str np.str_
# 
# Furthermore, in NumPy an int has several dtypes: int8, int16, int32, int64.  int8 means that a number created as int8 will be stored in 8 bits or 1 byte of memory.  And that is 
# why the larger the number of bits allocated to a number, the larger the range of numbers can be held.
# 
# 
# 
# Type      Number Capacity
# 
#    int8      (-128 to 127)
# 
#    Int16 -- (-32,768 to +32,767)
# 
#    Int32 -- (-2,147,483,648 to +2,147,483,647)
# 
#    Int64 -- (-9,223,372,036,854,775,808 to +9,223,372,036,854,775,807)
# 
# When creating a list, NumPy automatically detects the type of data the list is made up of and allocates a data type that 
# fits your list based on several factors, including the computer's architecture.  Because of this, we do not need to worry about 
# which NumPy data type to allocate to our data types as NumPy does that automatically for us.  In the case when we need to 
# specify the dtype argument in NumPy functions, in this course we will be using the standard Python data types rather than the NumPy data types.
# 
# 
# <exersice>
# 
# 
# create a NumPy array from l
# 
# create a NumPy array from l of type float
# 
# using this list l create a string version of numpy array
# np.array(l, dtype=str)  
# Note:  U is for unicode 6 is the number of characters
# 
# =============
# 
# # Other operations
# 
# adding items
# 
# np.sort  example. sort in ascending order np.sort(a)
# sort in descending order: np.flip(np.sort(a))
# np.concatentate: joins two lists together
# 
# c = [1,2,3]
# d = [4,5,6]
# np.concatenate((c,d))
# c and d can be of type ndarray as well
# 
# 
# ## Slicing NumPy arrays
# To get the value of the specific data items in the array we do that in the same way we do in Python listss: by using the square 
# brackets e.g. 
# a[2]
# a[2:5]
# a[1:8:2]
# 
# # Broadcasting
# 
# One of the main differences between standard Python data sequences such as lists and NumPy arrays is that it uses a vectorised system 
# which allows us to perform operations over all the ndarray object using one line of code as opposed to  using a loop as we do 
# with lists.
# 
# #Extract items in the list that are >60
# a > 60
# returns a list of True and False; True if the data item is > 60, and False otherwise.
# 
# To get the actual data items we have to use our comparison statement inside the [] as essentially we want to slice our 
# ndarray based on a condition:
# a[a > 60]
# 
# This is similar to the way we extract items from vectors in R.  
# 
# You can combine multiple comparison statements using the & (and) and | (or) logical operators
# # get the marks that are > 60 and < 90.  
# a[(a > 60)  & (a < 90)]
# 
# 
# mathematical operations
# 
# # Mathematical Functions
# There are several functions that oers
# 
# https://numpy.org/doc/stable/reference/routines.math.html
# 
# ### Random sampling
# 
# To generate a random number we first call default_rng() method to create an instance of Generator

# In[ ]:


import numpy as np

seed = 12345
rng = np.random.default_rng(seed=seed)
#generate 3 random integers between 1 and 10 (excluded)
rints = rng.integers(low=1, high=10, size=3)
print(rints)

# generate 3 random decimal numbers in the range[0,1]
rfloat = rng.random(3)
print(rfloat)


# You can also draw samples from a distribution.  For example
# For a whole list of distributions see [here](https://numpy.org/devdocs/reference/random/generator.html#distributions)
# 
# #draw 5 samples from the normal distribution where mean=0 and standard deviation is 0.1
# mu, sigma = 0, 0.1 # mean and standard deviation
# sample_normal = rng.normal(mu, sigma, 5)
# print(sample_normal)