####################################################################################################################################################
####################################################################################################################################################
#################################################################################################################################################### 
import sys;
import Kombinatoryka; from Kombinatoryka import *;

from PDB_FileContentsModule import PdbFileContent
from SetOfN_TMs_SetRepresentationsModule import SetOfN_TMs_SetRepresentations
from GeometricalClassesModule import HierarchicalSetOfPoints

import sys

from TextLinesModule import *

MainDirectory = './DaneWyjsciowe/ExtractedTransmembraneHelices'
# MainDirectory = './DaneWyjsciowe/ExtractedTransmembraneHelicesInteracting'

def grabHelix ( Family, PDBCode, ChainID, HelixID ): # ok czyli mozna sie tym probowac juz bawic, ale powinienem isc spac teraz

   InputPath = MainDirectory + '/' + Family  + '/' +  PDBCode +'/' + ChainID + '/' + PDBCode + '_' + ChainID + '_' + HelixID + '.pdb'

   PDBFileContentsInstance = ReadLinesFromFile ( InputPath );

#   ProteinChainInstance = PDBFileContentsInstance.ExtractProteinChains ( ) [0]

   return PDBFileContentsInstance

#################################################################################################################################################### 

def ParallelPairs ( CrossAngMatrix, DihAngMatrix ):

    ParallelPairs = [ ]

    Pairs = [ [0,1,2],[1,2,0],[0,2,1] ]

#    Lexicon = {}; Lexicon [ 0_1

### osobno dla gory i osobno dla dolu
### jesli dwie helisy sa parallell 
### to zdefiniujmy plaszczyzne przez HalfHelix-COM
### i sprawdzmy dihedral tej plaszczyzny z plaszczyzne HH-os Z ale najpierw projekt 

    for Pair in Pairs:

           if -15.0 <= DihAngMatrix [Pair[0]] [Pair[1]] >= 15.0:
              
              if -15.0 <= CrossAngMatrix [Pair[0]] [Pair[1]] <= 15.0:

                 ParallelPairs. append ( Pair )

    return ParallelPairs
#################################################################################################################################################### 

def ParallelRozkraki ( CrossAngMatrix, DihAngMatrix ):

    ParallelPairs = [ ]

    Pairs = [ [0,1,2],[1,2,0],[0,2,1] ]

#    Lexicon = {}; Lexicon [ 0_1

### osobno dla gory i osobno dla dolu
### jesli dwie helisy sa parallell 
### to zdefiniujmy plaszczyzne przez HalfHelix-COM
### i sprawdzmy dihedral tej plaszczyzny z plaszczyzne HH-os Z ale najpierw projekt 

    for Pair in Pairs:

           if -15.0 <= DihAngMatrix [Pair[0]] [Pair[1]] >= 15.0:
              
              if ( -15.0 >= CrossAngMatrix [Pair[0]] [Pair[1]] ) or ( CrossAngMatrix [Pair[0]] [Pair[1]] >= 15.0 ):

                 ParallelPairs. append ( Pair )

    return ParallelPairs

#################################################################################################################################################### 

def AntiParallelPairs ( CrossAngMatrix, DihAngMatrix ):

    ParallelPairs = [ ]

    Pairs = [ [0,1,2],[1,2,0],[0,2,1] ]

#    Lexicon = {}; Lexicon [ 0_1

### osobno dla gory i osobno dla dolu
### jesli dwie helisy sa parallell 
### to zdefiniujmy plaszczyzne przez HalfHelix-COM
### i sprawdzmy dihedral tej plaszczyzny z plaszczyzne HH-os Z ale najpierw projekt 

    for Pair in Pairs:

           if 165.0 <= DihAngMatrix [Pair[0]] [Pair[1]] <= 195.0:
              
              if 165.0 <= CrossAngMatrix [Pair[0]] [Pair[1]] <= 195.0:

                 ParallelPairs. append ( Pair )

    return ParallelPairs
                                          
# musze zdefiniowac funkcje przyjmujaca dwie matryce za argument
# bla, to trudne 
#################################################################################################################################################### 

def AntiParallelRozkraki ( CrossAngMatrix, DihAngMatrix ):


    ParallelPairs = [ ]

    Pairs = [ [0,1,2],[1,2,0],[0,2,1] ]

#    Lexicon = {}; Lexicon [ 0_1

### osobno dla gory i osobno dla dolu
### jesli dwie helisy sa parallell 
### to zdefiniujmy plaszczyzne przez HalfHelix-COM
### i sprawdzmy dihedral tej plaszczyzny z plaszczyzne HH-os Z ale najpierw projekt 

    for Pair in Pairs:

           if 165.0 <= DihAngMatrix [Pair[0]] [Pair[1]] <= 195.0:
              
              if ( 165.0 >= CrossAngMatrix [Pair[0]] [Pair[1]] ) or  (CrossAngMatrix [Pair[0]] [Pair[1]] >= 195.0):

                 ParallelPairs. append ( Pair )

    return ParallelPairs
    

    return

#################################################################################################################################################### 

def CrossedPair ( CrossAngMatrix, DihAngMatrix ):

    return

#################################################################################################################################################### 

def ReadLinesFromFile ( InputPath ):

    FileInstance = open ( InputPath, 'r' )

    Lines = FileInstance. readlines ( )

    FileInstance. close ( )

    return Lines

#################################################################################################################################################### 
#################################################################################################################################################### 

class NSetRepresentation ( list ):


      def __init__ ( self, \
                     HELIX_IDSInput, \
                     TILTS_OF_HELICESI, \
                     TILTS_OF_HALF_HELICES, \
                     ContactPatternMatrices, \
                     CONTACT_RESIDUES_EC_MM_ICI, \
                     MinimumDistanceMatricesI, \
                     HelixNterDescriptorsI, \
                     ProteinNterDescriptorI, \
                     RelativeOrientationMatrixI, \
                     AASEQs, \
                     CENTREs, \
                     I1_3_VECs, \
                     AXES, \
                     CrossingAnglesMatrices, \
                     PDBCode = 'CODE', \
                     ChainID = 'ID', \
                     Family = 'DummyFamily', \
                     MM_SLICE_COMs_AngleI = 'NA', \
                     ClockwiseAntiClockwiseI = 'NS' \

                      ): # Representations
# kolejnosc jest inna niz w outpucie mozliwe ze gdzies, gdzie jest tworzona ta reprezentacja kolejnosc jest inna,
# dlatego lepiej jest uzywac keyword based arguments bo wtedy nie liczy sie kolejnosc
# trzeba to skrocic :) 
          self. HELIX_IDS = HELIX_IDSInput
          self. Order = len ( self. HELIX_IDS )
          self. TILTS_OF_HELICES = TILTS_OF_HELICESI
          self. TILTS_OF_HALF_HELICES = TILTS_OF_HALF_HELICES
          self. ContactPatternMatrices = ContactPatternMatrices
          self. CONTACT_RESIDUES_EC_MM_IC = CONTACT_RESIDUES_EC_MM_ICI
          self. MinimumDistanceMatrices = MinimumDistanceMatricesI
          self. HelixNterDescriptors = HelixNterDescriptorsI
          self. ProteinNterDescriptor = ProteinNterDescriptorI
          self. RelativeOrientationMatrix = RelativeOrientationMatrixI
          self. AASEQs = AASEQs
