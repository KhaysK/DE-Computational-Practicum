from exact_solution import ExactSolution
import numpy as np

class MyOwnSolution(ExactSolution):
    def __init__(self, N, y0, x0, X):
        ExactSolution.__init__(self, N, y0, x0, X)
        self.exactSolution()
    
    # overriding abstract method
    def Derivative(self, x, y):
        return np.power(np.e, 2*x) + np.power(np.e, x) + np.power(y, 2) - 2*y*np.power(np.e, x)

    # overriding abstract method
    def exactSolution(self):
        x = self.X
        y = self.Y 
        constant = -1/(self.Y0 - np.power(np.e, self.X0)) - self.X0
        for i in range(self.N):
            if i == 0: y[i] = self.Y0
            else: y[i] = np.power(np.e, x[i-1]) - 1/(constant+x[i-1])
        
        self.Y = y

        