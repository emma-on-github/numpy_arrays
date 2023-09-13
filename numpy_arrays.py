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

# import numpy and pyplot
import numpy as np
from matplotlib import pyplot as plt

# create scatter plot, generate values within start and stop numbers for x and y 
plt.scatter(np.arange(0, 7),
            np.arange(-3,4))

# display the scatter plot
plt.show()


# Example 4

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


#Example 5

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