#          print CENTREs 
# ja pierdole, musze zrobic porzadek,
# musze zrobic pare zalozen:
#                            1) translacja jest zmiana instancji, a nie produkuje nowej instancji
#                            2) potrzebny jest copy constructor, zeby bekapowac 

          self. CENTREs = CENTREs # pytanie czemu nie moga passowac instancji
#          print 'Now Printing self. CENTREs'
#          self. CENTREs. Print ( )
#          print 'Done Printing self. CENTREs'
#          print 'Now Printing CENTREs'
#          CENTREs. Print ( )
#          print 'Done Printing CENTREs'
#          self. CENTREs. Print ( )

#          print self. CENTREs[0].Content
          self. I1_3_VECs = I1_3_VECs
          self. AXES = AXES
          self. MM_SLICE_COMs_Angle = MM_SLICE_COMs_AngleI
          self. ClockwiseAntiClockwiseI = ClockwiseAntiClockwiseI
          self. PDBCode = PDBCode
          self. ChainID = ChainID
          self. CrossingAnglesMatrices = CrossingAnglesMatrices
          self. Family = Family
#          HelicesPDBLines = [ grabHelix (self. Family, self. PDBCode, self.ChainID, HelixID ) for HelixID in self. HELIX_IDS   ]
          PDBLines = [ ]
#          for LinesOfHelix in HelicesPDBLines:
#              for HelixLine in LinesOfHelix:
#                  PDBLines. append ( HelixLine )
#          self. PdbFileContentInstance = PdbFileContent ( PDBLines );

#          print self.PDBCode

#####################################################################################################################################################

      def RuleBasedClassifier ( self ):

          Classes = [ '','' ]

          for N in range ( 2 ):

              ParallelPairsI = ParallelPairs ( self. DihedralAnglesMatrices[N], self. CrossingAnglesMatrices[N] )
              AntiParallelPairsI = AntiParallelPairs ( self. DihedralAnglesMatrices[N], self. CrossingAnglesMatrices[N] )

              PlaneNormal = SetOfVectors ( self. AXES [ ParallelPairsI [ 0 ] ], self. AXES [ ParallelPairsI [ 1 ] ] ). VectorProduct ( )

              if  80.0 <= SetOfVectors ( PlaneNormal, self. AXES [ ParallelPairsI [ 2 ] ] ). AngleDEG ( ) <= 100.0:

                  Classes [N] = 'CrossedParallelPair'

              elif 80.0 <= SetOfVectors ( PlaneNormal, self. AXES [ AntiParallelPairsI [ 2 ] ] ). AngleDEG ( ) <= 100.0:

                  Classes [N] = 'CrossedAntiParallelPair' 

              ParallelRozkrakiI = ParallelRozkraki ( self. DihedralAnglesMatrices[N], self. CrossingAnglesMatrices[N] )
              AntiParallelRozkrakiI = AntiParallelRozkraki ( self. DihedralAnglesMatrices[N], self. CrossingAnglesMatrices[N] )

              PlaneNormal = SetOfVectors ( self. AXES [ ParallelPairsI [ 0 ] ], self. AXES [ ParallelPairsI [ 1 ] ] ). VectorProduct ( )

              if  80.0 <= SetOfVectors ( PlaneNormal, self. AXES [ ParallelRozkrakiI [ 2 ] ] ). AngleDEG ( ) <= 100.0:

                  Classes [N] = 'CrossedParallelV'

              elif 80.0 <= SetOfVectors ( PlaneNormal, self. AXES [ AntiParallelRozkrakiI [ 2 ] ] ). AngleDEG ( ) <= 100.0:

                  Classes [N] = 'CrossedAntiParallelV'

# zostawic to na razie ..., pomyslec co dac na plakacie, moze jeszcze jakis graf i jakies definicje, a potem to policze
### osobno dla gory i osobno dla dolu
### jesli dwie helisy sa parallell 
### to zdefiniujmy plaszczyzne przez HalfHelix-COM
### i sprawdzmy dihedral tej plaszczyzny z plaszczyzne HH-os Z ale najpierw projekt 
                        
# musze zdefiniowac funkcje przyjmujaca dwie matryce za argument
# bla, to trudne 

          return Classes

#####################################################################################################################################################

      def FitHelixToTemplate ( self, HelixNo, CentreTemplate, HelicesLinesTemplate ):

# i tutaj sie dzieje magia
# moze powinienem isc do roboty, a moze jutro rano
# moze moglbym pocwiczyc

# zawsze jest to samo, powinna byc ta funkcja zdefiniowana dla Atom Recordsow i dla Centrow, ktore sa SetOfPoints, ktoe bedzie polegalo na tych trzech ruchach

# 1 szy ruch ) naloz oba do ( 0,0,0 )
# 2 gi ruch ) zrob rotacje 1 na dwa
# 3ci ruch przesuniecie templatu na swoje miejsce i query na templat

# to jest glowna zasada, metoda jest definiowana u zrodla :)

# musielibysmy zdefiniowac plane tych dwoch parallell

# ale musze zrobic poster przed tym!
                              

          return

#####################################################################################################################################################

      def ModelAfterTemplate ( self, Template ):

          for N in range ( Template. Order ):

              self. FitHelixToTemplate ( N, Template. CENTREs [ N ], Template. HelicesPDBLines [ N ] ) 


#####################################################################################################################################################

      def RMSDToNearestTemplate ( self, Templates ):

          return min([ SetOfNTMS_SetRepresentations ( self, Template ). RMSD () for Template in Templates ])

#####################################################################################################################################################

      def ConservedInside ( self):

          return True

#####################################################################################################################################################

      def ContainsSSACs ( self ): # Single Solvent Accessible Cysteines

          return False

#####################################################################################################################################################
# musze znalezc jakis sposob zeby to zintegrowac


#####################################################################################################################################################

      def CorrectNHelixPacking (self, N, RMSDThreshold ):

          NPodzbioryI = self. NPodzbiory ( N )
# musze mu wyslac jakies wyniki
          for NPodzbiorI in NPodzbiory. Content:
              if NPodzbiorI. RMSDToNearestTemplate ( Templates ) >= Threshold:
                 return False

# musze zjesc kurczaka i isc pobiegac          

#####################################################################################################################################################

      def ModelAfterTemplates ( self, Templates ):

          if self. Order == 3:

             FirstThreeHelicesModelledAfterDifferentTemplatesSet = [ self. ModelAfterTemplate ( Template ) for Template in Templates ]

             
             
# wiec jesli sa tylko 3 helisy to modelujemy podlug roznych mozliwosci
# po prostu musimy troche przebudowac ten sposob
             

# ok trzeba to teraz jakos przepisac :D
# po prostu stworzmy strukture ktora bedzie troche inna, niech Helix Lines ma hierarchiczna strukture :D
          HelicesPDBLines [0] # to jest pierwsza Helisa 
          


# model first three Helices
          if self. Order == 4:

             FirstThreeHelicesModelledAfterDifferentTemplatesSet = []

# no wlasnie, wypiszmy kroki po polsku, dla N helis
# najpierw dla trzech helis 1-2-3 morfujemy w inny tryplet,
# potem dla trzech drugich helis morfujemy w 2-3-4 z dwiema pierwszymi constrained
# potem dla trzech trzecich helis 3-4-5 morfujemy z dwiema pierwszymi constrained
# potem dla trzech czwartych helis 4-5-6 morfujemy z dwiema pierwszymi constrained
          PoczatkoweModele

