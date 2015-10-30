import numpy as np
import sys, os

import Kombinatoryka; from Kombinatoryka import *;
import PlotToolsModule; from PlotToolsModule import HistogramPlot

import numpy, scipy
from scipy.cluster.vq import *

from GeometricalClassesModule import * 

import PlotToolsModule; from PlotToolsModule import ScatterPlot

from PlotToolsModule import ScatterPlot1

import ChemiaFizyka

import Parametry
LetterNumber = { 'A':1.0,'C':2.0,'D':3.0,'E':4.0,'F':5.0,'G':6.0,'H':7.0,'I':8.0,'K':9.0,'L':10.0,\
'M':11.0,'N':12.0,'P':13.0,'Q':14.0,'R':15.0,'S':16.0,'T':17.0,'V':18.0,'W':19.0,'Y':20.0}

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

def ReadRMSDMatrix ( InputPath ):

    ReadRMSDMatrix = [ ]

    InputFile = open ( InputPath, 'r' )

    for InputLine in InputFile. readlines ( ):

        ReadRMSDMatrixRow = [ float ( RMSDValue ) for RMSDValue in InputLine. split ('\t') ]

        ReadRMSDMatrix. append ( ReadRMSDMatrixRow )      

    return np.array ( ReadRMSDMatrix )

#####################################################################################################################################################
# ok potem jeszcze stestowac z wlasna osia :)

#####################################################################################################################################################

def KMeansClusterings ( Matrix, NRange, GraphFileName = 'NoClusters_Variance' ):

    NoClusters_Variance_Array = [ ]

    for N in range(NRange[0],NRange[1]):
    
        centroids, idx = kmeans ( Matrix, N ) #musze sprawdzic co to robi

#        print centroids # chyba czeba isc do roboty

        NoClusters_Variance_Array. append ( [ float(N), idx ] )

        code,distance = vq(Matrix,centroids)

        clustersDict = {}; 
        for I in range ( N ): # stwor leksykon pusty zawierajacy rzeczy w klastrach
            clustersDict [ I ] = [ ];

        for M in range (len ( code)): 

            clustersDict [ code [ M ] ]. append (  M  )

        ScatterPlot1 ( numpy.array ( NoClusters_Variance_Array ), 'NoClusters_Variance' )

    return clustersDict

#####################################################################################################################################################

def KMeansClustering ( Matrix, N ):

    centroidsIndexes = [ ]

    NoClusters_Variance_Array = [ ]    
    
    centroids, idx = kmeans ( Matrix, N ) 

    print 'Matrix' + str( Matrix )

    print 'Centroids' + str( centroids )
#    print [ numpy.unravel_index(centroid, centroids.shape) for centroid in centroids ]
#    print [ centroids.index(centroid) for centroid in centroids ]

    for centroid in centroids:
        centroidList = [ el for el in centroid ]

        centroidsIndexes. append ( centroidList.index( min ( centroid ) ) );

    print 'End Centroids'

#    NoClusters_Variance_Array. append ( [ float(N), idx ] )

    code, distance = vq (Matrix,centroids) # to zwraca nke?

    clustersDict = {}; 

#    print code; print distance;

    for I in range ( N ): # stwor leksykon pusty zawierajacy rzeczy w klastrach
        clustersDict [ I ] = [ ];

    for M in range (len ( code)): # nie no musze inaczej 

        print M

        clustersDict [ code[ M ] ]. append (  M  )

#        ScatterPlot1 ( numpy.array ( NoClusters_Variance_Array ), 'NoClusters_Variance' )

    return  [ clustersDict, centroidsIndexes, idx ]

#clustering powinien byc klasa sama w sobie :)

#####################################################################################################################################################

class ClusteringResults ( list ):

      def __init__ ( clustersDict, centroidsIndexes ):

          return

#####################################################################################################################################################

def Nakladanie ( IDs1, IDs2 ):

    Nakladanie = [ ]

    for Element in IDs2:

        IDs2NMinusOne = NMinusOne (IDs2, Element )

        print IDs2NMinusOne; print IDs1;
         
        if IsSubset( IDs2NMinusOne, IDs1 ):

           return IDs2NMinusOne

    for Element in IDs1:

        IDs1NMinusOne = NMinusOne (IDs1, Element )

        if IsSubset ( IDs1NMinusOne, IDs2  ):

           return IDs1NMinusOne

    return [ ]

#####################################################################################################################################################

def NMinusOne ( IDs, Element):

    NMinusOneI = [ ]

    for ElementI in IDs:

        if ElementI != Element:

           NMinusOneI. append ( ElementI )

#    print IDs; print NMinusOneI

    return NMinusOneI

#####################################################################################################################################################

def IsSubset ( Small, Big ):

    for Element in Small:

        if Element not in Big:

           return False

    return True

#####################################################################################################################################################

def MergeMatrices ( Matrix1, Matrix2, NakladanieI ): # i tak raczej nie bedziemy tego robic

    return MergedMatrix

#####################################################################################################################################################

def MergeRepresentations ( Representation1, Representation2, NakladanieI ):

    HELIX_IDSI = [ ]

# musze to sobie lepiej przemyslec w tym momencie bo Nakladanie sklada sie z N minus jeden elementow

    IndexyNakladania1 = [ ]
    for Element in NakladanieI:
        IndexyNakladania1. append ( Representation1. HELIX_IDS.index ( Element ) )

    IndexyNakladania2 = [ ]
    for Element in NakladanieI:
        IndexyNakladania2. append ( Representation2. HELIX_IDS.index ( Element ) )

    TILTS_OF_HELICESI = [ ]

########################################################################################################

    for N in range ( len ( Representation1.HELIX_IDS ) ):

        if N not in IndexyNakladania1:

           HELIX_IDSI. append ( Representation1.HELIX_IDS [ N ] )

    for N in range ( len ( Representation1.HELIX_IDS ) ):

        if N in IndexyNakladania1:

           HELIX_IDSI. append ( Representation1.HELIX_IDS [ N ] )

    for N in range ( len ( Representation2.HELIX_IDS ) ):

        if N not in IndexyNakladania2:

           HELIX_IDSI. append ( Representation2.HELIX_IDS [ N ] ) 

########################################################################################################

    for N in range ( len ( Representation1.TILTS_OF_HELICES ) ):

        if N not in IndexyNakladania1:

           TILTS_OF_HELICESI. append ( Representation1.TILTS_OF_HELICES [ N ] )

    for N in range ( len ( Representation1.TILTS_OF_HELICES ) ):

        if N in IndexyNakladania1:

           TILTS_OF_HELICESI. append ( Representation1.TILTS_OF_HELICES [ N ] )

    for N in range ( len ( Representation2.TILTS_OF_HELICES ) ):

        if N not in IndexyNakladania2:

           TILTS_OF_HELICESI. append ( Representation2.TILTS_OF_HELICES [ N ] ) 

########################################################################################################

    TILTS_OF_HALF_HELICESI = [ ]; TILTS_OF_HALF_HELICES_IC = [ ];

    for K in range ( len ( Representation1.TILTS_OF_HALF_HELICES) ):

        for N in range ( len ( Representation1.TILTS_OF_HALF_HELICES [ K ] ) ):

            if N not in IndexyNakladania1:

               TILTS_OF_HALF_HELICESI. append ( Representation1.TILTS_OF_HALF_HELICES [ K ] [ N ] )

        for N in range ( len ( Representation1.TILTS_OF_HALF_HELICES ) ):

            if N in IndexyNakladania1:

               TILTS_OF_HALF_HELICESI. append ( Representation1.TILTS_OF_HALF_HELICES [ K ] [ N ] )

        for N in range ( len ( Representation2.TILTS_OF_HALF_HELICES ) ):

            if N not in IndexyNakladania2:

               TILTS_OF_HALF_HELICESI. append ( Representation2.TILTS_OF_HALF_HELICES [ K ] [ N ] )   

########################################################################################################## 
# teraz jest zagwozdka jak zrobic zeby polaczyc Contact Pattern Matrices                                 #

########################################################################################################
################ HelixNterDescriptors ##################################################################
########################################################################################################

    HelixNterDescriptorsI = [ ]

    for N in range ( len ( Representation1.HelixNterDescriptors ) ):

        if N not in IndexyNakladania1:

           HelixNterDescriptorsI. append ( Representation1.HelixNterDescriptors [ N ] )

    for N in range ( len ( Representation1.HelixNterDescriptors ) ):

        if N in IndexyNakladania1:

           HelixNterDescriptorsI. append ( Representation1.HelixNterDescriptors [ N ] )

    for N in range ( len ( Representation2.HelixNterDescriptors ) ):

        if N not in IndexyNakladania2:

           HelixNterDescriptorsI. append ( Representation2.HelixNterDescriptors [ N ] ) 

##########################################################################################################

    ProteinNterDescriptorI = Representation1.ProteinNterDescriptor

###########################################################################################################
### potrzebuje backupu, przerwy, potem latwiej rozkminic AASEQi, potem Matryce na koncu ###################
###########################################################################################################

#### aby rozkminic AASEQ i trzebaby je pogrupowac w momencie czytania reprezentacji ######################
##########################################################################################################
##################### AASEQs ###########################################################################
########################################################################################################

    AASEQsI = [ ]

    for N in range ( len ( Representation1.AASEQs ) ):

        if N not in IndexyNakladania1:

           AASEQsI. append ( Representation1.AASEQs [ N ] )

    for N in range ( len ( Representation1.AASEQs ) ):

        if N in IndexyNakladania1:

           AASEQsI. append ( Representation1.AASEQs [ N ] )

    for N in range ( len ( Representation2.AASEQs ) ):

        if N not in IndexyNakladania2:

           AASEQsI. append ( Representation2.AASEQs [ N ] ) 

##########################################################################################################

