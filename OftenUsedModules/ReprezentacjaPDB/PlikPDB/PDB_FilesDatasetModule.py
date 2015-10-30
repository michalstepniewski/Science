######################################################
###### potrzebuje directory na lancuchypolipeptydowe i na segmenty transblonowe, a potem na pary' ###
### tak zeby bylo wszystko pod scisla kontrola ###
### ide spac, jutro dzien w Aleksandrii ###

# jakies komentarze moglbym popisac, jakas standardowa dokumentacje, ale chyba potrzebuje drugiej kawy w tym momencie #

import sys; 

SoftwarePath = '/home/soutys/Science/Software'

#sys.path.append (SoftwarePath + '/Moduly/ReprezentacjaPDB/ZbiorNHelisTransblonowychPDB' )
import os; import N_TMs_Sets; from N_TMs_Sets import SetOfK_N_TMs_Sets

#####################################################################################################################################################

def ReadPDBFileContents ( FilePath ): # 
    import PDB_FileContentsModule; from PDB_FileContentsModule import PdbFileContent;

    print FilePath;

    OpenedFileInstance=open( FilePath,'r' )    
    PDBFileContentInstance = PdbFileContent ( OpenedFileInstance.readlines() )
    OpenedFileInstance.close()

    return PDBFileContentInstance

#####################################################################################################################################################

def ReadDatasetFile ( DatasetFile ):

    ReadFileInstance = open ( DatasetFile, 'r' ) 

    ReadFileContents = ReadFileInstance.readlines ( )

    ReadFileInstance.close ( )

    Dataset = [ ]    

    for Line in ReadFileContents:

        Dataset. append ( Line.strip ( ) ) 

    return Dataset # dataset to lista sciezek do plikow


#musze zmienic troche system zeby

#####################################################################################################################################################
# i teraz musze troche uzyc xlrd

def ReadDatasetFileXLS ( DatasetFilePath ):

    from xlrd import open_workbook

    wb = open_workbook( DatasetFilePath )

    Paths = [ ]

    for s in wb.sheets():
        if s.name == 'Tilts':
           print 'Sheet:',s.name

           for row in range(s.nrows):
# na razie to wywalam
               if s.cell(row,44).value == 'YES':
#'/'. join ( [ s.cell(row,N).value for N in range(3)  ] ) + \
                  Paths. append ( \

                  s.cell(row, 0).value+'/'+s.cell(row, 6).value+'/'+'/'+s.cell(row,7).value+'/'+s.cell(row, 6).value+'_'+s.cell(row, 7).value+'.pdb' )
 
    return PdbFilesDataset ( Paths ) # dataset to lista sciezek do plikow


#musze zmienic troche system zeby


#####################################################################################################################################################
#####################################################################################################################################################

class ProteinFamilyDataset ( list ):

      def ExtractConsecutiveTriplets ( list ):
          print 'lala'
# moze zainicjowac z nazwa rodziny

#####################################################################################################################################################
#####################################################################################################################################################

class PdbFilesDataset ( list ):
      import PDB_FileContentsModule; from PDB_FileContentsModule import PdbFileContent;
# zastanawiam sie nad sposobem inicjowania tego tego, klasa jest lista sciezek plikow, to wszystko

      def __init__ ( self, InputFilePathInstances  ):
          self.Content = [ ]

          for InputFilePathInstance in InputFilePathInstances:

              self.Content. append ( InputFilePathInstance )

#####################################################################################################################################################

      def NoCAVsZSliceWidthGraph ( ): # trzeba jeszcze wiedziec, gdzie sa Srodki SliceOw
# i jak bym te funkcje zaprojektowal?, no jak, potrzebuje herbaty i cos zjesc, nie wiem

          for SliceWidth in range ( 1, 5 ): #

              AverageNoCaInZSlice ( float ( SliceWidth ) ) 

          return
      
#####################################################################################################################################################

      def AverageNoCaInZSlice (self ):

          return

