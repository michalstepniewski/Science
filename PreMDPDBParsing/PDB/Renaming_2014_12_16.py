import sys

plik = open ( 'POPC_AA_Res_Renamed.pdb', 'r' )

lines = plik. readlines (); plik. close ()

Atomy = lines [ 5 : ]

nazwy = [ line [ 12 : 21 ] for line in Atomy ]

#*************************************************************************************************

plik2 = open ( '/home/soutys/Science/Trzaskowski/Projekt/TomkaModele/popc_128bal/PDB/Membrane/POPC_20ns.pdb', 'r' )

lines2 = plik2. readlines (); plik2. close ()

Bufor = []

for N in range(len(lines2)):

    line = lines2 [N]

    if line [ : 4 ] == 'ATOM':

       print line [ 17 : 20 ]

       if line [ 17 : 20 ] == 'POP':

          NewLine = line [ : 12 ] + nazwy [ int ( (N-5)  %134)  ] + line [ 21 : ]

       else: NewLine = line

    else: NewLine = line

    Bufor. append ( NewLine )

OutFile = open ( 'POPC_AA_20ns_Renamed.pdb', 'w' )
       
for line in Bufor: OutFile. write ( line )

OutFile. flush ()
OutFile. close ()