########################################################################################################

    CENTREsI = [ ]

    for N in range ( len ( Representation1.CENTREs ) ):

        if N not in IndexyNakladania1:

           CENTREsI. append ( Representation1.CENTREs [ N ] )

    for N in range ( len ( Representation1.CENTREs ) ):

        if N in IndexyNakladania1:

           CENTREsI. append ( Representation1.CENTREs [ N ] )

    for N in range ( len ( Representation2.CENTREs ) ):

        if N not in IndexyNakladania2:

           CENTREsI. append ( Representation2.CENTREs [ N ] ) 

##########################################################################################################

########################################################################################################

    I1_3_VECsI = [ ]

    for N in range ( len ( Representation1.I1_3_VECs ) ):

        if N not in IndexyNakladania1:

           I1_3_VECsI. append ( Representation1.I1_3_VECs [ N ] )

    for N in range ( len ( Representation1.I1_3_VECs ) ):

        if N in IndexyNakladania1:

           I1_3_VECsI. append ( Representation1.I1_3_VECs [ N ] )

    for N in range ( len ( Representation2.I1_3_VECs ) ):

        if N not in IndexyNakladania2:

           I1_3_VECsI. append ( Representation2.I1_3_VECs [ N ] ) 

##########################################################################################################

########################################################################################################

    AXESI = [ ]

    for N in range ( len ( Representation1.AXES ) ):

        if N not in IndexyNakladania1:

           AXESI. append ( Representation1.AXES [ N ] )

    for N in range ( len ( Representation1.AXES ) ):

        if N in IndexyNakladania1:

           AXESI. append ( Representation1.AXES [ N ] )

    for N in range ( len ( Representation2.AXES ) ):

        if N not in IndexyNakladania2:

           AXESI. append ( Representation2.AXES [ N ] ) 

##########################################################################################################

    ContactPatternMatrix_EC = [ ]

# pytanie brzmie jak sie merguje 2 matryce majac indeksy nakladania w pierwszej itd
# pewnie trzebaby wydobyc indexy nienakladania
# nakladania itd
#     TM1 TM2
# TM1  40   1
# TM2   1  40
#
#
#     TM2 TM3
# TM2  50   2
# TM3   2  50
#
#     TM1 TM3
# TM1  40   3
# TM3   3  50
#
# no wlasnie, potrzwbujemy jeszcze trzeciej reprezentacji! zeby zrobic matryce kontaktow!
#
# TM1, TM3
#     TM1 TM2 TM3
# TM1  40   1   3   
# TM2   1  50   2
# TM3   3   2  50
#
# a jak to bedzie wygladac dla N wiekszego np N = 3, N+1 = 4
# potrzebujemy duzo reprezentacji, trzeba sie zachowywac jak przy ekstrakcji zamknietego, musze isc spac teraz bo juz dzis nie wymysle tego
# smieszna rzecz polega na tym, ze o wiele prosciej byloby moze isc od gory, wszak dla zbioru
# Helis Transblonowych Mozna tez pokusic sie o taka reprezentacje
# potem w takiej reprezentacji szukalibysmy submatryc i to by byl jazz
# ale najpierw musialbym zrobic reprezentacje zbioru wszystkich helis w lancuchu
# 
#     TM1 TM2 TM3     
# TM1  40   1   3 TM1
# TM2   1  50   2 TM2
# TM3   3   2  50 TM4
#
#     TM2 TM3 TM4
# TM2  50   2   4
# TM3   2  50   5
# TM4   4   5  60
#
#     TM1 TM2 TM3 TM4
# TM1  40   1   3
# TM2
# TM3
# TM4
###########################################################################################################      
     
    from N_TMs_SetRepresentationModule import NSetRepresentation;  

    return NSetRepresentation ( \
                     HELIX_IDSI, \
                     TILTS_OF_HELICESI, \
                     TILTS_OF_HALF_HELICESI, \
                     ContactPatternMatrices, \
                     CONTACT_RESIDUES_EC_MM_ICI, \
                     MinimumDistanceMatricesI, \
                     HelixNterDescriptorsI, \
                     ProteinNterDescriptorI, \
                     RelativeOrientationMatrixI, \
                     AASEQsI, \
                     CENTREsI, \
                     I1_3_VECs, \
                     AXESI, \
                     MM_SLICE_COMs_AngleI = 'NA', \
                     ClockwiseAntiClockwiseI = 'NS', \
                     ) # Representations

#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

class SetOfN_TMs_SetRepresentations ( list ): # trudno, musze to zrobic jutro

      def __init__ ( self, Input_N_TMs_SetRepresentationInstances ):

          self.Content  = [ N_TMs_SetRepresentationInstance for N_TMs_SetRepresentationInstance in Input_N_TMs_SetRepresentationInstances ]

####################################################################################################################################################

      def PrzepiszTiltyDoArkusza ( self, OutFile):

          for Reprezentacja in self. Content:
# musze przeczytac xlwt i po prostu to zrobic
# ide spac? jutro rano zrobie ... moze na poczatku rano pobiegam 1/2h
# musze biegac wiecej, okazuje sie
# jak to bedzie wygladac, na poziomie Setu :) musze zmienic czytanie p
#1) na poziomie tego musze miec leksykon 
#1) zaprojektowac jak by mial taki arkusz wygladac
#2) pobiegac pol godziny
#) wyjsc o 12.30 zeby o 13.30 byc w labie
#moglbym dzis na praktyke jechac, a tak polacze przyjemne z pozytecznym

              Reprezentacja. PrzepiszTiltyDoArkusza (  )

          return

####################################################################################################################################################

      def Output ( self, Path ):

          ProteinNterDescriptor = 'XX'

          for N_TMs_SetRepresentationInstance in self. Content:

              N_TMs_SetRepresentationInstance. Output ( ProteinNterDescriptor, Path )

          return

####################################################################################################################################################

      def SuperpositionMatrix ( self, AllowPerturbations, AllowFlip ):

#          print self. Content [0]. CENTREs [0]. Content # czy moge tak zrobic?, chyba nie :P

          RotationMatrix = HierarchicalSetsOfPoints ( [ self. Content [0]. CENTREs, self. Content [1]. CENTREs ] ). SuperpositionMatrix ( AllowPerturbations, AllowFlip )

          return RotationMatrix

####################################################################################################################################################

      def KMeansClustering ( self, N=10, AllowPerturbations = False, AllowFlip = False, RMSDMatrixI = [] ):
# i teraz musimy wziac znalezc funkcje klastrowania, ktora jest gdzies w study sdf file

          if RMSDMatrixI != []:


             return KMeansClustering ( RMSDMatrixI, N )

          else:

             return KMeansClustering ( self. RMSDMatrix( AllowPerturbations, AllowFlip ), N )

####################################################################################################################################################

# i teraz musimy wziac znalezc funkcje klastrowania, ktora jest gdzies w study sdf file

#          return KMeansClusterings ( self. RMSDMatrix( AllowPerturbations ), N )

#####################################################################################################################################################
# niech printuje centroidy najpierw :)
      def KMeansClusters ( self, N , AllowPerturbations = False, AllowFlip = False, RMSDMatrix = False, Out = 'ConsecutiveCentroidFile.txt'  ):

          if RMSDMatrix != []:

             RMSDMatrix = ReadRMSDMatrix(RMSDMatrix)

          KMeansClustersI = [ ]
          ClusteringResults = self. KMeansClustering ( N, AllowPerturbations, AllowFlip, RMSDMatrix )
          ClustersDict = ClusteringResults [0]
          CentroidsIndexes = ClusteringResults [1]
          Variance = ClusteringResults [2]

          print 'CentroidsIndexes'

          CentroidFile = open ( Out, 'w' )
          
          for Index in CentroidsIndexes:

              CentroidFile. write ( self.Content[Index].PDBCode +' '+ str( self.Content[Index]. ChainID) + ' ' + str ( self.Content[Index]. HELIX_IDS ) + '\n' ) 

          Centroids = [ self.Content[Index] for Index in CentroidsIndexes ]

          for Key in ClustersDict. keys ( ):

              KMeansCluster = [  self.Content[i] for i in ClustersDict [Key] ]
              Lista = [ Trip. PDBCode +' '+str(Trip. ChainID)+' '+ str(Trip. HELIX_IDS) for Trip in KMeansCluster ]
              print str(Key) +' '+ str(Lista)

              KMeansClustersI. append (  SetOfN_TMs_SetRepresentations ( KMeansCluster ) )
          
              CentroidFile. write ( str(Key) +' '+ str(Lista) )

          Variance

          CentroidFile. write ( 'Variance: '+ str(Variance) )

          CentroidFile. close ( )

          return [ KMeansClustersI, Centroids ]

####################################################################################################################################################

      def ClusterAxesVectors ( self, AllowPerturbations = False, AllowFlip = False, RMSDMatrix = [ ] ):

          return

