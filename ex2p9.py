import numpy as np
import random

#first part
#print(np.random.normal(5,2,10))

#second part
def findPi(npoints=1000):
    allp=[]
    goodp=[]
    for i in range(0,npoints):
        x=random.random()
        y=random.random()
        allp.append((x,y))
        if (x-0.5)**2+(y-0.5)**2<=0.25:
            goodp.append((x,y))
    #print(allp)
    #print(goodp)
    newpi=4*len(goodp)/npoints
    return newpi

#change amount of pi's
'''
a=[findPi() for i in range(0,10)]
print(np.mean(a),np.std(a))

a=[findPi() for i in range(0,100)]
print(np.mean(a),np.std(a))

a=[findPi() for i in range(0,1000)]
print(np.mean(a),np.std(a))
'''
#increase number of points,std goes down
a=[findPi(10) for i in range(0,100)]
print(np.mean(a),np.std(a))

a=[findPi(100) for i in range(0,100)]
print(np.mean(a),np.std(a))

a=[findPi(1000) for i in range(0,100)]
print(np.mean(a),np.std(a))
