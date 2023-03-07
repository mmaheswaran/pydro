import numpy as np
from abc import ABC, abstractmethod
from _operator import index

class ScalarProperty(ABC):
    
    def __init__(self,size):
        self.data = np.zeros(size)
        
    def __init__(self,array_data):
        self.data = np.array(array_data)
        
    def get(self,index):
        return self.data[index]
    
    def set(self,index,value):
        self.data[index] = value
        
    def get_data(self):
        return self.data
    
    #def datalen(self):
    #    return self.data.size
        
    @abstractmethod
    def __str__(self):
        pass
    
    
class Energy(ScalarProperty):
    
    def __str__(self):
        return 'Energy'
    
class Density(ScalarProperty):
    
  #  def update(self, mass, volume):
  #      np.seterr(divide="raise")
  #      self.data = mass.get_data()/volume.get_data()
    
    def __str__(self):
        return 'Density'
    
class Pressure(ScalarProperty):
    
    def __str__(self):
        return 'Pressure'
    
class Mass(ScalarProperty):
    
 #   def update(self,density,volume):
 #       self.data = density.get_data()*volume.get_data()      
    def __str__(self):
        return 'Mass'

    
class SoundSpeed2(ScalarProperty):
    
    def __str__(self):
        return 'SoundSpeedSquared'
    
class Volume(ScalarProperty):
    
    def __init__(self,size):
        pass
    
    def __str__(self):
        return 'Volume'
    
   # def update(self, ndpositions, mesh):
   #     noelements = (self.data).size()
   #     for e in range(noelements):
   #         self.data[e] = mesh.get_volume(e,ndpositions)
            