####################################################################################################################################################

      def EkselowyPlikTwoHelices (self, Path):

          import xlwt

          book = xlwt. Workbook()
          sheet = book.add_sheet('TwoHelicesSheet')
          rowx = 1
          colx=0

          sheet.write(0, 0, 'Code')
          sheet.write(0, 1, 'Chain ID')

          sheet.write(0, 2, 'TM1 ID')
          sheet.write(0, 3, 'TM2 ID')
          sheet.write(0, 4, 'Crossing Angle (deg)')
          sheet.write(0, 5, 'Crossing Angle in Extracellular Leaflet (deg)')
          sheet.write(0, 6, 'Crossing Angle in Intracellular Leaflet (deg)')
          sheet.write(0, 7, 'Minimum Distance in Extracellular Slice (A)')
          sheet.write(0, 8, 'Minimum Distance in Intracellular Slice (A)')
          sheet.write(0, 9, 'Minimum Distance in Membrane Middle Slice (A)')
          sheet.write(0,10, 'Minimum Distance (A)')
          sheet.write(0,11, 'Contact Residues in Extracellular Slice')
          sheet.write(0,12, 'Contact Residues in Intracellular Slice')
          sheet.write(0,13, 'Contact Residues in Membrane Middle Slice')
          
          rowx = 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. PDBCode)

              rowx += 1

          rowx =  1
          colx += 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. ChainID)

              rowx += 1

          rowx = 1
          colx += 1
          
          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. HELIX_IDS[0])

              rowx += 1

          rowx = 1
          colx += 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. HELIX_IDS[1])

              rowx += 1

          rowx = 1
          colx += 1


          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. CrossingAnglesMatrices [2][0][1])

              rowx += 1


          rowx = 1
          colx += 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. CrossingAnglesMatrices [0][0][1])

              rowx += 1


          rowx = 1
          colx += 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. CrossingAnglesMatrices [1][0][1])

              rowx += 1


          rowx = 1
          colx += 1


          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. MinimumDistanceMatrices[0][0][1])

              rowx += 1

          rowx = 1
          colx += 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. MinimumDistanceMatrices[2][0][1])

              rowx += 1

          rowx = 1
          colx += 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. MinimumDistanceMatrices[1][0][1])

              rowx += 1

          rowx = 1
          colx += 1

          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, min(RepresentationInstance. MinimumDistanceMatrices[0][0][1], RepresentationInstance. MinimumDistanceMatrices[1][0][1],RepresentationInstance. MinimumDistanceMatrices[2][0][1]))

              rowx += 1

          rowx = 1
          colx += 1


          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. CONTACT_RESIDUES_EC_MM_IC [0][0][1])

              rowx += 1
              
          rowx = 1
          colx += 1


          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. CONTACT_RESIDUES_EC_MM_IC [2][0][1])

              rowx += 1
              
          rowx = 1
          colx += 1


          for RepresentationInstance in self. Content:

              sheet.write(rowx, colx, RepresentationInstance. CONTACT_RESIDUES_EC_MM_IC [1][0][1])

              rowx += 1
              
          rowx = 1
          colx += 1


          book.save('TwoHelicesWorksheetInteracting20150724.xls')

####################################################################################################################################################

      def EkselowyPlikOneHelix (self, Path):

          import xlwt

          book = xlwt. Workbook()
          sheet = book.add_sheet('OneHelixSheet')
          rowx = 1
          colx=0

          sheet.write(0, 0, 'Code')
          sheet.write(0, 1, 'Chain ID')
          sheet.write(0, 2, 'TM ID')
          sheet.write(0, 3, 'Tilt PCA (deg)')
          sheet.write(0, 4, 'Tilt MC  (deg)')
          sheet.write(0, 5, 'Kink Angle (deg)')
          sheet.write(0, 6, 'Overhang Length (A)')
          sheet.write(0, 7, 'Tilt PCA of Extracellular Leaflet Half-Helix (deg)')
          sheet.write(0, 8, 'Tilt PCA of Intracellular Leaflet Half-Helix (deg)')
          sheet.write(0, 9, 'Tilt MC of Extracellular Leaflet Half-Helix (deg)')
          sheet.write(0,10, 'Tilt MC of Intracellular Leaflet Half-Helix (deg)')

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. HELIX_IDS:

                  sheet.write(rowx, colx, RepresentationInstance. PDBCode)
                  rowx += 1

          colx += 1
          rowx  = 1



          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. HELIX_IDS:

                  sheet.write(rowx, colx, RepresentationInstance. ChainID)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. HELIX_IDS:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. PCATILTS_OF_HELICES:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. COMTILTS_OF_HELICES:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. KinkAngles:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. OverhangLengths:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. PCATILTS_OF_HALF_HELICES [0]:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. PCATILTS_OF_HALF_HELICES [1]:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1


          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. COMTILTS_OF_HALF_HELICES [0]:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          colx += 1
          rowx  = 1

          for RepresentationInstance in self. Content:

              for Tilt in RepresentationInstance. COMTILTS_OF_HALF_HELICES [1]:

                  sheet.write(rowx, colx, Tilt)
                  rowx += 1

          book.save('OneHelixWorksheet.xls')
              
          return
          
####################################################################################################################################################

      def HierarchicalClusters ( self, linkage = 'single' , AllowPerturbations = False, AllowFlip = False, RMSDMatrix = [] ):

          Lista = range ( len ( RMSDMatrix ) )

          Merges = [ ]

# musze skopiowac moje rozwiazanie klastrow
# mamy RMSDMatrix, i teraz pytanie czy przerobic je na similarity matrix czy po prostu dostosowac do 
# wiec najpierw znalezc pare ktora jest min

          if RMSDMatrix != []:

             RMSDMatrix = ReadRMSDMatrix(RMSDMatrix)

          while len ( RMSDMatrix ) >> 1:

                minRMSD = 1000.0

# znajdujemy najmniejsze najpierw

                for I in range( len ( RMSDMatrix ) ): 

                    for J in range ( I+1, len ( RMSDMatrix ) ):

                        if  RMSDMatrix [I][J] <= minRMSD:

                            minRMSD = RMSDMatrix [I][J]

                            minI = I

                            minJ = J

                #newRow = []

                if linkage == 'single':

                   import hcluster
                   import matplotlib.pyplot as plt
                   import pickle
                   import urllib
  
                   url = "http://examples.obspy.org/dissimilarities.pkl"
                   dissimilarity = pickle.load(urllib.urlopen(url))
  
                   plt.subplot(121)
                   plt.imshow(1 - dissimilarity, interpolation="nearest")
  
                   dissimilarity = hcluster.squareform(dissimilarity)
                   threshold = 0.3
                   linkage = hcluster.linkage(dissimilarity, method="single")
                   clusters = hcluster.fcluster(linkage, 0.3, criterion="distance")
  
                   plt.subplot(122)
                   hcluster.dendrogram(linkage, color_threshold=0.3)
                   plt.xlabel("Event number")
                   plt.ylabel("Dissimilarity")
                   plt.show()

                   newRow = np.array ([ min ( RMSDMatrix[minI][J], RMSDMatrix[minJ][J]  ) for J in range( len ( RMSDMatrix ) ) ])
#                   newColumn = np.hstack ( [ np.transpose(newRow), [0.0] ] )
                   
                elif linkage == 'complete':

                   newRow = [ max ( RMSDMatrix[minI][J], RMSDMatrix[minJ][J]  ) for J in range( len ( RMSDMatrix ) ) ]
                newColumn = np.zeros(  (len ( RMSDMatrix ) + 1, 1) )
                print newColumn[0,0]

                

                for K in range ( len ( newRow ) ):
                    newColumn[K,0] = newRow [ K ]

#                print RMSDMatrix

                print np.shape ([newRow]); print np.shape ( newColumn );

                RMSDMatrix = np. vstack ( [ RMSDMatrix, [newRow] ] )
                
                print np.shape( RMSDMatrix );
                RMSDMatrix = np. hstack ( [ RMSDMatrix, newColumn ] )

                RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minJ],0); RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minJ],1)
                RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minI],0); RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minI],1)                       

                                       
                Merges. append ( [ minI, minJ ] )
          
          print Merges
# teraz z Mergesami wypisac klaster

          for N in range ( len ( Merges ) ):

#              print Merges [N][0]

#              print Lista

              

              NowyKlaster = [ Lista [ Merges [N][0]], Lista [ Merges [N][1] ] ]

              Lista. append ( NowyKlaster )

              del Lista [ Merges [N][1] ]
              del Lista [ Merges [N][0] ]

              

          
          print Lista
    
          return

#####################################################################################################################################################

      def HierarchicalClustersCentroids ( self, linkage = 'single' , AllowPerturbations = False, AllowFlip = False, RMSDMatrixI = [], CentroidsFile = '' ):

          if RMSDMatrixI != []:

             RMSDMatrixI = ReadRMSDMatrix(RMSDMatrixI)

          Centroids = ReadCentroidsFromTXT (CentroidsFile)
          CentroidIndexesI = CentroidIndexes (Parametry. NsetRepresentationsDatasetFilePCA, Centroids )
#          print CentroidIndexesI

          RMSDMatrix = PodMatrycaZIndeksami (RMSDMatrixI, CentroidIndexesI)    
#          print RMSDMatrix      

          Lista = range ( len ( RMSDMatrix ) )

          Merges = [ ]

# musze skopiowac moje rozwiazanie klastrow
# mamy RMSDMatrix, i teraz pytanie czy przerobic je na similarity matrix czy po prostu dostosowac do 
# wiec najpierw znalezc pare ktora jest min

          while len ( RMSDMatrix ) >> 1:

                minRMSD = 1000.0

# znajdujemy najmniejsze najpierw

                for I in range( len ( RMSDMatrix ) ): 

                    for J in range ( I+1, len ( RMSDMatrix ) ):

                        if  RMSDMatrix [I][J] <= minRMSD:

                            minRMSD = RMSDMatrix [I][J]

                            minI = I

                            minJ = J

                #newRow = []

                if linkage == 'single':


                   import hcluster
                   import matplotlib.pyplot as plt
                   import pickle
                   import urllib
  
                   url = "http://examples.obspy.org/dissimilarities.pkl"

                   for N in range(len(RMSDMatrix)):
                       RMSDMatrix[N][N] = 0.0

                   dissimilarity = np.array (RMSDMatrix) # pickle.load(urllib.urlopen(url))

                   print dissimilarity;# quit ()
  
                   plt.subplot(121)
                   plt.imshow(1 - dissimilarity, interpolation="nearest")
  
                   dissimilarity = hcluster.squareform(dissimilarity)
                   threshold = 0.3
                   linkage = hcluster.linkage(dissimilarity, method="single")
                   clusters = hcluster.fcluster(linkage, 0.3, criterion="distance")
  
                   plt.subplot(122)
                   hcluster.dendrogram(linkage, color_threshold=0.3)
                   plt.xlabel("Centroid number")
                   plt.ylabel("Dissimilarity")
                   plt.show()


                   newRow = np.array ([ min ( RMSDMatrix[minI][J], RMSDMatrix[minJ][J]  ) for J in range( len ( RMSDMatrix ) ) ])
