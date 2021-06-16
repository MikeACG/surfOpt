import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

# creates a problem given by 2 independent variables (x and y) and an outcome variable
class Surf3d:
    def __init__(self, f, dlims, ulims):
        self.f = f # user defined function
        self.ulims = ulims # upper limits of x and y
        self.dlims = dlims # lower limits of x and y
        # interpolations for graphical representations
        self.x = np.linspace(self.dlims[0], self.ulims[0])
        self.y = np.linspace(self.dlims[1], self.ulims[1])
        self.xg, self.yg = np.meshgrid(self.x, self.y)
    
    # plots a 2d representation of the search space and individuals if provided
    def plot2d(self, ga = None):
        plt.figure(figsize = (8,5))
        plt.imshow(self.f([self.xg, self.yg]), extent = [self.dlims[0], self.ulims[0], self.ulims[1], self.dlims[1]], cmap = plt.cm.jet)
        plt.xlabel('x', size = 15)
        plt.ylabel('y', size = 15)
        plt.colorbar()
        if ga is not None:
            plt.scatter([i[0] for i in ga.pop], [i[1] for i in ga.pop], color = "black", alpha = 0.9)
        plt.show()
    
    # plots a 3d representation of the search space and individuals if provided
    def plot3d(self, ga = None):
        fig = plt.figure(figsize = (8,5))
        ax = fig.add_subplot(111, projection = '3d')
        if ga is not None:
            a = 0.2
        else:
            a = 1
        ax.plot_surface(self.xg, self.yg, self.f([self.xg, self.yg]), rstride = 1, cstride = 1, cmap = plt.cm.jet, linewidth = 0, antialiased = False, alpha = a)
        ax.set_xlabel('x', size = 15)
        ax.set_ylabel('y', size = 15)
        ax.set_zlabel('f(x,y)', size = 15)
        if ga is not None:
            ax.scatter([i[0] for i in ga.pop], [i[1] for i in ga.pop], ga.evals, color = "black", alpha = 1)
        plt.show()
        
