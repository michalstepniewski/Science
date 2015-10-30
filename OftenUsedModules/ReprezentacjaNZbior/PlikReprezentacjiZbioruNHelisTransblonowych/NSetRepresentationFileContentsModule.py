from GeometricalClassesModule import Point, SetOfPoints, HierarchicalSetOfPoints

#####################################################################################################################################################
#####################################################################################################################################################

class RepresentationFileContents ( list ):

# sklada sie z Linii tekstu

      def __init__ ( self, InputLines, PDBCode = 'CODE', ChainID ='ID', Family = 'DummyFamily'   ):
          self. PDBCode = PDBCode;
          self. ChainID = ChainID;
          self. Family = Family;
          self.Content = [ ]

          print self. Family

          for InputLine in InputLines:

              self.Content. append ( InputLine )

#####################################################################################################################################################

      def ReadRepresentation ( self ):

          ContactPatternMatrix_EC = [ ]; ContactPatternMatrix_MM = [ ]; ContactPatternMatrix_IC = [ ];
          ContactResiduesMatrix_EC = [ ]; ContactResiduesMatrix_MM = [ ]; ContactResiduesMatrix_IC = [ ];
          MiminumDistanceMatrix_EC = [ ]; MiminumDistanceMatrix_MM = [ ]; MiminumDistanceMatrix_IC = [ ];
          RelativeOrientationMatrixI = [ ]; AASEQs = [ ]; CENTREs = [ ]; I1_3_VECs = [ ]; AXES = [ ]
          CONTACT_RESIDUES_EC_MM_ICI = [ ]; CrossingAnglesMatrixEC = [ ]; CrossingAnglesMatrixIC = [ ];
          CrossingAnglesMatrixMain = [ ];
          AASEQs_Z = [ ]; DihedralAnglesMatrixIC = [ ]; DihedralAnglesMatrixEC = [ ];
          

          for N in range( len (self.Content) ):

              Line = self.Content [ N ]
              print Line
#              quit()

              if '#REMARK  HELIX IDS' in Line:

                 HELIX_IDSI = [ ]
                 for HelixID in Line[ 19: ]. split ( ): 
                     HELIX_IDSI. append ( HelixID [ 2: ] ) 

              elif 'TILTS OF HELICES to Z AXIS [DEG]' in Line:
                 TILTS_OF_HELICESI = [float(i) for i in self.Content [ N+2 ][ 0: ]. split ( )]
#                   PCA TILTS OF HELICES to Z AXIS [DEG]
                 if 'PCA TILTS OF HELICES to Z AXIS [DEG]' in Line: #PCA TILTS OF HELICES to Z AXIS [DEG]
                    PCATILTS_OF_HELICES = [float(i) for i in self.Content [ N+2 ][ 0: ]. split ( )]

                 elif 'COM VECTOR TILTS OF HELICES to Z AXIS [DEG]' in Line:
                    COMTILTS_OF_HELICES = [float(i) for i in self.Content [ N+2 ][ 0: ]. split ( )]

              elif '#REMARK  PCA TILTS OF HALF HELICES to Z AXIS [ DEG ]' in Line:

                 TILTS_OF_HALF_HELICES = [ ]
                 TILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+2 ][ 8: ].split ( ) [1:] ] )
                 TILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+3 ][ 8: ].split ( ) [1:] ] )

                 PCATILTS_OF_HALF_HELICES = [ ]
                 PCATILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+2 ][ 8: ].split ( ) [1:] ] )
                 PCATILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+3 ][ 8: ].split ( ) [1:] ] )

              elif '#REMARK  COM VECTOR TILTS OF HALF HELICES to Z AXIS [ DEG ]' in Line:
                  

#                 TILTS_OF_HALF_HELICES = [ ]
#                 TILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+2 ][ 8: ].split ( ) [1:] ] )
#                 TILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+3 ][ 8: ].split ( ) [1:] ] )

                 COMTILTS_OF_HALF_HELICES = [ ]
                 COMTILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+2 ][ 8: ].split ( ) [1:] ] )
                 COMTILTS_OF_HALF_HELICES. append ( [ float(i) for i in self.Content [ N+3 ][ 8: ].split ( ) [1:] ] )
 
              elif '#REMARK OVERHANG LENGTHS OF HELICES to Z AXIS [DEG]' in Line:

                 OverhangLengths = [float(i) for i in self.Content [ N+3 ][ 3: ]. split ( )]

              elif '#REMARK  ContactPatternMatrix  EC' in Line:

                 ContactPatternMatrix_EC . append ( [ int(i) for i in Line[34:]. split ( )] )

              elif '#REMARK  ContactPatternMatrix  MM' in Line:

                 ContactPatternMatrix_MM . append ( [ int(i) for i in Line[34:]. split ( ) ] )

              elif '#REMARK  ContactPatternMatrix  IC' in Line:

                 ContactPatternMatrix_IC . append ( [ int(i) for i in Line[34:]. split ( ) ] )
