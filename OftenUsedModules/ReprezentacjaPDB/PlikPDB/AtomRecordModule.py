import PdbRecordModule; from PdbRecordModule import *;

import GeometricalClassesModule;
from   GeometricalClassesModule  import Point


#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

class AtomRecord ( object ):  #mozna by tylko dawac te rzeczy przy inicjalizacji                                               # ATOM record

   def __init__(self, *args, **kwargs):

       self. s = str(*args, **kwargs)
       self. X = float( self.s[(31-1):(38)] )
       self. Y = float( self.s[(39-1):(46)] )
       self. Z = float( self.s[(47-1):(54)] )
       self. XYZ = Point([ self.X, self.Y, self.Z ])

       self. Name = self.s[(13-1):(16)]
       self. AAThreeLetter = self.s [ (18-1) : (20) ]

#####################################################################################################################################################

   def HydrogenBondDonor ( self ):

       Type = 'NH '

       AminoacidAtomLexicon = { 'ARG' : 'NE ', \
                                'ASN' : 'ND2', \
                                'HIS' : 'NE2', \
                                'SER' : 'OG ', \
                                'TYR' : 'OH ', \
                                'ARG' : 'NH1', \
                                'CYS' : 'SG ', \
                                'HIS' : 'ND1', \
                                'THR' : 'OG1', \
                                'ARG' : 'NH2', \
                                'GLN' : 'NE2', \
                                'LYS' : 'NZ ', \
                                'TRP' : 'NE1'    }

       if self. Name == Type:

          return True

       elif self. AAThreeLetter in AminoacidAtomLexicon. keys ( ):

            if self. Name == AminoacidAtomLexicon [ self. AAThreeLetter ]:

               return True

       return False

# Hydrogen donor protein atoms
# analyzed in this study were: NH of the main chain, ARG NE,
# ASN ND2, HIS NE2, SER OG, TYR OH, ARG NH1, CYS
# SG, HIS ND1, THR OG1, ARG NH2, GLN NE2, LYS NZ
# and TRP NE1; 

#####################################################################################################################################################

   def HydrogenBondAcceptor ( self ):

       Type = 'O  '

       AminoacidAtomLexicon = { 'ASN' : 'OD1', \
                                'GLN' : 'OE1', \
                                'MET' : 'SD ', \
                                'ASP' : 'OD1', \
                                'GLU' : 'OE1', \
                                'SER' : 'OG ', \
                                'ASP' : 'OD2', \
                                'GLU' : 'OE2', \
                                'THR' : 'OG1', \
                                'CYH' : 'SG ', \
                                'HIS' : 'ND1', \
                                'TYR' : 'OH '     }

       if self. Name == Type:

          return True

       elif self. AAThreeLetter in AminoacidAtomLexicon. keys ( ):

            if self. Name == AminoacidAtomLexicon [ self. AAThreeLetter ]:

               return True

       return False

# Acceptor atoms were: carboxyl oxygen of the
# main chain, ASN OD1, GLN OE1, MET SD, ASP OD1, GLU
# OE1, SER OG, ASP OD2, GLU OE2, THR OG1,CYH SG,
# HIS ND1 and TYR OH.

#####################################################################################################################################################

   def Print ( self ):
       print self.s

#####################################################################################################################################################
 
#   def AtomName ( self ):                          #13 - 16        Atom            Atom name.

#       self.Name=self.s[(13-1):(16)]

#       return self.Name

#####################################################################################################################################################

   def Element ( self ): # 77 - 78        LString(2)      Element symbol, right-justified.  

       self.ElementI = self.s [ (77-1): 78 ]

       if self.ElementI == '  ':

          self.ElementI = ' '+self.s [ 13 ] # ' ' added for internal consistency reasons

       return self.ElementI

#####################################################################################################################################################

                                  #23 - 26        Integer         Residue sequence number. 
   def ResidueSequenceNumber ( self ):

#       print self.s

       self.ResSeqNo = int ( self.s [23:26] ) # watch out!

       return self.ResSeqNo

#####################################################################################################################################################

   def Mass ( self ):

# 77 - 78        LString(2)      Element symbol, right-justified.

#       print self.s[ (77-1): (79-1)  ]

       Element = self.s [ (77-1):(79-1) ]

       ElementMassLexicon =  { ' C' : 12.011, \
                               ' H' : 1.008 , \
                               ' O' : 15.999, \
                               ' N' : 14.007, \
                               ' P' : 30.973762, \
                               ' S' : 32.06         }

       try:

            Mass = ElementMassLexicon [ Element ]

       except KeyError:

            Element = ' '+self.s [ 13 ]
            Mass = ElementMassLexicon [ Element ]

       return Mass

#####################################################################################################################################################

   def AA ( self ):

       ThreeLetterToOneLetterLexicon      = { 'ARG' : 'R', \
                                              'HIS' : 'H', \
                                              'LYS' : 'K', \
                                              'ASP' : 'D', \
                                              'GLU' : 'E', \
                                              'SER' : 'S', \
                                              'THR' : 'T', \
                                              'ASN' : 'N', \
                                              'GLN' : 'Q', \
                                              'CYS' : 'C', \
                                              'SEC' : 'U', \
                                              'GLY' : 'G', \
                                              'PRO' : 'P', \
                                              'ALA' : 'A', \
                                              'VAL' : 'V', \
                                              'ILE' : 'I', \
                                              'LEU' : 'L', \
                                              'MET' : 'M', \
                                              'PHE' : 'F', \
                                              'TYR' : 'Y', \
                                              'TRP' : 'W', \
                                              'UNK' : 'X'    }

       self.AAOneLetter = ThreeLetterToOneLetterLexicon [ self.AAThreeLetter ] 
    
       return self.AAOneLetter

#####################################################################################################################################################

   def Chain ( self ):

       self.ChainID = self.s [ (22-1) ]

       return self.ChainID

#####################################################################################################################################################

   def VdWRadius ( self ):

       ElementRadiusLexicon = { ' H' : 1.20, \
                                ' C' : 1.70, \
                                ' N' : 1.55, \
                                ' O' : 1.52, \
                                ' F' : 1.47, \
                                ' P' : 1.80, \
                                ' S' : 1.80, \
                                'CL' : 1.75, \
                                'CU' : 1.4, }

       VdWRadiusI = ElementRadiusLexicon [ self.Element() ]

       return VdWRadiusI

#####################################################################################################################################################

   def RotateByMatrix ( self, RotationMatrix ):

       self. XYZ. Rotate ( RotationMatrix )

       [ self. X, self.Y, self.Z ]  = self. XYZ # ok :)

       self.s = self.s [ :30 ]+ ''.join( [ '%8.3f' % Coord for Coord in self. XYZ ]) +self.s[ 54: ]

#####################################################################################################################################################

   def Translate ( self, Vector ):

#       print self. XYZ
#       print Vector

       self. XYZ. Translate ( Vector )

#       print self. XYZ

       [ self. X, self.Y, self.Z ]  = self. XYZ

       self.s = self.s [ :30 ]+ ''.join( [ '%8.3f' % Coord for Coord in self. XYZ ]) + self.s[ 54: ]

