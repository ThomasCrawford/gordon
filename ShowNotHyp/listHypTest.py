import snappy
from unHyp import *

manifoldName = 'm125'
cuspNum = 0

surgeryList = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, 2), (2, 1)]

for (a,b) in surgeryList:
	M=snappy.Manifold(manifoldName)
	M.dehn_fill((a,b),cuspNum)
	N=M.filled_triangulation()
	t = SnapPeaTriangulation(N._to_string())
	print isHyp(t)