#                   newColumn = np.hstack ( [ np.transpose(newRow), [0.0] ] )
                   
                elif linkage == 'complete':



                   import hcluster
                   import matplotlib.pyplot as plt
                   import pickle
                   import urllib
  
                   url = "http://examples.obspy.org/dissimilarities.pkl"

                   for N in range(len(RMSDMatrix)):
                       RMSDMatrix[N][N] = 0.0

                   dissimilarity = np.array (RMSDMatrix) # pickle.load(urllib.urlopen(url))

                   print dissimilarity;# quit ()
  
                   plt.subplot(121)
                   plt.imshow(1 - dissimilarity, interpolation="nearest")
  
                   dissimilarity = hcluster.squareform(dissimilarity)
                   threshold = 0.3
                   linkage = hcluster.linkage(dissimilarity, method="complete")
                   clusters = hcluster.fcluster(linkage, 0.3, criterion="distance")
  
                   plt.subplot(122)
                   hcluster.dendrogram(linkage, color_threshold=0.3)
                   plt.xlabel("Centroid number")
                   plt.ylabel("Dissimilarity")
                   plt.show()


                   newRow = np.array ([ min ( RMSDMatrix[minI][J], RMSDMatrix[minJ][J]  ) for J in range( len ( RMSDMatrix ) ) ])
#                   newColumn = np.hstack ( [ np.transpose(newRow), [0.0] ] )
                   


                   newRow = [ max ( RMSDMatrix[minI][J], RMSDMatrix[minJ][J]  ) for J in range( len ( RMSDMatrix ) ) ]
                newColumn = np.zeros(  (len ( RMSDMatrix ) + 1, 1) )
                print newColumn[0,0]

                

                for K in range ( len ( newRow ) ):
                    newColumn[K,0] = newRow [ K ]

#                print RMSDMatrix

                print np.shape ([newRow]); print np.shape ( newColumn );

                RMSDMatrix = np. vstack ( [ RMSDMatrix, [newRow] ] )
                
                print np.shape( RMSDMatrix );
                RMSDMatrix = np. hstack ( [ RMSDMatrix, newColumn ] )

                RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minJ],0); RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minJ],1)
                RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minI],0); RMSDMatrix = np. delete ( RMSDMatrix, np.s_[minI],1)                       

                                       
                Merges. append ( [ minI, minJ ] )
          
          print Merges
# teraz z Mergesami wypisac klaster

          for N in range ( len ( Merges ) ):

#              print Merges [N][0]

#              print Lista

              

              NowyKlaster = [ Lista [ Merges [N][0]], Lista [ Merges [N][1] ] ]

              Lista. append ( NowyKlaster )

              del Lista [ Merges [N][1] ]
              del Lista [ Merges [N][0] ]

                        
          print Lista
    
          return

#####################################################################################################################################################


      def NajbardziejPopularneRozbicia ( self ):

          return

####################################################################################################################################################

      def NPodzbiory ( self, N ): # ok, zrobie to jutro na kazcu, najwazniejsze ze TM wyekstrahowane

          NPodzbioryI = [ ]

          for N_TMs_SetRepresentationInstance in self. Content:

              for NPodzbior in N_TMs_SetRepresentationInstance. NPodzbiory ( N ). Content:

                  NPodzbioryI. append ( NPodzbior )

          print len (  NPodzbioryI )

          return SetOfN_TMs_SetRepresentations  ( NPodzbioryI )

####################################################################################################################################################

      def NPodzbioryTouching ( self, N ): # ok, zrobie to jutro na kazcu, najwazniejsze ze TM wyekstrahowane

          NPodzbioryI = [ ]

          for N_TMs_SetRepresentationInstance in self. Content:

              print 'IloscPodzbiorowWszystkich '+str ( len ( N_TMs_SetRepresentationInstance. NPodzbioryTouching ( N ). Content ) )

              for NPodzbior in N_TMs_SetRepresentationInstance. NPodzbioryTouching ( N ). Content:

                  NPodzbioryI. append ( NPodzbior )

          print 'IloscPodzbiorow '+str( len ( NPodzbioryI ) )

          return SetOfN_TMs_SetRepresentations  ( NPodzbioryI )

#####################################################################################################################################################

      def NPodzbioryConsecutive ( self, N ): # ok, zrobie to jutro na kazcu, najwazniejsze ze TM wyekstrahowane

          NPodzbioryI = [ ]

          for N_TMs_SetRepresentationInstance in self. Content:

              print 'IloscPodzbiorowWszystkich '+str ( len ( N_TMs_SetRepresentationInstance. NPodzbioryTouching ( N ). Content ) )

              for NPodzbior in N_TMs_SetRepresentationInstance. NPodzbioryConsecutive ( N ). Content:

                  NPodzbioryI. append ( NPodzbior )

          print 'IloscPodzbiorow '+str( len ( NPodzbioryI ) )

          return SetOfN_TMs_SetRepresentations  ( NPodzbioryI )

#####################################################################################################################################################

      def Consecutive ( self ):

          ConsecutiveSetsI = [ ]

          for Set in self.Content:
 
              if Set.Consecutive ( ):

                 ConsecutiveSetsI. append ( Set )

          return SetOfN_TMs_SetRepresentations ( ConsecutiveSetsI )

#####################################################################################################################################################

      def ConsecutiveAndTouching ( self ):

          ConsecutiveAndTouchingSetsI = [ ]

          for Set in self.Content:
 
              if Set. Consecutive ( ) and Set. Touching ( ) :

                 ConsecutiveAndTouchingSetsI. append ( Set )

          return SetOfN_TMs_SetRepresentations ( ConsecutiveAndTouchingSetsI )

#####################################################################################################################################################

      def MaxTiltOverThreshold ( self, Threshold ):

          ConsecutiveSetsI = [ ]

          for Set in self.Content:
 
              if Set.MaxTiltOverThreshold ( Threshold ):

                 ConsecutiveSetsI. append ( Set )

          return SetOfN_TMs_SetRepresentations ( ConsecutiveSetsI )

#################################################################
#####################################################################################################################################################

      def MaxTilts ( self ):

          MaxTiltsI = [ ]

          for Set in self.Content:

              MaxTiltsI. append ( Set.MaxTilt ( ) )

          return MaxTiltsI

#################################################################
#####################################################################################################################################################

      def CrossingAnglesHistogram ( self, OutputFile ):

          HistogramPlot ( self.CrossingAnglesArray ( ), OutputFile )

          return # idzie tylko o to zeby nie liczyc podwojnie

#####################################################################################################################################################

      def ValueHistogram ( self, OutputFile, Value = 'Tilt', Min = -18, Max = 18, BinNo = 37 ):

          Plik = open (Value + '.csv', 'w')
          
          for X in self. ValueArray ( Value ):

              Plik. write (str(X)+'\n')
          
          Plik. flush ()
          Plik. close ()

          HistogramPlot ( self. ValueArray ( Value ), OutputFile, Min, Max, BinNo)

          return

#####################################################################################################################################################

      def CrossingAnglesArray ( self, Range = '[0.0:90.0]' ):

          CrossingAnglesArrayI = [ ]

          for RepresentationInstance in self. Content:

              print ' CrossingAnglesInRep'
              print CrossingAnglesArrayI

              for CrossingAngleI in RepresentationInstance. CrossingAngles ( ):

                  if Range == '[0.0:90.0]' and CrossingAngleI >= 90.0:

                     CrossingAnglesArrayI. append ( 180.0 - CrossingAngleI )

                  else:
                     
                     CrossingAnglesArrayI. append ( CrossingAngleI )

          return np. array ( CrossingAnglesArrayI )

#####################################################################################################################################################

      def Ro3VsRo2ScatterPlot (self):

#          Ro3s = self. ValueArray ( Value = 'Fi3Fi1' );
          Ro3s = self. ValueArray ( Value = 'Fi3Fi2' );
          Ro2s = self. ValueArray ( Value = 'Fi2Fi1' );
          
          Ro2_Ro3_Array = np.vstack ( [Ro2s, Ro3s] )

          import matplotlib.pyplot as plt

#          plt.scatter ( Ro2s,Ro3s)

#          plt.savefig ('Ro3VsRo2ScatterPlot.png' ,dpi=320)
#          plt.clf()
       

          print Ro2_Ro3_Array;  #quit ();

          ScatterPlot1 ( numpy.array ( Ro2_Ro3_Array ), 'Ro3VsRo2ScatterPlot' )

          return

#####################################################################################################################################################

#options = { 'PCADev': 

#0 : zero,
#                1 : sqr,
#                4 : sqr,
#                9 : sqr,
#                2 : even,
#                3 : prime,
#                5 : prime,
#                7 : prime,
#}
#def PCADevs ():
#    return

#####################################################################################################################################################

# powinienem stworzyc funkcje ktora bedzie od Value Array

      def ValueArray ( self, Value = 'Tilt' ):
#sprobowac instrukcji case (moze miec lokalizacje potrzebnych modulow w dokumentacji
          ValueArrayI = [ ]

          for RepresentationInstance in self. Content:

#moglbym to uproscic?
#          for RepresentationInstance in self. Content:

              if   Value == 'PCADev':

                   print 'Fejslik'

               #  for PCADevI in RepresentationInstance. PCADevs:

               #      ValueArrayI. append ( PCADevI )


              elif Value == 'Fi3Fi2':

                 R1, R2, Fi, Theta1, Fi1, Theta2, Fi2, Theta3, Fi3 = RepresentationInstance. CENTREs. CartesianToISC ( )

                 ValueArrayI. append ( Fi3 - Fi2 )

              elif Value == 'Fi':

                 R1, R2, Fi, Theta1, Fi1, Theta2, Fi2, Theta3, Fi3 = RepresentationInstance. CENTREs. CartesianToISC ( )

                 ValueArrayI. append ( Fi )


              elif Value == 'Fi3Fi1':

                 R1, R2, Fi, Theta1, Fi1, Theta2, Fi2, Theta3, Fi3 = RepresentationInstance. CENTREs. CartesianToISC ( )

                 ValueArrayI. append ( Fi3 - Fi1 )


              elif Value == 'Fi2Fi1':

                 R1, R2, Fi, Theta1, Fi1, Theta2, Fi2, Theta3, Fi3 = RepresentationInstance. CENTREs. CartesianToISC ( )

                 ValueArrayI. append ( Fi2 - Fi1 )


              elif Value == 'Tilt':

                 for TiltI in RepresentationInstance. TILTS_OF_HELICES:

                     ValueArrayI. append ( TiltI )


              elif Value == 'PCATilt':

                 for TiltI in RepresentationInstance. PCATILTS_OF_HELICES:

                     ValueArrayI. append ( TiltI )

              elif Value == 'StatystykaContactAminoAcids_EC':

