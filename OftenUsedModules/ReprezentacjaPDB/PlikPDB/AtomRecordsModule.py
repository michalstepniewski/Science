import sys

import  GeometricalClassesModule;
from GeometricalClassesModule import SetOfPoints;

#import PDB_FileContentsModule; from PDB_FileContentsModule import *; # PDB_file contents is highe so...
#from PDB_FileContentsModule import PdbRecords;

import SetOfAtomsModule;
from   SetOfAtomsModule import Residue, SetOfAtoms;

import AtomRecordModule; from AtomRecordModule import *;

from math import sqrt; 

#####################################################################################################################################################
#####################################################################################################################################################
# nie jestem pewien czy ten mmodul jest potrzebny jeszcze

class PdbRecords( list ):
      
   def funkcja():
      print 'lala'

#####################################################################################################################################################
#####################################################################################################################################################

class AtomRecords ( list ):
      
      def __init__ ( self, InputAtomRecords ):

          
# musze przemyslec te klasy dziedziczace po stringu!
          self. Content = [ ]

          for InputAtomRecord in InputAtomRecords:

              AtomRecordInstance = AtomRecord ( InputAtomRecord.s )
              self. Content. append ( AtomRecordInstance )

#          print    self. Content [ 0 ].s

#      def funkcja( self ):
#          print 'lala'

#####################################################################################################################################################

      def XYZs ( self ):

          return SetOfPoints ( [ PointInstance. XYZ for PointInstance in self. Content ] ) 

#####################################################################################################################################################

      def Center ( self ):

          return self. XYZs(). Center ( )

#####################################################################################################################################################

      def Print ( self ):

          for self.AtomRecordInstance in self.Content:

              self.AtomRecordInstance. Print ( )

#####################################################################################################################################################

      def ExtractProteinResidues ( self ):

          self.Residue = [ ]; self.Residues = [ ]

          self.Residue.append ( self.Content [ 0 ] ) # extract the first one
       
          for N in range ( 1, len ( self.Content ) ):

              CurrentAtom = self.Content[N]; PreviousAtom = self.Content[(N-1)];
              PreviousResSeqNo  = PreviousAtom. ResidueSequenceNumber ( )
              CurrentResSeqNo  =  CurrentAtom.  ResidueSequenceNumber ( ) # nie wiem czmu tak 
#           Dummy = PreviousAtom.ResidueSequenceNumber ( )
# wiec on uwaza ze ta nazwa jest zwiazana stringiem?
#           print self.Content[N].ResidueSequenceNumber ( )
#           I = N - 1; self.PreviousResidueSequenceNumber =  AtomRecord ( self.Content[1] ). ResidueSequenceNumber ( )  
              if CurrentResSeqNo != PreviousResSeqNo :

                 self.Residues.append ( Residue ( self.Residue ) )

                 self.Residue = [ ]

                 self.Residue. append ( self.Content [ N ] )

              else: 

                 self.Residue.append ( self.Content [ N ] )
       
          self.Residues.append ( Residue ( self.Residue ) ) # extract the last Residue      

          return self.Residues # returning list of Residues, atom by atom, now to the Extraction but after lunch and everything

#####################################################################################################################################################
      def AddLipids ( self, Lipids ): 

       LipidInTheCorner = Lipids. Corner0_0Lipid ( )

       # Trzy Klasy Lipidow
       # Inicjalizacja

       Dodane, Brzeg, Klaszujace, Niesprawdzone = [ [], [], [], [] ]

       Brzeg = LipidInTheCorner

       Klaszujace = Lipids. Klaszujace ( self ) 

       Niesprawdzone = Lipids.OdejmijLipidy ( Brzeg );
       Niesprawdzone = Niesprawdzone. OdejmijLipidy ( Klaszujace );

       update = True

       while update:

             Dodane = Dodane. DodajLipidy ( Brzeg );

             NowyBrzeg = Niesprawdzone. Kontaktujace ( Brzeg ); Niesprawdzone. OdejmijLipidy ( NowyBrzeg );             
             Brzeg = NowyBrzeg;

             if Brzeg == []: update = False
    

       return Dodane

#####################################################################################################################################################

      def RotateByMatrix ( self, RotationMatrix ):

          [ Atom. RotateByMatrix ( RotationMatrix ) for Atom in self. Content ]

#####################################################################################################################################################

      def Translate ( self, Vector ):

          [ Atom.Translate ( Vector ) for Atom in self. Content ]

#####################################################################################################################################################

      def SuperimposeOnTemplate ( self, Template ):

# przygotowanie

          TemplateGeometricalCenter = Template. Center ( )

# trzy kroki
# 1szy krok

          self. MoveToOrigin ()
          Template. MoveToOrigin ()

# 2gi krok

          self. RotateOnTemplate ( Template )

# 3ci krok

          self. Translate ( TemplateGeometricalCenter )
          Template. Translate ( TemplateGeometricalCenter )

          return

#####################################################################################################################################################

class Lipidy ( list ):

#      def __init__ ( self ):

#####################################################################################################################################################

      def DodajLipidy ( self ):
          return

#####################################################################################################################################################

      def OdejmijLipidy ( self ):
          return

#####################################################################################################################################################

      def Klaszujace ( self, ZbiorAtomow ):
          return

#####################################################################################################################################################

      def Kontaktujace ( self, ZbiorLipidow ):
          return

#####################################################################################################################################################
#####################################################################################################################################################

class Lipid ( SetOfAtoms ):

#####################################################################################################################################################

      def DummyMethod ( self ):

          return

#####################################################################################################################################################
#####################################################################################################################################################

# potem musze zrobic to pierwsze cwiczenie, bo nie zostalo duzo czasu
# moze kiborda sobie kupie, zobacze ile stoja... 

####################################################################################################
# powinienem tez wymyslec cos zeby wiedziec, ktore aminokwasy sie kontaktuja ... to jest dla pary ...
# po matrycy minimalnych dystansow powinna byc matryca jakie pary residuow biora udzial w takim wiazaniu
# czyli np
# CONTACT RESIDUES EC TM1/TM2: [[109S,164E],[123E,165G]]
# CONTACT RESIDUES EC TM2/TM3: [[109S,164E],[123E,165G]]
# CONTACT RESIDUES EC TM1/TM3: [[109S,164E],[123E,165G]] 
# CONTACT RESIDUES IC TM1/TM2: [[109S,164E],[123E,165G]]
# CONTACT RESIDUES IC TM2/TM3: [[109S,164E],[123E,165G]]
# CONTACT RESIDUES IC TM1/TM3: [[109S,164E],[123E,165G]]
# i zobaczymy ile bedzie tryptofanow w tym ...

class Setof2AtomRecords ( list ):                                      # Pair of Atoms

      def __init__ ( self, InputAtomRecords ): 

          self. Content = [ ]

          for InputAtomRecord in InputAtomRecords:
              AtomRecordInstance = AtomRecord ( InputAtomRecord.s )
             
              self. Content. append ( AtomRecordInstance )
# learn to handle directionality in sequence, maybe use reverse? 

#####################################################################################################################################################

      def Vector(self):

          Atom1 = self.Content [0]
          Atom2 = self.Content [1]

          Vector = [ Atom2.X - Atom1.X, Atom2.Y - Atom1.Y, Atom2.Z - Atom1.Z ]

          return Vector

#####################################################################################################################################################
 
      def Distance(self):

          VectorI= self.Vector()
          DistanceI = sqrt( (VectorI[0]**2.0) + (VectorI[1]**2.0) + (VectorI[2]**2.0)  )

          return DistanceI

#####################################################################################################################################################

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

######################

