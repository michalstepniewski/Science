def ReadLines ( FilePath ):

    """
    returns TextLines read from TextFile
    """

    OpenFile = open ( FilePath, 'r' )

    ReadLinesI = OpenFile. readlines ( )

    OpenFile. close ( )

    return ReadLinesI

############################# a moze lepiej by udekorowac ich readlinesa? #
