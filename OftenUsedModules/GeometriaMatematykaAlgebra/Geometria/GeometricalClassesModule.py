import numpy as np
import sys;
import match; 

from match import rmsd, optimal_superposition

import Kombinatoryka;

from Kombinatoryka import Perturbations

import math; from math import *;

#ok, jutro rano zrobimy do konca ;-)

import functions_module
from functions_module import *;

def Generate3DRotationMatrix ( Angle ): # angle counter-clockwise

    RotationMatrix3D = [ [ cos ( Angle ), - sin ( Angle ), 0.0 ], \
                         [ sin ( Angle ),   cos ( Angle ), 0.0 ], \
                         [ 0.0,             0.0,           1.0 ] ]

#    print RotationMatrix2D

    return RotationMatrix3D # tymczasowo

# print functions_module. Generate3DRotationMatrix ( 360.0 )

# from functions_module import Generate3DRotationMatrix;

import copy;

# w miare uprzatniete, ale punkt to tak naprawde to samo co wektor!
# mozliwe ze powinno to byc zdefiniowane w TM Helix
#####################################################################################################################################################
#####################################################################################################################################################
#####################################################################################################################################################

class SetOfVectors ( list ):

      """
      stores N Kdimensional vectors
      """

      def __init__ ( self, Vectors ):

          self. Content = [ ]

          for InputVector in Vectors:

              self.Content. append ( InputVector ) 
          
          return

#####################################################################################################################################################
# hmm jakbym mogl udekorowac liste :) hmmm

          """
          returns the dihedral of two anchored vectors
          """

      def Dihedral ( self ):


          Axis =  SetOfPoints ( [self. Content [ 0 ]. AnchorPoint, self. Content [ 1 ]. AnchorPoint ] ). Vector ( )
          print Axis

          Vector1 = SetOfVectors ( [ self. Content [ 0 ], Axis ] ). VectorProduct ( )
          print Vector1
          Vector2 = SetOfVectors ( [ Axis, self. Content [ 1 ] ] ). VectorProduct ( )
          print Vector2
          return SetOfVectors ( [ Vector1, Vector2 ] ). AngleDEG ( )

#####################################################################################################################################################

      def VectorProduct ( self ): # ok since you can only compute cross product in 3D space, then the vectors would be 3D with Z = 0

          """
          returns VectorProduct of Two Vectors
          """

          A_3D = self.Content [ 0 ]
          B_3D = self.Content [ 1 ]

#
          if len ( A_3D) == 2: 

             A_3D. append ( 0.0 ) # makes it possible to do vector product for 2D vectors

          if len ( B_3D ) == 2:

             B_3D. append ( 0.0 ) # extenstion to 2D, add 3rd dimension
#
          Cx = ( A_3D [ 1 ] * B_3D [ 2 ] ) - ( A_3D [ 2 ] * B_3D [ 1 ] )
          Cy = ( A_3D [ 0 ] * B_3D [ 2 ] ) - ( A_3D [ 2 ] * B_3D [ 0 ] )
          Cz = ( A_3D [ 0 ] * B_3D [ 1 ] ) - ( A_3D [ 1 ] * B_3D [ 0 ] )

          C  = [ Cx, Cy, Cz ] 

          return Vector (C)

#####################################################################################################################################################

      def DotProduct ( self ):

          DotProductI = 0.0

          for N in range( len(self.Content[0]) ):

              DotProductI += ( self.Content[0][N] * self.Content[1][N] )            

          return DotProductI

#####################################################################################################################################################

      def Angle ( self, AccountForAngleDirection = 'No' ):

          """
          returns Angle between two vectors [Rad]
          """
# zle bo dlugosc sie nie liczy
          self.Cos = self.DotProduct () / ( self. Content [ 0 ]. Length () * self. Content [ 1 ]. Length () ) 
#          print self. Cos;
          if 0.999 <= self.Cos <= 1.001: # obsluga wyjatku

             return 0.0   

           

          else: self.Angle = acos ( self.Cos )

          self. Sin = self.VectorProduct () [2] / ( self. Content [ 0 ]. Length () * self. Content [ 1 ]. Length () )

          if AccountForAngleDirection == 'Yes' and self. Sin <= 0.0:

             return ( -1.0 * self. Angle )

          return self.Angle

#####################################################################################################################################################

      def AngleDEG ( self, AccountForAngleDirection = 'No' ): # powinno byc w funkcjach matematycznych

          """
          returns Angle between two vectors [DEG]
          """

          return ( (self.Angle(AccountForAngleDirection)/(2*math.pi))*360 )

# contact pattern is easier than 

#####################################################################################################################################################

      def Sum ( self ):

          """
          returns a sum of N vectors
          """

          SumI = [ 0.0 for N in range( len ( self. Content [0] ) ) ]

          for VectorI in self. Content:

              for I in range( len ( self. Content [0] ) ):

                  SumI[I] += VectorI [ I ]
          
          return Vector ( SumI )

