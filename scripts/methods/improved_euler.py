import numerical_method
from numerical_method import NumericMethod

class ImprovedEulerMethod(NumericMethod):
    def __init__(self, N, y0, x0, X, DE):
        NumericMethod.__init__(N, y0, x0, X, DE)
    
    # overriding abstract method    
    def calculateY(self, x, y):
        h = NumericMethod.h
        Y = y + (h/2) * (NumericMethod.exactSolution.Derivative(x, y) +
         NumericMethod.exactSolution.Derivative(x + h, y + h * NumericMethod.exactSolution.Derivative(x, y)))
        return Y