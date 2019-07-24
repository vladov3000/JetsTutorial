import numpy as np
import random
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

def findz():
    #PDF(z)= 1/(z+1) and range is [0,1]
    #CDF(z)=ln(z+1) so range is [0,ln(2)]
    y=random.random()*np.log(2)
    return np.e**y-1

def findtheta():
    #PDF(z)=1/(z+1) and range is [0,pi/2]
    #CDF(z)=ln(z+1) so range is [0,ln(pi/2+1)]
    y=random.random()*np.log(np.pi/2+1)
    #return np.e**y-1
    return np.pi/6

def findazu():
    return random.random()*np.pi

class Fmv(): #four-momentum vector
    def __init__(self,E,px,py,pz,azuangle=0,polarangle=0):
        self.E=E
        self.px=px
        self.py=py
        self.pz=pz
        self.azuangle=azuangle
        self.polarangle=polarangle

    def __str__(self):
        return str((self.E,self.px,self.py,self.pz))

    def getP(self): #returns magnitude
        return (self.px**2+self.py**2+self.pz**2)**0.5

    def getV(self): #returns magnitude and components
        p=(self.px**2+self.py**2+self.pz**2)**0.5
        v=2*self.E/p
        vx=v*np.cos(self.azuangle)
        vy=v*np.sin(self.azuangle)
        vz=v*np.cos(self.polarangle)
        return (v,vx,vy,vz)


def findPseudoJets(fmv,x0=0,y0=0,z0=0,level=0):

    #travel time
    t=1

    #energy scale threshold
    Ecrit=10

    #current travel direction
    #angle=np.arctan(py/px)

    if fmv.E<=Ecrit:
        return [fmv]

    p=fmv.getP()
    E=fmv.E
    v=fmv.getV()

    x1=v[1]*t+x0
    y1=v[2]*t+y0
    z1=v[3]*t+z0
    coordinates.append((x0,y0,z0,x1,y1,z1))

    theta=findtheta()
    azu=findazu()

    z=findz()
    E1=E*z
    E2=E-E1
    p1=p*np.sqrt(z)
    p2=p-p1

    p1x=p1*np.cos(fmv.azuangle)
    p1y=p1*np.sin(fmv.azuangle)
    p1z=p1*np.cos(fmv.polarangle+theta)
    fmv1=Fmv(E1,p1x,p1y,p1z,fmv.azuangle,fmv.polarangle+theta)

    p2x=p2*np.cos(fmv.azuangle)
    p2y=p2*np.sin(fmv.azuangle)
    p2z=p2*np.cos(fmv.polarangle-theta)
    fmv2=Fmv(E2,p2x,p2y,p2z,fmv.azuangle,fmv.polarangle+theta)

    #plot energy/momentum/velocity
    #plt.scatter(level,E)
    #plt.scatter(level,p)
    #plt.scatter(level,v[0])

    return findPseudoJets(fmv1,x1,y1,z1,level+1)+findPseudoJets(fmv2,x1,y1,z1,level+1)

'''
#testing generating z's
zs=[findtheta() for i in range(0,100000)]
plt.hist(zs)
'''

coordinates=[]

Pa=findPseudoJets(Fmv(1000,10,20,20))
#Pb=findPseudoJets(100,-10,20,20)
#P=Pa+Pb
print(Pa)
#print(coordinates)


fig = plt.figure()
ax = plt.axes(projection='3d')

#displacement vectors
for vector in coordinates:
    ax.plot3D([vector[0], vector[3]], [vector[1], vector[4]],[vector[2], vector[5]])#unfold list into plot's arguments

plt.show()