# jeeej potem mozna jeszcze zdefiniowac pozostale funkcje

          for N in range ( Order - 3 ):

              NoweModele = []

              for Model in PoczatkoweModele:

                  for Template in Templaty:

                      NowyModel = Model. MorphModelIntoTemplateWithFirstTwoConstrained ( Template )

                      NoweModele. append ( NowyModel ) 

          PoczatkoweModele = NoweModele

                  

          return PoczatkoweModele

#####################################################################################################################################################

      def Translate ( self, Vector ):

          self. CENTREs. Translate ( Vector ) 
          self. PdbFileContentInstance. Translate ( Vector )

#####################################################################################################################################################

      def CrossingAngles ( self ): # acha, ale to tylko chwilowo, musi byc roznie dla roznych definicji!

          CrossingAnglesI = [ ]

          EC, IC, Main = self. CrossingAnglesMatrices

          for I in range ( len ( EC ) ):

              CrossingAnglesI = [ float (Main [ I ][ J ]) for J in range ( I+1, len ( EC ) )  ]

#              print 'CrossingAnglesI'

          return CrossingAnglesI

#####################################################################################################################################################

      def BinarizedContactPatternMatrices ( self ):

          import sys;
          import functions_module; from functions_module import BinarizeMatrix;

          BinarizedContactPatternMatricesI = [ BinarizeMatrix ( ContactPatternMatrix )  for ContactPatternMatrix in self. ContactPatternMatrices]
          
          return BinarizedContactPatternMatricesI

#####################################################################################################################################################

      def RozbijNaPodzbioryWgRzedow ( self, ListaRzedow, Nakladanie = 0 ):

# wariant dla Nakladania Rownego Zero
# moze internet cos wie na ten temat: wybor kilku podzbiorow ze zbioru

          return Rozbicia

#####################################################################################################################################################

      def RozbijNaPodzbioryWgIndeksow ( self, ListyIndeksow ):

          PodzbioryI = [ NPodzbior ( ListaIndeksow ) for ListaIndeksow in ListyIndeksow ]
          
          return PodzbioryI

#####################################################################################################################################################

      def Consecutive ( self ):

          if Consecutive ( self. HELIX_IDS ):

             return True

          return False

#####################################################################################################################################################

      def MaxTiltOverThreshold ( self, Threshold ):

          if self. MaxTilt >= Threshold:

             return True

          return False

#####################################################################################################################################################

      def MaxTilt ( self ):

          return max ( self. TILTS_OF_HELICES  ) # nie powinienem tych zmiennych trzymac w stringach ale w takich wartosciach w jakich sa,
# potrzebna kolejna przebudowa programu

#####################################################################################################################################################

      def FlattenedContactPatternMatrix ( self ):

          EC, MM, IC = self. ContactPatternMatrices

          Order = len ( self. HELIX_IDS )

          FlattenedContactPatternMatrixI = [ ]

          for I in range ( Order ):
              
              FlattenedContactPatternMatrixI_Row = [ ( int(EC[I][J]) + int(MM[I][J]) + int(IC[I][J]) ) for J in range ( Order ) ]

              FlattenedContactPatternMatrixI. append ( FlattenedContactPatternMatrixI_Row )

          return FlattenedContactPatternMatrixI

#####################################################################################################################################################

      def Closed ( self ):

          if Closed ( self. FlattenedContactPatternMatrix ( ) ):

             return True

          return False

#####################################################################################################################################################

      def Touching ( self ):

          if Touching ( self. FlattenedContactPatternMatrix ( ) ):

             
             return True
#             print 'False'; quit()          
          return False          

#####################################################################################################################################################



#####################################################################################################################################################

      def ClosedOrOpen ( self ):

          FlattenedContactPatternMatrixI = self. FlattenedContactPatternMatrix ( )

          for I in range ( Order ):

              for J in range ( Order ):

                  if FlattenedContactPatternMatrixI [I][J] == 0:

                     return 'Open'

#          print 'Closed'

          return 'Closed'

#####################################################################################################################################################

      def TouchingNMinusOneSubsets ( self ):

          FlattenedContactPatternMatrixI = self.FlattenedContactPatternMatrix ( )

          NMinusOneIndexes = TouchingNMinusOneSubmatrices ( FlattenedContactPatternMatrixI )

          TouchingNMinusOneSubsetsI = [ self.NMinusOneSubset ( NMinusOneIndex ) for NMinusOneIndex in NMinusOneIndexes ]               
          
          return TouchingNMinusOneSubsetsI

#####################################################################################################################################################

      def NPodzbiory ( self, N ):

          K = len ( self. HELIX_IDS )

          MozliwosciIndeksow = MozliwosciWyboruNzK ( N, K )

          NPodzbioryI = SetOfN_TMs_SetRepresentations ( [ self. NPodzbior ( Indeksy ) for Indeksy in MozliwosciIndeksow ] )
#          print 'Printing NPodzbioryI. Content [ 1 ]. Center ( )'
#          print NPodzbioryI. Content [ 1 ]. Center ( )

          return SetOfN_TMs_SetRepresentations ( [ self. NPodzbior ( Indeksy ) for Indeksy in MozliwosciIndeksow ] )

#####################################################################################################################################################

      def NPodzbioryTouching ( self, N ):

          K = len ( self. HELIX_IDS )

          MozliwosciIndeksow = MozliwosciWyboruNzK ( N, K )

          NPodzbioryI_Touching = [ ]

          for Indeksy in MozliwosciIndeksow:

              NPodzbiorI = self. NPodzbior ( Indeksy )

              if NPodzbiorI. Touching ( ):

                 NPodzbioryI_Touching. append ( NPodzbiorI )

          print 'Ilosc Z Jednej Reprezentacji ' + str ( len ( NPodzbioryI_Touching  ) )


          return SetOfN_TMs_SetRepresentations ( NPodzbioryI_Touching )
#####################################################################################################################################################

      def NPodzbioryConsecutive ( self, N ):

          K = len ( self. HELIX_IDS )

          MozliwosciIndeksow = MozliwosciWyboruNzK ( N, K )

          NPodzbioryI_Consecutive = [ ]

          for Indeksy in MozliwosciIndeksow:

              NPodzbiorI = self. NPodzbior ( Indeksy )

              if NPodzbiorI. Consecutive ( ):

                 NPodzbioryI_Consecutive. append ( NPodzbiorI )

          print 'Ilosc Z Jednej Reprezentacji ' + str ( len ( NPodzbioryI_Consecutive  ) )


          return SetOfN_TMs_SetRepresentations ( NPodzbioryI_Consecutive )

#####################################################################################################################################################

      def WszystkiePodzbiory ( self ):

          WszystkiePodzbioryI = [ ]

          for N in range (2, len ( self. HELIX_IDS ) ):

              PodzbioryDlaN = self.NPodzbiory ( N )

              for PodzbiorI in PodzbioryDlaN:

                  WszystkiePodzbioryI. append ( PodzbiorI )

          return WszystkiePodzbioryI

