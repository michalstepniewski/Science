import sys

ChainName =' '


def AddChainNameLine ( Line, ChainName ):

    NewLine = Line[:21]+ChainName+Line[22:]

    return NewLine


def AddChainNameLines ( Lines ):

    NewLines = []
    NewChainName ='A'
    for Line in Lines:

        if Line[:4] == 'ATOM':

           ChainName = Line[21]

           if ChainName == ' ':

              NewLine = AddChainNameLine ( Line, NewChainName )

           else:

              NewLine = Line

           NewLines. append ( NewLine )


        else: NewLines. append ( Line )

    return NewLines

def AddChainNameFile ( InFilePath, OutFilePath ):

    InFile = open ( InFilePath, 'r' )

    InLines = InFile. readlines ()

    OutLines = AddChainNameLines ( InLines )

    OutFile = open ( OutFilePath, 'w' )

    for OutLine in OutLines:

        OutFile. write ( OutLine )

    OutFile. flush ()

    OutFile. close ()

    return

AddChainNameFile ( sys. argv[1], sys.argv[2] )
 
