# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:39:19 2020

@author: Alex
"""
import numpy as np

class simplex_algo:
    
    def __init__(self, Objective_Func, **Constraints):
        
        self.O=Objective_Func
        self.A_eq = Constraints.get('A_eq')
        self.A_ineq = Constraints.get('A_ineq')
        self.b_eq = Constraints.get('b_eq')
        self.b_ineq = Constraints.get('b_ineq')
        
        if (self.A_eq==None and self.A_ineq==None):
            raise Exception('No constraint matrices found. Please make sure to enter them as matrices, A_eq=[[...], ...] and/or A_ineq=[[...], ...]')
  
        self.T = []
        if self.A_ineq!=None:
            if (self.b_ineq==None):
                raise Exception('You forgot the vector b_ineq for A_ineq*x=b_ineq!')
                
            l=len(self.A_ineq)
            for i, x in enumerate(self.A_ineq):
                self.T.append(x+[1 if j==i else 0 for j in range(0,l)]+[self.b_ineq[i]])
             
            if self.A_eq!=None:
                if (self.b_eq==None):
                    raise Exception('You forgot the vector b_eq for A_eq*x=b_eq!')
                for i, x in enumerate(self.A_eq):
                    self.T.append(x+[0]*l+[self.b_eq[i]])
                    
            self.T.append(self.O+[0]*l+[0])
            
        else:
            if (self.b_eq==None):
                    raise Exception('You forgot the vector b_eq for A_eq*x=b_eq!')
            for i, x in enumerate(self.A_eq):
                self.T.append(x+[self.b_eq[i]])
                
            self.T.append(self.O+[0])
            
        self.T=np.array(self.T)
        print(self.T)
            
        
        
Mod = simplex_algo([6,14,13], A_ineq=[[0.5,2,1],[1,2,4]], b_ineq=[24,60])