#####################################################################################################################################################
          
      def NMinusOneSubsets ( self ):

          NMinusOneSubsetsI = [ ]

          FlattenedContactPatternMatrixI = self.FlattenedContactPatternMatrix ( )

          NMinusOneIndexes = range ( len ( FlattenedContactPatternMatrixI ) )

          for NMinusOneIndex in NMinusOneIndexes:

              NMinusOneSubsetI = self.NMinusOneSubset ( NMinusOneIndex )

              NMinusOneSubsetsI. append ( NMinusOneSubsetI )               
          
          return NMinusOneSubsetsI

#####################################################################################################################################################

#      def AllLowerOrderSubsets ( self ):

#          LowerOrderSubsets = [ self ]

#          while Order >= 2:

#                print 'Lala'

# moze jednak pojde spac                

# trzeba isc spac i wymyslec cos lepszego jutro, bo takie cos nie ma sensu              

#####################################################################################################################################################

      def NMinusOneSubset ( self, NMinusOneIndex ):

          HelixIDSI = ListaBezIndexu ( self. HELIX_IDS, NMinusOneIndex )

          TILTS_OF_HELICESI = ListaBezIndexu ( self. TILTS_OF_HELICES, NMinusOneIndex )

          EC_TILTS_OF_HALF_HELICES = ListaBezIndexu ( self. TILTS_OF_HALF_HELICES [ 0 ], NMinusOneIndex )
          IC_TILTS_OF_HALF_HELICES = ListaBezIndexu ( self. TILTS_OF_HALF_HELICES [ 1 ], NMinusOneIndex )

          TILTS_OF_HALF_HELICES = [ EC_TILTS_OF_HALF_HELICES, IC_TILTS_OF_HALF_HELICES ]
          ContactPatternMatrices = self. ContactPatternMatrices; # trzeba uzyc podmatrycy
          
          CONTACT_RESIDUES_EC_MM_ICI = [ [], [], [] ]
          
          for N in range ( len ( HelixIDSI ) ): 
              CONTACT_RESIDUES_EC_MM_ICI [0]. append ( [ ] );
              CONTACT_RESIDUES_EC_MM_ICI [1]. append ( [ ] );             
              CONTACT_RESIDUES_EC_MM_ICI [2]. append ( [ ] );
 
          MinimumDistanceMatricesI = self. MinimumDistanceMatrices; # to musze zmienic
          HelixNterDescriptorsI = ListaBezIndexu ( self. HelixNterDescriptors, NMinusOneIndex )
          ProteinNterDescriptorI = self. ProteinNterDescriptor
          RelativeOrientationMatrixI = self. RelativeOrientationMatrix
          AASEQs = ListaBezIndexu ( self. AASEQs, NMinusOneIndex )
          CENTREs = ListaBezIndexu ( self. CENTREs, NMinusOneIndex )
          I1_3_VECs =  ListaBezIndexu ( self. I1_3_VECs, NMinusOneIndex )
          AXES = ListaBezIndexu ( self. AXES, NMinusOneIndex )

          MM_SLICE_COMs_AngleI = self. MM_SLICE_COMs_Angle
          ClockwiseAntiClockwiseI = self. ClockwiseAntiClockwiseI

#          print HelixIDSI
          
          NMinusOneSubsetI = NSetRepresentation (                       HelixIDSI, \
                     TILTS_OF_HELICESI, \
                     TILTS_OF_HALF_HELICES, \
                     ContactPatternMatrices, \
                     CONTACT_RESIDUES_EC_MM_ICI, \
                     MinimumDistanceMatricesI, \
                     HelixNterDescriptorsI, \
                     ProteinNterDescriptorI, \
                     RelativeOrientationMatrixI, \
                     AASEQs, \
                     CENTREs, \
                     I1_3_VECs, \
                     AXES, \
                     MM_SLICE_COMs_AngleI = 'NA', \
                     ClockwiseAntiClockwiseI = 'NS' )

          return NMinusOneSubsetI

#####################################################################################################################################################

      def NPodzbior ( self, Indeksy ):

          HelixIDSI = ListaZIndeksami ( self. HELIX_IDS, Indeksy )

#          HelixIDSI = self. HELIX_IDS; HelixIDSI. pop ( NMinusOneIndex ) # dlaczego to tak dziala ?

          TILTS_OF_HELICESI = ListaZIndeksami ( self. TILTS_OF_HELICES, Indeksy )

          EC_TILTS_OF_HALF_HELICES = ListaZIndeksami ( self. TILTS_OF_HALF_HELICES [ 0 ], Indeksy )
          IC_TILTS_OF_HALF_HELICES = ListaZIndeksami ( self. TILTS_OF_HALF_HELICES [ 1 ], Indeksy )

          TILTS_OF_HALF_HELICES = [ EC_TILTS_OF_HALF_HELICES, IC_TILTS_OF_HALF_HELICES ]
          
          EC = PodMatrycaZIndeksami ( self. ContactPatternMatrices [ 0 ], Indeksy ) #skomentowac to musze
          MM = PodMatrycaZIndeksami ( self. ContactPatternMatrices [ 1 ], Indeksy ) # jakis plan programu oprocz tego
          IC = PodMatrycaZIndeksami ( self. ContactPatternMatrices [ 2 ], Indeksy ) # plan struktury danych         

          ContactPatternMatrices = [ EC, MM, IC ] # trzeba uzyc podmatrycy
          
          EC = PodMatrycaZIndeksami ( self.CONTACT_RESIDUES_EC_MM_IC [ 0 ], Indeksy )
          MM = PodMatrycaZIndeksami ( self.CONTACT_RESIDUES_EC_MM_IC [ 1 ], Indeksy )
          IC = PodMatrycaZIndeksami ( self.CONTACT_RESIDUES_EC_MM_IC [ 2 ], Indeksy )           
 
          CONTACT_RESIDUES_EC_MM_ICI = [ EC, MM, IC ]

          EC = PodMatrycaZIndeksami ( self.MinimumDistanceMatrices [ 0 ], Indeksy )
          MM = PodMatrycaZIndeksami ( self.MinimumDistanceMatrices [ 1 ], Indeksy )
          IC = PodMatrycaZIndeksami ( self.MinimumDistanceMatrices [ 2 ], Indeksy )

          MinimumDistanceMatricesI = [ EC, MM, IC ]

          HelixNterDescriptorsI = ListaZIndeksami ( self. HelixNterDescriptors, Indeksy )
          ProteinNterDescriptorI = self. ProteinNterDescriptor

          RelativeOrientationMatrixI = PodMatrycaZIndeksami ( self. RelativeOrientationMatrix, Indeksy )
          AASEQs = ListaZIndeksami ( self. AASEQs, Indeksy )

          EC_Fis = ListaZIndeksami ( self. EC_Fis, Indeksy )
          IC_Fis = ListaZIndeksami ( self. IC_Fis, Indeksy )

          CENTREs = HierarchicalSetOfPoints ( ListaZIndeksami ( self. CENTREs. Content, Indeksy ) )

          CENTREs. Print ( )

