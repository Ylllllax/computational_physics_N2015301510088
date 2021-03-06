import numpy as np
import matplotlib.pyplot as plt

class THREE(object):
    def __init__(self, _mJ):
        self.dt, self.time=0.001, 100
        self.n=int(self.time/self.dt)
        self.GMS= 4*(np.pi)**2
        self.GMJ, self.GME = _mJ*self.GMS/1000, self.GMS/330000
        self.xE, self.yE, self.vxE, self.vyE = [1], [0], [0], [np.sqrt(self.GMS)]
        self.xJ, self.yJ, self.vxJ, self.vyJ = [5.2], [0], [0], [np.sqrt(self.GMS/5.2)]
        self.xS, self.yS, self.vxS, self.vyS = [0], [0], [0], [-_mJ*np.sqrt(self.GMS/5.2)/1000]
        
    def calculate(self):
        for i in range(self.n):
            self.rSE=np.sqrt((self.xE[-1]-self.xS[-1])**2+(self.yE[-1]-self.yS[-1])**2)
            self.rSJ=np.sqrt((self.xJ[-1]-self.xS[-1])**2+(self.yJ[-1]-self.yS[-1])**2)
            self.rEJ=np.sqrt((self.xE[-1]-self.xJ[-1])**2+(self.yE[-1]-self.yJ[-1])**2)
            
            self.vxE.append(self.vxE[-1]-self.dt*(self.GMS*(self.xE[-1]-self.xS[-1])/self.rSE**3)-self.dt*(self.GMJ*(self.xE[-1]-self.xJ[-1])/self.rEJ**3))
            self.vyE.append(self.vyE[-1]-self.dt*(self.GMS*(self.yE[-1]-self.yS[-1])/self.rSE**3)-self.dt*(self.GMJ*(self.yE[-1]-self.yJ[-1])/self.rEJ**3))
            self.vxJ.append(self.vxJ[-1]-self.dt*(self.GMS*(self.xJ[-1]-self.xS[-1])/self.rSJ**3)-self.dt*(self.GME*(self.xJ[-1]-self.xE[-1])/self.rEJ**3))
            self.vyJ.append(self.vyJ[-1]-self.dt*(self.GMS*(self.yJ[-1]-self.yS[-1])/self.rSJ**3)-self.dt*(self.GME*(self.yJ[-1]-self.yE[-1])/self.rEJ**3))
            self.vxS.append(self.vxS[-1]-self.dt*(self.GMJ*(self.xS[-1]-self.xJ[-1])/self.rSJ**3)-self.dt*(self.GME*(self.xS[-1]-self.xE[-1])/self.rSE**3))
            self.vyS.append(self.vyS[-1]-self.dt*(self.GMJ*(self.yS[-1]-self.yJ[-1])/self.rSJ**3)-self.dt*(self.GME*(self.yS[-1]-self.yE[-1])/self.rSE**3))
            
            self.xE.append(self.xE[-1]+self.dt*self.vxE[-1])
            self.xJ.append(self.xJ[-1]+self.dt*self.vxJ[-1])
            self.xS.append(self.xS[-1]+self.dt*self.vxS[-1])
            self.yE.append(self.yE[-1]+self.dt*self.vyE[-1])
            self.yJ.append(self.yJ[-1]+self.dt*self.vyJ[-1])
            self.yS.append(self.yS[-1]+self.dt*self.vyS[-1])
                        
    def plot_trajectory(self,_ax):
        _ax.plot(self.xE,self.yE,'-b',label='Earth')
        _ax.plot(self.xJ,self.yJ,'-r',label='Jupiter')
        _ax.plot(self.xS,self.yS,'-g',label='Sun')
        
fig= plt.figure(figsize=(14,7))
ax1=plt.subplot(121)
ax2=plt.subplot(122)

'''
comp1=THREE(1)
comp1.calculate()
comp1.plot_trajectory(ax1)
comp2=THREE(10)
comp2.calculate()
comp2.plot_trajectory(ax2)

ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax1.set_xlim(-6.0,6.0)
ax1.set_ylim(-6.0,6.0)
ax1.set_xlabel(r'$x (AU)$',fontsize=14)
ax1.set_ylabel(r'$y (AU)$',fontsize=14)
ax1.set_title('3-body simulation Earth plus Jupiter:'+r' $M_J$',fontsize=14)
ax2.set_xlim(-6.0,6.0)
ax2.set_ylim(-6.0,6.0)
ax2.set_xlabel(r'$x (AU)$',fontsize=14)
ax2.set_ylabel(r'$y (AU)$',fontsize=14)
ax2.set_title('3-body simulation Earth plus Jupiter:'+r' $10M_J$',fontsize=14)
plt.show()
'''
    
comp1=THREE(100)
comp1.calculate()
comp1.plot_trajectory(ax1)
comp2=THREE(1000)
comp2.calculate()
comp2.plot_trajectory(ax2)

ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
ax1.set_xlim(-6.0,6.0)
ax1.set_ylim(-6.0,6.0)
ax1.set_xlabel(r'$x (AU)$',fontsize=14)
ax1.set_ylabel(r'$y (AU)$',fontsize=14)
ax1.set_title('3-body simulation Earth plus Jupiter:'+r' $100M_J$',fontsize=14)
ax2.set_xlim(-80.0,80.0)
ax2.set_ylim(-30.0,30.0)
ax2.set_xlabel(r'$x (AU)$',fontsize=14)
ax2.set_ylabel(r'$y (AU)$',fontsize=14)
ax2.set_title('3-body simulation Earth plus Jupiter:'+r' $1000M_J$',fontsize=14)
plt.show()
