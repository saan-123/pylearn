import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self):
        self.X = np.linspace(-3, 3, num=1000)
        self.domain = self.X
        self.Y = np.log(np.abs(self.X ** 2 - 1) + .5)

    def local_regression(self, x0, tau):
        x0 = [1, x0]
        X = [[1, i] for i in self.X]
        X = np.asarray(X)
        Xw = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau))
        beta = np.linalg.pinv(Xw @ X) @ Xw @ self.Y @ x0
        return beta

    def draw(self, tau):
        prediction = [self.local_regression(x0, tau) for x0 in self.domain]
        plt.plot(self.X, self.Y, 'o', color='black')
        plt.plot(self.domain, prediction, color='red')
        plt.show()

# Usage example
#lr = LinearRegression()
#lr.draw(10)
#lr.draw(0.1)
#lr.draw(0.001)
