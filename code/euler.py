from numerical_method import NumericMethod
import numpy as np 
from my_own_solution import MyOwnSolution

class EulerMethod(NumericMethod):
    globalError = []

    def __init__(self, N, y0, x0, X, DE):
        NumericMethod.__init__(self, N, y0, x0, X, DE)
    
    # overriding abstract method
    def calculateY(self, x, y):
        h = self.h
        Y = y + h * self.exactSolution.Derivative(x, y)
        return Y

    def calculateGlobalError(self, n0):
        error = np.empty(self.N - n0, dtype=float)
        for i in range(n0,self.N):
            exact=MyOwnSolution(i,self.Y0,self.X0,self.bigX)
            method = EulerMethod(i,self.Y0,self.X0,self.bigX,exact)
            print(max(method.localError))
            error[i - n0] = max(method.localError) 
        self.globalError = error