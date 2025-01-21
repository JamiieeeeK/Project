import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

angleD = [30,45,60,70.5,78,85] #all the angle
a = -9.81
dt = 0.01
# for points
closest_r = 0
closest_t = 0
furthest_r = 0
furthest_t = 0
closest_x = 0
closest_y = 0
furthest_x = 0
furthest_y = 0

fig,ax = plt.subplots()
for item in angleD: #calculate each line
    t = 0
    v = 10
    iH = 0
    thetaD = item
    thetaR = (2*(math.pi))*(thetaD/360)
    Vv = round((v*math.sin(thetaR)),10)
    Hv = round((v*math.cos(thetaR)),10)
    s = 0
    x = []
    y = []
    r = []
    time = []

    X = 0
    Y = iH
    R = 0
    r3 = 0
    r2 = 0
    r1 = 0
    
    while t <= 2.5:
        X = Hv*t

        s = Vv*dt + 0.5*a*dt**2
        Y = Y+s
        Vv = a*dt + Vv
            
        if Y >= -5:
            x.append(X)
            y.append(Y)
        time.append(t)
        t = t + dt

        R = math.sqrt(X**2 + (Y-iH)**2) #
        r.append(R)

        r3 = r2
        r2 = r1
        r1 = R
        if r2>r3 and r2>r1: #furthest point
            furthest_r = r2
            furthest_t = t-dt
            furthest_x = X
            furthest_y = Y
        elif r2<r3 and r2<r1: #closest point
            closest_r = r2
            closest_t = t-dt
            closest_x = X
            closest_y = Y
            
    plt.figure(1)
    ax.plot(time,r,markersize=15,label=f"θ ={thetaD}°") #plot each line
    plt.legend()
    if closest_r != 0: #plot pointss
        ax.plot(closest_t, closest_r, '*')
        plt.figure(2)
        plt.plot(closest_x, closest_y, '*')
    if furthest_r != 0:
        ax.plot(furthest_t, furthest_r, '*')
        plt.figure(2)
        plt.plot(furthest_x, furthest_y, '*')
    plt.figure(2)
    plt.plot(x, y, markersize=15, label=f"θ ={thetaD}°") #plot each line
    plt.legend()

plt.figure(1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xlabel("time / s")
plt.ylabel("range r / m")
plt.title("Projectile model motion challenge 7")
plt.grid()

plt.figure(2)
#plt.set_position('axes', 0)
plt.yticks(np.arange(-5,6,2.5))
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.title("Projectile model motion challenge 7")
plt.grid()
plt.show()









    
