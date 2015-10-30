import sys, math
from math import *


###################################################

def Generate2DRotationMatrix ( Angle ): # angle counter-clockwise

    RotationMatrix2D = [ [ cos ( Angle ), - sin ( Angle ) ], \
                         [ sin ( Angle ),   cos ( Angle ) ] ]

#    print RotationMatrix2D

    return RotationMatrix2D

# orientation One Absolute Descriptor ( N ter, ) two Relative Ones (two other helices
# ok a jak wyglada w 3d?

###################################################

def Generate3DRotationMatrix ( Angle ): # angle counter-clockwise

    RotationMatrix3D = [ [ cos ( Angle ), - sin ( Angle ), 0.0 ], \
                         [ sin ( Angle ),   cos ( Angle ), 0.0 ], \
                         [ 0.0,             0.0,           1.0 ] ]

#    print RotationMatrix2D

    return RotationMatrix3D

# orientation One Absolute Descriptor ( N ter, ) two Relative Ones (two other helices
# ok a jak wyglada w 3d?


###################################################

def BinarizeNat ( Nat ):

    if Nat == 0:
       return 0
    else: 
       return 1

#####################################################

 



