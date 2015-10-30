from math import sqrt
import sys

def PointContact (Point1, Point2, Threshold):

    if Distance (Point1,Point2) <= Threshold: return True
    else: return False

####################################################################################################

def Distance (Point1,Point2):

    return sqrt ( ((Point1[0]- Point2[0])**2.0) + ((Point1[1]- Point2[1])**2.0) + ((Point1[2]- Point2[2])**2.0) )

####################################################################################################
#troche przejebane

####################################################################################################

def ECL2LowestDistanceToMAb ( ECL2, mAb):
    LowestDistances = []

    for Residue1 in ECL2:

        LowestDistances. append ( '%s %8.3f \n' %(Residue1[0][18-1:27], ResLowestDistanceToMAb (Residue1, mAb))   )  
#        print '%s %8.3f' %(Residue1[0][18-1:27], ResLowestDistanceToMAb (Residue1, mAb)) 

    return LowestDistances

####################################################################################################


def ResLowestDistanceToMAb (Residue1, mAb):

    LowestDistance = 1000.0

    for Residue2 in mAb:

        LowestDistanceI = ResLowestDistancetoRes ( Residue1, Residue2 )

        if LowestDistanceI <= LowestDistance:

           LowestDistance = LowestDistanceI

    return LowestDistance

####################################################################################################

def ResLowestDistancetoRes ( Residue1, Residue2 ):

    LowestDistance = 1000

    for Atom1 in Residue1:

        for Atom2 in Residue2:

            AtomDistanceI = AtomDistance ( Atom1, Atom2)

            if AtomDistanceI <= LowestDistance:

               LowestDistance = AtomDistanceI

    return LowestDistance
####################################################################################################

def AtomDistance (Atom1,Atom2):

# 31 - 38        Real(8.3)       Orthogonal coordinates for X in Angstroms.
# 39 - 46        Real(8.3)       Orthogonal coordinates for Y in Angstroms.
# 47 - 54        Real(8.3)       Orthogonal coordinates for Z in Angstroms.

    Point1 = [ float(Atom1 [31-1:38]), float(Atom1 [39-1:46]), float(Atom1 [47-1:54]) ]
    Point2 = [ float(Atom2 [31-1:38]), float(Atom2 [39-1:46]), float(Atom2 [47-1:54]) ]
#    print Point1

    return Distance (Point1,Point2)
####################################################################################################

def AtomContact (Atom1,Atom2,Threshold):

# 31 - 38        Real(8.3)       Orthogonal coordinates for X in Angstroms.
# 39 - 46        Real(8.3)       Orthogonal coordinates for Y in Angstroms.
# 47 - 54        Real(8.3)       Orthogonal coordinates for Z in Angstroms.

    Point1 = [ float(Atom1 [31-1:38]), float(Atom1 [39-1:46]), float(Atom1 [47-1:54]) ]
    Point2 = [ float(Atom2 [31-1:38]), float(Atom2 [39-1:46]), float(Atom2 [47-1:54]) ]
#    print Point1

    return PointContact (Point1,Point2,Threshold)

####################################################################################################

def ResidueContact (Residue1, Residue2, Threshold):
# zakladam ze wszystkie jednak

    for Atom1 in Residue1:
        for Atom2 in Residue2:

            if AtomContact (Atom1, Atom2, Threshold): return True
   
    return False

####################################################################################################

def ResidueShortestDistance (Residue1, Residue2, Threshold):
# zakladam ze wszystkie jednak

    for Atom1 in Residue1:
        for Atom2 in Residue2:

            if AtomContact (Atom1, Atom2, Threshold): return True
   
    return False

####################################################################################################

def ResiduesContacts (Residues1, Residues2, Threshold):

    Contacts = [ ]

    for Residue1 in Residues1:

        for Residue2 in Residues2:        

            if ResidueContact (Residue1, Residue2, Threshold):

               Contacts. append ( [ Residue1, Residue2 ]  )

    return Contacts

