import snappy
from unHyp import *

manifoldName = 'm129'
cuspNum = 0

print M

M=snappy.Manifold(manifoldName)
M.dehn_fill((-5,1),cuspNum)
N=M.filled_triangulation()
t = SnapPeaTriangulation(N._to_string())


print isHyp(t)