#####################################################################################################################################################

      def RotationMatrix ( self ):

          """
          returns a rotation from 0th vector to 1st vector
          """

          print np.array(self.Content[0]).shape
          print np.array(self.Content[1])

          return optimal_superposition( np.array( [ [ 0.0, 0.0, 0.0  ], self.Content[0] ] ), np.array( [ [ 0.0, 0.0, 0.0  ], self.Content[1] ] ) ).T

# jakies optimal superposition


#####################################################################################################################################################
#####################################################################################################################################################

class Vector ( list ):

      """
      stores one N dimensional vector

      """

#####################################################################################################################################################

      def CartesianToSpherical ( self ):

          X, Y, Z = self

          R = sqrt  ( X**2 + Y**2 + Z**2 )

          if R == 0.0: Theta = 0.0

          else: Theta = acos ( Z/R ) * ( 180 / math.pi )

          if X == 0.0: fi = 0.0

          else: fi = atan ( Y/X ) * ( 180 / math.pi )

          return Point ( [ R, Theta, fi ] ) # moze lepiej byloby to przerobic na stopnie

#####################################################################################################################################################

      def AnchorInPoint ( self, Point ):

          self. AnchorPoint = Point
          print self. AnchorPoint
#          quit ()

#####################################################################################################################################################

      def ZPlaneIntersectionPoint ( self, Zz ):

          ScalingFactor = ( Zz - self.AnchorPoint [ 2] ) / self [ 2 ]

          ZPlaneIntersectionPointI = self. AnchorPoint . Translate ( self. Scale ( ScalingFactor ) )

          return ZPlaneIntersectionPointI

#####################################################################################################################################################

      def Print ( self ):

          print self

#####################################################################################################################################################

      def Scale ( self, ScalingFactor ):

          """
          Scales a Vector by Scaling Factor
          """          

          return [ Coord * ScalingFactor for Coord in self ]  

#####################################################################################################################################################

      def Length ( self ):

          """
          returns Length of the vector
          """

          LengthSq = 0.0;

          for N in range ( len ( self ) ): LengthSq += self [ N ]**2

          return sqrt ( LengthSq )  

#####################################################################################################################################################

      def AngleToAxis ( self, Axis, Unit = 'DEG', AccountForAngleDirection = 'No' ):

          """
          returns Angle between Vector and input Axis
          """

          VectorProduct = SetOfVectors ( [ self, Axis ] ).VectorProduct ( )

          VectorProductLength = Vector ( VectorProduct ).Length ( ) 

          SinAngle = VectorProduct [ 2 ] / ( self.Length ( ) * 1 )   # 1 being X Axis unit vector length
# beceause vector is in form 0,0, X
# trzeva uwazac bo dlugosc tez powinna byc w 3D 
# trudno te cwiartki sprawdzac teraz ...

          if self [ 0 ] >= 0.0: # testuje dla roznych cwiartek

             Angle = asin ( SinAngle )

          elif self [ 0  ] <= 0.0:

               Angle = (math.pi/2) + ( ( math.pi/2 ) - asin ( SinAngle ) )

          if Unit == 'DEG':

             return SetOfVectors ( [ self, Axis ] ). AngleDEG ( )

          if Unit == 'RAD':

             return SetOfVectors ( [ self, Axis ] ). Angle ( AccountForAngleDirection )

#####################################################################################################################################################

      def AngleToXAxis ( self ):

          """
          returns Angle to X Axis
          """

          XAxis = Vector ( [ 1.0, 0.0, 0.0 ] )

          return self. AngleToAxis ( XAxis, Unit = 'RAD', AccountForAngleDirection = 'Yes' )

#####################################################################################################################################################

      def AngleToZAxis ( self ):

          """
          returns Angle to X Axis
          """

          ZAxis = Vector ( [ 0.0, 0.0, 1.0 ] )

          return self. AngleToAxis ( ZAxis )

#####################################################################################################################################################

      def SmallestAngleToZAxis ( self ):

          ZAxis = [ 0.0, 0.0, 1.0 ]

          VectorProduct = SetOfVectors ( [ ZAxis, self ] ).VectorProduct ( )



          VectorProductLength = Vector ( VectorProduct ).Length ( ) 

          print self
          print VectorProduct
          print self.Length ( )
          print 

          SinAngle = VectorProductLength / ( self.Length ( ) * 1.0 )   # 1 being Z Axis unit vector length
# beceause vector is in form 0,0, Z
# trzeva uwazac bo dlugosc tez powinna byc w 3D 

#          if self [ 2 ] >= 0.0: # teraz sprawdzanie cwiartki :)

#          print SinAngle

          Angle = asin ( SinAngle )

#          elif self [ 2  ] <= 0.0:

#               Angle = (math.pi/2) + ( ( math.pi/2 ) - asin ( SinAngle ) )


#           if Angle >= (np.pi/2.0):
#              Angle = 

          return ( Angle/(2*np.pi) ) * 360

#####################################################################################################################################################
#####################################################################################################################################################
#

