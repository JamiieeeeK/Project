import matplotlib.pyplot as plt
import matplotlib as mpl
import math

g = 9.81
a = -9.81
cDrag = 0.43 #float(input("Drag coefficient cD: "))
aDensity = 1 #float(input("Air Density/kgm^-3: "))
oMass = 0.1 #float(input("Object Mass/kg: "))
oCSArea = 0.007854 #float(input("Object's cross sectional Area: "))
arFactor_k = float((0.5*cDrag*aDensity*oCSArea)/oMass) #calculate the air resistance factor
print(arFactor_k, '\n')
thetaD = float(input('Launch angle: '))
thetaR = 2*(math.pi)*(thetaD/360)
iv = int(input('Initial speed: '))
dt = 0.01
t = 0
iHv = iv*math.cos(thetaR) #initial horizontal velocity
iVv = iv*math.sin(thetaR) #initial vertical velocity
iHeight = float(input("The original height : "))
vHeight = iHeight
hDistance = 0

v = iv
Hv = iHv
Vv = iVv

NHv = iHv #normal, without air resistance
NVv = iVv
s = 0
Ny = iHeight
Nx = 0


ARx = []
ARy = []
NX = []
NY = []


X = 0
Y = 0
n = 1

Ha = (-1*Hv/v)*arFactor_k*(v**2)
Va = -g-((Vv/v)*arFactor_k*(v**2))
#air resistant-------
while vHeight > 0:

    #Ha = ((-1*Hv)/v)*arFactor_k*(v**2)
    #Va = -g-((Vv/v)*arFactor_k*(v**2))
    
    X = Hv*dt + 0.5*Ha*dt**2
    hDistance = hDistance + X
    Y = Vv*dt + 0.5*Va*dt**2
    vHeight = vHeight + Y

    Hv = Hv + Ha*dt
    Vv = Vv + Va*dt

    v = math.sqrt((Hv**2) + (Vv**2))
    
    ARx.append(hDistance)
    ARy.append(vHeight)

    t = t+dt
    n += 1

#Normal -------
while Ny > 0:
    Nx = Nx + NHv*dt
    Ny = Ny + NVv*dt + 0.5*a*dt**2
    NVv = a*dt + NVv
    NX.append(Nx)
    NY.append(Ny)

    
    
    
fig,ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')    

ax.plot(NX, NY, '.', markersize=3, c='royalblue', label='Without resistance')
ax.plot(ARx, ARy,'.', markersize=2, c='firebrick', label='Air resistance')
ax.legend()


plt.xlabel(" horizontal distance/m ")
plt.ylabel(" vertical distance/m ")
plt.title("Projectile model motion challenge 9")
plt.grid()
plt.show()

    