#          quit ()

          I1_3_VECs =  ListaZIndeksami ( self. I1_3_VECs, Indeksy )
          AXES = ListaZIndeksami ( self. AXES, Indeksy )

          MM_SLICE_COMs_AngleI = self. MM_SLICE_COMs_Angle
          ClockwiseAntiClockwiseI = self. ClockwiseAntiClockwiseI
          EC = PodMatrycaZIndeksami ( self. CrossingAnglesMatrices[0], Indeksy )
          IC = PodMatrycaZIndeksami ( self. CrossingAnglesMatrices[1], Indeksy )
          Main = PodMatrycaZIndeksami ( self. CrossingAnglesMatrices[2], Indeksy )
          CrossingAnglesMatricesI = [ EC, IC, Main ]
          
          NPodzbiorI = NSetRepresentation (                       HelixIDSI, \
                     TILTS_OF_HELICESI, \
                     TILTS_OF_HALF_HELICES, \
                     ContactPatternMatrices, \
                     CONTACT_RESIDUES_EC_MM_ICI, \
                     MinimumDistanceMatricesI, \
                     HelixNterDescriptorsI, \
                     ProteinNterDescriptorI, \
                     RelativeOrientationMatrixI, \
                     AASEQs, \
                     CENTREs, \
                     I1_3_VECs, \
                     AXES, \
                     CrossingAnglesMatricesI, \
                     PDBCode = self. PDBCode, \
                     ChainID = self. ChainID, \
                     Family = self. Family, \
                     MM_SLICE_COMs_AngleI = 'NA', \
                     ClockwiseAntiClockwiseI = 'NS' )

          NPodzbiorI. EC_Fis = EC_Fis
          NPodzbiorI. IC_Fis = IC_Fis          

          return NPodzbiorI

#####################################################################################################################################################

      def StraightOrKinked ( self, TiltDifferenceThreshold ):

          return

#####################################################################################################################################################

      def OutputPDB ( self, OutputPath = 'DummyPath' ): # aha bo to nie ma self. Contentu

# teraz jest zagadnienie takie zeby to translatowac przez odpowiednia matryce, zeby to nalozyc na jakis srodek klastra :)
# to by
# napisac plan jakby to mialo wygladac wiec mam ten klaster i chce go zalignowac na klaster od zero

#          import sys

#          sys.path.append ('./Moduly/Text' )

#          from TextLinesModule import *

# musze wyoutputowac do jednego pliku

#          HelicesPDBLines = [ grabHelix (self. Family, self. PDBCode, self.ChainID, HelixID ) for HelixID in self. HELIX_IDS   ]

#          PDBLines = [ ]
#          for LinesOfHelix in HelicesPDBLines:
#              for HelixLine in LinesOfHelix:
#                  PDBLines. append ( HelixLine )
          
#          PDBLines = TextLines ( [[ HelixLine for HelixLine in LinesOfHelix ] for LinesOfHelix in HelicesPDBLines ] )  # zobaczymy czy to dziala                 

#          print len ( PDBLines )
#          print PDBLines[0]

#          TextLines ( PDBLines ). WriteToFile ( OutputPath + '/' + self.PDBCode  + '_' + self.ChainID +'_' + '_'.join( self. HELIX_IDS ) + '.pdb' )

#          print OutputPath

          self. PdbFileContentInstance. WriteAtomRecords ( OutputPath + '/' + self.PDBCode  + '_' + self.ChainID +'_' + '_'.join( self. HELIX_IDS ) + '.pdb' );

          return 

#####################################################################################################################################################

      def MyWayOfClassification ( ):
# use perceptron algorithm
          return

#####################################################################################################################################################

      def RotateByMatrix ( self, RotationMatrix ):

          self. CENTREs. RotateByMatrix ( RotationMatrix )
          self. PdbFileContentInstance. RotateByMatrix ( RotationMatrix )

          return

#####################################################################################################################################################

      def Center ( self ):

          return self. PdbFileContentInstance. AtomRecords. Center ( )

#          return self. CENTREs. Center ( )

#####################################################################################################################################################

      def MoveToOrigin ( self ):
# przy nonhierarchicznosci musi byc jakis problem
#          self. GeoCenter = self. Center ( )
#          print 'Now Printing Center before centering'
#          print GeoCenter
#          print 'Done Printing Center before centering'

          self. GeoCenter = self. PdbFileContentInstance. AtomRecords. Center () # zmieniamy na chwile

          self. Translate ( [ -self. GeoCenter [0], -self. GeoCenter [1], -self. GeoCenter [2] ] )
          print [ -self. GeoCenter [0], -self. GeoCenter [1], -self. GeoCenter [2] ]
#          print 'Moving By Vector'
#          print [ -GeoCenter [0], -GeoCenter [1], -GeoCenter [2] ]
#          print 'Now Printing Center after centering'
#          print self. Center ( )
#          print 'Done Printing Center after centering'
          return

#####################################################################################################################################################

      def OutputPDBAlignedOn ( self, TemplateRepresentation, OutputPath = 'DummyPath', AllowPerturbations = False, AllowFlip = False ):
# powinienem zobaczyc gdzie jest blad, musze sie zdecydowac na cos 

          QueryGeometricalCenter    = self. Center ( );
          TemplateGeometricalCenter = TemplateRepresentation. Center ( );

#          TemplateRepresentation. PdbFileContentInstance. WriteAtomRecords ( OutputPath + '/' + TemplateRepresentation.PDBCode  + '_' + TemplateRepresentation.ChainID +'_' + '_'.join( TemplateRepresentation. HELIX_IDS ) + '_template_test.pdb' );

          TemplateRepresentation. MoveToOrigin ( ); self. MoveToOrigin ( );
          TemplateRepresentation.OutputPDB ( 'TemplateInOrigin' );
          print 'Now Printing Template Center'
          print TemplateRepresentation. Center ( )
          print ' Done Printing Template Center'

          TemplateRepresentation. PdbFileContentInstance. WriteAtomRecords ( OutputPath + '/' + TemplateRepresentation.PDBCode  + '_' + TemplateRepresentation.ChainID +'_' + '_'.join( TemplateRepresentation. HELIX_IDS ) + '_templateInOrigin_test.pdb' );
          self. PdbFileContentInstance. WriteAtomRecords ( OutputPath + '/' + self.PDBCode  + '_' + self.ChainID +'_' + '_'.join( self. HELIX_IDS ) + '_self_in_origin_test.pdb' );

################# przesunac oba do srodka ######################################

          RotationMatrix = SetOfN_TMs_SetRepresentations ( [ self, TemplateRepresentation ] ). SuperpositionMatrix ( AllowPerturbations, AllowFlip )

          self. RotateByMatrix ( RotationMatrix )
          self. PdbFileContentInstance. WriteAtomRecords ( OutputPath + '/' + self.PDBCode  + '_' + self.ChainID +'_' + '_'.join( self. HELIX_IDS ) + '_rotated_test.pdb' );
          self. Translate ( TemplateGeometricalCenter );

          self. PdbFileContentInstance. WriteAtomRecords ( OutputPath + '/' + self.PDBCode  + '_' + self.ChainID +'_' + '_'.join( self. HELIX_IDS ) + '.pdb' );
  

          return

#####################################################################################################################################################

      def CENTREsArray ( self ):


          Array = [ ]

          for Helix in self.CENTREs:

              for PointI in Helix. Content:

                  Array. append ( PointI )

          return Array

#####################################################################################################################################################


      def AlignedOn ( self, TemplateRepresentation ):
          from match import optimal_superposition

          RotationMatrix = SetsOfPoints ( [ self[0]. CENTREs, TemplateRepresentation.CENTREs ] ). SuperpositionMatrix ( )

          return

