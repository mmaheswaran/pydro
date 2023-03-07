import unittest
import numpy as np
from scalar_property import *
from vector_property import *

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
        self.assertEqual(limiter, [0.0,0.0,1.0,(2.0/3.0)*1.25])
    
    def test_apply_boundary_conditions(self):
        gradv_l = np.roll(self.gradient,1)
        gradv_r = np.roll(self.gradient,-1)
        self.q.apply_boundary_conditions(gradv_l,gradv_r)

    # def test_solve(self):
    #     nel = 4
    #     ndpos = Position([0.0,1.0,2.0,3.0])
    #     ndvel = Velocity([1.0,1.0,0.0,0.0])
    #     elccs2 = SoundSpeed2([0.2,0.3,0.4,0.5])
    #     elden = Density([2.0,2.0,1.0,1.0])
    #     hydro_properties = {elden.__str__():elden, \
    #                elccs2.__str__():elccs2, \
    #                ndpos.__str__():ndpos, \
    #                ndvel.__str__():ndvel}
        
    #     q_answer = self.q.solve(hydro_properties,nel)
    #     print(q_answer)

if __name__=='__main__':
    unittest.main()