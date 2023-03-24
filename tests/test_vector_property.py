import unittest
import numpy as np

from scalar_property import *
from vector_property import *
from mesh import FEM1D


class TestVectorProperties(unittest.TestCase):
    def setUp(self):
        self.mesh = FEM1D(1)
        self.connectivity = np.array([[0, 1]])
        self.mesh.get_connectivity(self.connectivity)

    def tearDown(self):
        pass

    def test_position_update(self):
        velocity = Velocity([1.0, 1.0])
        dt = 0.5
        ndpos = Position([0.0, 1.0])
        ndpos.update(velocity, dt)
        print(ndpos.get_data())
