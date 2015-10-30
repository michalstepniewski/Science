import sys
import Parametry

import inspect


import AtomRecordsModule;
from  AtomRecordsModule import AtomRecords;

import TMHelixModule; from TMHelixModule import *;

import AtomRecordModule;
from   AtomRecordModule import *;

import SetOfAtomsModule; from SetOfAtomsModule import Residue, SetOfResidues;

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

class SetOfSetsOfResidues ( list ):

      def __init__ ( self, InputSetsOfResidues ):

          self. Content = [ InputSetOfResidues for InputSetOfResidues in InputSetsOfResidues ]

#####################################################################################################################################################
# musze to uporzadkowac od poczatku
      def Print ( self ):

          [ SetOfResiduesInstance. Print ( ) for SetOfResiduesInstance in self. Content ]

      
#####################################################################################################################################################
#####################################################################################################################################################

class ProteinChain ( SetOfResidues ): # ok lets say the it consists of Residues
# or maybe list of residues

   def __init__ (self, InputResidueInstances, InputChainID = 'X' ):

       self.Content = []    
       self.ChainID = InputChainID 

       for InputResidueInstance in InputResidueInstances: 
           
#           ResidueInstance = Residue ( InputResidueInstance ) # dlatego z tym tez sobie dajemy spokoj chwilowo
#           ResidueInstance. Print ()
           self.Content. append ( InputResidueInstance ) # chwilowo, ciezko wymyslec dobry konstruktor

# problem pojawia sie w inicjowaniu z ResidueInstance w robieniu Residue z ResidueInstance i to jest bol...
# na razie zostawmy to tak

#####################################################################################################################################################

   def OutputToPdbFile ( self, Path ):

       FileName = Path  + self.ChainID + '.pdb';

       OpenedFileInstance = open ( FileName, 'w' )

       for ResidueInstance in self.Content:

           for AtomRecordInstance in ResidueInstance.Content:

               OpenedFileInstance.write ( AtomRecordInstance.s ) # powinienem to bardziej hierarchicznie zdefiniowac I pass File Instance to another file  

       OpenedFileInstance.flush ( ); OpenedFileInstance.close ( );

       print 'PDB File written'

#####################################################################################################################################################

   def IsPairABridge ( self, ListOfResidues ):

       Residue1 = PickResidueByNumber ( ResiduesList [0] )

       Residue2 = PickResidueByNumber ( ResiduesList [1] )

       if SetOfResidues ( [ Residue1, Residue2  ] ).IsABridge:

          return True

       return False

#####################################################################################################################################################

   def ArePairsBridges ( self, ListsOfResidues ):

       self. NoCorrectPredictions = 0

       Lexicon = { }

       for ResiduePair in ListsOfResidues:

           if self. IsPairABridge ( ResiduePair ):

              Lexicon [ ResiduePair ] = 1

              self. NoCorrectPredictions += 1

       return Lexicon

#####################################################################################################################################################

   def AASEQ ( self ):

       self.AASEQ = ''

       return ''.join ( [ self.Residue. AA ( ) for self. Residue in self. Content ] )

#####################################################################################################################################################
# ok, to teraz moze sprobuje to outputowac :)

   def AASEQ_Z ( self ):

       return '\n'.join([ ' '.join(['#AASEQ_Z TM', str(self. ID), self.Residue. AA ( ), str( self.Residue. Z ( ) ) ]) for self.Residue in self.Content ]) + '\n'

#####################################################################################################################################################

   def Segment (FirstResNo, LastResNo ):

       self. Segment = [ ]

       for self.Residue in self.Content:

           if ( FirstResNo <= self.Residue.SequenceNumber ( ) <= LastResNo ):

              self. Segment. append ( self. Residue ) 

       return self. Segment

#####################################################################################################################################################

   def MRegionResidues (self): #need to define class Residue, the Residues of Membrane Region

       self.MResidues = [ ]

       for self.Residue in self.Content: 

           if self.Residue .M ( ): # if it is in the membrane

              self.MResidues.append ( self.Residue )

       return self.MResidues

#####################################################################################################################################################
# ze dlugie, trzebaby uproscic #

   def MRegionResiduesSegments ( self ): # the Segments of Membrane Region, # how to handle soluble chains!, i need to make it more systematic

       self. MRegionResidues_I = self. MRegionResidues ( )

       # wiec sa jakies ekstrahowane. A jak jest z segmentami? ech spac ... 

       self. MRegionResiduesSegments_I = [ ];

       if self.MRegionResidues_I != [ ]:

          self.MRegionResiduesSegment = [ ];

          self.MRegionResiduesSegment.append ( self.MRegionResidues_I [ 0 ] ) # take care of the First Residue

          for N in range ( 1, len ( self.MRegionResidues_I ) ):

              if self.MRegionResidues_I [ N ]. SequenceNumber ( ) - self.MRegionResidues_I [ N - 1 ]. SequenceNumber ( ) == 1 :