# jest troche bol z tym lepszym do maszynowego czytania bylby format matrycy, ale format matrycy bylby z kolei gorszy
# do czytania ocznego
              elif '# CONTACT RESIDUES EC' in Line:

                 ContactResiduesMatrix_EC. append ( Line[22:].strip(). split ( '\t' ) )

              elif '# CONTACT RESIDUES MM' in Line:

                 ContactResiduesMatrix_MM. append ( Line[22:].strip(). split ( '\t'  ) )

              elif '# CONTACT RESIDUES IC' in Line:

                 ContactResiduesMatrix_IC. append ( Line[22:].strip(). split ( '\t'  ) )

              elif '#REMARK  MinimumDistanceMatrix  EC' in Line:

                   MiminumDistanceMatrix_EC. append ( [ float(i) for i in Line[34:]. split ( ) ] )

              elif '#REMARK  MinimumDistanceMatrix  MM' in Line:

                   MiminumDistanceMatrix_MM. append ( [float(i) for i in Line[34:]. split ( ) ] ) 

              elif '#REMARK  MinimumDistanceMatrix  IC' in Line:

                   MiminumDistanceMatrix_IC. append ( [ float(i) for i in Line[34:]. split ( ) ] )   

              elif '#REMARK NterDescriptors Protein ' in Line:

                   print Line

                   HelixNterDescriptorsI = self.Content [ N + 1 ] [ 23: ].split ( ) [1:] 
                   ProteinNterDescriptorI = self.Content [ N + 1 ] [ 23: ].split ( ) [0]

#                   quit ()

              elif '#REMARK RelativeOrientationMatrix' in Line:

                   RelativeOrientationMatrixI.append ( Line [ 34: ] . split ( ) )

              elif '#REMARK CrossingAnglesMatrix EC' in Line:                  

                   CrossingAnglesMatrixEC. append ( [float(i) for i in Line[ 33: ]. split ( )] )

              elif '#REMARK CrossingAnglesMatrix IC' in Line:

                   CrossingAnglesMatrixIC. append ( [float(i) for i in Line[ 33: ]. split ( )] )               

              elif '#REMARK CrossingAnglesMatrix Main' in Line:

                   CrossingAnglesMatrixMain. append ( [float(i) for i in Line[ 33: ]. split ( )] )               


              elif '#REMARK DihedralAnglesMatrix EC' in Line:                  

                   DihedralAnglesMatrixEC. append ( [float(i) for i in Line[ 33: ]. split ( )] )

              elif '#REMARK DihedralAnglesMatrix EC' in Line:                  

                   DihedralAnglesMatrixEC. append ( [float(i) for i in Line[ 33: ]. split ( )] )


              elif '#REMARK DihedralAnglesMatrix IC' in Line:

                   DihedralAnglesMatrixIC. append ( [float(i) for i in Line[ 33: ]. split ( )] )
              elif '#AASEQ ' in Line:

                   AASEQs. append ( Line [ 7: ]. strip ( ) )

              elif '#AASEQ_Z' in Line:

                   AASEQs_Z. append ( Line [ 8: ]. strip ( ) )
# potem to rozsegregowac

              elif '#CENTRE' in Line:

                   CENTREs. append ( Point( [ float(i) for i in Line [ 19: ]. split ( ) ] ) ) # raczej tak, a musimy tego przynajmniej sprobowac,
# inaczej jest coraz wiecej problemow potem

              elif '#1-3VEC' in Line:

                   I1_3_VECs. append ( [ float(i) for i in Line [ 19: ]. split ( ) ] )

              elif '#AXIS' in Line:

                   AXES. append ( [ float(i) for i in Line [ 19: ]. split ( ) ] )


              elif '#REMARK  KINK ANGLES OF HELICES to Z AXIS [DEG]' in Line:

                   KinkAngles = [float(i) for i in self.Content [ N+3 ][ 0: ]. split ( )]

              elif 'EC Fis' in Line:

                   EC_Fis = [float(i) for i in self.Content [ N ][ 7: ]. split ( )]

              elif 'IC Fis' in Line:

                   IC_Fis = [float(i) for i in self.Content [ N ][ 7: ]. split ( )]

          ContactPatternMatrices = [ ContactPatternMatrix_EC, ContactPatternMatrix_MM, ContactPatternMatrix_IC ]
          MiminumDistanceMatrices = [ MiminumDistanceMatrix_EC, MiminumDistanceMatrix_MM, MiminumDistanceMatrix_IC ]
          ContactResiduesMatrices = [ ContactResiduesMatrix_EC, ContactResiduesMatrix_MM, ContactResiduesMatrix_IC ]
