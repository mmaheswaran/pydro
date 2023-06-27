import numpy as np
from scalar_properties import Mass, Pressure
from physical_property import PhysicalProperty

class Position(PhysicalProperty):
    
    def __init__(self,list):
        self.data = np.array(list)
    
    def __str__(self):
        return 'Position'
    
    def update(self,velocity,dt):
        self.data = self.data + velocity.get_data()*dt
        
        
class Velocity(PhysicalProperty):
    
    def __str__(self):
        return 'Velocity'
    
    def update(self,acceleration,dt):
        self.data = self.data + acceleration.get_data()*dt
        
class Force(PhysicalProperty):
    
    def __str__(self):
        return 'Force'
    
    def update(self,pressure,area,el2nodemap):
        #temp solution needs work
        self.data = pressure.get_data()*area+el2nodemap
    
        
class Acceleration(PhysicalProperty):
    
    def __str__(self):
        return 'Acceleration'
    
    def update(self,force,mass):
        np.seterr(divide="raise")
        self.data = force.get_data()/mass.get_data() 