class Point ( list ): # cartesian Point as default but we can convert to 

      """
      stores an N dimensional Point 
      """

      # could be merged with vector in the future

#####################################################################################################################################################

      def Copy ( self ):

          return CopyI

#####################################################################################################################################################

      def CartesianToSpherical ( self ):

          X, Y, Z = self

          R = sqrt  ( X**2 + Y**2 + Z**2 )

          if R == 0.0: Theta = 0.0

          else: Theta = acos ( Z/R ) * ( 180 / math.pi )

          if X == 0.0: fi = 0.0
         
          else: fi = atan ( Y/X ) * ( 180 / math.pi )

          return Point ( [ R, Theta, fi ] )

#####################################################################################################################################################

      def Rotate ( self, RotationMatrix  ):

# ok, tu jest problem, musze ustalic gdzie

          """
          returns Point rotated by a Rotation Matrix
          """

          # could be changed so that the point is altered by the rotation ( with no returning)
# poczytac w wikipedii, potem uogolnic

          Point1 = [ ]
          print self
          print RotationMatrix

          for I in range (  len ( self ) ):
              Coord = 0.0

              for J in range ( len ( self ) ):

                  Coord += RotationMatrix [I][J] * self [J]
              Point1. append ( Coord )

          return Point1

#####################################################################################################################################################

      def Print ( self ):

          """
          prints Point
          """

          print self

#####################################################################################################################################################

      def Translate ( self, Vector ):

          """
          Translates point by Vector
          """

          for N in range ( len ( self ) ):
              
              self [ N ] += Vector [ N ]

# this does not return anything, the Point is altered by Translation
#####################################################################################################################################################

      def RotateByAngle ( self, Angle ): # in 2D in XY plane

          """
          juz rozumiem jest problem ze zwrotem
          returns Point rotated By Angle ( in 2D)
          """

          if len ( self ) == 2:

             RotationMatrix = Generate2DRotationMatrix ( Angle )


          elif len ( self ) == 3:

             RotationMatrix = Generate3DRotationMatrix ( Angle )
          
          Point1 = self.Rotate ( RotationMatrix )

          return Point1

#####################################################################################################################################################
#####################################################################################################################################################

class SetOfPoints ( list ):

      """
      stores Set of N Kdimensional points
      """

#####################################################################################################################################################

      def __init__ ( self, InputPoints ):

          self. Content = [ InputPoint for InputPoint in InputPoints ] 

#####################################################################################################################################################

      def RotateByAngle ( self, Angle ):

          [ PointI. RotateByAngle ( Angle ) for PointI in self. Content ]

#####################################################################################################################################################

      def CartesianToSpherical ( self ):

          return SetOfPoints ( [ PointI. CartesianToSpherical ( ) for PointI in self. Content ] )

#####################################################################################################################################################

      def SuperimposeOnTemplate ( self, Template ):

          """
          alters the SetOfPoints so it is superimposed on another another SetOfPoints ( template )
          """

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

      def Superimpose3On2Template ( self, Template ):
# przygotowanie

          TemplateGeometricalCenter = Template. Center ( ) # jest ok
          SelfGeometricalCenter = FirstTwoOfSelf. Center ( )

# trzy kroki
# 1szy krok

          self. Translate ( [ -Coord for Coord in SelfGeometricalCenter ]  )
          Template. MoveToOrigin ()

# 2gi krok

          self. Rotate3On2Template ( Template )

# 3ci krok

          self. Translate ( TemplateGeometricalCenter )
          Template. Translate ( TemplateGeometricalCenter )

          return

#####################################################################################################################################################
# moze bedzie trzeba to przedefiniowac ale nie uprzedzajmy faktow

      def Rotate3On2Template ( ):

          FirstTwoOfSelf = SetOfPoints ( self. Content [:1] )
          RotationMatrix = SetsOfPoints ( FirstTwoOfSelf, Template )

# moglbym tez uogolnic metode rotacji
          self. Rotate ( RotationMatrix )
          
          return

#####################################################################################################################################################

      def MorphIntoTemplateTwoFirstFixed ( self, Template ):

# wybieramy 2 pierwsze helisy
          TwoFirstSelf =  SetOfPoints ( self. Content [ :1 ] )
          TwoFirstTemplate = SetOfPoints ( Template. Content [ :1 ] )

# musimy nalozyc 2 pierwsze helisy na 2 pierwsze helisy wzorca
          TwoFirstSelf. SuperimposeOnTemplate ( TwoFirstTemplate )

# aaa fuck, musze nalozyc 3 helisy na dwie pierwsze wzorca

          LastSelf = SetOfPoints ( self. Content [ 2 ] )
          LastTemplate = SetOfPoints ( Template. Content [ 2 ] )

          LastSelf. SuperimposeOnTemplate ( LastTemplate )
          
#####################################################################################################################################################

      def Print ( self ):

          """
          prints the Set Of points
          """

          [ PointInstance. Print ( ) for PointInstance in self. Content ]

