from decimal import Decimal

class Grid:
    X = []
    Y = []
    N = 10
    X0 = 0
    bigX = 15
    Y0 = 0
    h= 0

    def __init__(self, n, y0, x0, X):
        self.Y = [None] * n
        self.X = [None] * n
        self.X0 = x0
        self.bigX = X
        self.Y0 = y0
        self.N = n
        self.h = (X - x0)/(n)
        self.Y[0] = y0
        
        for i in range(n):
            if i == 0 :
                self.X[i] = x0
            else:
                self.X[i] = self.X[i - 1] + self.h