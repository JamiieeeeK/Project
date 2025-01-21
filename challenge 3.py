import math
from matplotlib import pyplot as plt
import numpy as np

fig,ax = plt.subplots()

#initialises variables
a = -9.81
dt = 0.01
t = 0
s = 0
X = 1000 
Y = 300
u = 150 

#high ball ------
high_x = np.linspace(0,1000,200)
high_y = (high_x*(math.tan(1.3254))) - (9.81*(1+(math.tan(1.3254))**2)*(high_x**2))/(2*(u**2))

ax.plot(high_x, high_y,'.', markersize='3', label='high ball')


#low ball ------
low_x = np.linspace(0,1000,100)
low_y = (low_x*(math.tan(0.5368))) - (9.81*(1+(math.tan(0.5368))**2)*(low_x**2))/(2*(u**2))

ax.plot(low_x, low_y,'.', markersize='3', label='low ball')


#minimum speed -------
min1 = (Y + math.sqrt(X**2 + Y**2))/X
min_angleR = math.atan(min1)
min_angleD = math.degrees(min_angleR)
print("minimum speed angle:" , round(min_angleD,2))

minU = (math.sqrt(9.81))* (math.sqrt(Y+ (math.sqrt(X**2 + Y**2))))
print("minimum speed: " , round(minU,2))

VminU = round((minU*math.sin(min_angleR)),5)
HminU = round((minU*math.cos(min_angleR)),5)

minX = []
minY = []

Height = 0
vDistance = Height
hDistance = 0

while hDistance <= 1000:
    hDistance = HminU*t
    minX.append(hDistance)

    s = VminU*t + 0.5*a*t**2
    vDistance = Height + s
    minY.append(vDistance)

    t = t + dt


ax.plot(minX, minY, markersize='10', label='Min u')
#----------------------


ax.plot(X,Y,'*', label='target')
ax.legend()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')   
plt.xlabel(" x horizontal distance/m ")
plt.ylabel(" y vertical distance/m ")
plt.title("Projectile model motion challenge 3")

plt.show()
    
