import ObjectiveFunction as ObjFunction
import numpy as  np
import matplotlib.pyplot as plt
import random,math

class CSIndividual:
    def __init__(self,vardim,bound):
        self.vardim=vardim
        self.bound=bound
        self.position=np.zeros(self.vardim)
        self.fitness=0.

    def gernate(self):
        for i in range(0,self.vardim):
            self.position[i]=(self.bound[1,i]-self.bound[0,i])*random.random()+self.bound[0,i]

    def calcuateFitness(self):
        self.fitness=ObjFunction.Sphere(self.vardim,self.position)
