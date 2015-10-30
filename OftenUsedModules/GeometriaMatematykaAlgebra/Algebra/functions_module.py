import sys, math
from math import *


#####################################################################################################################################################

def Generate2DRotationMatrix ( Angle ): # angle counter-clockwise

    """
    Generates a 2D rotation matrix around axis paralell to plane from Angle
    """

    RotationMatrix2D = [ [ cos ( Angle ), - sin ( Angle ) ], \
                         [ sin ( Angle ),   cos ( Angle ) ] ]

    return RotationMatrix2D

# orientation One Absolute Descriptor ( N ter, ) two Relative Ones (two other helices

#####################################################################################################################################################

def BinarizeNat ( Nat ):

    """
    returns: 1 if Nat >= 0
             0 if Nat == 0

    """

    if Nat == 0:
       return 0
    else: 
       return 1

#####################################################################################################################################################

def BinarizeMatrix ( Matrix ):

    """
    returns a Matrix of Binary numbers
    from Matrix of Natural numbers
    """

    BinarizedMatrix = [ ]

    for I in range ( len ( Matrix ) ):

        BinarizedMatrixRow = [ ]

        for J in range ( len ( Matrix ) ):

            BinarizedMatrixRow. append ( BinarizeNat ( int(Matrix [I][J]) ) )

        BinarizedMatrix. append ( BinarizedMatrixRow )

    return BinarizedMatrix

#####################################################################################################################################################

