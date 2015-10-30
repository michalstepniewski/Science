#to jest stara wersja niestety, musze przywrocic nowa

import ParameterFilePathFile

ParameterFileInstance = open ( ParameterFilePathFile. ParameterFilePath, 'r' )

ParameterFileContent = ParameterFileInstance. readlines ( )

ParameterFileInstance. close ( )

for Line in ParameterFileContent:

        if 'VdWContactThreshold =' in Line:

           VdWContactThreshold = float ( Line. split ('=') [ 1 ]. split ( ) [ 0 ] )

        elif 'PruneBasedOnHalfHelixDiscrepancy =' in Line:

           PruneBasedOnHalfHelixDiscrepancyStr = str ( Line. split ('=') [ 1 ]. strip ( ) )

           if PruneBasedOnHalfHelixDiscrepancyStr == 'Yes':

              PruneBasedOnHalfHelixDiscrepancy = True

           else:

              PruneBasedOnHalfHelixDiscrepancy = False


        elif 'NoVdWContactsThreshold =' in Line:

           NoVdWContactsThreshold = int ( Line. split('=') [1].strip() )

        elif 'CrossingAnglesDefinition =' in Line:

           CrossingAnglesDefinition = Line. split('=') [1].strip()

        elif 'AminoAcidMembraneDepthPreferenceBinWidth =' in Line:

           AminoAcidMembraneDepthPreferenceBinWidth = float ( Line. split ('=') [ 1 ]. split ( ) [ 0 ] )

        elif 'MembraneLimits =' in Line:

           MembraneLimits = [ float(item) for item in Line. split ('=') [ 1 ]. split ( ',' ) ]
#           print MembraneLimits; quit ();

        elif 'PercentHelicityThreshold =' in Line:

           PercentHelicityThreshold = float ( Line. split ('=') [ 1 ]. split ( ) [ 0 ] )

        elif 'TMHelicesOutputPath =' in Line:

           TMHelicesOutputPath = Line. split ('=') [ 1 ]

        elif 'ReferenceFrame =' in Line:

           ReferenceFrame = Line. split ('=') [ 1 ]

        elif 'HydrogenBondDistanceThreshold =' in Line:

           HydrogenBondDistanceThreshold  = float ( Line. split ('=') [ 1 ]. split ( ) [ 0 ]  )

        elif 'HydrogenBondAngleRange =' in Line:

           HydrogenBondAngleRange = Line. split ('=') [ 1 ] # musze poczytac o HydrogenBondach

        elif 'Width_Of_Thin_Slices =' in Line:

           Width_Of_Thin_Slices = float ( Line. split ('=') [ 1 ]. split ( ) [ 0 ] )

        elif 'AminoAcidPerSliceBinWidth =' in Line:

           AminoAcidPerSliceBinWidth = float ( Line. split ('=') [ 1 ]. split ( ) [ 0 ] )

        elif 'AminoAcidPerSliceBinCenters =' in Line:

           AminoAcidPerSliceBinCenters = [ float ( i. split ( ) [ 0 ] ) for i in  Line. split ('=') [ 1 ] . split ( ';' ) ]

        elif 'COMs_Of_Thin_Slices =' in Line:

           COMs_Of_Thin_Slices = [ float ( i. split ( ) [ 0 ] ) for i in  Line. split ('=') [ 1 ] . split ( ';' ) ]

           print COMs_Of_Thin_Slices

        elif 'COMs_Of_Wide_Slices' in Line:

           COMs_Of_Wide_Slices = [ float ( i. split ( ) [ 0 ] ) for i in  Line. split ('=') [ 1 ] . split ( ';' ) ]

        elif 'Width_Of_Wide_Slices =' in Line:

           Width_Of_Wide_Slices = float ( Line. split ('=') [ 1 ] )

        elif 'NoAAPerSliceRange =' in Line:

           NoAAPerSliceRange = [ int(item) for item in Line. split ('=') [ 1 ]. split (',' ) ]            

        elif 'TripletsExtractionRule =' in Line:

           TripletsExtractionRule = Line. split ('=') [ 1 ]. strip ( )

        elif 'TripletAxisDefinition =' in Line:

           TripletAxisDefinition = Line. split ('=') [ 1 ]. strip ( )

        elif 'MainAxisDefinition =' in Line:

           MainAxisDefinition = Line. split ('=') [ 1 ]. strip ( )

        elif 'HalfHelixAxesDefinition =' in Line:

           HalfHelixAxesDefinition = Line. split ('=') [ 1 ]. strip ( )

        elif 'PDBFilelistFile =' in Line:

           PDBFilelistFile = Line. split ('=') [ 1 ]. strip ( )

        elif 'TMBundlesRepresentationFilelistFile =' in Line:  

           TMBundlesRepresentationFilelistFile = Line. split ('=') [ 1 ]. strip ( )


        elif 'NsetRepresentationsDatasetFile =' in Line:  

           NsetRepresentationsDatasetFile = Line. split ('=') [ 1 ]. strip ( )

           print NsetRepresentationsDatasetFile

        elif 'Version =' in Line:  

           Version = Line. split ('=') [ 1 ]. strip ( )

           print Version

        elif 'TripletRepresentationsDatasetFile =' in Line:  

           TripletRepresentationsDatasetFile = Line. split ('=') [ 1 ]. strip ( )

           print TripletRepresentationsDatasetFile


        elif 'NsetRepresentationsDatasetFilePCA =' in Line:  

           NsetRepresentationsDatasetFilePCA = Line. split ('=') [ 1 ]. strip ( )

           print NsetRepresentationsDatasetFilePCA

        elif 'NsetRepresentationsDatasetFileCOM =' in Line:  

           NsetRepresentationsDatasetFileCOM = Line. split ('=') [ 1 ]. strip ( )

           print NsetRepresentationsDatasetFileCOM

        elif 'PDBDatasetFilePath =' in Line:  

           PDBDatasetFilePath = Line. split ('=') [ 1 ]. strip ( )


        elif 'HelixDirectionality =' in Line:

           HelixDirectionality = Line. split ('=')[ 1 ]. strip ( )


        elif 'NsetsExtractionRule' in Line:

           NsetsExtractionRule = Line. split ('=')[ 1 ]. strip ( )

        elif 'PCASlicesRanges =' in Line:

           Ranges = Line. split('=')[1].split(';')

           PCASlicesRanges = [[ float(item) for item in Range.split(',')] for Range in Ranges ]

        elif 'PCAMCTiltDifferenceThreshold =' in Line:

           PCAMCTiltDifferenceThreshold = Line. split('=')[1]. split() [0]

        elif 'TiltDefinition =' in Line:

           TiltDefinition = Line. split('=')[1]


        elif 'AtomicContactZRange =' in Line:

           AtomicContactZRange = [ float(item) for item in Line. split('=')[1]. split(',') ]


        


