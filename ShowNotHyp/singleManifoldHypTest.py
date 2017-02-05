import snappy
from unHyp import *

M=snappy.Manifold('m129')

print M

M.dehn_fill((-5,1),0)
N=M.filled_triangulation()
t = SnapPeaTriangulation(N._to_string())


print isHyp(t)
