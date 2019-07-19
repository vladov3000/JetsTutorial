import numpy as np
import random
from matplotlib import pyplot as plt
from math import e

#first part
#print(np.random.normal(5,2,10))

#second part
#PFD=e^(-x) with range of [0,5]
#CDF is -e^(-x) so yrange is [-1,-e^(-5)]
ys=[]

for i in range(0,1000):
    ys.append(random.random()*(-e**(-5)+1)-1)
#print(ys)

#inverse CDF is -ln(-y)
xs=[-np.log(-y) for y in ys]
#print(xs)

#plot to check if it looks ok
plt.hist(xs)
plt.title("histogram")
plt.show()
