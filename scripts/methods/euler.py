import numerical_method
from numerical_method import NumericMethod

class EulerMethod(NumericMethod):
    def __init__(self, N, y0, x0, X, DE):
        NumericMethod.__init__(N, y0, x0, X, DE)
    
    # overriding abstract method
    def calculateY(self, x, y):
        h = NumericMethod.h
        Y = y + h * NumericMethod.exactSolution.Derivative(x, y)
        return Y