# teraz jak bedziemy wybierac te reszty?

####################################################################################################
#usunac wodory, ale jak ...
def ResiduesContactsInFrames (InFilePath, OutFilePath):

    InFile = open ( InFilePath, 'r' )
    Title =''
    OutFile = open ( OutFilePath, 'w' )

    InLine = ' '

    Frame = [ ]

    while InLine:

          InLine = InFile. readline () 

          if InLine[:6] == 'ENDMDL':
#             print 'ENDMDL'
             print Title
             OutFile. write ( Title )

             for OutLine in ResidueContactsInFrame (Frame):

                 OutFile. write ( OutLine )

             Frame = [ ]


          elif InLine[:5] == 'TITLE':

             Title = InLine

          else:

             Frame. append ( InLine )

#mozliwe ze drukowanie

    InFile. close ()
    OutFile. flush()
    OutFile. close()

    return

####################################################################################################

#ECL2- zakres
# przeciwcialo, chains H i L
# 

# >sp|P51681|167-198
# TRSQKEGLHYTCSSHFPYSQYQFWKNFQTLKI

def ExtractAtoms ( Lines ):

    Atoms = []

    for Line in Lines:

        if Line[:4] == 'ATOM':

           Atoms. append (Line)

    return Atoms

####################################################################################################

def ExtractHeavyAtoms ( Lines ):

    Atoms = []

    for Line in Lines:

        if Line[:4] == 'ATOM'and Line[14-1]!='H':

           Atoms. append (Line)

    return Atoms

####################################################################################################

def SplitToResidues ( AtomLines ):

    PrevResSeqNo = ' '

    Residue = []

    Residues = []

    for Line in AtomLines:

#23 - 26        Integer         Residue sequence number. 
        ResSeqNo = Line [ 23-1:26 ]

        if ResSeqNo != PrevResSeqNo:

           PrevResSeqNo = ResSeqNo

           Residues. append ( Residue )

           Residue = [ ]

        Residue. append ( Line )

    Residues. append ( Residue )

    return Residues[1:]

####################################################################################################

def PickResiduesByChainName (Residues, ChainName):

    SelectedResidues = []

    for Residue in Residues:

        ResChainName = Residue[0][22-1]

        if ResChainName == ChainName:

           SelectedResidues. append ( Residue )

    return SelectedResidues

####################################################################################################

def PickResiduesByResSeqNo (Residues, SeqNoRange ):

    SelectedResidues = []

#23 - 26        Integer         Residue sequence number. 

    for Residue in Residues:

        ResSeqNo = int(Residue[0][23-1:26])

        if ResSeqNo >= SeqNoRange[0] and ResSeqNo <= SeqNoRange[1]:

           SelectedResidues. append ( Residue )

    return SelectedResidues

####################################################################################################

def ResidueContactsInFrame (Frame):

    HeavyAtoms = ExtractHeavyAtoms (Frame)
#    print Atoms

    Residues = SplitToResidues ( HeavyAtoms )
#    print Residues[0]; quit()
#    print Residues
    chainA = PickResiduesByChainName ( Residues, 'A' )
#    print chainA
    ECL2 = PickResiduesByResSeqNo (chainA, [167, 198] )



#    print ECL2[0]; quit ()
    chainH = PickResiduesByChainName ( Residues, 'H' )

    chainL = PickResiduesByChainName ( Residues, 'L' )

    mAb = [ ]

    for Residue in chainH:

        mAb. append (Residue)

    for Residue in chainL:

        mAb. append (Residue)

    ECL2LowestDistanceToMAb ( ECL2, mAb)

#    Contacts = ResiduesContacts (ECL2, Przeciwcialo, 3.0)

#    for Contact in Contacts: print Contact

    return ECL2LowestDistanceToMAb ( ECL2, mAb)

####################################################################################################

ResiduesContactsInFrames (sys. argv[1], sys.argv[2])