#####################################################################################################################################################

      def ExtractProteinChains ( self, OutputPath = 'ExtractedProteinChains'):
          import os

          ProteinChainsInstances = [ ]
          
          for FilePathInstance in self.Content:

              FilePathInstance_Split = FilePathInstance. split ('/')
              Code = FilePathInstance_Split [ -1 ] [:4];
              Family = FilePathInstance_Split [ -2 ]
              os.system ( 'mkdir ./DaneWyjsciowe/ExtractedProteinChains' );
              os.system ( 'mkdir ./DaneWyjsciowe/ExtractedProteinChains'+'/'+Family );
              os.system ( 'mkdir ./DaneWyjsciowe/ExtractedProteinChains'+'/'+Family+'/'+Code );
              
              OutputPath = './DaneWyjsciowe/ExtractedProteinChains'+'/'+Family+'/'+Code+'/'+Code+'_'

              

              PDBFileContentsInstance = ReadPDBFileContents ( FilePathInstance )
              PDBFileProteinChains    = PDBFileContentsInstance. ExtractProteinChains ( OutputPath )      

              for ProteinChainInstance in PDBFileProteinChains: # 

                  ProteinChainsInstances. append ( ProteinChainInstance )

          return ProteinChainsInstances

#####################################################################################################################################################

      def ExtractTMSegments ( self, OutputPath = 'ExtractedTransmembraneHelices' ):
          

          Directory = '/home/soutys/Praca/Science/Science/Finlandia/Triplets/Dane/'
          os.system ( 'mkdir '+ Directory + '/DaneWyjsciowe' )
          os.system ( 'mkdir '+ Directory + '/DaneWyjsciowe/ExtractedTransmembraneHelices/' )

          OutputDirectory = Directory + '/DaneWyjsciowe/ExtractedTransmembraneHelices/'

          TMHelixInstances = [ ]

          InputDirectory = '/home/soutys/Praca/Science/Science/Finlandia/Triplets/Dane/DaneWejsciowe/ZbioryPlikowPDB/IntegralneAlfaHelikalneBialkaBlonowe/ByChain/'

#przestawic zeby bylo z parametrow

          print self.Content; # quit ();
          
          for FilePathInstance in self.Content:

              FilePathI = FilePath ( FilePathInstance )

              os.system ( 'mkdir ' + OutputDirectory +'/'+FilePathI.Family );
              print FilePathI.Family; print FilePathI.Code
              os.system ( 'mkdir ' + OutputDirectory +'/'+FilePathI.Family+'/'+FilePathI.Code );

              print FilePathI.Family; print FilePathI.Code; # quit ()

              OutputPath = OutputDirectory +'/'+FilePathI.Family+'/'+FilePathI.Code+'/'+FilePathI.Code+'_'

              PDBFileContentsInstance = ReadPDBFileContents ( InputDirectory + FilePathInstance )

              PDBFileTMSegments = PDBFileContentsInstance. ExtractTMSegments ( OutputPath )  # a wiec tutaj

              for TMHelixInstance in PDBFileTMSegments: # 

                  TMHelixInstances. append ( TMHelixInstance )

          return SetOfK_N_TMs_Sets ( TMHelixInstances )

#####################################################################################################################################################

      def ExtractTriplets(self, OutputPath = 'ExtractedTripletsDataset'):

          return [ NoAllInteractingTriplets, NoNotAllInteractingTriplets ]

