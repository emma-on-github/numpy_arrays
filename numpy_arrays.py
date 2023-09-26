#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Example 1

# import numpy
import numpy as np

# create an array using numpy module random, random function, specifying size - 2 rows with 4 columns
np.random.random((2,4))


# Example 2

# import numpy
import numpy as np

# create an array using numpy module zeros, specifying shape of array - 7 rows, 5 columns
np.zeros((7,5))


# Example 3

# import numpy
import numpy as np

# create an array from a list
months_array = np.array(['Jan', 'Feb', 'March', 'Apr', 'May'])

# print items in the array starting at index 0 to 5, but every 2nd index position
print(months_array[0:5:2])


#Example 4

# import numpy
import numpy as np

# create two lists months and prices
months = [1, 2, 3]
prices = [238.11, 237.81, 238.91]

# create an array from lists month and prices
cpi_array = np.array([months, prices])

# print array
print(cpi_array)


# Example 5

# import numpy
import numpy as np

# create a list prices
prices = [238.11, 237.81, 238.91]

# create an array from list prices
prices_array = np.array(prices)

# print the array mean and standard deviation
print(np.mean(prices_array))
print(np.std(prices_array))


# Example 6

# import numpy and pyplot
import numpy as np
from matplotlib import pyplot as plt

# create scatter plot, generate values within start and stop numbers for x and y 
plt.scatter(np.arange(0, 7),
            np.arange(-3,4))

# display the scatter plot
plt.show()


# Example 7

# import numpy and pyplot
import numpy as np
from matplotlib import pyplot as plt

# create an array 
rgb = np.array([[[255, 0, 0],[255, 0, 0],[255, 0, 0]],
                [[0, 255, 0],[0, 255, 0],[0, 255, 0]],
                [[0, 0, 255],[0, 0, 255],[0, 0, 255]]])

# display data as image
plt.imshow(rgb)

# display the plot
plt.show()


#Example 8

# import numpy and pyplot
import numpy as np
from matplotlib import pyplot as plt

# create an array 
rgb = np.array([[[255, 0, 0],[255, 255, 0],[255, 255, 255]],
                [[255, 0, 255],[0, 255, 0],[0, 255, 255]],
                [[0, 0, 0],[0, 255, 255],[0, 0, 255]]])

# display data as image
plt.imshow(rgb)

# display the plot
plt.show()


# In[ ]:




