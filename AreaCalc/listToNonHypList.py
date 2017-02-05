import snappy
# import hikmot
import cmath
import fractions
from termcolor import colored

r=20

mList = [
	#cusp area <5.24
	'm125', 'm129', 'm203', 'm292', 'm295', 's596',	
	#cusp area >5.24
	's647',	's774',	's776', 's780',	's782',	's785',
	'v2124', 'v2355', 'v2533', 'v2644', 'v2731', 'v3108', 'v3127', 'v3211', 'v3376'
]

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

def getNonHypList (manifoldName, cuspNum, coprimeList):
	nonHypList = []
	M = snappy.Manifold(manifoldName)
	for [i,j] in coprimeList: 
		M = snappy.Manifold(manifoldName)
		M.dehn_fill((i,j), cuspNum)
		if M.volume() < 0.94:
			nonHypList.append((i,j))
	return nonHypList

total = 0

for manifoldName in mList:
	M=snappy.Manifold(manifoldName)
	C=M.cusp_neighborhood()
	for cuspNum in range(C.num_cusps()):
		C = M.cusp_neighborhood()
		C.set_displacement(100, cuspNum)
		xTranslation = reformatNumber(C.all_translations()[cuspNum][1])
		yTranslation = reformatNumber(C.all_translations()[cuspNum][0])
		coprimeList = coprimes(r, xTranslation, yTranslation)
		print manifoldName + ' cusp ' + str(cuspNum)
		nonHyplist =  getNonHypList(manifoldName, cuspNum, coprimeList)
		total = total + len(nonHyplist)
		print nonHyplist
print total





