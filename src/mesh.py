import numpy as np
from abc import ABC, abstractmethod

class Mesh:
    
    @abstractmethod
    def get_volume(self,element):
        pass
    
    def __str__(self):
        return 'Mesh'
    
    

class FEM1D(Mesh):
    
    def __init__(self,elements):
        self.el2nodemap = np.empty([elements,2])
        
    def get_connectivity(self,nodemap):
        self.el2nodemap = np.array(nodemap)

    def get_volume(self,element,ndpositions):
        nodpos=ndpositions.get_data()
        node1 = self.el2nodemap[element][0]
        node2 = self.el2nodemap[element][1]

        dl = abs(nodpos[node2]-nodpos[node1])
        
        return dl
    
    def calc_divergence(field):
        
        
    