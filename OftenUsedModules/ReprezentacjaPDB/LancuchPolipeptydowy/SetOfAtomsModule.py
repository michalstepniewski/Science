###################################################
# musze ogarnac teraz ta superpozycje
# jak dziedziczyc jedna klase z innych, initem? moze initem
import sys;

import Parametry;


import AtomRecordModule;
from AtomRecordModule import *;

import AtomRecordsModule 

import GeometricalClassesModule;
from GeometricalClassesModule import *;


#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

class SetOfAtoms ( list ):

      def __init__ ( self, InputAtomRecords ):

          self. Content = [ ]

          for InputAtomRecord in InputAtomRecords:

              AtomRecordInstance = AtomRecord ( InputAtomRecord.s )
 
              self. Content. append ( AtomRecordInstance )

          return

#####################################################################################################################################################

      def Print ( self ):

          for AtomRecordInstance in self.Content:

              AtomRecordInstance. Print ( )

#####################################################################################################################################################

      def CenterOfMass ( self ):

          if self.Content == []: # check if there are any atoms to compute COM from ...
             print self
             print 'AtomSetIsEmpty. Unable to calcuate Center Of Mass.'
#             quit()

          X_Sum, Y_Sum, Z_Sum, Mass_Sum  = [ 0.0, 0.0, 0.0, 0.0 ] 

          for Atom in self. Content:
          
              X_Sum += ( Atom .X * Atom .Mass () ) # bo od tego sa wagi
              Y_Sum += ( Atom .Y * Atom .Mass () ) # zeby wazyc
              Z_Sum += ( Atom .Z * Atom .Mass () ) 

              Mass_Sum += Atom .Mass ()

          CenterOfMass = [ (Coord_Sum / Mass_Sum) for Coord_Sum in [X_Sum, Y_Sum, Z_Sum ] ]

          return CenterOfMass

#####################################################################################################################################################

      def Vector ( self ):

          Atom1 = self.Content [0]
          Atom2 = self.Content [1]

          VectorI = [ Atom2.X - Atom1.X, Atom2.Y - Atom1.Y, Atom2.Z - Atom1.Z ]
          print VectorI

          return Vector ( VectorI )

#####################################################################################################################################################
 
      def Distance ( self ):

          return self.Vector ( ). Length ( )

#####################################################################################################################################################
#musze zrobic przejrzystrza strukture
      def VdWContact (self):

          SumOfVdWRadiuses = self.Content[0].VdWRadius ( ) + self.Content[1].VdWRadius ( )

          if self.Distance() <= ( 1.0 * SumOfVdWRadiuses ) : # to jest Clash, dla kontaktu damy inny zasieg, np.
# przemnazamy przez 1.1 

             return True

          else:

             return False

#####################################################################################################################################################

      def VdWContactConstantThreshold (self, ConstantThreshold = 4.50 ):

          SumOfVdWRadiuses = self.Content[0].VdWRadius ( ) + self.Content[1].VdWRadius ( )

          if self.Distance() <= ConstantThreshold : # to jest Clash, dla kontaktu damy inny zasieg, np.
# przemnazamy przez 1.1
# myslec o tym ze kazdy wegiel ma wodory jeszcze i zastanowic sie nad tym pomiedzy jakimi atomami sa mozliwe takie kontakty 

             return True

          else:

             return False

#####################################################################################################################################################

      def HydrogenBond ( self ):

# jakie jest kryterium wiazania wodorowego

          return False

#####################################################################################################################################################
#####################################################################################################################################################

class Residue ( SetOfAtoms ):

      def __init__ ( self, InputAtomRecords ):

          self. Content = [ ]

          for InputAtomRecord in InputAtomRecords:

              AtomRecordInstance = AtomRecord ( InputAtomRecord.s )
 
              self. Content. append ( AtomRecordInstance )
          
          return

#####################################################################################################################################################

      def HydrogenBondDonors ( self ) :

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

          HydrogenBondDonorsI = [ ]

          HydrogenBondDonorsI. append ( self. SelectAtomByName ( Type ) )

          if self. Name in AminoacidAtomLexicon. keys ( ):

             HydrogenBondDonorsI. append ( self. SelectAtomByName ( AminoacidAtomLexicon [ self. Name ] ) )

          return HydrogenBondDonorsI