#####################################################################################################################################################

      def AlignOnZAxis ( self ):

          from match import optimal_superposition

          NSetAxis = self. NormalizedMainAxis ( ); ZAxis = [0.0,0.0,1.0];

          RotationMatrix = optimal_superposition ( np.array ( NSetAxis ), np.array ( ZAxis ) ).T

          self.RotateByMatrix ( RotationMatrix ) # i tyle

          return

#####################################################################################################################################################

      def MainAxis ( self ):

          MainAxisI = [ 0.0, 0.0, 0.0 ]

          for HelixInstance in self.Content:

              for I in range ( len ( MainAxisI ) ):

                  MainAxisI [ I ] += HelixInstance. MainAxis ( ) [ I ]

          return Vector(MainAxisI)

#####################################################################################################################################################

      def NormalizedMainAxis ( self ):

          MainAxisI = self. MainAxis ( );

          LengthI = MainAxisI. Length ( );

          NormalizedMainAxisI = [ MainAxisI [ I ] / LengthI for I in range ( len ( MainAxisI ) ) ] 

          return NormalizedMainAxisI

#####################################################################################################################################################

      def Output ( self, ProteinNterDescriptor, Path ): # to PDB(like) format file

          import os

          Order = str ( len ( self. HELIX_IDS ) );

          BasicOutputDirectory = '/home/soutys/Science/Triplets/DaneWyjsciowe/ExtractedTouchingNSetsRepresentations/'+Order;

          BasicOutputDirectory = Path;

          Path = BasicOutputDirectory +'/'+ self. Family + '/' + self.PDBCode + '/' + self. ChainID + '/' + self. PDBCode + '_' + self. ChainID

          if os.path.exists ( BasicOutputDirectory +'/'+ self. Family ) == False: os. system ( 'mkdir '+ BasicOutputDirectory +'/'+ self. Family );

          if os.path.exists ( BasicOutputDirectory +'/'+ self. Family + '/' + self.PDBCode ) == False:

             os. system ( 'mkdir '+BasicOutputDirectory +'/'+  self. Family + '/' + self.PDBCode );

          if os.path.exists ( BasicOutputDirectory +'/'+ self. Family + '/' + self.PDBCode + '/' + self. ChainID ) == False:

             os. system ( 'mkdir '+ BasicOutputDirectory +'/'+  self. Family + '/' + self.PDBCode + '/' + self. ChainID  );

#          Path = self. PDBCode +'_'+ self. ChainID

          Threes = ['EC','MM','IC']

          line = '#REMARK  HELIX IDS                        '

          self.HelixIDsI = self. HELIX_IDS

          File_Name = Path

          for HelixIDI in self.HelixIDsI:
              File_Name = File_Name + '_'+ str ( HelixIDI )
          File_Name = File_Name +  '_Representation.txt'
          print 'FileName'
          print File_Name

          file = open ( File_Name, 'w' )

          for N in range ( len ( self.HelixIDsI ) ): #ok wiec jak to teraz 

              line = line +'  TM' + str( self.HelixIDsI [ N ] )

          line = line + '\n'

          file. write ( line )

          line = '#REMARK\n'; file. write ( line );
# na razie wygaszamy
#          line = '#REMARK MM SLICE COMs (TM'+ID1+'-TM'+ID2+')|(TM'+ID2+'-TM'+ID3+') vectors Angle [DEG] %8.3f\n' % self. MMTM1TM2TM3VectorsAngleDEG ( ); file. write ( line );
# %8.3f
#          line = line +'%8.3f\n'  str ( self. MMTM1TM2TM3VectorsAngleDEG ( ) ) + '\n'; file. write ( line )

          line = '#REMARK\n'; file. write ( line );

          line = '#REMARK Clockwise/AntiClockwise (Nter EC)        '
#          line = line + self.ClockwiseAntiClockwise() + '\n'; file. write ( line ); 
          line = '#REMARK\n'; file. write ( line );
          line = '#REMARK  TILTS OF HELICES to Z AXIS [DEG] '
          for HelixIDI in self.HelixIDsI:
              line = line+'  TM'+str(HelixIDI)
          line = line+'\n'; file. write ( line );

          line = '#REMARK                                   '
          for HelixTilt in self. TILTS_OF_HELICES: # musze isc spac, problemem jest to ze rzeczy sczytalem jako stringi, nie wiem czy to dobrze 
              line = line + '%8.3f' % float (HelixTilt);
          line = line + '\n'; file. write ( line )
          line = '#REMARK\n'; file. write ( line );
          line = '#REMARK  TILTS OF HALF HELICES to Z AXIS [ DEG ] '

          for HelixIDI in self.HelixIDsI:
              line = line+' TM'+str(HelixIDI)
          line = line + '\n'; file. write ( line );

          line = '#REMARK                                       EC '

          for ECHalfHelixTilt in self. TILTS_OF_HALF_HELICES [ 0 ]:
              line = line + '%8.3f' % float (ECHalfHelixTilt);
          line = line + '\n'; file. write ( line );
          line = '#REMARK                                       IC '

          for ICHalfHelixTilt in self. TILTS_OF_HALF_HELICES [ 1 ]:
              line = line + '%8.3f' % float (ICHalfHelixTilt);
          line = line + '\n'; file. write ( line );

          line = '#REMARK\n'; file. write ( line );

#          line = '#REMARK  ContactPatternMatrix      TM'+ID1+'/TM'+ID2+'  TM'+ID2+'/TM'+ID3+'  TM'+ID1+'/TM'+ID3+'\n'; file. write ( line );

          for HelixIDI in self.HelixIDsI:
              line = line + '  TM'+str(HelixIDI)
          line = line + '\n'; file. write ( line );
# musze sie polozyc i odpoczac ale jestem na pewno na dobrej drodze ... :) 
          

          BinaryContactPatternMatrices = self. ContactPatternMatrices  # wiec powinno chodzic

          for N in range ( len (BinaryContactPatternMatrices) ):
              line = '#REMARK\n'; file. write ( line );

              BinaryContactPatternMatrix = BinaryContactPatternMatrices [ N ]

              Halfs = ['EC','IC', 'Main']

              for I in range ( len ( BinaryContactPatternMatrix  ) ): # mysle ze cos zle zrobilem

                  line = '#REMARK  ContactPatternMatrix  '+Threes[N]
              
                  for J in range ( len ( BinaryContactPatternMatrix [ I ] ) ):

                      line = line +'        '+ str ( BinaryContactPatternMatrix [ I ] [ J ] )

                  line = line + '\n'; file. write ( line );

              line = '#REMARK\n'; file. write ( line );
# musze zmienic format tego

          CONTACT_RESIDUES_MATRICES =  self. CONTACT_RESIDUES_EC_MM_IC
# zmieniam format
          
          for N in range ( len ( CONTACT_RESIDUES_MATRICES ) ):

              CONTACT_RESIDUES_MATRIX = CONTACT_RESIDUES_MATRICES [ N ]

              for I in range ( len ( CONTACT_RESIDUES_MATRIX ) ):

                  line = '# CONTACT RESIDUES '+Threes [ N ]

                  for J in range ( len ( CONTACT_RESIDUES_MATRIX [ I ] ) ):
# tez powinien byc sposob wydrukowania tego na matrycy
                      line = line + '\t' + str( CONTACT_RESIDUES_MATRIX [I][J] )

                  line = line + '\n'; file. write ( line );