#                 for ContactAminoAcidEC in RepresentationInstance. ContactAminoAcidsEC: #zmienic w przeczytaniu

                     ContactResiduesMatrix_EC = RepresentationInstance. ContactResiduesMatrices[0]

                     for I in range(len(ContactResiduesMatrix_EC)):
                         for J in range(len(ContactResiduesMatrix_EC)):
                             if len(ContactResiduesMatrix_EC [I][J][1:-1]) != 0:
#                                print len(ContactResiduesMatrix_EC [I][J])
                                print ContactResiduesMatrix_EC [I][J]
                                for Res in ContactResiduesMatrix_EC [I][J][2:-2]. split(','):
                                    print Res
                                    if Res[-2]!='\'':
                                       print LetterNumber[Res[-2]]
                                       print Res[-2]; ValueArrayI. append(LetterNumber[Res[-2]])

#                     print RepresentationInstance. ContactResiduesMatrices[0][0][2]; quit()
#                     ValueArrayI. append ( ContactAminoAcidEC )

              elif Value == 'StatystykaContactAminoAcids_MM':

#                 for ContactAminoAcidEC in RepresentationInstance. ContactAminoAcidsEC: #zmienic w przeczytaniu

                     ContactResiduesMatrix_MM = RepresentationInstance. ContactResiduesMatrices[1]

                     for I in range(len(ContactResiduesMatrix_MM)):
                         for J in range(len(ContactResiduesMatrix_MM)):
                             if len(ContactResiduesMatrix_MM [I][J][1:-1]) != 0:
#                                print len(ContactResiduesMatrix_EC [I][J])
                                for Res in ContactResiduesMatrix_MM [I][J][2:-2]. split(','):
                                    if Res[-2]!='\'':
                                       print LetterNumber[Res[-2]]
                                       print Res[-2]; ValueArrayI. append(LetterNumber[Res[-2]])

#                     print RepresentationInstance. ContactResiduesMatrices[0][0][2]; quit()
#                     ValueArrayI. append ( ContactAminoAcidEC )


              elif Value == 'StatystykaContactAminoAcids_IC':

#                 for ContactAminoAcidEC in RepresentationInstance. ContactAminoAcidsEC: #zmienic w przeczytaniu

                     ContactResiduesMatrix_IC = RepresentationInstance. ContactResiduesMatrices[2]

                     for I in range(len(ContactResiduesMatrix_IC)):
                         for J in range(len(ContactResiduesMatrix_IC)):
                             if len(ContactResiduesMatrix_IC [I][J][1:-1]) != 0:
#                                print len(ContactResiduesMatrix_EC [I][J])
                                for Res in ContactResiduesMatrix_IC [I][J][2:-2]. split(','):
                                    if Res[-2]!='\'':
                                       print LetterNumber[Res[-2]]
                                       print Res[-2]; ValueArrayI. append(LetterNumber[Res[-2]])
#musze to ogarnac, tak zeby regulowac krok w histogramie, na pewnoe gdzies jest taka opcja
#                     print RepresentationInstance. ContactResiduesMatrices[0][0][2]; quit()
#                     ValueArrayI. append ( ContactAminoAcidEC )

              elif Value == 'StatystykaWysokosciKontaktu':

                     ZnakNumer = { '000':0.0, '001':1.0, '010':2.0, '011':3.0, '100':4.0, \
                                   '101':5.0, '110':6.0, '111':7.0 }

                     ContactPatternMatrix_EC, \
                     ContactPatternMatrix_MM, \
                     ContactPatternMatrix_IC =RepresentationInstance. ContactPatternMatrices
                     print RepresentationInstance. FlattenedContactPatternMatrix ( )

                     for I in range( len(ContactPatternMatrix_EC) ):
                         for J in range( len(ContactPatternMatrix_EC) ):

                             if I!=J:

                              Znak = str(Delta(ContactPatternMatrix_EC[I][J])) + \
                                     str(Delta(ContactPatternMatrix_MM[I][J])) + \
                                     str(Delta(ContactPatternMatrix_IC[I][J]))
 
                              print Znak

                              ValueArrayI. append (ZnakNumer [Znak] )

              elif Value == 'COMTilt':

                 for TiltI in RepresentationInstance. COMTILTS_OF_HELICES:

                     ValueArrayI. append ( TiltI )

              elif Value == 'COMPCATiltDifference':

                 PCATilts = RepresentationInstance. PCATILTS_OF_HELICES

                 COMTilts = RepresentationInstance. COMTILTS_OF_HELICES

                 print len (PCATilts)

                 for N in range(len(PCATilts)):

                     ValueArrayI. append ( abs(COMTilts[N] - PCATilts[N]) )
                     print (COMTilts[N] - PCATilts[N])     

              elif Value == 'COMPCAHalfHelixTiltDifference':

                 PCATilts = [];
                 for HalfHelixTilt in RepresentationInstance. PCATILTS_OF_HALF_HELICES [0]: PCATilts. append (HalfHelixTilt)
                 for HalfHelixTilt in RepresentationInstance. PCATILTS_OF_HALF_HELICES [1]: PCATilts. append (HalfHelixTilt)

#                 PCATilts = RepresentationInstance. PCATILTS_OF_HELICES
                 COMTilts = [];
                 for HalfHelixTilt in RepresentationInstance. COMTILTS_OF_HALF_HELICES [0]: COMTilts. append (HalfHelixTilt)
                 for HalfHelixTilt in RepresentationInstance. COMTILTS_OF_HALF_HELICES [1]: COMTilts. append (HalfHelixTilt)

#                 COMTilts = RepresentationInstance. COMTILTS_OF_HELICES

                 print len (PCATilts)

                 for N in range(len(PCATilts)):

                     ValueArrayI. append ( abs(COMTilts[N] - PCATilts[N]) )
#                     print (COMTilts[N] - PCATilts[N])         

              elif Value == 'CrossingAngleEC':

                 for Row in RepresentationInstance. CrossingAnglesMatrices[0]:

                     for ValueI in Row:

                         ValueArrayI. append ( ValueI )

              elif Value == 'CrossingAngleIC':

                 for Row in RepresentationInstance. CrossingAnglesMatrices[1]:

                     for ValueI in Row:

                         ValueArrayI. append ( ValueI )

              elif Value == 'CrossingAngleMain':

                 for Row in RepresentationInstance. CrossingAnglesMatrices[2]:

                     for ValueI in Row:

                         ValueArrayI. append ( ValueI )



              elif Value == 'ECTilt':

                 for TiltI in RepresentationInstance. TILTS_OF_HALF_HELICES[0]: #no wlasnie, a jaka metoda sa polhelisy?

                     ValueArrayI. append ( TiltI )

              elif Value == 'ICTilt':

                 for TiltI in RepresentationInstance. TILTS_OF_HALF_HELICES[1]:

                     ValueArrayI. append ( TiltI )

              elif Value == 'PCAECTilt':

                 for TiltI in RepresentationInstance. PCATILTS_OF_HALF_HELICES[0]:

                     ValueArrayI. append ( TiltI )

              elif Value == 'COMECTilt':

                 for TiltI in RepresentationInstance. COMTILTS_OF_HALF_HELICES[0]:

                     ValueArrayI. append ( TiltI )

              elif Value == 'PCAICTilt':

                 for TiltI in RepresentationInstance. PCATILTS_OF_HALF_HELICES[1]:

                     ValueArrayI. append ( TiltI )

              elif Value == 'COMICTilt':

                 for TiltI in RepresentationInstance. COMTILTS_OF_HALF_HELICES[1]:

                     ValueArrayI. append ( TiltI )

#dobra to zobaczymy, moze medyt
              elif Value == 'OverhangLength':

                 for TiltI in RepresentationInstance. OverhangLengths:

                     ValueArrayI. append ( TiltI )

              elif Value == 'KinkAngle':

                 for TiltI in RepresentationInstance. KinkAngles:

                     ValueArrayI. append ( TiltI )

          return np. array ( ValueArrayI )

#####################################################################################################################################################

      def OutputPDB ( self, OutputPath= './DummyPath' ):

          os.system ( 'mkdir ' + OutputPath )
 
          for NsetInstance in self. Content: 

              NsetInstance. OutputPDB ( OutputPath   )

          return

#####################################################################################################################################################

      def OutputPDBAlignedToFirst ( self, OutputPath= './DummyPath', AllowPerturbations = False ):

          os.system ( 'mkdir ' + OutputPath )
 
          for NsetInstance in self. Content: 

              NsetInstance. OutputPDBAlignedOn (self. Content [0], OutputPath, AllowPerturbations )

          return

####################################################################################################################################################




#####################################################################################################################################################

      def OutputPDBAlignedToCentroid ( self, OutputPath, Centroid, AllowPerturbations = False, AllowFlip = False ):

          os.system ( 'mkdir ' + OutputPath )
 
          for NsetInstance in self. Content: 

              NsetInstance. OutputPDBAlignedOn (Centroid, OutputPath, AllowPerturbations, AllowFlip )

          return

#####################################################################################################################################################

      def OutputPDBAlignedToAnotherSet ( self, OutputPath, AnotherSet, AllowPerturbations = False, AllowFlip = False ): # i to jest rdzen tego
# tylko potrzebuje teraz wlasciwego Maina

          os.system ( 'mkdir ' + OutputPath )

          for N in range ( len ( self.Content ) ): 

              self. Content [ N ] . OutputPDBAlignedOn ( AnotherSet. Content [ N ], OutputPath, AllowPerturbations, AllowFlip )

          return

