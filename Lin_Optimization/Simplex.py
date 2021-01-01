# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:39:19 2020

@author: Alex
"""
import numpy as np

class simplex_algo:
    
    def __init__(self, Objective_Func, **Constraints):
        
        np.set_printoptions(precision=3, suppress=True)
        self.build_tableau(Objective_Func, **Constraints)
        
        while not self.is_optimal():
            self.pivot()
        
        self.get_solution()
 
        s0='z='+' + '.join([f'{Objective_Func[i]}*x{i}' for i in range(self.N)])+\
            f' obtains the max value of {self.Sol[-1]+0} for the given constraints when:'
            
        print('='*len(s0),'\n')
        print('Final Tableau:')
        print(self.T,'\n')
        print('Solution:')
        print(s0)
        print(', '.join([f'x{i} = {n:.4g}' for i , n in enumerate(self.Sol[0:self.N]+0)]),'\n')
        
        print('Slack Variables: ')
        
        print(', '.join([f's{i} = {n:.4g}' for i , n in enumerate(self.Slack+0)]),'\n')
        print('='*len(s0))
    
    def build_tableau(self, Objective_Func, **Constraints):
        A_eq = Constraints.get('A_eq')
        A_ineq = Constraints.get('A_ineq')
        b_eq = Constraints.get('b_eq')
        b_ineq = Constraints.get('b_ineq')
        
        self.N=len(Objective_Func)
        self.T = []
        
        try:
            if A_ineq!=None:
                if (b_ineq==None):
                    raise Exception('You forgot the vector b_ineq for A_ineq*x=b_ineq!')
                    
                l=len(A_ineq)
                for i, x in enumerate(A_ineq):
                    self.T.append(x+[1 if j==i else 0 for j in range(0,l)]+[b_ineq[i]])
                 
                if A_eq!=None:
                    if (b_eq==None):
                        raise Exception('You forgot the vector b_eq for A_eq*x=b_eq!')
                    for i, x in enumerate(A_eq):
                        self.T.append(x+[0]*l+[b_eq[i]])
                        
                self.T.append(Objective_Func+[0]*l+[0])
                
            else:
                if (self.b_eq==None):
                        raise Exception('You forgot the vector b_eq for A_eq*x=b_eq!')
                for i, x in enumerate(A_eq):
                    self.T.append(x+[b_eq[i]])
                    
                self.T.append(Objective_Func+[0])
        except:
            raise Exception('No constraint matrices found. Please make sure to enter them as matrices, A_eq=[[...], ...] and/or A_ineq=[[...], ...]')
  
        self.N_T=len(self.T[0])-1
        self.T=np.array(self.T, dtype='float')

        self.Basic_Var = []
        for i in range(self.N_T):
            if np.count_nonzero(self.T[:-1,i])==1:
                self.Basic_Var.append(i)
        
    
    def is_optimal(self):
        return (self.T[-1,:-1]<=0).all()       
               
    def pivot(self):
        P_var = np.argmax(self.T[-1,:-1])
        r_test = self.T[:-1,-1]/self.T[:-1,P_var]
        L_var_i = np.argmin(np.ma.masked_where(r_test<=0,r_test))
        self.Basic_Var[L_var_i]=P_var
        L_row = self.T[L_var_i]/self.T[L_var_i, P_var]

        for i, row in enumerate(self.T):
            if i==L_var_i:
                self.T[i]=L_row
            else:
                self.T[i]=self.T[i]-(self.T[i,P_var])*L_row

    def get_solution(self):
        self.Sol = np.zeros(self.N_T+1)
        self.Sol[-1]=-self.T[-1,-1]
        self.Sol[self.Basic_Var]=self.T[:-1,-1]
        self.Slack = self.Sol[self.N:-1]+0
       

               
Mod = simplex_algo([6,14,13], A_ineq=[[0.5,2,1],[1,2,4]], b_ineq=[24,60])

O=[4,3,-3,1]
A = [[5,-1,-1,5], [6,1,-6,-4], [-2, 3, 5, 7]]
b = [10, 4, 9]

Mod2 = simplex_algo(O, A_ineq=A, b_ineq=b)