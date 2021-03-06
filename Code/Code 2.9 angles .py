import math
import matplotlib.pyplot as pl
x=[]
y=[]
v_x=[]
v_y=[]
t=[]
i=[]
angle_list=[]
x_list=[]
v=[]
dt=0.01
g=-9.8
v_0=700
B=0.00004
y_0 = 0.0001
for angle in range(35,56):
    i.append(0);v.append(v_0)
    v_x.append(v_0*math.cos(angle*math.pi/180))
    v_y.append(v_0*math.sin(angle*math.pi/180))
    x.append(0.0)
    y.append(0.0)
    t.append(0.0)
    while y[-1]>=0.0:
        v.append(math.sqrt(v_x[-1]**2+v_y[-1]**2))
        x_tmp=x[-1]+dt*v_x[-1]
        x.append(x_tmp)
        v_x_tmp=v_x[-1]-math.exp(-y[-1]*y_0)*B*v[-1]*v_x[-1]*dt
        v_x.append(v_x_tmp)
        y_tmp=y[-1]+dt*v_y[-1]
        y.append(y_tmp)
        v_y_tmp=v_y[-1]+dt*g-math.exp(-y[-1]*y_0)*B*v[-1]*v_y[-1]*dt
        v_y.append(v_y_tmp)
        i_tmp=i[-1]+1
        i.append(i_tmp)
        t.append(dt*i[-1]) 
    angle_list.append(angle);x_list.append(x[-1])

pl.figure(figsize=(10,6))
pl.plot(angle_list,x_list,'o')
pl.xlabel("$angle/\circ$")
pl.ylabel("x/m")
pl.show()