#####################################################################################################################################################

      def PruneModelsForCorrectNHelixPacking ( self, N, RMSDThreshold ):

          PrunedModels = [ ]

          for Model in self. Content:

              if Model. CorrectNHelixPacking (N, RMSDThreshold ):

                 PrunedModels.append ( Model )

          return PrunedModels

#####################################################################################################################################################

      def MaxTiltHistogram ( self, OutputFile ):

          HistogramPlot ( self.MaxTilts ( ), OutputFile )

#####################################################################################################################################################

      def HistogramMatrycKontaktow ( self, N = 3 ):

          HistogramMatrycKontaktowI = { }

          NumerowaneMozliweTypyMatrycI = NumerowaneMozliweTypyMatryc ( N )

          OutputFile = open ( 'NumerowaneMozliweTypyMatrycI.txt', 'w' )

          for Key in NumerowaneMozliweTypyMatrycI:

              Line = '# '+str(Key) + ' '+ str(NumerowaneMozliweTypyMatrycI [ Key ])+'\n'
              OutputFile. write ( Line )

          print NumerowaneMozliweTypyMatrycI [ 0 ]

          for NumerTypu in NumerowaneMozliweTypyMatrycI.keys(): 
              HistogramMatrycKontaktowI [ NumerTypu ] = 0
# mamy NumerowaneMozliweTypyMatryc 
          print 'Zbinaryzowana Matryca'
          print self.Content[0]. BinarizedContactPatternMatrices()
          print 'Zbinaryzowana Matryca'       
          for NSetI in self.Content:

              for NumerTypu in NumerowaneMozliweTypyMatrycI.keys():
                  

                  if NumerowaneMozliweTypyMatrycI [NumerTypu] == NSetI. BinarizedContactPatternMatrices() :
                     
 
                     HistogramMatrycKontaktowI [ NumerTypu  ] += 1 

#          print NSetI. BinarizedContactPatternMatrices()

          print self.Content[0]. BinarizedContactPatternMatrices()

          return DictHistogram ( HistogramMatrycKontaktowI )

########################################################################
#####################################################################################################################################################

      def GroupAnalysis ( self, NoClustersRange ):

          return NoClustersVarianceArray # te rzeczy robilem w innym miejscu

#####################################################################################################################################################


      def RMSDClusters ( self, NoClusters ):

          return RMSDClustersI

#####################################################################################################################################################
# should think about how to allow flip :)
      def RMSD ( self, AllowPerturbations = False, AllowFlip = False ): # jestem pewien ze juz to liczylem, jesli tak to musialem gdzies to zgubic
          print 'ComputingRMSD'
          from Kombinatoryka import Perturbations

          minRMSD = 1000.0

          print self.Content[0].CENTREs. Content

#          quit ( )

          if AllowPerturbations:

             Centres1 = self.Content[1].CENTREs

             print Centres1; print Centres1.Content [0].Content[0][0];
             
             Centres1. Print (); # quit ();

             for Perturbation in Perturbations( len ( self.Content[1].CENTREs.Content ) ):

                 Centres1Perturbation = HierarchicalSetOfPoints ( [ Centres1.Content [i] for i in Perturbation ] )

                 minRMSD = min ( minRMSD, HierarchicalSetsOfPoints ( [ self.Content[0]. CENTREs, Centres1Perturbation ] ).RMSD ( ) )

#SetsOfPoints ( [ self.Content[0]. CENTREs, Centres1Perturbation ]). RMSD ( )  )


                 if AllowFlip == True: # ok zaaplikowane

                     FlippedHelices = HierarchicalSetOfPoints ( [ SetOfPoints(Helix.Content[::-1]) for Helix in self.Content[1].CENTREs.Content ] )

                     minRMSD = min ( minRMSD, HierarchicalSetsOfPoints ( [ self.Content[0]. CENTREs, FlippedHelices ]). RMSD ( )  )

                     print minRMSD
# musze to jakos uporzadkowac, ok, to powinno byc w pliku z parametrami
                 
             return minRMSD # poprawic

          else:

             return HierarchicalSetsOfPoints ( [ self.Content[0]. CENTREs, self.Content[1].CENTREs ] ).RMSD ( )

# powinienem to ujednolicic, powinienem zrobic RMSD dla setu wektorow po prostu, przepisac to tam i byloby dobrze
#####################################################################################################################################################

      def ISCRMSD ( self ):

          return 

#####################################################################################################################################################

      def PerturbRMSD ( self ): # ok to teraz generator dla N :D

          N = len ( self. HELIX_IDs )

          PerturbationsI = [ [self.Content.CENTREs[i], self.Content.CENTREs[j], self.Content.CENTREs[k] ] for i,j,k in Perturbations ( N ) ] 

          RMSDs = [ SetsOfPoints ( [ self.Content[0]. CENTREs, Perturbation  ] ).RMSD ( ) for Perturbation in PerturbationsI ]

          return min (RMSDs)

#####################################################################################################################################################

      def ECCrossingAngleVsICCrossingAngle ( self, Path, Range = '[0.0,90.0]' ):

          EcIcArray = []

          for RepI in self. Content:

              EC, IC, Main = RepI. CrossingAnglesMatrices

              for I in range( len(EC) ):

                  for J in range( len( EC[0] ) ):

                      if Range == '[0.0,90.0]':

                         ECi = EC[I][J]; ICi = IC[I][J];  

                         if EC[I][J] >= 90.0:

                            ECi = 180.0 - EC[I][J]

                         if IC[I][J] >= 90.0:
                            ICi = 180.0 - IC[I][J]

                         EcIcArray. append ( [ ECi, ICi ] )

                      else: EcIcArray. append ( [ EC[I][J], IC[I][J] ] )

          print np. array ( EcIcArray )

          ScatterPlot1 ( np. array ( EcIcArray ), Path )

          return
#####################################################################################################################################################

      def ECCrossingAngleVsICCrossingAnglePearsonCorrelationCoefficient ( self, Path, Range = '[0.0,90.0]' ):

          EcIcArray = []; EcArray = []; IcArray = []

          for RepI in self. Content:

              EC, IC, Main = RepI. CrossingAnglesMatrices

              for I in range( len(EC) ):

                  for J in range( len( EC[0] ) ):

                      if Range == '[0.0,90.0]':

                         ECi = EC[I][J]; ICi = IC[I][J];  

                         if EC[I][J] >= 90.0:

                            ECi = 180.0 - EC[I][J]

                         if IC[I][J] >= 90.0:
                            ICi = 180.0 - IC[I][J]

                         EcIcArray. append ( [ ECi, ICi ] )
                         EcArray. append (ECi); IcArray. append (ICi);

                      else: 

                         EcIcArray. append ( [ EC[I][J], IC[I][J] ] )
                         EcArray. append (ECi); IcArray. append (ICi);

          print np. array ( EcIcArray )

#          ScatterPlot1 ( np. array ( EcIcArray ), Path )
          import scipy
#          Pearson = scipy.stats.pearsonr(EC, IC)
          from scipy.stats.stats import pearsonr
          Pearson = pearsonr (EcArray, IcArray)
          print "Correlation coefficient: "+str(Pearson)
#          print Pearson
          return

#####################################################################################################################################################

      def EcTiltVsIcTilt ( self, Path, Range = '[0.0,90.0]' ):

          EcIcArray = []

          for RepI in self. Content:

              EC, IC = RepI. TILTS_OF_HALF_HELICES

              for I in range( len(EC) ):

                      if Range == '[0.0,90.0]':
                         ECi = EC[I]; ICi = IC[I];
                         if EC[I] >= 90.0: ECi = 180.0 - ECi
                         if IC[I] >= 90.0: ICi = 180.0 - ICi
                         EcIcArray. append ( [ ECi, ICi ] )
                         
                      else: EcIcArray. append ( [ EC[I], IC[I] ] )

          print np. array ( EcIcArray )

          ScatterPlot1 ( np. array ( EcIcArray ), Path )
          
          return

#####################################################################################################################################################

      def Fi1Fi2Fi3 ( self ):

          Fi1Fi2Fi3s = [ ]

          for RepI in self. Content:
#              print self.Content [0]. EC_Fis; quit ()

              EC, IC = RepI. EC_Fis, RepI. IC_Fis

              Fi1Fi2Fi3s. append ( [EC, IC] )          

          return Fi1Fi2Fi3s

#####################################################################################################################################################

      def SubsetWithinBin ( self, Value ='Fi', Range = [ -20.0, 20.0 ], Path ='' ):

          return

#####################################################################################################################################################

      def AminoAcidsPerSlice ( self, Path ):

           BinCenters = Parametry. AminoAcidPerSliceBinCenters
           BinWidth   = Parametry. AminoAcidPerSliceBinWidth

           NoECs =[]; NoMMs = []; NoICs = [ ];

           """
           returns histogram for aminoacids per slice
           """
           
           for RepI in self. Content:

               ResI = '1';

               NoEC = 0.0; NoMM = 0.0; NoIC = 0.0;

               for Res in RepI. HelicesAASEQs_Z:

                   if Res in RepI. HelicesAASEQs_Z:

                      if Res[0] != ResI:

                         print Res[0];# quit ( )

                         NoECs. append ( NoEC ); NoMMs. append ( NoMM ); NoICs. append ( NoIC );

                         NoEC = 0.0; NoMM = 0.0; NoIC = 0.0;
                         ResI = Res[0]

                      if    BinCenters[0]-BinWidth/2.0 <= Res[2] <= BinCenters[0]+BinWidth/2.0: NoIC += 1.0
                      elif  BinCenters[1]-BinWidth/2.0 <= Res[2] <= BinCenters[1]+BinWidth/2.0: NoMM += 1.0 
                      elif  BinCenters[2]-BinWidth/2.0 <= Res[2] <= BinCenters[2]+BinWidth/2.0: NoEC += 1.0

               NoECs. append ( NoEC ); NoMMs. append ( NoMM ); NoICs. append ( NoIC );
           print Path +'_'+'EC'+str(BinWidth)
           HistogramPlot ( np. array ( NoECs ), Path +'_'+'EC'+str(BinWidth)[0] )
           HistogramPlot ( np. array ( NoMMs ), Path +'_'+'MM'+str(BinWidth)[0] )
           HistogramPlot ( np. array ( NoICs ), Path +'_'+'IC'+str(BinWidth)[0] )
               