#####################################################################################################################################################

      def ExtractConsecutiveTriplets ( self, OutputPath = 'ExtractedTripletsDataset' ):
          from SetOfTripletsModule import ConsecutiveTriplets

          ConsecutiveTripletsFromDataset = [ ]
         
          for PDBFilePath in self: # dla kazdej sciezki 

              OpenedFileInstance=open(PDBFilePath,'r')
              PdbFileContentInstance = PdbFileContent ( OpenedFileInstance.readlines() )
              OpenedFileInstance.close() # to by mozna bylo uproscic w jednej funkcji ReadFileContents ( FilePath ):

              PDBFilePath_Split = PDBFilePath.split ( '/' )
              IMP_DatasetPath = PDBFilePath_Split [ 0 ]; FamilyPath = PDBFilePath_Split [ 1 ]; 
              pdb_file = PDBFilePath_Split [ 2 ];
              ConsecutiveTripletsDatasetPath = 'ConsecutiveTripletsDataset'
              PDB_Code =  pdb_file [:4]             
 
              PDBFileOutputPath = ConsecutiveTripletsDatasetPath + '/' + FamilyPath + '/' + PDB_Code + '/' + pdb_file

              import os;
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ ConsecutiveTripletsDatasetPath)
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ ConsecutiveTripletsDatasetPath + '/' + FamilyPath );
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ ConsecutiveTripletsDatasetPath + '/' + FamilyPath + '/' + PDB_Code  );

              ConsecutiveTripletsFromFile = PdbFileContentInstance.ExtractConsecutiveTriplets ( PDBFileOutputPath )
              
              for ConsecutiveTripletFromFile in ConsecutiveTripletsFromFile.Content:

                  ConsecutiveTripletsFromDataset. append ( ConsecutiveTripletFromFile )         

          return ConsecutiveTriplets ( ConsecutiveTripletsFromDataset )

#####################################################################################################################################################

      def ExtractTouchingTriplets ( self, OutputPath = 'ExtractedTouchingTripletsDataset' ):
          from SetOfTripletsModule import ConsecutiveTriplets

          TouchingTripletsFromDataset = [ ]
         
          for PDBFilePath in self: # dla kazdej sciezki 

              OpenedFileInstance=open(PDBFilePath,'r')

              PdbFileContentInstance = PdbFileContent ( OpenedFileInstance.readlines() )
              OpenedFileInstance.close()
              PDBFilePath_Split = PDBFilePath.split ( '/' )
              IMP_DatasetPath = PDBFilePath_Split [ 0 ]; FamilyPath = PDBFilePath_Split [ 1 ]; 
              pdb_file = PDBFilePath_Split [ 2 ];
              TouchingTripletsDatasetPath = 'TouchingTripletsDataset'
              PDB_Code =  pdb_file [:4]             
 
              PDBFileOutputPath = TouchingTripletsDatasetPath + '/' + FamilyPath + '/' + PDB_Code + '/' + pdb_file

              import os;
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ TouchingTripletsDatasetPath)
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ TouchingTripletsDatasetPath + '/' + FamilyPath );
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ TouchingTripletsDatasetPath + '/' + FamilyPath + '/' + PDB_Code  );

              TouchingTripletsFromFile = PdbFileContentInstance.ExtractTouchingTriplets ( PDBFileOutputPath )
              
              for TouchingTripletFromFile in TouchingTripletsFromFile.Content:

                  TouchingTripletsFromDataset. append ( TouchingTripletFromFile )          

          return TouchingTripletsFromDataset ( TouchingTripletsFromDataset )

#####################################################################################################################################################

      def ExtractTouchingPairs ( self, OutputPath = 'ExtractedTouchingTripletsDataset' ):
          from SetOfTripletsModule import ConsecutiveTriplets

          TouchingPairsFromDataset = [ ]
          
          for PDBFilePath in self: # dla kazdej sciezki 

              OpenedFileInstance=open(PDBFilePath,'r')

              PdbFileContentInstance = PdbFileContent ( OpenedFileInstance.readlines() );                      
              OpenedFileInstance.close()
