import math
from matplotlib import pyplot as plt

#initialises variables
a = -9.81
dt = 0.01
t = 0
u = float(input("Launch speed: "))
angle = math.radians(float(input("Launch angle: ")))  
Height = float(input("Launch height: ")) 
hDistance = 0
s = 0
vDistance = Height

#seperates horizontal and vertical components of initial velocity 
vVelocity = round((u*math.sin(angle)),5)
hVelocity = round((u*math.cos(angle)),5)

x = []
y = []

while vDistance > 0:
    hDistance = hVelocity*t
    x.append(hDistance)

    s = vVelocity*t + 0.5*a*t**2
    vDistance = Height + s
    y.append(vDistance)

    t = t + dt

fig,ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')    

plt.plot(x,y)
plt.xlabel(" horizontal distance/m ")
plt.ylabel(" vertical distance/m ")
plt.title("Projectile model motion challenge 1")
plt.show()