#####################################################################################################################################################

      def AminoAcidZPreference ( self, Path ):

          """
          returns AA Z Preference Graph And CsV File
          """

          AA_ZsLexicon = { }

          for AA in ChemiaFizyka. AAs: AA_ZsLexicon [ AA ] = [ ]

          for RepI in self. Content:

              for Res in RepI. AASEQs_Z:

                  AA_ZsLexicon [ Res [ 0 ] ]. append ( Res [ 1 ] )

          for AA in AA_ZsLexicon. keys ():

              if AA_ZsLexicon [AA] != []:

                 HistogramPlot ( np. array ( AA_ZsLexicon [ AA ] ), Path +'_'+AA )

                 Plik = open ('AminoAcidZPreference_'+ AA+'.csv' , 'w' )

                 Plik. write (AA+'\n')

                 for Z in AA_ZsLexicon [ AA ]:

                     Plik. write (str(Z)+'\n')

                 Plik. flush ()

                 Plik. close ()

                     
# napisac plik .csv; jaki mialby miec on format; 
# najlepiej w kolumnach 
# A, C, D itd.
# z1
#z2


          return

#####################################################################################################################################################
# moge sprobowac zdefiniowac nowa
      def RMSDMatrix ( self, AllowPerturbations = False, AllowFlip = False, OutputPath = 'RMSDMAtrixClosedTripletsNoPerNoFlip.txt' ):
          

          RMSDMatrixI = [ [ 0.0 for I in range( len ( self. Content ) ) ] for J in range(len ( self. Content ) ) ]

#          [[ RMSDMatrixI[I][J] = SetOfN_TMs_SetRepresentations ( [ self.Content [I], self. Content [J] ] ). RMSD ( )\
#                               for I in range( len ( self. Content ) ) ]
#                               for J in range(len ( self. Content ) ) ]

          OutputFile = open ( OutputPath, 'w' )

          for I in range( len ( self. Content ) ):
              for J in range(len ( self. Content ) ):

                  RMSDMatrixI[I][J] = SetOfN_TMs_SetRepresentations ( [ self.Content [I], self. Content [J] ] ). RMSD ( AllowPerturbations, AllowFlip )

              OutputLine = '\t'.join ( [ str(RMSDFloat) for RMSDFloat in RMSDMatrixI[I] ] ) + '\n'
              OutputFile. write ( OutputLine )

#         outputuje matryce RMSD, oprocz tego przydaloby sie uporzadkowanie calego programu

          OutputFile. close ( )

          return np. array ( RMSDMatrixI )

#####################################################################################################################################################
# moge sprobowac zdefiniowac nowa
      def RMSDMatrix2 ( self, AllowPerturbations = False, OutputPath = 'RMSDMAtrix.txt' ):

          RMSDMatrixI = [ [ 0.0 for I in range( len ( self. Content ) ) ] for J in range( len ( self. Content ) ) ]

          

#          [[ RMSDMatrixI[I][J] = SetOfN_TMs_SetRepresentations ( [ self.Content [I], self. Content [J] ] ). RMSD ( )\
#                               for I in range( len ( self. Content ) ) ]
#                               for J in range(len ( self. Content ) ) ]

          for I in range( len ( self. Content ) ):
              RMSDMatrixI[I][I] = 0.0
              for J in range(len (I+1, self. Content ) ):

                  RMSDMatrixI[I][J] = SetOfN_TMs_SetRepresentations ( [ self.Content [I], self. Content [J] ] ). RMSD ( AllowPerturbations )
# transponujemy :)

          for I in range(1, len ( self. Content ) ):

              for J in range( I-1 ):

                  RMSDMatrix[I][J] = RMSDMatrix[J][I]
# mozemy jeszcze przyspieszyc RMSD Matrix, zeby nie trzeba bylo na nowo obliczac centrow tylko zeby one byly juz
# ech trzebaby to tez skopiowac, ale to pozniej
# musze napisac plan

          OutputFile = open ( OutputPath, 'w' )

#         outputuje matryce RMSD, oprocz tego przydaloby sie uporzadkowanie calego programu

          for I in range ( len ( RMSDMatrix ) ):

              OutputLine = '\t'.join ( RMSDMatrixI[I] ) + '\n'

              OutputFile. write ( OutputLine )

          OutputFile. close ( )

          return np. array ( RMSDMatrixI )



#####################################################################################################################################################

      def Touching ( self ):

          TouchingTripletsI = [ ]

          for Triplet in self.Content:

              if Triplet.Touching ( ):

                 TouchingTripletsI. append ( Triplet )
                 print Triplet. FlattenedContactPatternMatrix ( )
#          quit ()
          return SetOfN_TMs_SetRepresentations ( TouchingTripletsI )

#####################################################################################################################################################

      def Closed ( self ):

          TouchingTripletsI = [ ]

          for Triplet in self.Content:

              if Triplet.Closed ( ):

                 TouchingTripletsI. append ( Triplet )

          return SetOfN_TMs_SetRepresentations ( TouchingTripletsI )

#####################################################################################################################################################

      def SlicesCOMsAlignedToXAxis ( self ):

          SlicesCOMsAlignedToXAxisI = [ ]

          for RepresentationInstance in self. Content:

              SlicesCOMsAlignedToXAxisI. append ( RepresentationInstance. SlicesCOMsAlignedToXAxis ( ) )

          return SlicesCOMs ( SlicesCOMsAlignedToXAxisI ) #trzebaby to przepisac :-/

#####################################################################################################################################################

      def MembMCArrangement ( self, Path ):
          """
          returns triplet slices through various z planes
          """

          print Path

          self. SlicesCOMsAlignedToXAxis ( ). ScatterPloty ( Path )

#####################################################################################################################################################

      def MembMCArrangementAngle ( self, Path ):
          """
          returns triplet slices through various z planes
          """

          print Path

          self. SlicesCOMsAlignedToXAxis ( ). HistogramyAngla ( Path )

#####################################################################################################################################################

      def Fi1Fi2Fi3DoPliku ( self, Path ):
          """
          returns Fi1Fi2Fi3 to file
          """

          print Path

          OpenFile = open ( Path, 'w' )

          for line in self. Fi1Fi2Fi3 ( ):
              
              [ [ OpenFile. write ( str (item) +' ' ) for item in Comp ] for Comp in line ]

              OpenFile. write ( '\n' )

          OpenFile. flush ()
          OpenFile. close ()

#          self. Fi1Fi2Fi3 ( ). Output ( Path )
#####################################################################################################################################################

      def ExtractNPlusOneOrderRepresentationsByApriori ( self ):
          NPlusOneOrderRepresentations = [ ]
          
          for NOrderRepresentation1 in self.Content:
              for NOrderRepresentation2 in self.Content:
                  NakladanieI = Nakladanie ( NOrderRepresentation1.HELIX_IDS, NOrderRepresentation2.HELIX_IDS  )
                  if NakladanieI!= [ ]:

                     NPlusOneOrderRepresentation = MergeRepresentations ( NOrderRepresentation1, NOrderRepresentation2, NakladanieI )
                     NPlusOneOrderRepresentations. append ( NPlusOneOrderRepresentation ) 

          return SetOfN_TMs_SetRepresentations ( NPlusOneOrderRepresentations )

#####################################################################################################################################################

# druga rzecz by bylo po prostu stworzenie itemsetow, czy fingerprintu dla kazdego trypletu
# jakie pary residuow sa w zamknietych trypletach, chcialbym to zrobic, ewentualnie zamkniete tryplety i pary residuow trzeba zakodowac w sensie
# 
# ech musze pobiegac 
#
# KodPDB	IDLancucha	IDHelis	MaxTilt [DEG]	DotykaSie	Zamkniety	NumerTypuMatrycyKontaktu AminokwasyKontaktu(EC,MM,IC?) 	
# 3EML		A		1, 2, 3	60 		TAK		TAK		511			[S,G], [L,I], [TRP]
#
#

#####################################################################################################################################################

      def OutputItemsets ( self, Path ):

          ItemsetsI = [ ]

          for RepresentationInstance in self.Content:

              ItemsetsI. append ( RepresentationInstance.Itemset ( ) )

          SetOfItemsets ( ItemsetsI ).Output ( Path )

          return SetOfItemsets ( ItemsetsI )

          # (Itemset powinien byc oddzielna klasa gdzie atrybuty beda sie zmieniac, tak zeby byc elastycznym )

#####################################################################################################################################################
#####################################################################################################################################################
# przydaloby sie to przeniesc do innego pliku

class Itemset ( list ):

      def __init__ ( self, \
                     InputPDBCode, \
                     InputChainID, \
                     InputHelixIDs, \
                     InputMaxTilt, \
                     InputTouching, \
                     InputClosed, \
                     InputNumerTypuMatrycyKontaktu, \
                     InputAminokwasyKontaktu ):

          self.PDBCode = InputPDBCode
          self.ChainID = InputChainID
          self.HelixIDs = InputHelixIDs
          self.MaxTiltI = InputMaxTilt
          self.TouchingI = InputTouching
          self.ClosedI = InputClosed
          self.NumerTypuMatrycyKontaktu = InputNumerTypuMatrycyKontaktu
          self.AminokwasyKontaktu = InputAminokwasyKontaktu
 
          return

#####################################################################################################################################################

      def Line ( self ):
          Lista = [ self.PDBCode , self.ChainID ,  str ( self.HelixIDs ) , self.MaxTiltI , self.TouchingI , self.ClosedI , self.NumerTypuMatrycyKontaktu , str ( self.AminokwasyKontaktu ) ]
          LineI = '\t'.join ( [str(i) for i in Lista] ) + '\n'

          return LineI

#####################################################################################################################################################
#####################################################################################################################################################