#          print ContactResiduesMatrices; quit ();
          GroupedAASEQs = [ ]

          for N in range (0, len ( AASEQs ), 3 ):
              HelixAASEQs = [ AASEQs [ N ], AASEQs [ N + 1 ], AASEQs [ N + 2 ] ]
              GroupedAASEQs. append ( HelixAASEQs )

          GroupedCENTREs = [ ]

          for N in range (0, len ( CENTREs ), 3 ): # jest dylemat, bo moze powinny to byc od razu instancje
              HelixCENTREs = SetOfPoints ( [ CENTREs [ N ], CENTREs [ N + 1 ], CENTREs [ N + 2 ] ] )
              GroupedCENTREs. append ( HelixCENTREs ) 

          GroupedI1_3_VECs = [ ]

          for N in range (0, len ( I1_3_VECs ), 2 ):
              HelixI1_3_VECs = [ I1_3_VECs [ N ], I1_3_VECs [ N + 1 ] ]
              GroupedI1_3_VECs. append ( HelixI1_3_VECs )

          GroupedAXES = [ ]

          for N in range (0, len ( AXES ), 2 ):
              HelixAXES = [ AXES [ N ], AXES [ N + 1 ] ]
              GroupedAXES. append ( HelixAXES )

          import sys
          
          import N_TMs_SetRepresentationModule; from N_TMs_SetRepresentationModule import NSetRepresentation;


          CrossingAnglesMatrices = [ CrossingAnglesMatrixEC, CrossingAnglesMatrixIC, CrossingAnglesMatrixMain  ]

          HierarchicalSetOfPoints ( GroupedCENTREs ). Print ( )


          GroupedCentresInstance = HierarchicalSetOfPoints ( GroupedCENTREs )

          print 'Printing GroupedCentresInstance'
          GroupedCentresInstance. Print ( )
          print 'DonePrinting GroupedCentresInstance' 

          print   self. PDBCode 

          

                    

          NSetRepresentationInstance = \
NSetRepresentation ( \
                 HELIX_IDSI, \
                 TILTS_OF_HELICESI, \
                 TILTS_OF_HALF_HELICES,\
                 ContactPatternMatrices, \
                 ContactResiduesMatrices, \
                 MiminumDistanceMatrices, \
                 HelixNterDescriptorsI, \
                 ProteinNterDescriptorI, \
                 RelativeOrientationMatrixI, \
                 GroupedAASEQs, \
                 GroupedCentresInstance, \
                 GroupedI1_3_VECs, \
                 GroupedAXES, \
                 CrossingAnglesMatrices, \
                 self.PDBCode, \
                 self.ChainID, \
                 self. Family, \
                 MM_SLICE_COMs_AngleI = 'NA', \
                 ClockwiseAntiClockwiseI = 'NS'   )

#          print 'PrintingCenters'
#          NSetRepresentationInstance. CENTREs. Print ( )
#          print 'DonePrintingCenters'

          NSetRepresentationInstance. OverhangLengths  = OverhangLengths

          NSetRepresentationInstance. KinkAngles = KinkAngles
          NSetRepresentationInstance. EC_Fis = EC_Fis # czyli sczytalismy, i teraz to jakos uzyc moze ... hmm
          NSetRepresentationInstance. IC_Fis = IC_Fis
          NSetRepresentationInstance. DihedralAnglesMatrices = [ DihedralAnglesMatrixEC, DihedralAnglesMatrixIC ]

          print AASEQs_Z

          NSetRepresentationInstance. AASEQs_Z = [ [ ASSEQ_Z.split ()[2], float ( ASSEQ_Z.split ()[3] ) ] for ASSEQ_Z in AASEQs_Z ]
          NSetRepresentationInstance. HelicesAASEQs_Z = [ [ ASSEQ_Z.split ()[1], ASSEQ_Z.split ()[2], float ( ASSEQ_Z.split ()[3] ) ] for ASSEQ_Z in AASEQs_Z ]

          NSetRepresentationInstance. PCATILTS_OF_HELICES = PCATILTS_OF_HELICES
          NSetRepresentationInstance. COMTILTS_OF_HELICES = COMTILTS_OF_HELICES

          NSetRepresentationInstance. PCATILTS_OF_HALF_HELICES = PCATILTS_OF_HALF_HELICES
          NSetRepresentationInstance. COMTILTS_OF_HALF_HELICES = COMTILTS_OF_HALF_HELICES
          NSetRepresentationInstance. ContactResiduesMatrices = ContactResiduesMatrices;
#          print NSetRepresentationInstance. ContactResiduesMatrices;#  quit ();

#          print NSetRepresentationInstance. EC_Fis; quit ()
          return NSetRepresentationInstance
# ( \
#                 HELIX_IDSI, \
#                 TILTS_OF_HELICESI, \
#                 TILTS_OF_HALF_HELICES,\
#                 ContactPatternMatrices, \
#                 ContactResiduesMatrices, \
#                 MiminumDistanceMatrices, \
#                 HelixNterDescriptorsI, \
#                 ProteinNterDescriptorI, \
#                 RelativeOrientationMatrixI, \
#                 GroupedAASEQs, \
#                 GroupedCentresInstance, \
#                 GroupedI1_3_VECs, \
#                 GroupedAXES, \
#                 CrossingAnglesMatrices, \
#                 self.PDBCode, \
#                 self.ChainID, \
#                 self. Family, \
#                 MM_SLICE_COMs_AngleI = 'NA', \
#                 ClockwiseAntiClockwiseI = 'NS'   )

# ok... potrzebuje dobrej sciezki i potrzebuje posegregowac i wtedy stamtad mozemy czytac 

#####################################################################################################################################################
#####################################################################################################################################################
