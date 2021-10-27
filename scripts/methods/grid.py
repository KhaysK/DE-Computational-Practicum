class Grid:
    X = []
    Y = []
    N: int
    X0: float
    bigX: float
    Y0: float
    h: float

    def __init__(self, N, y0, x0, X):
        self.Y = []
        self.X = []
        self.X0 = x0
        self.bigX = X
        self.Y0 = y0
        self.N = N
        self.h = (X - x0)/(N-1)
        self.Y[0] = y0

        for n in range(N):
            if n == 0 :
                self.X[n] = x0
            else:
                self.X[n] = self.X[n - 1] + self.h