#dosyc tego, zrobie tu ladny porzadek, wlasnie na tym pliku, bez zadnych szemranych rzeczy

                 self.MRegionResiduesSegment.append ( self.MRegionResidues_I [ N ] )
       
              else:
                 self.MRegionResiduesSegments_I. append ( SetOfResidues( self.MRegionResiduesSegment ) )

                 self.MRegionResiduesSegment = [ ]

                 self.MRegionResiduesSegment.append ( self.MRegionResidues_I [ N ] )
                 

          self.MRegionResiduesSegments_I. append ( SetOfResidues( self.MRegionResiduesSegment ) ) # take care of the last one
                                                                              # there are always some problems with that
       self.MRegionResiduesSegment = [ ]

#       [ MRegionResiduesSegment_I. Print () for MRegionResiduesSegment_I in self.MRegionResiduesSegments_I ]
       # a wiec ekstrahowane sa i segmenty
       return SetOfSetsOfResidues ( self. MRegionResiduesSegments_I ) # these are Membrane Region Segments, now we need to check if the Segment
                                           # is TransMembrane

#####################################################################################################################################################
# wszystko bedziemy tu drukowac, az dojdziemy, gdzie jest blad, przy okazji zrobimy porzadek!

   def TMSegments ( self ): # musze powaznie przemyslec w ktorym miejscu mojego programu pojawiaja sie parametry
       import TMHelixModule; from TMHelixModule import TMHelix; # problem polega na tym ze oba moduly wzajemne sie przywoluja

       MSegments = self. MRegionResiduesSegments ( ) # sprawdzamy to teraz

#       MSegments. Print ( ) # musimy zrobic tak zeby mialo to klase

# musze zrobic porzadek bo inaczej sie nie uda

       TMSegments_I = [ ]

       ID = 1

       for MSegmentI in MSegments.Content: # bo MSegments teraz same sa klasa

           MSegmentInstance = MSegment ( MSegmentI.Content ) # musze sprawdzic konstruktor tego MSegmenta

#           MSegmentInstance. Print ( )

#           if MSegmentInstance. TransMembrane (): # a moze z kontentu?

#              TMSegments_I. append ( TMHelix ( MSegmentInstance.Content, ID, ParametersInstance ) ); ID=ID+1;

#           for Monotonic in MSegmentInstance. ExtractMonotonics ( ):
#               Monotonic. Print ()

           if MSegmentInstance. CrossingMembrane () and  MSegmentInstance. TransMembrane ( ) and MSegmentInstance. Filtered ( ) :

#                  TMSegments_I. append ( TMHelix ( MSegmentInstance, ID, ParametersInstance ) ); ID=ID+1; # i teraz to zadziala

                  TMSegments_I. append ( TMHelix ( MSegmentInstance.Content, ID ) ); ID=ID+1; # i teraz to zadziala

       return   TMSegments_I

#####################################################################################################################################################

   def ProteinNterOrientation ( self ):

       NterOrientation_I = self. TMSegments ( ) [ 0 ]. NterDescriptor ( )

       return NterOrientation_I

#####################################################################################################################################################
#####################################################################################################################################################

class MSegment ( ProteinChain ): # dziedziczy konstruktor, a sam jest juz protein chainem, moze to zle

# a moze sie oplaca zeby dziedziczyl konstruktor z segmentu

#####################################################################################################################################################

      def CrossingMembrane ( self, MembraneBorders = [-10.0, 10.0 ] ) : # musi byc to sczytywane z parametrow

          FirstZ = self.Content [ 0 ]. Z ()

          if FirstZ <= 0.0:

             for ResidueI in self.Content:

                 if ResidueI. Z () >= 0.0: return True

          elif FirstZ >= 0.0:

             for ResidueI in self.Content:

                 if ResidueI. Z () <= 0.0: return True

          return False

#####################################################################################################################################################
# ok to teraz do read parameter file? czy nie?
      def Filtered ( self ):

