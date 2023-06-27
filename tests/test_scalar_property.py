import unittest
import numpy as np

from scalar_properties import *
from vector_properties import *
from mesh import FEM1D

class TestScalarProperties(unittest.TestCase):
    
    def setUp(self):
        self.mesh = FEM1D(1)
        self.ndpos = Position(1,0.0)
        t = [0.0,1.0]
        self.ndpos.set_data(t)
        self.connectivity = np.array([[0,1]])
        self.mesh.get_connectivity(self.connectivity)
        
    def tearDown(self):
        pass

    def test_energy_update(self):
        energy = Energy(3,0.0)
        expected = [0.0,0.0,0.0]
        np.testing.assert_allclose(energy.get_data(),expected)
    
    def test_density_update(self):
        density = Density(2,0.0)
        mass = Mass(2,1.0)
        volume = Volume(2,2.0)
        density.update(mass,volume)
        expected = [0.5,0.5]
        np.testing.assert_allclose(density.get_data(),expected)
        volume = Volume(2,0.0)
        self.assertRaises(AssertionError,density.update,mass,volume)
        
    def test_pressure_update(self):
        pressure = Pressure(3,0.0)
        expected = [0.0,0.0,0.0]
        np.testing.assert_allclose(pressure.get_data(),expected)
    
    def test_mass_update(self):
        density = Density(2,1.0)
        volume = Volume(2,2.0)
        mass = Mass(2,0.0)
        mass.update(density,volume)
        expected = [2.0,2.0]
        np.testing.assert_allclose(mass.get_data(),expected)
        

    def test_volume_update(self):
        volume = Volume(1,1.0)
        
        volume.update(self.ndpos,self.mesh)
        expected = [1.0]
        np.testing.assert_allclos(volume.get_data(), expected)
             
        
        
if __name__=='__main__':
    unittest.main()