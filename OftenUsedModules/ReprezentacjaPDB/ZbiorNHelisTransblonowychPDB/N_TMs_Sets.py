# musze sie zastanowic teraz jak to ladnie urzadzic #

class SetOfK_N_TMs_Sets ( ):


      def __init__ ( self, InputN_TMs_SetInstances ):

          self.Content = [ ]

          for InputN_TMs_SetInstance in InputN_TMs_SetInstances:

              self.Content. append ( InputN_TMs_SetInstance )

#####################################################################################################################################################



#####################################################################################################################################################

      def SuperimposeMainAxesOnZAxes ( self ):

          for Set in self.Content:

              Set. SuperimposeMainAxisonZAxis () # powinienem zaczac myslec nad tym czy nie lepiej czasem uzywac funkcji ktore zmieniaja zmienna
                                                 # zamiast uzywac nowych zmiennych, tak bedzie lepiej :)

          return 

#####################################################################################################################################################

      def Print ( self ):

          for self.N_TMs_SetInstance in self.Content:
              self.N_TMs_SetInstance. Print ( )

#####################################################################################################################################################

      def OutputToPdbFiles ( self, path ):                  # Output Triplets To PDB Files

          for self.N_TMs_SetInstance in self.Content:

              self.N_TMs_SetInstance. OutputToPdbFile ( path )

#####################################################################################################################################################

      def OutputRepresentations ( self, ProteinNterOrientation = 'XX', OutputPath='DummyPath' ):

          for self.N_TMs_SetInstance in self.Content: #or should I name it 'Content'

              self.N_TMs_SetInstance. OutputRepresentation ( ProteinNterOrientation, OutputPath )

          return

#####################################################################################################################################################

      def ExtractNPlus1_TMs_Sets ( ): # potrzebuje setu ID, potrzebuje fragmentu kodu najlepiej

          NPlusOneSets = [ ]

# wiec jak dziala Apriori 

          LenContent = len ( self.Content )

          for I in range ( LenContent ):

              for J in range ( I, LenContent ):

                  N_TMs_Set_Instance1 = self.Content [ 0 ]
                  N_TMs_Set_Instance2 = self.Content [ 1 ]

                  N_TMs_Set_Instance1IDs = N_TMs_Set_Instance1.IDs ( )
                  N_TMs_Set_Instance2IDs = N_TMs_Set_Instance2.IDs ( )

# teraz musze zrobic apriori                  

                  for ID in N_TMs_Set_Instance1IDs:

                      NMinus1N_TMs_Set_Instance1IDs = N_TMs_Set_Instance1IDs - ID # or remove ID, we will see
                      
                      if NMinus1N_TMs_Set_Instance1IDs in N_TMs_Set_Instance2IDs:

                         NPlusOneSetIDs = N_TMs_Set_Instance2IDs + ID

                         NPlusOneSet = N_TMs_SetInstanceFromIDsList ( NPlusOneSetIDs ) # musze miec funkcje ktora by ekstrahowala helisy z zestawu ID
                         NPlusOneSets. append ( NPlusOneSet )

          return NPlusOneSets

# musze teraz zrobic to samo na Reprezentacjach, bo duzo moge zrobic na reprezentacjach

