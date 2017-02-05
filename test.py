import unittest
from unHyp import *
import snappy


class Test(unittest.TestCase):
    def test_can_detect_non_hyperbolic_manifold(self):
        M = snappy.Manifold('m129')
        M.dehn_fill((-1,1),0)
        N=M.filled_triangulation()
        t = SnapPeaTriangulation(N._to_string())
        self.assertFalse(isHyp(t))

    def test_can_detect_hyperbolic_manifold(self):
        M = snappy.Manifold('m129')
        M.dehn_fill((5,1),0)
        N=M.filled_triangulation()
        t = SnapPeaTriangulation(N._to_string())
        self.assertTrue(isHyp(t))


unittest.main()