import numpy as np
from physical_property import PhysicalProperty
from _operator import index

class Energy(PhysicalProperty):

    #find divergence of velocity field

    #energy calcualated using rho*dE/dt = -pdv

    def __str__(self):
        return 'Energy'
    
class Density(PhysicalProperty):
    
    def update(self, mass, volume):
        np.seterr(divide="raise")
        assert (volume.get_data()!=0).all(), 'Division by zero'
        self.data = mass.get_data()/volume.get_data()
    
    def __str__(self):
        return 'Density'
    
class Pressure(PhysicalProperty):

    def update(self,density,energy):

        gruneisen_gamma = 1.4 #ideal gas
        self.data = density.get_data() * energy.get_data()*(gruneisen_gamma-1)

    def __str__(self):
        return 'Pressure'
    
class Mass(PhysicalProperty):
    
    def update(self,density,volume):
        self.data = density.get_data()*volume.get_data() 

    def __str__(self):
        return 'Mass'

    
class SoundSpeed2(PhysicalProperty):
    
    def __str__(self):
        return 'SoundSpeedSquared'
    
class Volume(PhysicalProperty):

    def __str__(self):
        return 'Volume'
    
    def update(self, ndpositions, mesh):
        noelements = (self.data).size()
        for e in range(noelements):
            self.data[e] = mesh.get_volume(e,ndpositions)
            