from numerical_method import NumericMethod
import numpy as np 
from my_own_solution import MyOwnSolution

class RungeKuttaMethod(NumericMethod):
    globalError = []

    def __init__(self, N, y0, x0, X, DE):
        NumericMethod.__init__(self, N, y0, x0, X, DE)
    
    # overriding abstract method    
    def calculateY(self, x, y):
        h  = self.h
        k1 = self.exactSolution.Derivative(x, y)
        k2 = self.exactSolution.Derivative(x + h / 2, y + (h * k1) / 2)
        k3 = self.exactSolution.Derivative(x + h / 2, y + (h * k2) / 2)
        k4 = self.exactSolution.Derivative(x + h, y + h * k3)
        Y  = y + h*(k1+2*k2+2*k3+k4)/6
        return Y

    def calculateGlobalError(self, n0):
        error = np.empty(self.N - n0, dtype=float)
        for i in range(n0,self.N):
            exact=MyOwnSolution(i,self.Y0,self.X0,self.bigX)
            method = RungeKuttaMethod(i,self.Y0,self.X0,self.bigX,exact)
            print(max(method.localError))
            error[i - n0] = max(method.localError) 
        self.globalError = error