#          line = '#REMARK  MinimumDistanceMatrix [A]   TM'+ID1+'/TM'+ID2+'  TM'+ID2+'/TM'+ID3+'  TM'+ID1+'/TM'+ID3+'\n'; file. write ( line );


          MinimumDistanceMatricesI = self.MinimumDistanceMatrices

          for N in range ( len ( MinimumDistanceMatricesI ) ):

              line = '#REMARK\n'; file. write ( line );

              MinimumDistanceMatrix = MinimumDistanceMatricesI [ N ]

              for I in range ( len ( MinimumDistanceMatrix ) ):

                  line = '#REMARK  MinimumDistanceMatrix  ' + Threes [ N ]
              
                  for J in range ( len ( MinimumDistanceMatrix [ I ] ) ):

                      line = line +'%8.3f' % float ( MinimumDistanceMatrix [ I ] [ J ] )

                  line = line + '\n'; file. write ( line );

          line = '#REMARK\n'; file. write ( line );

          line = '#REMARK NterDescriptors Protein '
          HelixNterDescriptorsI =  self. HelixNterDescriptors

          for HelixIDI  in self.HelixIDsI:
              line = line +' TM' + str(HelixIDI);
          line = line +'\n'; file. write ( line );

# i should leave it for later

          line = '#REMARK                      '+ProteinNterDescriptor

          for HelixNterDescriptor in self. HelixNterDescriptors:
              line = line + '  ' + HelixNterDescriptor

          line = line + '\n'; file. write ( line );

          line = '#REMARK\n'; file. write ( line );
# zmienic na matryce
          line = '#REMARK RelativeOrientationMatriI'
          for HelixIDI  in self.HelixIDsI:
              line = line +' TM'+str(HelixIDI);
          line = line +'\n'; file. write ( line );

          line = '#REMARK                      '; 
          RelativeOrientationMatrixI =  self. RelativeOrientationMatrix

          for I in range ( len ( RelativeOrientationMatrixI  ) ):
              line='#REMARK RelativeOrientationMatrix'
              for J in range ( len ( RelativeOrientationMatrixI [I] )  ):
                  line = line +' '+ RelativeOrientationMatrixI[I][J]
              line = line +'\n'; file. write ( line );

#              line = line + ' '+HelixRelativeOrientation;
# zrobie sobie matryce 

# zmienic na matryce
          line = '#REMARK\n'; file. write ( line );

          CrossingAnglesMatricesI = self. CrossingAnglesMatrices

          for N in range ( len ( CrossingAnglesMatricesI  ) ):
              line = '#REMARK\n'; file. write ( line ); 

              for I in range ( len ( CrossingAnglesMatricesI[N] ) ): 
                  line='#REMARK CrossingAnglesMatrix '+Halfs[N]
                  
                  JoinLista = "".join(format(x, "8.3f") for x in CrossingAnglesMatricesI[N][I])
                  
                  line=line+JoinLista+'\n'; file. write ( line );          

          line = '#REMARK\n'; file. write ( line );

          line = '#STARTMDL\n'; file. write ( line );
         
#        

#          print self.CENTREs
   
          for N in range ( len ( self.AASEQs ) ): # musze to lepiej ogarnac, ale na razie tyle

              IDi = self.HelixIDsI [ N ]

              EcAASEQ, MmAASEQ, IcAASEQ = self.AASEQs [ N ]

              line = '#AASEQ '+ EcAASEQ +'\n'; file. write ( line );

#              print self.CENTREs [ N ]

              EC_COM, MM_COM, IC_COM =  self.CENTREs. Content [ N ]. Content

              if len (self. CENTREs) >= 3:

                 self. ISC_IC = self.CENTREs. CartesianToISC_IC ( ) # ok i powinno jechac
                 self. ISC_EC = self.CENTREs. CartesianToISC_EC ( ) # ok i powinno jechac
                 self. ISC    = self.CENTREs. CartesianToISC    ( ) # ok i powinno jechac

              EC_1_3_VEC, IC_1_3_VEC = self. I1_3_VECs [ N ]

              line = '#CENTRE    TM%2d EC %8.3f %8.3f %8.3f\n' %( int(IDi), float(EC_COM[0]), float(EC_COM[1]), float(EC_COM[2]) ); file. write ( line );
              line = '#1-3VEC    TM%2d EC %8.3f %8.3f %8.3f\n' %( int(IDi), float(EC_1_3_VEC[0]), float(EC_1_3_VEC[1]), float(EC_1_3_VEC[2]) ); file. write ( line );

              EM_Axis, IM_Axis = self.AXES [ N ]

              line = '#AXIS      TM%2d EM %8.3f %8.3f %8.3f\n' %( int(IDi), float(EM_Axis[0]), float(EM_Axis[1]), float(EM_Axis[2]) ); file. write ( line );

              line = '#AASEQ '+MmAASEQ+'\n'; file. write ( line );

              line = '#CENTRE    TM%2d MM %8.3f %8.3f %8.3f\n' %( int(IDi), float(MM_COM[0]), float(MM_COM[1]), float(MM_COM[2]) ); file. write ( line );  
              line = '#1-3VEC    TM%2d IC %8.3f %8.3f %8.3f\n' %( int(IDi), float(IC_1_3_VEC[0]), float(IC_1_3_VEC[1]), float(IC_1_3_VEC[2]) ); file. write ( line );            

              line = '#AXIS      TM%2d IM %8.3f %8.3f %8.3f\n' %( int(IDi), float(IM_Axis[0]), float(IM_Axis[1]), float(IM_Axis[2]) ); file. write ( line );

              line = '#AASEQ '+IcAASEQ+'\n'; file. write ( line );

              line = '#CENTRE    TM%2d IC %8.3f %8.3f %8.3f\n' %( int(IDi), float(IC_COM[0]), float(IC_COM[1]), float(IC_COM[2]) ); file. write ( line );

              line = '#TER\n'; file. write ( line );

          line = '#ENDMDL\n'

          line = 'printing ISC_IC\n'; file. write ( line );
#musze jakos to ladnie wyprintowac, i cos zjesc dobrego
          if len(self. CENTREs)>=3:

             line = self.ISC_IC+['\n'];

             line = '#ISC    TM%2d IC %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC_IC[0]), float(self.ISC_IC[1]), float(self.ISC_IC[2]) ); file. write ( line );
             line = '#ISC    TM%2d IC %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC_IC[3]), float(self.ISC_IC[4]), float(self.ISC_IC[5]) ); file. write ( line );
             line = '#ISC    TM%2d IC %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC_IC[6]), float(self.ISC_IC[7]), float(self.ISC_IC[8]) ); file. write ( line );

             line = 'printing ISC_EC\n'; file. write ( line );
#musze jakos to ladnie wyprintowac, i cos zjesc dobrego
             line = self.ISC_EC+['\n'];

             line = '#ISC    TM%2d EC %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC_EC[0]), float(self.ISC_EC[1]), float(self.ISC_EC[2]) ); file. write ( line );
             line = '#ISC    TM%2d EC %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC_EC[3]), float(self.ISC_EC[4]), float(self.ISC_EC[5]) ); file. write ( line );
             line = '#ISC    TM%2d EC %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC_EC[6]), float(self.ISC_EC[7]), float(self.ISC_EC[8]) ); file. write ( line );


             line = 'printing ISC\n'; file. write ( line );
