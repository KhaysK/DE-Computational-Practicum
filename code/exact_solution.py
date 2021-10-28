from abc import ABC, abstractmethod
from grid import Grid


class ExactSolution(Grid, ABC):
    def __init__(self, N, y0, x0, X):
        Grid.__init__(self, N, y0, x0, X)
    
    @abstractmethod
    def Derivative(self, x, y):
        pass

    @abstractmethod
    def exactSolution(self):
        pass