#             PDBFilePath = 'IMP_DatasetPath/FamilyPath/pdb_file'
              PDBFilePath_Split = PDBFilePath.split ( '/' )
              IMP_DatasetPath = PDBFilePath_Split [ 0 ]; FamilyPath = PDBFilePath_Split [ 1 ]; 
              pdb_file = PDBFilePath_Split [ 2 ];
              TouchingPairsDatasetPath = 'TouchingPairsDataset'
              PDB_Code =  pdb_file [:4]             
 
              PDBFileOutputPath = TouchingPairsDatasetPath + '/' + FamilyPath + '/' + PDB_Code + '/' + pdb_file

              import os;
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ TouchingPairsDatasetPath)
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ TouchingPairsDatasetPath + '/' + FamilyPath );
              os.system ('mkdir /home/soutys/science/HelixTriplets/MojProgram/'+ TouchingPairsDatasetPath + '/' + FamilyPath + '/' + PDB_Code  );

              TouchingPairsFromFile = PdbFileContentInstance.ExtractTouchingPairs ( PDBFileOutputPath )
              
              for TouchingPairFromFile in TouchingPairsFromFile.Content:

                  TouchingPairsFromDataset. append ( TouchingPairFromFile )

          return TouchingPairsFromDataset ( TouchingPairsFromDataset )

#####################################################################################################################################################

      def ExtractNsetsUpToOrder_K ( K = 7 ):
          NsetsUpToOrder_K = ExtractNsetsUpToOrder_K ( K - 1 ) # jakas rekurencja, jakies apriori, bo inaczej nie ogarne tego kuzwa

          return

#####################################################################################################################################################

      def ExtractConsecutiveTripletsFromFamilies ( self ):

          return             

#####################################################################################################################################################

      def DoHenrisConsecutiveTripletsPlot ( self ):
# do Plot
          return

#####################################################################################################################################################

      def ExtractTouchingNSets (self, OutputPath = 'ExtractedTouchingNSets', Order = 2 ):
          import sys;
          sys.path.insert (0, './Moduly/ReprezentacjaPDB/ZbiorNHelisTransblonowychPDB' )
          import os; import N_TMs_Sets; from N_TMs_Sets import SetOfK_N_TMs_Sets

          TMHelixInstances = [ ]; TouchingNSets = [ ];
          
          for FilePathInstance in self.Content:

              FilePathInstance_Split = FilePathInstance. split ('/')
              Code = FilePathInstance_Split [ -1 ] [:4];
              Family = FilePathInstance_Split [ -2 ]

              os.system ( 'mkdir ./DaneWyjsciowe/ExtractedTouchingNSets' );
              os.system ( 'mkdir ./DaneWyjsciowe/ExtractedTouchingNSets/'+ str ( Order ) );
              os.system ( 'mkdir ./DaneWyjsciowe/ExtractedTouchingNSets/'+ str ( Order )+'/'+Family );
              os.system ( 'mkdir ./DaneWyjsciowe/ExtractedTouchingNSets/'+ str ( Order )+'/'+Family+'/'+Code );
              
              OutputPath = './DaneWyjsciowe/ExtractedTouchingNSets/'+ str ( Order )+'/'+Family+'/'+Code+'/'+Code+'_'

              PDBFileContentsInstance = ReadPDBFileContents ( FilePathInstance )
              PDBFileTouchingNSets    = PDBFileContentsInstance. ExtractTouchingNSets ( OutputPath, Order )  # wiec tu musi byc blad
# i tak konieczna bedzie reorganizacja tego    

              for TouchingNSet in PDBFileTouchingNSets: # 

                  TouchingNSets. append ( TouchingNSet )

          TouchingNSetsInstance = SetOfK_N_TMs_Sets ( TouchingNSet ) 

          return TouchingNSetsInstance

#####################################################################################################################################################
#####################################################################################################################################################

class ConsecutiveTripletFilesDataset ( list ):

      def DoHenrisPlot ( self ):

          return

#####################################################################################################################################################
#####################################################################################################################################################

class FilePath ( ):

      def __init__ ( self, InputPathString ):

          self.String = InputPathString

          self.StringSplit = self.String. split ('/')

          self.Code = self.StringSplit [-1].split('_')[0]
#          print self.StringSplit [6]; quit ()
#          print self.Code; quit()

          self. Family = self.StringSplit [ 0 ] # moze to zmienie



