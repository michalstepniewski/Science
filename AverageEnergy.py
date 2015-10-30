import sys

plik = open(sys.argv[1],'r')

InLines = plik.readlines ()

plik. close ()

Titles = [ ]

Energies = [ ]

NoEnergies = 0

for InLine in InLines:

	if InLine[:3] == '@ s':

		Titles.append ( InLine.split( '\"' )[1] )

		Energies. append (0.0)

	elif InLine [0] not in ['#','@' ]:
		print Titles
		n = 0
		NoEnergies += 1

		for Energy in InLine. split ()[1:]:
			print InLine.split()[1:]
			print n
			Energies[n]+= float(Energy)

			n += 1
			
print Energies

OutLines = [ ]

for n in range(len(Energies)):

	Energy = Energies[n]/float(NoEnergies)

	OutLine = Titles[n] + ' '+ str(Energy) + '\n'
	OutLines.append(OutLine)

OutFile	= open(sys.argv[2],'w')

for OutLine in OutLines:

	OutFile. write (OutLine)

OutFile. flush ()
OutFile. close ()


	
			
