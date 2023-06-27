import unittest
import numpy as np
from scalar_properties import *
from vector_properties import *

from artificial_viscosity import *

class TestArtificialViscosity(unittest.TestCase):

    def setUp(self):
        rigid_boundaryL = 1
        reflective_boundaryR = 2
        coefficients = [0.75,0.5]
        boundary_conditions = [rigid_boundaryL,reflective_boundaryR]
        self.q = ArtificialViscosity(coefficients,boundary_conditions)
        self.gradient = np.array([0.0,0.1,0.2,0.3],dtype=float)
        

    def tearDown(self):
        pass

    def test_calculate_limiter(self):
        limiter = self.q.calculate_limiter(self.gradient)
        expected = [0.0,0.0,1.0,(2.0/3.0)*1.25]
        np.testing.assert_allclose(limiter, expected,rtol=1e-10)
    
    def test_apply_boundary_conditions(self):
        gradv_l = np.roll(self.gradient,1)
        gradv_r = np.roll(self.gradient,-1)
        self.q.apply_boundary_conditions(gradv_l,gradv_r)
        expected_l = [0.0,0.0,0.1,0.2]
        expected_r = [0.1,0.2,0.3,0.3]
        np.testing.assert_allclose(gradv_l, expected_l,rtol=1e-10)
        np.testing.assert_allclose(gradv_r, expected_r,rtol=1e-10)

    def test_solve(self):
        nel = 4
        ndpos = Position([0.0,1.0,2.0,3.0])
        ndvel = Velocity([1.0,1.0,0.0,0.0])
        elccs2 = SoundSpeed2([0.2,0.3,0.4,0.5])
        elden = Density([2.0,2.0,1.0,1.0])
        hydro_properties = {elden.__str__():elden, \
                   elccs2.__str__():elccs2, \
                   ndpos.__str__():ndpos, \
                   ndvel.__str__():ndvel}
        
        q_answer = self.q.solve(hydro_properties,nel)
        expected = [0.0,0.45,0.2375,0.0]
        np.testing.assert_allclose(q_answer, expected,rtol=1e-10)

if __name__=='__main__':
    unittest.main()