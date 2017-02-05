import snappy
# import hikmot
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

##################################
#
#from analyzeManifold:
#
##################################


def reformatNumber ( snappyNumber ):
	imag = float(snappyNumber.imag())
	real = float(snappyNumber.real())
	return real + imag*1j

def coprimes (s, xTranslation, yTranslation):
	pairs= [[1,0],[0,1]]
	for a in range(1,s+1): 
		for b in range(1,s+1): 
			if fractions.gcd(a,b)==1:
				pairs.append([a,b])
				pairs.append([-a,b])
	return sorted(pairs, key = lambda x: float(abs( x[1]*xTranslation + x[0]*yTranslation)))
	# return sorted(pairs, key = lambda x: float(abs(x[1]))+float(abs(x[0])))


M = snappy.Manifold(twoCuspMfld)
print M.identify()
C=M.cusp_neighborhood()

xTranslation = reformatNumber(C.all_translations()[whichCusp][1])
yTranslation = reformatNumber(C.all_translations()[whichCusp][0])

greaterThan = []
lessThan = []
notHyp = []
miss = []

for [i,j] in coprimes(r , xTranslation, yTranslation):
	# print i,j
	M = snappy.Manifold(twoCuspMfld)
	M.dehn_fill((i,j),whichCusp)
	if M.volume() > 0.5:
		try:
			C = M.cusp_neighborhood()
			C.set_displacement(100)
			surgeryLength = abs(i*yTranslation+j*xTranslation)
			cuspArea = C.volume()*2
			print "{0:.3f}".format(surgeryLength) + '\t' + cutoffColor(cuspArea) + '\t' + str((i,j))
			if C.volume()<2.6201: lessThan.append((i,j))
			else:  greaterThan.append((i,j))

		except:
			print 'Failed to construct cusp for ' + str((i,j)) +' surgery' 
			miss.append((i,j))
			pass
	else: 
		print str((i,j)) + ' surgery is not hyperbolic'
		notHyp.append((i,j))

print 'Under cutoff: ' + str(len(lessThan))
print 'Over cutoff: ' + str(len(greaterThan))
print 'Not Hyperbolic: ' + str(len(notHyp))
print 'Could not construct cusp: ' + str(len(miss))