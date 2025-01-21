import math
from matplotlib import pyplot as plt

#initialises variables
a = -9.81
dt = 0.01
t = 0
u = float(input("Launch speed: "))
angle = math.radians(float(input("Launch angle: "))) 
iHeight = float(input("Launch height: "))
hDistance = 0
s = 0
vDistance = iHeight
step = 0 #points

vVelocity = round((u*math.sin(angle)),5)
hVelocity = round((u*math.cos(angle)),5)

x = []
y = []
dx = []
dy = []

while vDistance > 0:
    hDistance = hVelocity * t
    x.append(hDistance)

    s = vVelocity*t + 0.5*a*t**2
    vDistance = iHeight + s
    y.append(vDistance)

    
    if round(t,1) == step: #
        dx.append(hDistance)
        dy.append(vDistance)
        step = round(step + 0.1,1)

    t = t + dt

    
#calculate the apogee
vMaxHeight = -1*(vVelocity**2)/(2*a)
MaxTime = round(math.sqrt((-2*vMaxHeight)/a),5)
hMaxDistance = MaxTime * hVelocity
vMaxHeight = vMaxHeight + iHeight



fig,ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')    


plt.plot(x,y, c='darkblue')
steps = ax.plot(dx,dy,'.', c='cornflowerblue', label='y vs x')
points = ax.plot(hMaxDistance,vMaxHeight, '*', c='orange', label='apogee')
ax.legend()

plt.xlabel(" horizontal distance/m ")
plt.ylabel(" vertical distance/m ")
plt.title("Projectile model motion challenge 2")
plt.grid()
plt.show()

