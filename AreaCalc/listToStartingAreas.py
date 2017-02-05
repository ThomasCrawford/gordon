import snappy
import hikmot
import cmath
import fractions
from termcolor import colored


mList = [
	#cusp area <5.24
	'm125', 'm129', 'm203', 'm292', 'm295', 
	's596',	
	#cusp area >5.24
	's647',	's774',	's776', 's780',	's782',	's785',
	'v2124', 'v2355', 'v2533', 'v2644', 'v2731', 'v3108', 'v3127', 'v3211', 'v3376'
]

def cutoffColor( x ):
	if x > 5.24: return colored(x, 'red')
	else: return colored(x, 'green')

for m in mList:
	print m
	M = snappy.Manifold(m)
	for cuspNum in range(M.num_cusps()):
		M = snappy.Manifold(m)
		C = M.cusp_neighborhood()
		C.set_displacement(100, cuspNum)
		area = 2*C.volume(cuspNum)
		print ' cusp number ' + str(cuspNum) + ' has area ' + str(cutoffColor(area))