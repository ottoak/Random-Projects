# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:01:49 2020

@author: Alex
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class diffusion_eqn:
    
    def __init__(self, Nx_, T, L=1):
        
        self.Nx=Nx_
        self.x = np.linspace(0, L, Nx_+1)
        self.Nt = int(2*Nx_**2*T/L)
        self.t = np.linspace(0, T, self.Nt+1)
        
        self.dx = self.x[1]-self.x[0]
        self.dt = self.t[1]-self.t[0]
        self.F = self.dt/(self.dx**2)
        
        self.u = np.zeros(Nx_+1)
        self.u_n = np.zeros(Nx_+1)
        
    def init_cond(self, I):
        for i in range(0, self.Nx+1):
            self.u_n[i]=I(self.x[i])
            
    def solve(self):
        
        fig, ax  = plt.subplots()
        plot, = ax.plot(self.x,self.u_n)
        txt = ax.text(0.5,0.25,'t=0 s')
        
        for n in range(0, self.Nt):
            for i in range(1, self.Nx):
                self.u[i] = self.u_n[i]+self.F*(self.u_n[i-1]-2*self.u_n[i]+self.u_n[i+1])
                
            self.u[0]=0
            self.u[self.Nx]=0
            
            self.u_n[:] = self.u
            
            plot.set_ydata(self.u)
            txt.set_text('t='+'%.3f'%(n*self.dt)+' s')
            
            fig.canvas.draw()
            fig.canvas.flush_events()
            
    

f = lambda x: np.exp(-(x-0.5)**2/0.01)
                 
test = diffusion_eqn(50,0.5)
test.init_cond(lambda x: f(x)-f(1))
test.solve()


            
        
        
    
        