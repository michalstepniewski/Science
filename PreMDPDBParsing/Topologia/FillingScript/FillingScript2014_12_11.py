import sys


TopFile = open ( sys.argv [3], 'r' )

Lines = TopFile. readlines(); TopFile. close ()

for N in range (len (Lines) ) : 

#    print Lines[N]

    if   '[ bondtypes ]'       in Lines [N] :          BondTypeLinesStart = N
    elif '[ constrainttypes ]' in Lines [N] :     ContraintTypeLinesStart = N
    elif '[ angletypes ]'      in Lines [N] :         AngleTypeLinesStart = N
    elif '[ dihedraltypes ]' in Lines [N] :        DihedralTypeLinesStart = N

AtomNo_AtomTypeLexicon = { }

# potem musze to ogarnac zmienie atom na C
#PreLines  = Lines [                    : AtomLinesStart     -1 ]
#AtomLines     = Lines [    AtomLinesStart  : BondLinesStart     -1 ]
BondTypeLines           = Lines [    BondTypeLinesStart        : ContraintTypeLinesStart      -1 ]
ConstraintTypeLines     = Lines [    ContraintTypeLinesStart   : AngleTypeLinesStart          -1 ]
AngleTypeLines          = Lines [    AngleTypeLinesStart       : DihedralTypeLinesStart       -1 ]
DihedralTypeLines       = Lines [ DihedralTypeLinesStart       :                                 ]

AtomType1_Atomtype2_BondtypeLexicon = {}
AtomType1_Atomtype2_Atomtype3_BondtypeLexicon = {}
AtomType1_Atomtype2_Atomtype3_Atomtype4_BondtypeLexicon = {}

for Line in BondTypeLines:

    if Line[0] not in [ ';', '[', '\n']:

       AtomType1 = Line. split ('\t') [0]
       AtomType2 = Line. split ('\t') [1]

       AtomType1_Atomtype2_BondtypeLexicon [ AtomType1+'_'+AtomType2 ] = '\t'. join ( Line. split ('\t') [2:] )
       AtomType1_Atomtype2_BondtypeLexicon [ AtomType2+'_'+AtomType1 ] = '\t'. join ( Line. split ('\t') [2:] )
 
for Line in AngleTypeLines:

    if Line[0] not in [ ';', '[', '\n']:

       if '\t' in Line:

        print Line

        AtomType1 = Line. split ('\t') [0]
        AtomType2 = Line. split ('\t') [1]
        AtomType3 = Line. split ('\t') [2]

       else:

        AtomType1 = Line. split () [0]
        AtomType2 = Line. split () [1]
        AtomType3 = Line. split () [2]

       AtomType1_Atomtype2_Atomtype3_BondtypeLexicon [ AtomType1+'_'+AtomType2+'_'+AtomType3 ] = '\t'. join ( Line. split ('\t') [3:] )
       AtomType1_Atomtype2_Atomtype3_BondtypeLexicon [ AtomType3+'_'+AtomType2+'_'+AtomType1 ] = '\t'. join ( Line. split ('\t') [3:] )




for Line in DihedralTypeLines:

    if Line[0] not in [ ';', '[', '\n']:

     AtomType1 = Line. split ('\t') [0]
     AtomType2 = Line. split ('\t') [1]
     AtomType3 = Line. split ('\t') [2]
     AtomType4 = Line. split ('\t') [3]

     AtomType1_Atomtype2_Atomtype3_Atomtype4_BondtypeLexicon [ AtomType1+'_'+AtomType2+'_'+AtomType3+'_'+AtomType4 ] = '\t'. join ( Line. split ('\t') [3:] )
     AtomType1_Atomtype2_Atomtype3_Atomtype4_BondtypeLexicon [ AtomType4+'_'+AtomType3+'_'+AtomType2+'_'+AtomType1 ] = '\t'. join ( Line. split ('\t') [3:] )

#######################################################################################

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

#       print line

       AtomNo   = int ( line.split()[0] )

       AtomType = line.split()[1] 

       AtomNo_AtomTypeLexicon [ AtomNo ] = AtomType

    Bufor. append (line)

#print 

for line in BondLines:

    if line[0] not in [ ';', '[', '\n' ]:

       AtomNo1  = int ( line. split() [0] ); AtomType1 = AtomNo_AtomTypeLexicon [ AtomNo1 ];
       AtomNo2  = int ( line. split() [1] ); AtomType2 = AtomNo_AtomTypeLexicon [ AtomNo2 ];

       Comment  = '; '+AtomNo_AtomTypeLexicon [ AtomNo1 ] + ' ' + AtomNo_AtomTypeLexicon [ AtomNo2 ] + '\n'
       try: 
        NewLine = line [:15] + AtomType1_Atomtype2_BondtypeLexicon [ AtomType1+'_'+AtomType2 ]  + Comment
       except KeyError:
        NewLine = line [:15] + 'NoBondTypeFound'  + Comment

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

       AtomType1 = AtomNo_AtomTypeLexicon [ AtomNo1 ]; AtomType2 = AtomNo_AtomTypeLexicon [ AtomNo2 ];
       AtomType3 = AtomNo_AtomTypeLexicon [ AtomNo3 ]; 


       Comment  = '; ' + AtomNo_AtomTypeLexicon [ AtomNo1 ] + ' ' + AtomNo_AtomTypeLexicon [ AtomNo2 ] \
                      +' '+ AtomNo_AtomTypeLexicon [ AtomNo3 ] + '\n'
       try:
        NewLine = line[:20] + AtomType1_Atomtype2_Atomtype3_BondtypeLexicon [ AtomType1+'_'+AtomType2+'_'+AtomType3 ]  + Comment
       except KeyError:
        NewLine = line [:15] + 'NoBondTypeFound'  + Comment

       Bufor. append (NewLine)

    else: Bufor. append ( line ) 


for line in DihedralLines:

    if line[0]  not in [ ';', '[', '\n' ]:

       AtomNo1  = int ( line. split() [0] )
       AtomNo2  = int ( line. split() [1] )
       AtomNo3  = int ( line. split() [2] )
       AtomNo4  = int ( line. split() [3] )

       AtomType1 = AtomNo_AtomTypeLexicon [ AtomNo1 ]; AtomType2 = AtomNo_AtomTypeLexicon [ AtomNo2 ];
       AtomType3 = AtomNo_AtomTypeLexicon [ AtomNo3 ]; AtomType4 = AtomNo_AtomTypeLexicon [ AtomNo4 ];
 

       Comment  = '; ' + AtomNo_AtomTypeLexicon [ AtomNo1 ] + ' ' + AtomNo_AtomTypeLexicon [ AtomNo2 ] \
                      +' '+ AtomNo_AtomTypeLexicon [ AtomNo3 ] +' '+ AtomNo_AtomTypeLexicon [ AtomNo4 ] + '\n'

       try:
        NewLine = line[:23] + AtomType1_Atomtype2_Atomtype3_Atomtype4_BondtypeLexicon [ AtomType1+'_'+AtomType2+'_'+AtomType3+'_'+AtomType4 ]  + Comment
       except KeyError:
        NewLine = line [:23] + 'NoBondTypeFound'  + Comment

#       NewLine = line[:64] + Comment

       Bufor. append (NewLine)

    else: Bufor. append ( line ) 


OutFile = open (sys. argv [2], 'w')

for Line in Bufor:

    OutFile. write (Line)

OutFile. close ()

