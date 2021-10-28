from abc import ABC, abstractmethod
from grid import Grid
from exact_solution import ExactSolution
import numpy as np 


class NumericMethod(ABC, Grid):
    exactSolution : ExactSolution
    localError = []
    def __init__(self, N, y0, x0, X, DE):
        Grid.__init__(self, N, y0, x0, X)
        self.exactSolution = DE
        X = self.X
        Y = self.Y
        for i in range(N):
            if i == 0:
                Y[i] = y0
            else:
                Y[i] = self.calculateY(X[i-1], Y[i-1])
        self.Y = Y
        self.calculateLocalError()

    def calculateLocalError(self):
        exactY = self.exactSolution.Y
        numericalY = self.Y
        error = np.empty(self.N, dtype=float)

        for i in range(self.N):
            error[i] = np.abs(exactY[i]-numericalY[i])
        
        self.localError = error

    @abstractmethod
    def calculateGlobalError(self, n0,):
        pass

    @abstractmethod
    def calculateY(self, x, y):
        pass