#####################################################################################################################################################

      def Vector ( self ):

          """
          returns Vector pointing from 0th point to 1st Point
          """

          self.Vector = [ ]

          for N in range ( len ( self. Content [0] ) ):

              self.Vector. append ( self. Content [1][N] - self. Content [0][N] )  

          return Vector ( self.Vector )

#####################################################################################################################################################

      def Distance ( self ):

          return self.Vector ( ). Length ()

#####################################################################################################################################################

      def PCAAxis ( self ):

          """
          returns Axis through SetOfPoints determined by PCA
          """

          data = np.array( self. Content )
#          print self. Content; quit ()
          datamean=data.mean(axis=0)
          uu, dd, vv = np.linalg.svd(data - datamean)
          PCAAxisI = vv[0]

          return Vector ( PCAAxisI )

#####################################################################################################################################################
# ok, to teraz to tez powinienem dac do outputu reprezentacji

      def DistanceToPCAAxis ( self, Axis =[] ):

          """
          returns distance to Axis through SetOfPoints determined by PCA
          """

          if Axis != []:

             PCAAxisI = Axis

          else:

             data = np.array( self. Content )
  #          print self. Content; quit ()
             datamean=data.mean(axis=0)
             uu, dd, vv = np.linalg.svd(data - datamean)
             PCAAxisI = vv[0]

          MC = self. Center ()

          a = PCAAxisI [2]/ PCAAxisI[0]
          b = PCAAxisI [2]/ PCAAxisI[1] 

          c = MC[2] - (a * MC[0]) - (b * MC[1])

          SumDsq = 0.0

          for P in self. Content:

              Dsq = ( (a*P[0]) + (b*P[1]) + c - P[2] )**2 / (a**2 + b**2) #nie jestem pewien czy to jest poprawne

              SumDsq += Dsq

          return sqrt ( SumDsq ) 

#####################################################################################################################################################

      def Center ( self ):

          """
          returns Geometrical center for SetOf(3D)Points
          """
#          print len ( self.Content )

#          quit ()

          self. SumX, self. SumY, self. SumZ  = [ 0.0, 0.0, 0.0 ]


          for PointInstance in self.Content:

              self.SumX += PointInstance [0]
              self.SumY += PointInstance [1]
              self.SumZ += PointInstance [2]

          No = float ( len ( self.Content ) )

          return [ self.SumX/No, self.SumY/No, self.SumZ/No ] 

#####################################################################################################################################################

      def Translate ( self, Vector ): #bedzie czeba to przebudowac

          """
          Translates each Point
          """

          [ Point. Translate ( Vector ) for Point in self. Content ]            

#####################################################################################################################################################

      def TranslateToOrigin ( self ): # moze tu jest blad

          """
          Translates SetOfPoints so that Geometrical Center is now in [ 0.0, 0.0, 0.0 ]
          """

          VectorI = self.Center ( )
          
          return self. Translate ( [-VectorI[0],-VectorI[1],-VectorI[2] ] )

#####################################################################################################################################################

      def RotateByMatrix ( self, RotationMatrix ):

          """
          rotates each Point by input Rotation Matrix
          """

          [ PointInstance. Rotate ( RotationMatrix ) for PointInstance in self. Content ]

#####################################################################################################################################################

      def Array (self):

          """
          returns SetOfPoints as an Array
          """

          ciag1 = [ ]

          for i in range ( len (self.Content ) ):

              for j in range ( len(self.Content[0]) ):

                  el1 = [ float (c) for c in self.Content[i] ]

                  ciag1. append ( el1 ); # moze bede mogl to zmienic

          return np.array(ciag1)

# teraz musze ta transformacje do main axis zaprogramowac # narysuje to sobie
#####################################################################################################################################################
#####################################################################################################################################################

class HierarchicalSetOfPoints ( list ):

      """
      stores some SetsOfPoints
      """

#####################################################################################################################################################

      def __init__ ( self, InputSetsOfPoints ):

          self. Content = [ InputSetOfPoints for InputSetOfPoints in InputSetsOfPoints ]

#####################################################################################################################################################

      def RotateByMatrix ( self, RotationMatrix ):

          """
          rotates SetsOfPoints By Matrix
          """

          [ SetOfPointsInstance. RotateByMatrix ( RotationMatrix ) for SetOfPointsInstance in self. Content ]

#####################################################################################################################################################

      def Translate ( self, VectorInstance ):

          """
          Translates each SetOfPoint by Vector
          """

          [ SetOfPointsInstance. Translate ( VectorInstance ) for SetOfPointsInstance in self. Content ]

#####################################################################################################################################################

      def CartesianToISC_IC ( self ): #tu musimy przyjac kilka zalozen mamy 6 punktow [ 3 x 2 ]
# pytanie brzmi czy dobrze to robie..., ktory jest 0, a ktory jest 1, jutro musimy sprawdzic w nsecie
# skomentuje ten kod
          Kopia = copy.deepcopy ( self )

          print 'Outputting ISCs'

