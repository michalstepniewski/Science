import sys

# 47 - 54        Real(8.3)       Orthogonal coordinates for Z in Angstroms.  

def WaterMoleculeInMembrane ( WaterMolecule, MembraneLimits ): 

    WaterAtomZCoord = float ( WaterAtom [ 47-1 : 54 ] )

    if (WaterAtomZCoord >= MembraneLimits [0]) and (WaterAtomZCoord <= MembraneLimits [1]): return True

    else: return False

def RemoveWatersInMembrane ( WaterMolecules, MembraneLimits ):

    for WaterMolecule in WaterMolecules:

        if WaterMoleculeInMembrane ( WaterMolecule, MembraneLimits ):

           WaterMolecules. remove ( WaterMolecule )

    return


# 18 - 20        Residue name    Residue name. 

def RemoveWatersInMembraneFromFile ( InFilePath, OutFilePath, MembraneLimits ):

    InFile = open ( InFilePath, 'r' )

    InLines = InFile. readlines ()

    InFile. close ()

    NotSOLLines = [ ]
    SOLLines    = [ ]

    for InLine in InLines:

        if InLine [:4] != 'ATOM': NotSOLLines. append (InLine)

        else:

           ResidueName  = InLine [ 18-1 : 20 ]

           if ResidueName != 'SOL':

              NotSOLLines. append (InLine)

           else:

              SOLLines. append ( InLine )

    for N in range ( int (SOLLines/3) ):

        WaterMolecule = [ SOLLines [3*N], SOLLines [(3*N)+1], SOLLines [(3*N)+2] ]

        WaterMolecules. append ( WaterMolecule )

    RemoveWatersInMembrane ( WaterMolecules, MembraneLimits )

    WaterMoleculeLines = WaterMoleculeLinesFromWaterMolecules ( WaterMolecules )

    OutFile = open ( OutFilePath, 'w' )

    for OutLine in NotSOLLines:

        OutFile. write ( NotSOLLines )

    for WaterMoleculeLine in WaterMoleculeLines:

        OutFile. write ( WaterMoleculeLine )

    OutFile. flush ()
    OutFile. close ()   

    return

def WaterMoleculeLinesFromWaterMolecules ( WaterMolecules ):

    WaterMoleculeLines = []

    for WaterMolecule in WaterMolecules:

        for WaterAtom in WaterAtoms:

            WaterMoleculeLines. append ( WaterAtom )

    return WaterMoleculeLines


MembraneLimits = [ float(sys.argv [3]), float(sys.argv[4]) ]

RemoveWatersInMembraneFromFile ( sys.argv [1], sys.argv [2], MembraneLimits )

