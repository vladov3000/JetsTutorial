import numpy as np
import random
from matplotlib import pyplot as plt

def findz():
    #PDF(z)= 1/(z+1) and range is [0,1]
    #CDF(z)=ln(z+1) so range is [0,ln(2)]
    y=random.random()*np.log(2)
    return np.e**y-1

def findtheta():
    #PDF(z)=1/(z+1) and range is [0,pi/2]
    #CDF(z)=ln(z+1) so range is [0,ln(pi/2+1)]
    y=random.random()*np.log(np.pi/2+1)
    return np.e**y-1
    #return np.pi/6

def findPseudoJets(E,px,py,x0=0,y0=0,level=0,angle=0):

    #travel time
    t=1

    #energy scale threshold
    Ecrit=10

    #current travel direction
    #angle=np.arctan(py/px)

    if E<=Ecrit:
        return [(E,px,py)]

    p=(px**2+py**2)**0.5

    v=2*E/p
    vx=v*np.cos(angle)
    vy=v*np.sin(angle)

    x1=vx*t+x0
    y1=vy*t+y0
    coordinates.append((x0,y0,x1,y1))

    theta=findtheta()
    newAngle1=angle+theta
    newAngle2=angle-theta

    z=findz()
    E1=E*z
    E2=E-E1
    #this may be wrong:
    p1=p*np.sqrt(z)
    p2=p-p1

    p1x=p1*np.cos(newAngle1)
    p1y=p1*np.sin(newAngle1)
    p2x=p2*np.cos(newAngle2)
    p2y=p2*np.sin(newAngle2)

    #plot energy/momentum/velocity
    #plt.scatter(level,E)
    #plt.scatter(level,p)
    #plt.scatter(level,v)

    return findPseudoJets(E1,p1x,p1y,x1,y1,level+1,newAngle1)+findPseudoJets(E2,p2x,p2y,x1,y1,level+1,newAngle2)

'''
#testing generating z's
zs=[findtheta() for i in range(0,100000)]
plt.hist(zs)
'''

coordinates=[]

Pa=findPseudoJets(100,30,40)
Pb=findPseudoJets(100,-30,40)
P=Pa+Pb
print(P)
#print(coordinates)


#displacement vectors
for vector in coordinates:
    plt.plot([vector[0], vector[2]], [vector[1], vector[3]]) #unfold list into plot's arguments

plt.show()
