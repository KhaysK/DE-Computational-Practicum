from exact_solution import ExactSolution
import numpy as np

class MyOwnSolution(ExactSolution):
    def __init__(self, N, y0, x0, X):
        ExactSolution.__init__(N, y0, x0, X)
        self.exactSolution()
    
    # overriding abstract method
    def Derivative(self, x, y):
        return np.power(np.e, 2*x) + np.power(np.e, x) + np.power(y, 2) - 2*y*np.power(np.e, x)

    # overriding abstract method
    def exactSolution(self):
        h = ExactSolution.h
        x = ExactSolution.X
        y = ExactSolution.Y

        for i in range(ExactSolution.N):
            if i == 0: y[i] = ExactSolution.Y0
            else: y[i] = np.power(np.e, x[i-1]) - 1/(1+x[i-1])
        
        ExactSolution.Y = y