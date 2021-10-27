import numerical_method
from numerical_method import NumericMethod

class RungeKuttaMethod(NumericMethod):
    def __init__(self, N, y0, x0, X, DE):
        NumericMethod.__init__(N, y0, x0, X, DE)
    
    # overriding abstract method    
    def calculateY(self, x, y):
        h  = NumericMethod.h
        k1 = NumericMethod.exactSolution.Derivative(x, y)
        k2 = NumericMethod.exactSolution.Derivative(x + h / 2, y + (h / 2) * k1)
        k3 = NumericMethod.exactSolution.Derivative(x + h / 2, y + (h / 2) * k2)
        k4 = NumericMethod.exactSolution.Derivative(x + h, y + h * k3)
        Y  = y + h*(k1+2*k2+2*k3+k4)/6
        return Y