BordersOfThinSlices = [ ]

for N in range ( len ( COMs_Of_Thin_Slices ) ):

        BordersOfThinSlices. append ( [ COMs_Of_Thin_Slices [ N ] - (Width_Of_Thin_Slices /2.0), COMs_Of_Thin_Slices [ N ] + (Width_Of_Thin_Slices /2.0)  ] )

BordersOfWideSlices = [ ]

for N in range ( len ( COMs_Of_Wide_Slices ) ):

        BordersOfWideSlices. append ( [ COMs_Of_Wide_Slices [ N ] - (Width_Of_Wide_Slices /2.0), COMs_Of_Wide_Slices [ N ] + (Width_Of_Wide_Slices /2.0)  ] )

#    return

# Parametry ( VdWContactThreshold, \
#                       HydrogenBondDistanceThreshold, \
#                       HydrogenBondAngleRange, \
#                       Width_Of_Thin_Slices, \
#                       COMs_Of_Thin_Slices, \
#                       Width_Of_Wide_Slices, \
#                       TripletsExtractionRule, \
#                       PDBFilelistFile, \
#                       TMBundlesRepresentationFilelistFile, \
#                       BordersOfThinSlices, \
#                       BordersOfWideSlices, \
#                       MainAxisDefinition, \
#                       HalfHelixAxesDefinition )

#####################################################################################################################################################

#ReadParameterFile ( ParameterFilePathFile. ParameterFilePath )

#####################################################################################################################################################

class Parametry ( list ):

      def __init__ ( self, VdWContactThreshold, \
                           HydrogenBondDistanceThreshold, \
                           HydrogenBondAngleRange, \
                           Width_Of_Thin_Slices, \
                           COMs_Of_Thin_Slices, \
                           Width_Of_Wide_Slices, \
                           TripletsExtractionRule, \
                           PDBFilelistFile, \
                           TMBundlesRepresentationFilelistFile, \
                           BordersOfThinSlices, \
                           BordersOfWideSlices, \
                           MainAxisDefinition, \
                           HalfHelixAxesDefinition ):

          self. VdWContactThreshold = VdWContactThreshold
          self. HydrogenBondDistanceThreshold = HydrogenBondDistanceThreshold
          self. HydrogenBondAngleRange = HydrogenBondAngleRange
          self. Width_Of_Thin_Slices = Width_Of_Thin_Slices
          self. COMs_Of_Thin_Slices = COMs_Of_Thin_Slices
          self. Width_Of_Wide_Slices = Width_Of_Wide_Slices
          self. TripletsExtractionRule = TripletsExtractionRule
          self. PDBFilelistFile = PDBFilelistFile
          self. TMBundlesRepresentationFilelistFile = TMBundlesRepresentationFilelistFile
          self. MainAxisDefinition = MainAxisDefinition
          self. BordersOfThinSlices = BordersOfThinSlices
          self. BordersOfWideSlices = BordersOfWideSlices
          self. HalfHelixAxesDefinition = HalfHelixAxesDefinition

#####################################################################################################################################################
#####################################################################################################################################################

