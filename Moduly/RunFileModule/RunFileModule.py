import sys

SoftwarePath = '/home/soutys/Science/Software'

sys.path.append (SoftwarePath+'/Moduly/BasicIO')
from BasicIOModule import ReadLines
#####################################################################################################################################################


def ReadRunFile ( RunFilePath ):

    FileContents = ReadLines ( RunFilePath )

# read tasks from Run File

    TasksToRunI = [ ]

    for Line in FileContents:

     if Line[0] != '#':

       TasksToRunI. append ( Line.strip () ) 

#       TasksToRunI = [ Line.strip() for Line in FileContents ]
#    print TasksToRunI

    return TasksToRunI

