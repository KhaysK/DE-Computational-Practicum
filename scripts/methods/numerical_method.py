from _typeshed import Self
from abc import ABC, abstractmethod
from grid import Grid
from exact_solution import ExactSolution
import numpy as np

class NumericMethod(ABC, Grid):
    exactSolution : ExactSolution
    localError = np.empty(Grid.N, dtype=float)

    def __init__(self, N, y0, x0, X, DE):
        Grid.__init__(N, y0, x0, X)
        self.exactSolution = DE
        h = Grid.h
        X = Grid.X
        Y = Grid.Y
        for i in range(N):
            if i == 0:
                Y[i] = y0
            else:
                Y[i] = self.calculateY(X[i-1], Y[i-1])
        Grid.Y = Y

    def calculateLocalError(self):
        exactY = self.exactSolution.Y
        numericalY = Grid.Y
        error = np.empty(Grid.N, dtype=float)

        for i in range(Grid.N):
            error[i] = np.abs(exactY[i]-numericalY[i])
        
        self.localError = error

    def calculateGlobalError(self):
        error = 0
        for i in range(Grid.N):
            if self.localError[i] > error : error = self.localError[i]
        return error

    @abstractmethod
    def calculateY(self, x, y):
        pass