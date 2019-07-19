import random
import numpy

#first case
a=[]
for i in range(0,1000):
    a.append(random.random())
h=numpy.histogram(a)
#print(h)

#second case
a1=[]
a1=[i*10+5 for i in a]
h1=numpy.histogram(a1)
print(h1)