#musze jakos to ladnie wyprintowac, i cos zjesc dobrego
             line = self.ISC_EC+['\n'];

             line = '#ISC    TM%2d AL %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC[0]), float(self.ISC[1]), float(self.ISC[2]) ); file. write ( line );
             line = '#ISC    TM%2d AL %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC[3]), float(self.ISC[4]), float(self.ISC[5]) ); file. write ( line );
             line = '#ISC    TM%2d AL %8.3f %8.3f %8.3f\n' %( int(IDi), float(self.ISC[6]), float(self.ISC[7]), float(self.ISC[8]) ); file. write ( line );

#          quit()
# i have to check the Contact Pattern Matrix so it is in agreement / derived from Minimum Distance Matrix

#####################################################################################################################################################

      def SlicesCOMsAlignedToXAxis ( self ):

          EC_SliceCOMs, MM_SliceCOMs, IC_SliceCOMs = [[],[],[]]

          for N in range ( len ( self.CENTREs. Content ) ) :

              EC_SliceCOMs. append ( self.CENTREs. Content [ N ]. Content [ 0 ] )
              MM_SliceCOMs. append ( self.CENTREs. Content [ N ]. Content [ 1 ] )
              IC_SliceCOMs. append ( self.CENTREs. Content [ N ]. Content [ 2 ] ) 

          SlicesCOMsAlignedToXAxisI = [ SlicePoints ( SliceCOM ). AlignToXAxis ( ) for SliceCOM in [EC_SliceCOMs, MM_SliceCOMs, IC_SliceCOMs ]  ]

          return SlicesCOMsAlignedToXAxisI

#####################################################################################################################################################

      def NumerTypuMatrycyKontaktu ( self ):

          import SetOfN_TMs_SetRepresentationsModule; from SetOfN_TMs_SetRepresentationsModule import NumerowaneMozliweTypyMatryc

          NumerowaneMozliweTypyMatrycI = NumerowaneMozliweTypyMatryc ( len ( self. HELIX_IDS ) )

          BinarizedContactPatternMatricesI = self. BinarizedContactPatternMatrices ( )

          for NumerTypu in NumerowaneMozliweTypyMatrycI.keys():

              if NumerowaneMozliweTypyMatrycI [NumerTypu] == BinarizedContactPatternMatricesI: 

                 return NumerTypu

#####################################################################################################################################################

      def AminokwasyKontaktu ( self ):

          EC, MM, IC = self. CONTACT_RESIDUES_EC_MM_IC

##############################################

          AminokwasyKontaktuEC = [ ]

          for I in range ( len ( EC )  ):

              for J in range ( I + 1, len ( EC ) ):

                  
                  if EC [I][J] != '[]':
                     

                     for Para in EC [I][J][1:-1].split('], ['):

                         for Aminokwas in Para [1:-1]. split ( ',' ):

                             if Aminokwas.strip('\'') not in AminokwasyKontaktuEC: AminokwasyKontaktuEC. append ( Aminokwas.strip('\'')[-1] )

                  ######################################

##############################################

          AminokwasyKontaktuMM = [ ]

          for I in range ( len ( MM )  ):

              for J in range ( I + 1, len ( MM ) ):
                  
                  if MM [I][J] != '[]':
                     
                     for Para in MM [I][J][1:-1].split('], ['):

                         for Aminokwas in Para [1:-1]. split ( ',' ):
#                             print Aminokwas
#                             print Aminokwas [-2]

                             if Aminokwas.strip('\'')[-1] not in AminokwasyKontaktuMM: AminokwasyKontaktuMM. append ( Aminokwas.strip('\'')[-1] )

                  ######################################

##############################################

          AminokwasyKontaktuIC = [ ]

          for I in range ( len ( IC )  ):

              for J in range ( I + 1, len ( IC ) ):

                  
                  if IC [I][J] != '[]':
                     
                     for Para in IC [I][J][1:-1].split('], ['):

                         for Aminokwas in Para [1:-1]. split ( ',' ):

                             if Aminokwas.strip('\'')[-1] not in AminokwasyKontaktuIC: AminokwasyKontaktuIC. append ( Aminokwas.strip('\'')[-1] )

                  ######################################

          return [ AminokwasyKontaktuEC, AminokwasyKontaktuMM, AminokwasyKontaktuIC ]

#####################################################################################################################################################

      def Itemset ( self ):

          self.NumerTypuMatrycyKontaktu = self.NumerTypuMatrycyKontaktu ( )
          self. AminokwasyKontaktu = self.AminokwasyKontaktu ( )
        
          import SetOfN_TMs_SetRepresentationsModule; from SetOfN_TMs_SetRepresentationsModule import Itemset;

          return Itemset ( self.PDBCode, \
                           self.ChainID, \
                           self. HELIX_IDS, \
                           self.MaxTilt(), \
                           self.Touching(), \
                           self.Closed(), \
                           self.NumerTypuMatrycyKontaktu, \
                           self.AminokwasyKontaktu )

#####################################################################################################################################################

      def RozbijNaPodzbioryZNakladaniem(self, Rzedy, Nakladanie = 0 ):
          import Rozbicia; from Rozbicia import SformatowaneRozbicia

          RozbiciaReprezentacji = [ ]

          RozbiciaI =  SformatowaneRozbiciaZNakladaniem ( range( self.HelixIDs ), Rzedy, Nakladanie )

          for RozbicieIndeksow in RozbiciaI:

              RozbicieReprezentacji = [ ]

              for ListaIndeksow in  RozbicieIndeksow:

                  RozbicieReprezentacji. append ( self.NPodzbior ( ListaIndeksow ) )

              RozbiciaReprezentacji. append ( Rozbicie )

          return RozbiciaReprezentacji

#####################################################################################################################################################
############## jakie jeszcze grafy chcial Henri #####################################################################################################
#####################################################################################################################################################

import GeometricalClassesModule; from GeometricalClassesModule import *;

class SlicePoints ( SetOfPoints ):

      def __init__ ( self, InputPoints ):

          self. Content = [ ]

          for InputPoint in InputPoints:

              NowyInputPoint = [ float ( InputPoint [ 0 ] ), float ( InputPoint [ 1 ] ) ] #, float ( InputPoint [ 2 ] ) ]

              self. Content. append ( Point ( NowyInputPoint ) )

#####################################################################################################################################################

      def TranslateH1ToOrigin ( self ):

          H1 = self.Content [0]

          H1_0 = SetOfPoints ( [self. Content [ 0 ], Point ( [ 0.0, 0.0, 0.0 ] ) ] ). Vector ( )
          
          self. Translate ( H1_0 )
  
          return

#####################################################################################################################################################

      def AlignToXAxis ( self ):

          import GeometricalClassesModule; from GeometricalClassesModule import Vector, Point, SetOfPoints;

          self.  TranslateH1ToOrigin ( )

          H1_H2 = SetOfPoints ( [ self. Content[0], self.Content[1] ] ).  Vector ()

#          print H1_H2. Length ()
#          quit ()

          Angle = H1_H2. AngleToXAxis ( )

          H1H2H3PointsRot = [ Point ( HPoint ). RotateByAngle ( Angle ) for HPoint in self. Content ]        

          return H1H2H3PointsRot

#####################################################################################################################################################

      def CenteredAndOriented ( self ):

          Centered = self. TranslateH1ToOrigin ( )
          Oriented = Centered .AlignH1H2ToXAxis ( )

          return Oriented

#####################################################################################################################################################
#####################################################################################################################################################
