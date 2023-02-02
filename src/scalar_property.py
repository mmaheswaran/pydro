import numpy as np
from abc import ABC, abstractmethod

class ScalarProperty(ABC):
    def __init__(self,size):
        self.data = np.zeros(size)
        
    @abstractmethod
    def __str__(self):
        pass
    
    
class Energy(ScalarProperty):
    
    def __str__(self):
        return 'Energy'
    
class Density(ScalarProperty):
    
    def __str__(self):
        return 'Density'
    
class Pressure(ScalarProperty):
    
    def __str__(self):
        return 'Pressure'
    
class Mass(ScalarProperty):
    
    def __str__(self):
        return 'Mass'
    
class SoundSpeed2(ScalarProperty):
    
    def __str__(self):
        return 'SoundSpeedSquared'
    
class Volume(ScalarProperty):
    
    def __str__(self):
        return 'Volume'
    
    def update(self, ndpositions, mesh):
        noelements = len(self.data)
        for e in range(noelements):
            self.data[e] = mesh.get_volume(e,ndpositions)
            