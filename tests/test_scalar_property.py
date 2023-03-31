import unittest
import numpy as np

from scalar_property import *
from vector_property import *
from mesh import FEM1D

class TestScalarProperties(unittest.TestCase):
    
    def setUp(self):
        self.mesh = FEM1D(1)
        self.ndpos = Position(1,0.0)
        self.ndpos.set_data([0.0,1.0])
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
        volume = Volume(2,1.0)
        
        volume.update(self.ndpos,self.mesh)
       # np.testing.assert_allclos(vol.get_data(), [1.0])
        
    # def test_density_update(self):
    #     density = Density(1)
    #     print(density.get_data())
    #     #mass = Mass(1)
    #     #mass.set(0,1.0)
    #     #vol = Volume(1)
    #     #vol.set(0,1.0) 
        
    #     #density.update(mass,vol)
    #     #self.assertEqual(density.get_data(), 1.0)       
        
        
if __name__=='__main__':
    unittest.main()