# Hydrogen donor protein atoms
# analyzed in this study were: NH of the main chain, ARG NE,
# ASN ND2, HIS NE2, SER OG, TYR OH, ARG NH1, CYS
# SG, HIS ND1, THR OG1, ARG NH2, GLN NE2, LYS NZ
# and TRP NE1;

#####################################################################################################################################################

      def SelectAtomByName ( self, Name ):

          for AtomInstance in self. Content:

              if AtomInstance. Name == Name:

                 return AtomInstance

#####################################################################################################################################################

      def HydrogenBondAPrimAcceptorPairs ( self ):

          AType = 'O  '

          APrimType = 'C  '

          AAminoacidAtomLexicon = { 'ASN' : 'OD1', \
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

          APrimAminoacidAtomLexicon = { 'ASN' : 'CG ', \
                                     'GLN' : 'CD ', \
                                     'MET' : 'CG ', \
                                     'ASP' : 'CG ', \
                                     'GLU' : 'CD ', \
                                     'SER' : 'CB ', \
                                     'ASP' : 'CG ', \
                                     'GLU' : 'CD ', \
                                     'THR' : 'CB ', \
                                     'CYH' : 'CB ', \
                                     'HIS' : 'CG ', \
                                     'TYR' : 'CZ '     }

          HydrogenBondAPrimAcceptorPairsI = [ ]

          HydrogenBondAPrimAcceptorPairsI. append ( [ self. SelectAtomByName ( APrimType ), self. SelectAtomByName ( AType ) ] )

          if self. Name in AAminoacidAtomLexicon. keys ( ):

             HydrogenBondAPrimAcceptorPairsI. append ( [ self. SelectAtomByName ( APrimAminoacidAtomLexicon [ self. Name ] ), self. SelectAtomByName ( APrimAminoacidAtomLexicon [ self. Name ] ) ] )

# czyli mamy residue 

          return self. HydrogenBondAPrimAcceptorPairsI

#####################################################################################################################################################

      def RotateByMatrix ( self, Matrix ):

          for AtomI in self. Content:

              AtomI. RotateByMatrix ( Matrix )

          return

#####################################################################################################################################################

      def Print ( self ):

          for AtomRecordInstance in self.Content:

              AtomRecordInstance. Print ( )

#####################################################################################################################################################

      def CA ( self ):                                                     # chain CA atoms

          for AtomRecordInstance in self.Content:

              Name = AtomRecordInstance. Name

              if Name == ' CA ':

                 CA = AtomRecordInstance
#                 break
# wiec co robimy jesli reszta nie ma CA? 
# mozemy wydrukowac 'Incomplete Residue'

          try: 
               return CA

          except UnboundLocalError:

                 print 'Incomplete Residue does not contain CA. Will try to go with N'
#                 print self 

                 for AtomRecordInstance in self.Content:

                     Name = AtomRecordInstance. Name

                     if Name == ' N  ' :

                        N = AtomRecordInstance

                 try: return N

                 except UnboundLocalError:

                        print 'Incomplete Residue does not contain CA nor N. Will try to go with C'
#                        print self 

                        for AtomRecordInstance in self.Content:

                            Name = AtomRecordInstance .Name 

                            if Name == ' C  ' :

                               C = AtomRecordInstance
                        self. Print ()
                        return C

#####################################################################################################################################################

      def M ( self ): # if it is a membrane residue

          Zcoord = self.Z ()

          if ( Zcoord  >= Parametry. MembraneLimits [0] ) and ( Zcoord  <=  Parametry. MembraneLimits [1] ) :  
             
             return True
          else:
                return False

#####################################################################################################################################################

      def SequenceNumber ( self ): # czemu tak?

          AtomRecordInstance = self.Content [ 0 ] # so just the seq number of first number, we have to remember that 
                                                # sometimes not everything is visible on Xray

          return AtomRecordInstance.ResidueSequenceNumber ( )

#####################################################################################################################################################

      def AA ( self ):

          AtomRecordInstance = self.Content  [ 0 ]

          return AtomRecordInstance.AA ( )

#####################################################################################################################################################

      def Chain ( self ):

          AtomRecordInstance = self.Content  [ 0 ]

          return AtomRecordInstance.Chain ( ) #dziwne ze nie chce ()

#####################################################################################################################################################

      def Name ( self ): # niektore funkcje powinienem przeniesc do initu
          NameI = str(self. SequenceNumber ( ))+self.AA();
          return NameI

#####################################################################################################################################################

      def Z ( self ):
          
          return self.CA (). Z

#####################################################################################################################################################

      def Mass ( self ):

          self.MassSum = 0.0

          for AtomRecordInstance in self.Content:  self.MassSum += AtomRecordInstance. Mass ( )

          return self.MassSum

#####################################################################################################################################################
#####################################################################################################################################################

class SetOfResidues ( list ):

      def __init__ (self, InputResidueInstances ):
          
          self.Content = []      

          for InputResidueInstance in InputResidueInstances: 
           

#           ResidueInstance = Residue ( InputResidueInstance ) # dlatego z tym tez sobie dajemy spokoj chwilowo
              self.Content. append ( InputResidueInstance ) # chwilowo, ciezko wymyslec dobry konstruktor 

#####################################################################################################################################################

      def Print ( self ):

          for ResidueInstance in self.Content:

              ResidueInstance. Print ( )

# musimy przy inicjowaniu to ogarniac

#####################################################################################################################################################

      def CenterOfMass ( self ):

          if self.Content == []: # check if there are any atoms to compute COM from ...
             print self
             print 'Set Of Residues is Empty. AtomSetIsEmpty'
#             quit()

          X_Sum, Y_Sum, Z_Sum, Mass_Sum = [ 0.0, 0.0, 0.0, 0.0 ]

          for ResidueInstance in self.Content:
          
              X_Sum += ( ResidueInstance.CenterOfMass()[0] * ResidueInstance .Mass () ) # bo od tego sa wagi
              Y_Sum += ( ResidueInstance.CenterOfMass()[1] * ResidueInstance .Mass () ) # zeby wazyc
              Z_Sum += ( ResidueInstance.CenterOfMass()[2] * ResidueInstance .Mass () ) 

              Mass_Sum += ResidueInstance .Mass () 

          CenterOfMassI = [ (CoordSum / Mass_Sum) for CoordSum in [ X_Sum, Y_Sum, Z_Sum] ]

          return CenterOfMassI

#####################################################################################################################################################

      def VdWContact ( self ):

          Res1, Res2 = self.Content

          for AtomRecordInstance1 in Res1.Content:

              for AtomRecordInstance2 in Res2.Content:

                  if SetOfAtoms ( [ AtomRecordInstance1, AtomRecordInstance2 ] ). VdWContact ():

                     return True

          return False

#####################################################################################################################################################

      def HydrogenBond ( self, DADistanceThreshold = 3.9  ):

          AA1 = self. Content [ 0 ]

          AA2 = self. Content [ 1 ]

# test AA1 as acceptor and AA2 as donor

          AcceptorAprimPairs = AA1. HydrogenBondAPrimAcceptorPairs ( )

          Donors = AA2. HydrogenBondDonors ( )

          for AcceptorAprimPair in AcceptorAprimPairs:

              Acceptor = AcceptorAprimPair [ 0 ]

              for Donor in Donors:

                  if [ Acceptor, Donor ]. Distance ( ) <= DADistanceThreshold:

                     if [ [ Acceptor, APrim ], [ Acceptor, Donor ] ]. Angle ( ):

                        return True      

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 

          AcceptorAprimPairs = AA2. HydrogenBondAPrimAcceptorPairs ( )

          Donors = AA1. HydrogenBondDonors ( )

          for AcceptorAprimPair in AcceptorAprimPairs:

              Acceptor = AcceptorAprimPair [ 0 ]

              for Donor in Donors:

                  if [ Acceptor, Donor ]. Distance ( ) <= DADistanceThreshold:

                     if [ [ Acceptor, APrim ], [ Acceptor, Donor ] ]. Angle ( ):

                        return True                   

# musze znac AJ-A-D 90.0, wiec tak naprawde potrzebuje czterech atomow

# A' - A -- D - D'                

# D-A < 3.9 A

          return False

#####################################################################################################################################################
# oprocz tego przydaloby sie wiedziec jakie reszty w tym uczestnicza, wiec dla pary Helis trzebaby miec liste vdw Kontaktow     

      def VdWContactOrHydrogenBond ( self ):

          Res1, Res2 = self.Content

          if ( self. VdWContact ( ) or  self. HydrogenBond () ):

             return True   

          return False

#####################################################################################################################################################

      def DisulfideBond (self, DistanceThreshold ):



          return False

#####################################################################################################################################################

      def CAs ( self ):

          return [ ResidueInstance. CA ( ) for ResidueInstance in self. Content ]