class SetOfItemsets ( list ):

      def __init__ ( self, InputItemsetInstances ):

          self.Content = [ ]
          
          for InputItemsetInstance in InputItemsetInstances:

              self.Content. append ( InputItemsetInstance )

          return

#####################################################################################################################################################

      def Output ( self, OutputPath ):

          FirstLine = 'Code\tID\tHelixID\tMaxTilt\tTouch\tClosed\tContactPattern\tContactAminoacids (EC,MM,IC)\n'

          OutputFile = open ( OutputPath, 'w' )
          OutputFile. write ( FirstLine )

          for ItemsetInstance in self.Content:

              OutputFile. write ( ItemsetInstance.Line ( ) )

          OutputFile.flush ( )
          OutputFile.close ( )


#####################################################################################################################################################

# potrzebuje teraz zeby ta funkcja dzielila mi N sety wedlug matrycy kontaktow
# musze myslec o tym zeby bylo prosto i zeby bylo szybko
# dla N = 2 mozliwe sa 2 matryce:
# 1)  A B   2)  A B
#   A   0     A   1
#   B         B    
#
# dla N = 3 mozliwe sa 
# 1)  A B C 2)  A B C 3)  A B C 
#   A   0 0   A   0 0   A   0 1 
#   B     0   B     1   B     0
#   C         C         C
# jest (N^2 - N)/2 pol do wypelnienia bo matryca jest trojkatna tak naprawde i te pola moga byc wypelnione jedynka 
# lub zerem wiec liczba kombinacji jest 2 ^ ( ( N^2 - N )/2 ). zeby mnie bola
# wiec dla 3 jest 8 kombinacji
# dla 4 jest 2^6 jest 64
# itd wiec 
# 0, 1
# 00, 01, 10, 11

Dlugosc = 1

###############
#####################################################################################################################################################
#####################################################################################################################################################

class DictHistogram ( dict ):

      def Output ( self, Path ):

          OutputFile = open ( Path, 'w' )          

          for Key in self.keys ( ):

              Line = str(Key) + ' '+ str(self [ Key ])+'\n'
              OutputFile. write ( Line )

          OutputFile. flush ()
          OutputFile. close ()

#####################################################################################################################################################

      def OutputNonZeroValues ( self, Path ):

          OutputFile = open ( Path, 'w' )          

          for Key in self.keys ( ):
              if self [ Key ] !=0:

                 Line = str(Key) + ' '+ str(self [ Key ])+'\n'
                 OutputFile. write ( Line )

          OutputFile. flush ()
          OutputFile. close ()

#####################################################################################################################################################

      def BarPlot ( self, Path ):

          import PlotToolsModule; from PlotToolsModule import BarPlot
          import numpy as np

          Array = [ ]
          
          for Key in self.keys ( ):

              if self [ Key ] != 0:
                 ArrayLine = [ Key, self [ Key ] ]
                 Array. append ( ArrayLine )

          InputArray = np.array ( Array )

          BarPlot ( InputArray, Path )

# musze znalezc ladny sposob zrobienia bar plota tego ; trzeba by ID dac w legendzie, chyba pora isc spac
          
#####################################################################################################################################################
#####################################################################################################################################################
# trzebaby to jakos rozbic po modulach

class SlicesCOMs ( list ):

      def __init__ ( self, SlajsyTrypletow ):

          self. Content = [ ]

          for SlajsTrypletu in SlajsyTrypletow:

              self. Content. append ( SlajsTrypletu )

          print self. Content # [ 0 ]

#          quit ( )

#####################################################################################################################################################

      def Output ( self, Path ):

             EC_Path = Path + '_EC.txt'
             MM_Path = Path + '_MM.txt'
             IC_Path = Path + '_IC.txt'          

             EC_FileInstance = open ( EC_Path, 'w' )

             for SlajsTrypletu in self.Content:

                 EC_Slajs = SlajsTrypletu [ 0 ]

                 line =''

                 for Point in EC_Slajs:

                     for Coord in Point:

                         line = line +'\t'+ str(Coord)

                 line = line + '\n'; EC_FileInstance.write ( line )

             MM_FileInstance = open ( MM_Path, 'w' )

             for SlajsTrypletu in self.Content:

                 EC_Slajs = SlajsTrypletu [ 1 ]

                 line =''

                 for Point in EC_Slajs:

                     for Coord in Point:

                         line = line +'\t'+ str(Coord)

                 line = line + '\n'; MM_FileInstance.write ( line )

             IC_FileInstance = open ( IC_Path, 'w' )

             for SlajsTrypletu in self.Content:

                 IC_Slajs = SlajsTrypletu [ 2 ]

                 line =''

                 for Point in EC_Slajs:

                     for Coord in Point:

                         line = line +'\t'+ str(Coord)

                 line = line + '\n'; IC_FileInstance.write ( line )

#####################################################################################################################################################

      def Arrays ( self ):

          import numpy as np; from numpy import *

          EC_Array = [ ]; MM_Array = [ ]; IC_Array = [ ]

          for SlajsTrypletu in self.Content:

              EC_Slajs, MM_Slajs, IC_Slajs = SlajsTrypletu

              EC_Array_Slajs = [ ]
              for Point in EC_Slajs:
                  EC_Array_Slajs. append ( Point [ 0 ]); EC_Array_Slajs. append ( Point [ 1 ]);
              EC_Array. append ( EC_Array_Slajs )

              MM_Array_Slajs = [ ]
              for Point in MM_Slajs:
                  MM_Array_Slajs. append ( Point [ 0 ]); MM_Array_Slajs. append ( Point [ 1 ]);
              MM_Array. append ( MM_Array_Slajs )

              IC_Array_Slajs = [ ]
              for Point in IC_Slajs:
                  IC_Array_Slajs. append ( Point [ 0 ]); IC_Array_Slajs. append ( Point [ 1 ]);
              IC_Array. append ( IC_Array_Slajs )


          return [ np.array ( EC_Array ), np.array ( MM_Array ), np.array ( IC_Array ) ]  
#####################################################################################################################################################

      def AngleArrays ( self ):

          import numpy as np; from numpy import *

          EC_Array = [ ]; MM_Array = [ ]; IC_Array = [ ]

          for SlajsTrypletu in self.Content:

              EC_Slajs, MM_Slajs, IC_Slajs = SlajsTrypletu

              ECAngle = SetOfVectors ( [ SetOfPoints ([ EC_Slajs[0],EC_Slajs[1] ]). Vector (), SetOfPoints ([ EC_Slajs[1],EC_Slajs[2] ]). Vector () ] ). AngleDEG (AccountForAngleDirection='Yes') 
              EC_Array. append ( ECAngle)

              MMAngle = SetOfVectors ( [ SetOfPoints ([ MM_Slajs[0],MM_Slajs[1] ]). Vector (), SetOfPoints ([ MM_Slajs[1],MM_Slajs[2] ]). Vector () ] ). AngleDEG (AccountForAngleDirection='Yes')
              MM_Array. append ( MMAngle)

              ICAngle = SetOfVectors ( [ SetOfPoints ([ IC_Slajs[0],IC_Slajs[1] ]). Vector (), SetOfPoints ([ IC_Slajs[1],IC_Slajs[2] ]). Vector () ] ). AngleDEG (AccountForAngleDirection='Yes')
              IC_Array. append ( ICAngle)

          return [ np.array ( EC_Array ), np.array ( MM_Array ), np.array ( IC_Array ) ] 

#####################################################################################################################################################
# jutro moglbym uporzadkowac, przepisac          

      def ScatterPloty ( self, Path ):

          EC_Array, MM_Array, IC_Array = self. Arrays ( )

#          print EC_Array[0]; quit ()

          ScatterPlot ( EC_Array, Path+'_EC' )
          ScatterPlot ( MM_Array, Path+'_MM' )
          ScatterPlot ( IC_Array, Path+'_IC' )

# to teraz powinienem zrobic grafy dla trypletow co sie dotykaja i trypletow co sa zamkniete
#####################################################################################################################################################

      def HistogramyAngla ( self, Path ):

          EC_Array, MM_Array, IC_Array = self. AngleArrays ( )

          HistogramPlot ( EC_Array, Path+'_EC', Min =-180.0, Max=180.0 )
          HistogramPlot ( MM_Array, Path+'_MM', Min =-180.0, Max=180.0 )
          HistogramPlot ( IC_Array, Path+'_IC', Min =-180.0, Max=180.0 )

# to teraz powinienem zrobic grafy dla trypletow co sie dotykaja i trypletow co sa zamkniete
#####################################################################################################################################################

def Delta (Liczba):

    if Liczba == 0:

       return 0

    else:

       return 1

#####################################################################################################################

def ReadCentroidsFromTXT (TextFilePath):

    No = int(TextFilePath. split('Triplets')[1].split('.')[0])

    CentroidTxtFile = open (TextFilePath, 'r')

    CentroidLines = CentroidTxtFile. readlines ()[:No]

    CentroidTxtFile. close ()

    CodeChainHelixIDsTxts = []

    for Line in CentroidLines:

        Code, Chain = Line. split ('[') [0]. split ()

        HelixIDs = [(Item.strip("'")) for Item in Line. split ('[') [1]. strip (']\n'). split (', ') ]

        CodeChainHelixIDsTxts. append (Code+'_'+Chain+'_'+'_'.join(HelixIDs))

    return CodeChainHelixIDsTxts

#####################################################################################################################

def  CentroidIndexes (FilelistFilePath, Centroids):

    CentroidIndexesI = []

    FilelistFile = open (FilelistFilePath, 'r')

    FilePaths = FilelistFile. readlines ()

    FilelistFile. close ()

    for N in range(len(FilePaths)):

        FileName = FilePaths[N]. split ('/')[-1]
        print FileName

        CodeChainHelixIDs = FileName. split ('_Representation')[0]

        print CodeChainHelixIDs; # quit ();

        if CodeChainHelixIDs in Centroids:

           CentroidIndexesI. append (N)

    return CentroidIndexesI

#####################################################################################################################
