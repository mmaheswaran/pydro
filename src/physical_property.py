import numpy as np
from abc import ABC, abstractmethod

class PhysicalProperty(ABC):

    def __init__(self,size,value):
        self.data = np.ones(size)*value
        
    def get(self,index):
        return self.data[index]
    
    def set(self,index,value):
        self.data[index] = value
        
    def get_data(self):
        return self.data
    
    def set_data(self,array_data):
        self.data = np.array(array_data)
        
    @abstractmethod
    def __str__(self):
        pass