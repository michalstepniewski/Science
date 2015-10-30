#####################################################################################################################################################

def ReadRepresentationFileContents ( FilePath, PDBCode='Code', ChainID = 'ID', Family = 'DummyFamily' ):

    import NSetRepresentationFileContentsModule; from NSetRepresentationFileContentsModule import RepresentationFileContents;

    OpenedFileInstance=open( FilePath,'r' )
    
    RepresentationFileContentsInstance = RepresentationFileContents ( OpenedFileInstance.readlines(), PDBCode, ChainID, Family )
#    print PDBCode; quit()
    OpenedFileInstance.close()

    return RepresentationFileContentsInstance

#####################################################################################################################################################

def ReadDatasetFile ( DatasetFile ):

    ReadFileInstance = open ( DatasetFile, 'r' ) 

    ReadFileContents = ReadFileInstance.readlines ( )

    ReadFileInstance.close ( )

    Dataset = [ ]    

    for Line in ReadFileContents:

        Dataset. append ( Line.strip ( ) ) 

    return RepresentationFilesDataset ( Dataset ) # dataset to lista sciezek do plikow


#musze zmienic troche system zeby
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

class RepresentationFilesDataset ( list ) :

      def __init__ ( self, InputFilePathInstances  ):

          self.Content = [ ]

          for InputFilePathInstance in InputFilePathInstances:

              self.Content. append ( InputFilePathInstance )

#####################################################################################################################################################

      def ReadRepresentations ( self ) :

          RepresentationInstances = [ ]

          for FilePathInstance in self.Content:

              PDBCode = FilePathInstance.split ('/') [ -1 ] [ :4 ]

              ChainID = FilePathInstance.split ('/') [ -2 ]

              Family = FilePathInstance.split ('/') [ -4 ]

              RepresentationFileContentsInstance = ReadRepresentationFileContents ( FilePathInstance, PDBCode, ChainID, Family )

#              print Family

              RepresentationInstance = RepresentationFileContentsInstance. ReadRepresentation ( )
#              print 'EC_Fis'
#              print RepresentationInstance. EC_Fis; quit ()

              RepresentationInstances. append ( RepresentationInstance )

          import SetOfN_TMs_SetRepresentationsModule;
          from SetOfN_TMs_SetRepresentationsModule import SetOfN_TMs_SetRepresentations;

#          print NSetRepresentationInstance. EC_Fis; quit ()
#          print 'EC Fis'
#          print SetOfN_TMs_SetRepresentations ( RepresentationInstances ). Content [ 0 ]. EC_Fis; quit () 
          return SetOfN_TMs_SetRepresentations ( RepresentationInstances ) 
