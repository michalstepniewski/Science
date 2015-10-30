import sys

#super, a teraz potrzebuję też translate hydrogen
##############################################33

AtomNameLexicon = { \

' HB2 ARG': ' HB1 ARG', \
' HB3 ARG': ' HB1 ARG', \
' HG2 ARG': ' HG1 ARG', \
' HG3 ARG': ' HG2 ARG', \
' HD2 ARG': ' HD1 ARG', \
' HD3 ARG': ' HD2 ARG', \


' HB2 ASN': ' HB1 ASN', \
' HB3 ASN': ' HB2 ASN', \

' HB2 ASP': ' HB1 ASP', \
' HB3 ASP': ' HB2 ASP', \

' HB2 CYS': ' HB1 CYS', \
' HB3 CYS': ' HB2 CYS', \
' HG  CYS': ' HG1 CYS', \

' HB2 GLN': ' HB1 GLN', \
' HB3 GLN': ' HB2 GLN', \
' HG2 GLN': ' HG1 GLN', \
' HG3 GLN': ' HG2 GLN', \

' HB2 GLU': ' HB1 GLU', \
' HB3 GLU': ' HB2 GLU', \
' HG2 GLU': ' HG1 GLU', \
' HG3 GLU': ' HG2 GLU', \

' HA2 GLY': ' HA1 GLY', \
' HA3 GLY': ' HA2 GLY', \

' HB2 HSD': ' HB1 HSD', \
' HB3 HSD': ' HB2 HSD', \

' HB2 HSE': ' HB1 HSE', \
' HB3 HSE': ' HB2 HSE', \
 
'HG12 ILE': 'HG11 ILE', \
'HG13 ILE': 'HG12 ILE', \

'HD11 ILE': ' HD1 ILE', \
'HD12 ILE': ' HD2 ILE', \
'HD13 ILE': ' HD3 ILE', \

' HB2 LEU': ' HB1 LEU', \
' HB3 LEU': ' HB2 LEU', \
 
' HB2 LYS': ' HB1 LYS', \
' HB3 LYS': ' HB2 LYS', \

' HG2 LYS': ' HG1 LYS', \
' HG3 LYS': ' HG2 LYS', \

' HD2 LYS': ' HD1 LYS', \
' HD3 LYS': ' HD2 LYS', \
 
' HE2 LYS': ' HE1 LYS', \
' HE3 LYS': ' HE2 LYS', \

' HB2 MET': ' HB1 MET', \
' HB3 MET': ' HB2 MET', \

' HG2 MET': ' HG1 MET', \
' HG3 MET': ' HG2 MET', \

' HB2 PHE': ' HB1 PHE', \
' HB3 PHE': ' HB2 PHE', \

' HB2 PRO': ' HB1 PRO', \
' HB3 PRO': ' HB2 PRO', \
' HG2 PRO': ' HG1 PRO', \
' HG3 PRO': ' HG2 PRO', \
' HD2 PRO': ' HD1 PRO', \
' HD3 PRO': ' HD2 PRO', \

' HB2 SER': ' HB1 SER', \
' HB3 SER': ' HB2 SER', \
' HG  SER': ' HG1 SER', \

' HB2 TRP': ' HB1 TRP', \
' HB3 TRP': ' HB2 TRP', \

' HB2 TYR': ' HB1 TYR', \
' HB3 TYR': ' HB2 TYR', \

}
# to musze tylko spojrzec w pdb
################################################

ResidueAtomOrderLexicon = {}

