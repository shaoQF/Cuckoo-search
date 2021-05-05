import math
import numpy as np


def Sphere(vardim,x):
    sum=0
    for i in range(vardim):
        sum=sum+x[i]**2
    return sum