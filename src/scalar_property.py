import numpy as np
from abc import ABC, abstractmethod

class ScalarProperty(ABC):
    def __init__(self,size):
        self.data = np.zeros(size)
        
    def __str__(self):
        return np.array_str(self.data)
    
    @abstractmethod
    def get_name(self):
        pass
    
    
class Energy(ScalarProperty):
    
    def get_name(self):
        return "Energy"
    
    
    