from exact_solution import ExactSolution
import numpy as np
from decimal import Decimal as D


class MyOwnSolution(ExactSolution):
    def __init__(self, N, y0, x0, X):
        ExactSolution.__init__(self, N, y0, x0, X)
        self.exactSolution()
    
    # overriding abstract method
    def Derivative(self, x, y):
        return D(np.e)**(2*x) + D(np.e)**x + y**2 - 2*y*D(np.e)**x

    # overriding abstract method
    def exactSolution(self):
        x = self.X0
        y = self.Y0
        constant = - (1/(y-D(np.e)**x)) - x
        for i in range(self.N):
            if i == 0: continue
            else: self.Y[i] = D(np.e)**self.X[i] - 1/(constant+self.X[i])

        