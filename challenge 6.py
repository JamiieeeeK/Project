import math
from matplotlib import pyplot as plt

fig,ax = plt.subplots()
#initialises variables
a = -9.81
dt = 0.01
At = 0
u = float(input("Launch speed: "))  
angle_d = float(input("Launch angle: "))
angle_r = math.radians(angle_d)  
iHeight = float(input("Launch height: "))
hDistance = 0
s = 0
vDistance = iHeight

vVelocity = round((u*math.sin(angle_r)),5)
hVelocity = round((u*math.cos(angle_r)),5)

x = []
y = []
x1 = 0
x2 = 0
y1 = iHeight
y2 = iHeight
temp = 0
Distance = 0

while vDistance > 0:
    hDistance = hVelocity*At
    x.append(hDistance)

    s = vVelocity*At + 0.5*a*At**2
    vDistance = iHeight + s
    y.append(vDistance)

    x2 = x1
    x1 = hDistance

    y2 = y1
    y1 = vDistance


    temp = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    Distance = Distance + temp

    At = At + dt
Distance = Distance - temp
At = At-dt


ax.plot(x,y,label=f"θ ={angle_d}°  T ={round(At,2)}s  Distance ={round(Distance,2)}m")

#Max Range ---------
Distance = 0
MaxAngle_r = math.asin(1/math.sqrt(2+2*(-1*a)*iHeight/u**2))
MaxAngle_d = math.degrees(MaxAngle_r)
hDistance = 0
vDistance = iHeight
print(MaxAngle_r)

vVelocity = round((u*math.sin(MaxAngle_r)),5)
hVelocity = round((u*math.cos(MaxAngle_r)),5)

Max_X = []
Max_Y = []
Bt = 0
x1 = 0
x2 = 0
y1 = iHeight
y2 = iHeight
temp = 0
while vDistance > 0:
    hDistance = hVelocity*Bt
    Max_X.append(hDistance)

    s = vVelocity*Bt + 0.5*a*Bt**2
    vDistance = iHeight + s
    Max_Y.append(vDistance)

    # Calculate the Distance -------
    x2 = x1
    x1 = hDistance
    y2 = y1
    y1 = vDistance
    temp = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    Distance = Distance + temp
    
    Bt = Bt + dt
Distance = Distance - temp
Bt = Bt-dt

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')    


ax.plot(Max_X, Max_Y,'.',markersize=4,label=f"θmax ={round(MaxAngle_d,1)}°  T ={round(Bt,2)}s  Distance ={round(Distance,2)}m")
ax.legend()
plt.xlabel(" horizontal distance/m ")
plt.ylabel(" vertical distance/m ")
plt.title("Projectile model motion challenge 4")

plt.show()
