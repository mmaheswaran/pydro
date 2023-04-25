import numpy as np
from scalar_property import Mass, Pressure
from abc import ABC, abstractmethod

class VectorProperty(ABC):
    def __init__(self,size,value):
        self.data = np.ones(size)*value
        
    def set_data(self,array_data):
        self.data = np.array(array_data)
    
    def get_data(self):
        return self.data
    
    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    

class Position(VectorProperty):
    
    def __init__(self,list):
        self.data = np.array(list)
    
    def __str__(self):
        return 'Position'
    
    def update(self,velocity,dt):
        self.data = self.data + velocity.get_data()*dt
        
        
class Velocity(VectorProperty):
    
    def __str__(self):
        return 'Velocity'
    
    def update(self,acceleration,dt):
        self.data = self.data + acceleration.get_data()*dt
        
class Force(VectorProperty):
    
    def __str__(self):
        return 'Force'
    
    def update(self,pressure,area,el2nodemap):
        #temp solution needs work
        self.data = pressure.get_data()*area+el2nodemap
    
        
class Acceleration(VectorProperty):
    
    def __str__(self):
        return 'Acceleration'
    
    def update(self,force,mass):
        np.seterr(divide="raise")
        self.data = force.get_data()/mass.get_data() 