# jesli gdzies bedzie zle to nie jest filtered, wiec jest false
          SlicesBorders = [ [ -12.0, -6.00 ], [ -3.00, 3.00 ], [ 6.00, 12.00 ] ] 

          NoAAsInSlices = [ 0, 0, 0 ]

          for ResidueI in self.Content:
              
              ResidueI_Z = ResidueI. Z ()

              for N in range(len (SlicesBorders) ):

                  if ( ResidueI_Z >= SlicesBorders[N][0]) and ( ResidueI_Z <= SlicesBorders[N][1] ):

                     NoAAsInSlices [N] += 1 
                     
          for N in range(len (SlicesBorders) ):
          
              if (NoAAsInSlices [N] <= (Parametry. NoAAPerSliceRange[0]-1)) or (NoAAsInSlices [N] >=( Parametry. NoAAPerSliceRange[1]-1)):

                 print Parametry. NoAAPerSliceRange[0]; print Parametry. NoAAPerSliceRange[1];

                 print NoAAsInSlices [N]; print 'too little or too many AAs in slices';#  quit ();

                 return False 
         
          print 'Found Filtered Helix'; # quit ();
          return True

#####################################################################################################################################################

      def TiltConsistent (self):

          if self. PCAMCTiltDifference <= Parametry. PCAMCTiltDifferenceThreshold:

             return True

#####################################################################################################################################################

      def Helical (self):

          if self. PercentHelicity >= Parametry. PercentHelicityThreshold:

             return True

          else:

             return False

#####################################################################################################################################################


      def TransMembrane ( self, MembraneBorders = [-10.0, 10.0 ] ) : # musi byc to sczytywane z parametrow 

#powinienem to sparametryzowac

          FirstZ, LastZ = [ ResidueI. Z ( ) for ResidueI in [ self.Content [ 0 ], self.Content [ -1 ] ]  ]

          if ( ( FirstZ <= MembraneBorders [0] ) and ( LastZ >= MembraneBorders [1] ) ) or \
             ( ( FirstZ >=  MembraneBorders [1] ) and ( LastZ <= MembraneBorders [0] ) ):

             return True

          else:

             return False

#####################################################################################################################################################

      def Monotoniczny ( self, Threshold = 5.0 ):

          FirstZ = self.Content [ 0 ]. Z ( );

          if FirstZ <= 0.0:

             HighestZ = FirstZ

             for ResidueI in self.Content:

                 HighestZ = max ( HighestZ, ResidueI. Z ( ) )

                 MonotonicityDeviation = HighestZ - ResidueI. Z ( )

                 if MonotonicityDeviation >= Threshold:

                    return False

          elif FirstZ >= 0.0:

             LowestZ = FirstZ

             for ResidueI in self.Content:

                 LowestZ = min ( LowestZ, ResidueI. Z ( ) )

                 MonotonicityDeviation = ResidueI. Z ( ) - LowestZ

                 if MonotonicityDeviation >= Threshold:

                    return False

          return True

#####################################################################################################################################################

      def ExtractMonotonics ( self, Threshold = 5.0 ):

          Monotonics = [ ]

          FirstZ = self.Content [ 0 ]. Z ( );

          Monotonic = [ ]

          N = 0

          while N <= ( len ( self. Content ) -1 ):
                Monotonic = [ ]

                FirstZ = self.Content [ N ]. Z ( )

                if FirstZ <= 0.0: # jesli jest mniejszy od zera?

                   HighestZ = FirstZ

                   MonotonicityDeviation = HighestZ - self.Content [ N ]. Z ( )
                   Monotonic = [ ]

                   while N <= ( len ( self. Content ) - 1 ) and MonotonicityDeviation <= Threshold :

                         HighestZ = max ( HighestZ, self.Content [ N ]. Z ( ) )

                         MonotonicityDeviation = HighestZ - self.Content [ N ]. Z ( )

                         Monotonic. append ( self.Content [ N ] )

                         N += 1

                   Monotonics. append ( MSegment ( Monotonic ) )
                   Monotonic = [ ]

                elif FirstZ >= 0.0:

                   LowestZ = FirstZ

                   MonotonicityDeviation = self.Content [ N ]. Z ( ) - LowestZ
                   Monotonic = [ ]

                   while N <= ( len ( self. Content ) -1 ) and MonotonicityDeviation <= Threshold :

                         LowestZ = min ( LowestZ, self.Content [ N ]. Z ( ) ) 

                         MonotonicityDeviation = self.Content [ N ]. Z ( ) - LowestZ

                         Monotonic. append ( self.Content [ N ] )

                         N += 1

                   Monotonics. append ( MSegment ( Monotonic ) )
                   Monotonic = [ ]
          
          return Monotonics
