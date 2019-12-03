import numpy as np
import matplotlib.pylab as plt

class myPlot():
    def __init__(self):
        self.tiempo = np.loadtxt('datos.txt', delimiter="\t", skiprows=1, usecols=[0])
        self.setpoint = np.loadtxt('datos.txt', delimiter="\t", skiprows=1, usecols=[1])
        self.pos = np.loadtxt('datos.txt', delimiter="\t", skiprows=1, usecols=[2])
        self.error = np.loadtxt('datos.txt', delimiter="\t", skiprows=1, usecols=[3])
        
    def printing(self):
        print("Tiempo", self.tiempo)
        print("Setpoint", self.setpoint)
        print("Posición", self.pos)
        print("Error", self.error)
    
    def graph_pos(self):
        plt.plot(self.tiempo, self.setpoint, label = "Setpoint")
        #plt.legend(['Setpoint'])
        plt.plot(self.tiempo, self.pos, label = "Posición")
        plt.legend(bbox_to_anchor=(0.5, 1), loc='upper left', borderaxespad=0.)
        #plt.legend(['Posición'])
        plt.xlabel('t')
        plt.ylabel('rad/seg')
        plt.show()
    def graph_err(self):
        plt.plot(self.tiempo, self.error, label = "Error")
        plt.legend(bbox_to_anchor=(0.5, 1), loc='upper left', borderaxespad=0.)
        #plt.legend(['Posición'])
        plt.xlabel('t')
        plt.ylabel('rad/seg')
        plt.show()
