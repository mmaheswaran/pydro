import unittest

from scalar_property import *
from vector_property import *
from mesh import FEM1D

class TestScalarProperties(unittest.TestCase):
    
    def setUp(self):
        self.mesh = FEM1D(1)
        self.ndpos = Position([0.0,1.0])
        self.connectivity = np.array([[0,1]])
        self.mesh.get_connectivity(self.connectivity)
        
    def tearDown(self):
        pass
    
    def test_volume_update(self):
        vol = Volume(1)
        self.assertEqual(vol.datalen(), 1)
        vol.update(self.ndpos,self.mesh)
        self.assertEqual(vol.get_data(), [1.0])
        
        
        
        
if __name__=='__main__':
    unittest.main()