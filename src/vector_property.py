import numpy as np
from abc import ABC, abstractmethod

class VectorProperty(ABC):
    def __init__(self,size):
        self.data = np.zeros(size)
        
    def __str__(self):
        return np.array_str(self.data)
    
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    

class Position(VectorProperty):
    
    def get_name(self):
        return "Position"
    
    def update(self,ndvelocity,dt):
        self.data = self.data + ndvelocity*dt
        
        
        
