import sys

InFile = open (sys. argv [1], 'r')


Lines = InFile. readlines()
InFile. close ()

for N in range (len (Lines) ) : 

    if   '[ atoms ]'     in Lines [N] :     AtomLinesStart = N
    elif '[ pairs ]'     in Lines [N] :     PairLinesStart = N
    elif '[ bonds ]'     in Lines [N] :     BondLinesStart = N
    elif '[ angles ]'    in Lines [N] :    AngleLinesStart = N
    elif '[ dihedrals ]' in Lines [N] : DihedralLinesStart = N
       

AtomNo_AtomTypeLexicon = { }


PreAtomLines  = Lines [                    : AtomLinesStart     -1 ]
AtomLines     = Lines [    AtomLinesStart  : BondLinesStart     -1 ]
BondLines     = Lines [    BondLinesStart  : PairLinesStart     -1 ]
PairLines     = Lines [    PairLinesStart  : AngleLinesStart    -1 ]
AngleLines    = Lines [    AngleLinesStart : DihedralLinesStart -1 ]
DihedralLines = Lines [ DihedralLinesStart :                       ]

Bufor         = PreAtomLines

for line in AtomLines:

    if line[0] not in [ ';', '[', '\n']:

       print line

       AtomNo   = int ( line.split()[0] )

       AtomType = line.split()[1] 

       AtomNo_AtomTypeLexicon [ AtomNo ] = AtomType

    Bufor. append (line)

print 

for line in BondLines:

    if line[0] not in [ ';', '[', '\n' ]:

       AtomNo1  = int ( line. split() [0] )
       AtomNo2  = int ( line. split() [1] )

       Comment  = '; '+AtomNo_AtomTypeLexicon [ AtomNo1 ] + ' ' + AtomNo_AtomTypeLexicon [ AtomNo2 ] + '\n'

       NewLine = line[:55] + Comment

       Bufor. append (NewLine)

    else: Bufor. append ( line )


for line in PairLines:

    if line[0]  not in [ ';', '[', '\n' ]:

       AtomNo1  = int ( line. split() [0] )
       AtomNo2  = int ( line. split() [1] )

       Comment  = '; '+AtomNo_AtomTypeLexicon [ AtomNo1 ] + ' ' + AtomNo_AtomTypeLexicon [ AtomNo2 ] + '\n'

       NewLine = line[:55] + Comment

       Bufor. append (NewLine)

    else: Bufor. append ( line )


for line in AngleLines:

    if line[0]  not in [ ';', '[', '\n' ]:

       AtomNo1  = int ( line. split() [0] )
       AtomNo2  = int ( line. split() [1] )
       AtomNo3  = int ( line. split() [2] )

       Comment  = '; ' + AtomNo_AtomTypeLexicon [ AtomNo1 ] + ' ' + AtomNo_AtomTypeLexicon [ AtomNo2 ] \
                      +' '+ AtomNo_AtomTypeLexicon [ AtomNo3 ] + '\n'

       NewLine = line[:59] + Comment

       Bufor. append (NewLine)

    else: Bufor. append ( line ) 


for line in DihedralLines:

    if line[0]  not in [ ';', '[', '\n' ]:

       AtomNo1  = int ( line. split() [0] )
       AtomNo2  = int ( line. split() [1] )
       AtomNo3  = int ( line. split() [2] )
       AtomNo4  = int ( line. split() [3] )

       Comment  = '; ' + AtomNo_AtomTypeLexicon [ AtomNo1 ] + ' ' + AtomNo_AtomTypeLexicon [ AtomNo2 ] \
                      +' '+ AtomNo_AtomTypeLexicon [ AtomNo3 ] +' '+ AtomNo_AtomTypeLexicon [ AtomNo4 ] + '\n'

       NewLine = line[:64] + Comment

       Bufor. append (NewLine)

    else: Bufor. append ( line ) 


OutFile = open (sys. argv [2], 'w')

for Line in Bufor:

    OutFile. write (Line)

OutFile. close ()

