#import sys

def MartaExtraction (FilelistPath, ICFilePath, ECFilePath, MainFilePath):

    FilelistFile = open ( FilelistPath, 'r' )

    PathLines = FilelistFile. readlines ()

    PathLinesPure = [ Path.strip() for Path in PathLines ]

    FilelistFile. close ()

    ICLines = [ ]; ECLines = [ ]; MainLines = [ ]; ISCLines = [];

    for Path in PathLinesPure:

        ISCLines = [ ]

        InFile = open ( Path, 'r')

        InLines = InFile. readlines ()

        InFile. close ()

        for InLine in InLines:

            if InLine[:4] == '#ISC':

               ISCLines. append (InLine)

#    print ISCLines
#           Liczby = InLine[17:]. split ()


        print ISCLines[0].strip(); print ISCLines[1][16:].strip()
        ICLines.   append (Path + ' IC ' + ISCLines[0].strip() +' '+ ISCLines[1][16:].strip()+' '+ ISCLines[2][16:]) 
        ECLines.   append (Path + ' IC ' + ISCLines[3].strip() +' '+ ISCLines[4][16:].strip()+' '+ ISCLines[5][16:])
        MainLines. append (Path + ' IC ' + ISCLines[6].strip() +' '+ ISCLines[7][16:].strip() +' '+ ISCLines[8][16:])

    ICFile = open ( ICFilePath, 'w' )

    for Line in ICLines:

        ICFile. write (Line)

    ICFile. flush ()
    ICFile. close ()


    ECFile = open ( ECFilePath, 'w' )

    for Line in ECLines:

        ECFile. write (Line)

    ECFile. flush ()
    ECFile. close ()

    MainFile = open ( MainFilePath, 'w' )

    for Line in MainLines:

        MainFile. write (Line)

    MainFile. flush ()
    MainFile. close ()