ResidueAtomOrderLexicon ['ARG'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','HG1','HG2','CD','HD1','HD2','NE','HE','CZ','NH1','HH11','HH12','NH2','HH21','HH22','C','O']
ResidueAtomOrderLexicon ['HIS'] = [' N  ','HN','CA','HA','CB','HB1','HB2','ND1','CG','CE1','HE1','NE2','HE2','CD2','HD2','C','O']
ResidueAtomOrderLexicon ['LYS'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','HG1','HG2','CD','HD1','HD2','CE','HE1','HE2','NZ','HZ1','HZ2','HZ3','C','O']

ResidueAtomOrderLexicon ['ASP'] = [' N  ','HN','CA','HA','CB','HB','HB1','HB2','CG','OD1','OD2','C','O']
ResidueAtomOrderLexicon ['GLU'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','HG1','HG2','CD','OE1','OE2','C','O']

ResidueAtomOrderLexicon ['SER'] = [' N  ','HN','CA','HA','CB','HB1','HB2','OG','HG1','C','O']
ResidueAtomOrderLexicon ['THR'] = [' N  ','HN','CA','HA','CB','HB','OG1','OG2','CG2','HG21','HG22','HG23','C','O']

ResidueAtomOrderLexicon ['ASN'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','OD1','ND2','HD21','HD22','C','O']
ResidueAtomOrderLexicon ['GLN'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','HG1','HG2','CD','OE1','NE2','HE21','HE22','C','O']
ResidueAtomOrderLexicon ['CYS'] = [' N  ','HN','CA','HA','CB','HB1','HB2','SG','C','O']

ResidueAtomOrderLexicon ['GLY'] = [' N  ','HN','CA','HA1','HA2','C','O']

ResidueAtomOrderLexicon ['PRO'] = [' N  ','CD','HD1','HD2','CA','HA','CB','HB1','HB2','CG','HG1','HG2','C','O']

ResidueAtomOrderLexicon ['ALA'] = [' N  ','HN','CA','HA','CB','HB1','HB2','HB3','C','O']

ResidueAtomOrderLexicon ['VAL'] = [' N  ','HN','CA','HA','CB','HB','CG1','HG11','HG12','HG13','CG2','HG21','HG22','HG23','C','O']
ResidueAtomOrderLexicon ['ILE'] = [' N  ','HN','CA','HA','CB','HB','CG2','HG21','HG22','HG23','CG1','HG11','HG12','CD','HD1','HD2','HD3','C','O']
ResidueAtomOrderLexicon ['LEU'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','HG','CD1','HD11','HD12','HD13','CD2','HD21','HD22','HD23','C','O']

ResidueAtomOrderLexicon ['MET'] = [' N  ','H1','H2','H3','CA','HA','CB','HB1','HB2','CG','HG1','HG2','SD','CE','HE1','HE2','HE3']
ResidueAtomOrderLexicon ['PHE'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','CD1','HD1','CE1','HE1','CZ','HZ','CD2','HD2','CE2','HE2','C','O']

ResidueAtomOrderLexicon ['TYR'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','CD1','HD1','CE1','HE1','CZ','OH','HH','CD2','HD2','CE2','HE2','C','O']
ResidueAtomOrderLexicon ['TYS'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','CD1','HD1','CE1','HE1','CZ','OH','S','CD2','HD2','CE2','HE2','C','O','O1','O2','O3']
ResidueAtomOrderLexicon ['TRP'] = [' N  ','HN','CA','HA','CB','HB1','HB2','CG','CD1','HD1','NE1','HE1','CE2','CD2','CE3','HE3','CZ3','HZ3','CZ2','HZ2','CH2','HH2','C','O']

###############################################################################
# 13 - 16 Atom Atom name.

def OutputAccordingToAtomOrder ( ResidueLines ):
# 18 - 20 Residue name Residue name.
    NewAtomLines = []

    AtomLine = {}

#    print ResidueLines

    for ResidueLine in ResidueLines:

        ResidueName = ResidueLine [18-1:20]
        AtomName = ResidueLine[13-1:16]

        AtomLine[AtomName] = ResidueLine

    print AtomLine

    AtomOrder = ResidueAtomOrderLexicon [ ResidueName ]

    for AtomName in AtomOrder:

        NewAtomLines. append ( AtomLine[AtomName] )

    return NewAtomLines

###############################################################################

def OutputResiduesAccordingToAtomOrder ( Residues ):

    NewLines = []

    for Residue in Residues:

        NewResidue = OutputAccordingToAtomOrder ( Residue )

        for NewLine in NewResidue:

            NewLines. append (NewLine)

    return NewLines

###############################################################################
# 23 - 26 Integer Residue sequence number.

def SplitPreAtomPostLines (Lines):

    PreAtomLines = []; AtomLines = []; PostAtomLines = [];

    N = 0

    while Lines[N][:4] != 'ATOM':

          PreAtomLines. append ( Lines[N] ) 
          N=N+1

    while Lines[N][:4] == 'ATOM':

          AtomLines. append ( Lines[N] ) 
          N=N+1

    while N<=len(Lines)-1:

          PostAtomLines. append ( Lines[N] ) 
          N=N+1

    return [ PreAtomLines, AtomLines, PostAtomLines ]

###############################################################################


def SplitLinesIntoResidues ( Lines ):

    Residues = []
    Residue  = []
    PreviousResidueNumber = ''

    for Line in Lines:

        ResidueNumber = Line[23-1:26]

        if ResidueNumber!= PreviousResidueNumber:

           Residues. append (Residue)
           Residue = []

        Residue. append (Line)

        PreviousResidueNumber = ResidueNumber

    return Residues[1:]

###############################################################################

def ProcessLines (Lines):

    NewLines = []

    PreAtomLines, AtomLines, PostAtomLines = SplitPreAtomPostLines (Lines)

    Residues = SplitLinesIntoResidues (AtomLines)
    NewAtomLines = OutputResiduesAccordingToAtomOrder ( Residues )

    NewLines = []

    for Line in  PreAtomLines: NewLines. append ( Line )
    for Line in     AtomLines: NewLines. append ( Line )
    for Line in PostAtomLines: NewLines. append ( Line )

    return NewLines

###############################################################################

def ProcessFile (InFileName,OutFileName):

    InFile = open (InFileName,'r' )
    Lines  = InFile. readlines()
    InFile. close ()
    NewLines = ProcessLines (Lines)

    OutFile = open (OutFileName,'w')

    for NewLine in NewLines:

        OutFile. write (NewLine)

    OutFile. flush ()
    OutFile. close ()

    return 

#################################################################################

ProcessFile (sys.argv[1], sys. argv[2])
