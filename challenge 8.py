import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

fig,ax = plt.subplots()

a = -9.81
t = 0
dt = 0.01
c = 0.7
v = float(input('The initial velocity of the projectile: '))
thetaD = float(input('The angle the object was projected at: '))
thetaR = (2*(math.pi))*(thetaD/360)
bounce = 0
Vv = round((v*math.sin(thetaR)),10)
Hv = round((v*math.cos(thetaR)),10)

Y = int(input('The original height: '))
s = 0
i = True

x = []
y = []

X = 0
while i==True:
    X = Hv*t

    s = Vv*dt + 0.5*a*dt**2
    Y = Y + s
    Vv = a*dt+Vv

    t = t+dt
    
    if Y <= 0:
        Vv = Vv*c*-1 #change the direction of the velocity
        Y = 0
        if Vv<=1: #stop when vertical velocity fall below 1
            i = False
        else:
            bounce += 1
    x.append(X)
    y.append(Y)
    
print (t, bounce)

plt.plot(x, y,markersize=15)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlabel("horizontal distance/m")
plt.ylabel("vertical distance/m")
plt.title("Projectile model motion challenge 8")

plt.show()