#          print self.Content[0]
#          print self.Content[0].Content[0]
#          print Kopia.Content[0]
#          print Kopia.Content[0].Content[0]          

          Wektor = SetOfPoints ([ Kopia. Content[0]. Content[0], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia. Translate ( Wektor ); #Move to [0,0,0]

          Kat = SetOfVectors([ SetOfPoints( [ Kopia. Content[0]. Content[0], Kopia. Content[1]. Content[0] ]).Vector(), Vector([1.0,0.0,0.0])  ]). Angle ( )
#mozliwe ze jest zbyt skomplikowane
          Kopia. RotateByAngle ( -Kat )# orient H1H2 to X Axis

          R1 = Kopia. Content[1]. Content[0]. CartesianToSpherical ( ) [0]
          R2, Theta, Fi = Kopia. Content[2]. Content[0]. CartesianToSpherical ( )

          R, Theta1, Fi1 = Kopia. Content[0]. Content[1]. CartesianToSpherical ( )

          Kopia2 = copy. deepcopy ( Kopia. Content[1] )

          Wektor2 = SetOfPoints( [Kopia2. Content [ 0 ], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia2. Translate ( Wektor2 )

          R, Theta2, Fi2 = Kopia2. CartesianToSpherical ( ). Content [1]

          Kopia3 = copy.deepcopy ( Kopia. Content[2] )

          Wektor3 = SetOfPoints( [Kopia3. Content [ 0 ], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia3. Translate ( Wektor3 )

          R, Theta3, Fi3 = Kopia3. CartesianToSpherical ( ). Content [1]

# w IDE trzeba to robic
          
#jak sie definiuje operatory w pythonie? np. -> (oznaczalby wektor, to by uproscilo wiele spraw, wprowadzenie nowych operatorow)
# np. Kopia2 -> [0,0,0] i tyle
# MoveTo maybe?

          return [ R1, R2, Fi, Theta1, Fi1, Theta2, Fi2, Theta3, Fi3 ]

#####################################################################################################################################################
#####################################################################################################################################################

      def CartesianToISC_EC ( self ): #tu musimy przyjac kilka zalozen mamy 6 punktow [ 3 x 2 ]
# pytanie brzmi czy dobrze to robie..., ktory jest 0, a ktory jest 1, jutro musimy sprawdzic w nsecie
# skomentuje ten kod
          Kopia = copy.deepcopy ( self )

          print 'Outputting ISCs'

#          print self.Content[0]
#          print self.Content[0].Content[0]
#          print Kopia.Content[0]
#          print Kopia.Content[0].Content[0]          

          Wektor = SetOfPoints ([ Kopia. Content[0]. Content[1], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia. Translate ( Wektor ); #Move to [0,0,0]

          Kat = SetOfVectors([ SetOfPoints( [ Kopia. Content[0]. Content[1], Kopia. Content[1]. Content[1] ]).Vector(), Vector([1.0,0.0,0.0])  ]). Angle ( )
#mozliwe ze jest zbyt skomplikowane
          Kopia. RotateByAngle ( -Kat )# orient H1H2 to X Axis

          R1 = Kopia. Content[1]. Content[1]. CartesianToSpherical ( ) [0]
          R2, Theta, Fi = Kopia. Content[2]. Content[1]. CartesianToSpherical ( )

          R, Theta1, Fi1 = Kopia. Content[0]. Content[2]. CartesianToSpherical ( )

          Kopia2 = copy. deepcopy ( Kopia. Content[1] )

          Wektor2 = SetOfPoints( [Kopia2. Content [ 1 ], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia2. Translate ( Wektor2 )

          R, Theta2, Fi2 = Kopia2. CartesianToSpherical ( ). Content [2]

          Kopia3 = copy.deepcopy ( Kopia. Content[2] )

          Wektor3 = SetOfPoints( [Kopia3. Content [ 1 ], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia3. Translate ( Wektor3 )

          R, Theta3, Fi3 = Kopia3. CartesianToSpherical ( ). Content [2]
          
#jak sie definiuje operatory w pythonie? np. -> (oznaczalby wektor, to by uproscilo wiele spraw, wprowadzenie nowych operatorow)
# np. Kopia2 -> [0,0,0] i tyle
# MoveTo maybe?

          return [ R1, R2, Fi, Theta1, Fi1, Theta2, Fi2, Theta3, Fi3 ]

#####################################################################################################################################################
#####################################################################################################################################################

      def CartesianToISC ( self ): #tu musimy przyjac kilka zalozen mamy 6 punktow [ 3 x 2 ]
# pytanie brzmi czy dobrze to robie..., ktory jest 0, a ktory jest 1, jutro musimy sprawdzic w nsecie
# skomentuje ten kod
          Kopia = copy.deepcopy ( self ) #czy to dziala? nie wiem

          print 'Outputting ISCs'

#          print self.Content[0]
#          print self.Content[0].Content[0]
#          print Kopia.Content[0]
#          print Kopia.Content[0].Content[0]  

#skomentowac kod, ewentualnie rozbic na dwie funkcje        
          H1 = Kopia. Content[0]
          H2 = Kopia. Content[1] # moze jutro, mam teze do napisania, kuzwa ..

          Wektor = SetOfPoints ([H1. Content[0], [0.0, 0.0, 0.0 ]]). Vector ( )

#          Kopia. Content [1]. Print (); quit ()
#          Kopia. Content [1]. Content [0]; quit ();

          Kopia. Translate ( Wektor ); #Move to [0,0,0]

          Kat = SetOfVectors([ SetOfPoints( [ H1. Content[0], H2. Content[0] ]).Vector(), Vector([1.0,0.0,0.0])  ] ). Angle ( )
#mozliwe ze jest zbyt skomplikowane
          Kopia. RotateByAngle ( -Kat )# orient H1H2 to X Axis

#####################################
# musze to rozbic


          H3 = Kopia. Content[2]



          R1            = H2. Content[0]. CartesianToSpherical ( ) [0]
          R2, Theta, Fi = H3. Content[0]. CartesianToSpherical ( )

          print Kopia. Content[0]; Kopia. Content[0]. Content[-1]; # quit ()

          R, Theta1, Fi1 = H1. Content[-1]. CartesianToSpherical ( )

          Kopia2 = copy. deepcopy ( H2 )

          Wektor2 = SetOfPoints( [Kopia2. Content [ 0 ], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia2. Translate ( Wektor2 )

          R, Theta2, Fi2 = Kopia2. CartesianToSpherical ( ). Content [-1] #co to i dlaczego takie?

          Kopia3 = copy.deepcopy ( H3 )

          Wektor3 = SetOfPoints( [Kopia3. Content [0], [0.0, 0.0, 0.0 ]]). Vector ( )

          Kopia3. Translate ( Wektor3 )

          R, Theta3, Fi3 = Kopia3. CartesianToSpherical ( ). Content [-1]
          
#jak sie definiuje operatory w pythonie? np. -> (oznaczalby wektor, to by uproscilo wiele spraw, wprowadzenie nowych operatorow)
# np. Kopia2 -> [0,0,0] i tyle
# MoveTo maybe?

          return [ R1, R2, Fi, Theta1, Fi1, Theta2, Fi2, Theta3, Fi3 ]

#####################################################################################################################################################


      def RotateByAngle ( self, Angle ):

          [ SetOfPointsI. RotateByAngle ( Angle ) for SetOfPointsI in self. Content ]

#####################################################################################################################################################

      def NonHierarchicalSetOfPoints ( self ):

          """
          joins SetsOfPoints into one SetOfPoint
          """

#          print 'printing self'
#          self. Print ( )
#          print 'done printing self'

          self.NonHierarchicalSetOfPointsInstance = []

          for SetOfPointsInstance in self.Content:

              for PointInstance in SetOfPointsInstance. Content:
#                  print PointInstance

                  self.NonHierarchicalSetOfPointsInstance. append ( PointInstance )
#          print 'printing NonHierarchicalSetOfPointsInstance'
#          print NonHierarchicalSetOfPointsInstance
#          print 'done printing NonHierarchicalSetOfPointsInstance'

          return SetOfPoints ( self. NonHierarchicalSetOfPointsInstance )
# zeby znalezc blad nalezy testowac proste operacje
#####################################################################################################################################################

      def Print ( self ):
          """
          prints set Of Points
          """

          # print method could be more generic

          [ SetOfPointsInstance. Print ( ) for SetOfPointsInstance in self. Content ] 

#####################################################################################################################################################

      def Center ( self ):

          """
          returns GeometricalCenter for SetsOfPoints
          """

          return self. NonHierarchicalSetOfPoints ( ). Center ( )    

#####################################################################################################################################################
#####################################################################################################################################################

class SetOfHierarchicalSetsOfPoints ( list ):

      """
      stores N SetsOfPoints
      """

#####################################################################################################################################################

      def __init__ ( self, InputHierarchicalSetsOfPoints ):

          self. Content = [ InputHierarchicalSetOfPoints for InputHierarchicalSetOfPoints in InputHierarchicalSetsOfPoints ]

#####################################################################################################################################################

      def SuperpositionMatrix ( self, AllowPerturbations = False, AllowFlip = False ):

          """
          returns rotation matrix from 0th HierSetOfPoints to 1stHierSetOfPoints
          """

          HierarchicalSetOfPointsInstance1, HierarchicalSetOfPointsInstance2  = self. Content

          NonHierarchicalSetOfPointsInstance1 = [ ]

          for SetOfPointsInstance in self. Content [0]:

              NonHierarchicalSetOfPointsInstance1. append ( SetOfPointsInstance )

# pierwszy set jest gotowy

          if AllowPerturbations:

             RMSDs = [ ]; Matrices = [ ];

             minRMSD = 1000.0

             for Perturbation in Perturbations( len ( self. Content[1] ) ):

                 PerturbationInstance = [ self. Content [ 1 ] [i] for i in Perturbation ]

                 NonHierarchicalSetOfPointsInstance2 = [ ]

                 for SetOfPointsInstance in PerturbationInstance:

                     NonHierarchicalSetOfPointsInstance2. append ( SetOfPointsInstance )
             
                 Matrices. append ( optimal_superposition ( np.array(ciag1), np.array(ciag2) ).T )
                 RMSDs. append ( rmsd (np.array(ciag1), np.array(ciag2))  )

                 if AllowFlip:

                    ciag2 = []

                    for i in range ( len (self[0] ) ):

                        for j in range ( len(self[0][0])-1,-1,-1 ):

                            el2 = [ float (c) for c in Centres1Perturbation [i][j] ]

                            ciag2. append ( el2 );
             
                    Matrices. append ( optimal_superposition ( np.array(ciag1), np.array(ciag2) ).T )
                    RMSDs. append ( rmsd (np.array(ciag1), np.array(ciag2))  )

             minRMSD = min ( RMSDs ); 

             return Matrices [ RMSDs. index ( minRMSD) ]


          else:

             ciag2 = [ ]

             for i in range ( len (self[0] ) ):

                 for j in range ( len(self[0][0]) ):

                     el2 = [ float (c) for c in self[1][i][j] ]

                     ciag2. append ( el2 );

          return optimal_superposition( np.array(ciag1), np.array(ciag2) ).T # ok a wiec gdzie jest translacja do zera?
          

#####################################################################################################################################################
#####################################################################################################################################################

class SetsOfPoints ( list ):

      """
      contains N sets of points
      """

#####################################################################################################################################################
# no i gdzie mialem te listy z flip RMSD itd

      def RMSD ( self ):

          """
          returns RMSD between two sets of points
          """
        
#          print len ( self [0]), powinna byc jakas obrona prze kreacja emptiseta
#          quit ()

          ciag1 = []; ciag2 = []

          for i in range ( len (self[0] ) ):

              for j in range ( len(self[0][0]) ):

                  el1 = [ float (c) for c in self[0][i][j] ]
                  el2 = [ float (c) for c in self[1][i][j] ]

                  ciag1. append ( el1 ); ciag2. append ( el2 );

          ciag1C = SetOfPoints ( ciag1 ). TranslateToOrigin (). Array ( ); # tu jest blad
          ciag2C = SetOfPoints ( ciag2 ). TranslateToOrigin ( ). Array ( ); # to jest template!
          
#          print rmsd (np.array(ciag1), np.array(ciag2))
          return  rmsd (np.array(ciag1C), np.array(ciag2C)) # to bedzie z match.py

#####################################################################################################################################################

      def SuperpositionMatrix ( self, AllowPerturbations = False, AllowFlip = False ):

          """
          returns rotation from 0th SetOfPoints on 1st SetOfPoints
          """

          print self[0][0]

          ciag1 = []

          for i in range ( len ( self [0] ) ):

              for j in range ( len ( self [0][0] ) ):

                  Punkt1 = [ float ( Coord ) for Coord in self[0][i][j] ]

                  ciag1. append ( Punkt1 )


# i powinien chodzic

# ciag 1 jest gotowy
# musze sie doksztalcic z pythona znowu

          if AllowPerturbations:

             RMSDs = [ ]; Matrices = [ ];

             minRMSD = 1000.0;

             Centres1 = self.Content[1]

             for Perturbation in Perturbations( len ( self.Content[1] ) ):

                 Centres1Perturbation = [ Centres1 [i] for i in Perturbation ]

                 ciag2 = [] 

                 for i in range ( len (self[0] ) ):

                     for j in range ( len(self[0][0]) ):

                         el2 = [ float (c) for c in Centres1Perturbation [i][j] ]

                         ciag2. append ( el2 );
             
                 Matrices. append ( optimal_superposition ( np.array(ciag1), np.array(ciag2) ).T )
                 RMSDs. append ( rmsd (np.array(ciag1), np.array(ciag2))  )

                 if AllowFlip:

                    ciag2 = []

                    for i in range ( len (self[0] ) ):

                        for j in range ( len(self[0][0])-1,-1,-1 ):

                            el2 = [ float (c) for c in Centres1Perturbation [i][j] ]

                            ciag2. append ( el2 );
             
                    Matrices. append ( optimal_superposition ( np.array(ciag1), np.array(ciag2) ).T )
                    RMSDs. append ( rmsd (np.array(ciag1), np.array(ciag2))  )

             minRMSD = min ( RMSDs ); 

             return Matrices [ RMSDs. index ( minRMSD) ]


          else:

             ciag2 = [ ]

             for i in range ( len (self[0] ) ):

                 for j in range ( len(self[0][0]) ):

                     el2 = [ float (c) for c in self[1][i][j] ]

                     ciag2. append ( el2 );

          return optimal_superposition( np.array(ciag1), np.array(ciag2) ).T # ok a wiec gdzie jest translacja do zera?

# wiec niekoniecznie jest to dobry sposob, musze zrobic riport ktory bedzie porownywal efekt alajnu z perturbacjami i bez, musze tez pomyslec o moim sposobie klasyfikacji :)
#####################################################################################################################################################
#####################################################################################################################################################

class HierarchicalSetsOfPoints ( list ):

      """
      contains N HierSetsOfPoints
      """

      def __init__ ( self, InputHierarchicalSetsOfPoints ):

          self. Content = [ InputHierarchicalSetOfPoints for InputHierarchicalSetOfPoints in InputHierarchicalSetsOfPoints ]

#####################################################################################################################################################

      def RMSD ( self, AllowPerturbations = False, AllowFlip = False ):
         
          """
          compute RMSD between 0th and 1st SetOfPoints
          """

          Array1 = self.Content[0]. NonHierarchicalSetOfPoints ( ). Array ( )

          if AllowPerturbations:

             RMSDs = [ ];

             minRMSD = 1000.0

             Centres1 = self. Content[1] # bo to przeciez ten drugi, blargh
# a wiec ten pierwszy powinien byc zrobiony juz tutaj

             for Perturbation in Perturbations( len ( self.Content [1] ) ):

                 Centres1Perturbation = [ Centres1 [i] for i in Perturbation ]

                 Array2 = Centres1Perturbation. NonHierarchicalSetOfPoints ( ). Array ( )

                 RMSDs. append ( rmsd (Array1, Array2)  )

                 if AllowFlip:

                    FlippedSet = [ Helix[::-1] for Helix in Centres1Perturbation ]
                    Array2 = FlippedSet. NonHierarchicalSetOfPoints ( ). Array ( )
             
                    RMSDs. append ( rmsd (Array1, Array2)  )

             minRMSD = min ( RMSDs ); 

          else:

             Array2 = self.Content[1]. NonHierarchicalSetOfPoints ( ). Array ( )

             return rmsd (Array1, Array2).T # ok a wiec gdzie jest translacja do zera?

# wiec niekoniecznie jest to dobry sposob, musze zrobic riport ktory bedzie porownywal efekt alajnu z perturbacjami i bez, musze tez pomyslec o moim sposobie klasyfikacji :)

#####################################################################################################################################################

      def SuperpositionMatrix ( self, AllowPerturbations = False, AllowFlip = False ):

          """
          returns rotation between 0th and 1st HierSetOfPoints
          """

          Array1 = self.Content[0]. NonHierarchicalSetOfPoints ( ). Array ( )

          if AllowPerturbations:

             RMSDs = [ ]; Matrices = [ ];


             minRMSD = 1000.0

             Centres1 = self. Content[1] # bo to przeciez ten drugi, blargh
# a wiec ten pierwszy powinien byc zrobiony juz tutaj


             for Perturbation in Perturbations( len ( self.Content [1] ) ):

                 Centres1Perturbation = [ Centres1 [i] for i in Perturbation ]

                 Array2 = Centres1Perturbation. NonHierarchicalSetOfPoints ( ). Array ( )
             
                 Matrices. append ( optimal_superposition ( Array1, Array2 ).T )
                 RMSDs. append ( rmsd (Array1, Array2)  )

                 if AllowFlip:

                    FlippedSet = [ Helix[::-1] for Helix in Centres1Perturbation ]
                    Array2 = FlippedSet. NonHierarchicalSetOfPoints ( ). Array ( )
             
                    Matrices. append ( optimal_superposition ( Array1, Array2 ).T )
                    RMSDs. append ( rmsd (Array1, Array2)  )

             minRMSD = min ( RMSDs ); 

             return Matrices [ RMSDs. index ( minRMSD) ]


          else:

             Array2 = self.Content[1]. NonHierarchicalSetOfPoints ( ). Array ( )

             return optimal_superposition( Array1, Array2 ).T # ok a wiec gdzie jest translacja do zera?

# wiec niekoniecznie jest to dobry sposob, musze zrobic riport ktory bedzie porownywal efekt alajnu z perturbacjami i bez, musze tez pomyslec o moim sposobie klasyfikacji :)

#####################################################################################################################################################
#####################################################################################################################################################

# oprocz tego skonczyc perceptron, 3)
# movielensy, 4)
# grup riport 2)
# publikacja 1)

class ISCPoint ( ):

      def DummyMethod ( ):

          return

#####################################################################################################################################################
#####################################################################################################################################################

class SetOfISCPoints ( ):

      def DummyMethod ( ):

          return

#####################################################################################################################################################
#####################################################################################################################################################
# ok, damy sobie rade i z tym .., moze byc RMSE z cartesian kabsch
class HierarchicalSetOfISCPoints ( ):

      def DummyMethod ( ):

          return

#####################################################################################################################################################
#####################################################################################################################################################

class SetOfSetsOfISCPoints ( ):

      def RMSD ( ): # from formula for RMSE :)

          return

#####################################################################################################################################################
#####################################################################################################################################################

class SetOfHierarchicalSetsOfISCPoints ( ):

      def RMSD ( ):

          return
