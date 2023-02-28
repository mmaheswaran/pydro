import unittest

from predictor_corrector import *

class TestPredictorCorrector(unittest.TestCase):

    def setUp(self):
        self.mesh = FEM1D(1)
        self.ndpos = Position([0.0,1.0])
        self.connectivity = np.array([[0,1]])
        self.mesh.get_connectivity(self.connectivity)
        
        self.hydroproperties = {mesh.__str__():self.mesh, \
                   elenergy.__str__():elenergy, \
                   eldensity.__str__():eldensity, \
                   elpressure.__str__():elpressure, \
                   elccs2.__str__():elccs2, \
                   elmass.__str__():elmass, \
                   elvolume.__str__():elvolume, \
                   ndpositions.__str__():ndpositions, \
                   ndvelocity.__str__():ndvelocity}