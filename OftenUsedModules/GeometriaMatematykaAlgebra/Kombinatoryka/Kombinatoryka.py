def Perturbations ( N ):

    """
    returns Perturbations of set of N consecutive numbers from 0 to N
    """
    
    if N==3:

       return [ [0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0] ]

    elif N==4:

       return [ [0,1,2,3], [0,1,3,2], [0,2,1,3], [0,2,3,1], [0,3,1,2], [0,3,2,1],\
                [1,0,2,3], [1,0,3,2], [1,2,0,3], [1,2,3,0], [1,3,0,2], [1,3,2,0],\
                [2,0,1,3], [2,0,3,1], [2,1,0,3], [2,1,3,0], [2,3,0,1], [2,3,1,0],\
                [3,0,1,2], [3,0,2,1], [3,1,0,2], [3,1,2,0], [3,2,0,1], [3,2,1,0]   ]

    elif N==5:

       return [ [0,1,2,3,4], [0,1,2,4,3], [0,1,3,2,4], [0,1,3,4,2], [0,1,4,2,3], [0,1,4,3,2],\
                [0,2,1,3,4], [0,2,1,4,3], [0,2,3,1,4], [0,2,3,4,1], [0,2,4,1,3], [0,2,4,3,1],\
                [0,3,1,2,4], [0,3,1,4,2], [0,3,2,1,4], [0,3,2,4,1], [0,3,4,1,2], [0,3,4,2,1],\
                [0,4,1,2,3], [0,4,1,3,2], [0,4,2,1,3], [0,4,2,3,1], [0,4,3,1,2], [0,4,3,2,1],\
                [1,0,2,3,4], [1,0,2,4,3], [1,0,3,2,4], [1,0,3,4,2], [1,0,4,2,3], [1,0,4,3,2],\
                [1,2,0,3,4], [1,2,0,4,3], [1,2,3,0,4], [1,2,3,4,0], [1,2,4,0,3], [1,2,4,3,0],\
                [1,3,0,2,4], [1,3,0,4,2], [1,3,2,0,4], [1,3,2,4,0], [1,3,4,0,2], [1,3,4,2,0],\
                [1,4,0,2,3], [1,4,0,3,2], [1,4,2,0,3], [1,4,2,3,0], [1,4,3,0,2], [1,4,3,2,0],\
                [2,0,1,3,4], [2,0,1,4,3], [2,0,3,1,4], [2,0,3,4,1], [2,0,4,1,3], [2,0,4,3,1],\
                [2,1,0,3,4], [2,1,0,4,3], [2,1,3,0,4], [2,1,3,4,0], [2,1,4,0,3], [2,1,4,3,0],\
                [2,3,0,1,4], [2,3,0,4,1], [2,3,1,0,4], [2,3,1,4,0], [2,3,4,0,1], [2,3,4,1,0],\
                [2,4,0,1,3], [2,4,0,3,1], [2,4,1,0,3], [2,4,1,3,0], [2,4,3,0,1], [2,4,3,1,0],\
                [3,0,1,2,4], [3,0,1,4,2], [3,0,2,1,4], [3,0,2,4,1], [3,0,4,1,2], [3,0,4,2,1],\
                [3,1,0,2,4], [3,1,0,4,2], [3,1,2,0,4], [3,1,2,4,0], [3,1,4,0,2], [3,1,4,2,0],\
                [3,2,0,1,4], [3,2,0,4,1], [3,2,1,0,4], [3,2,1,4,0], [3,2,4,0,1], [3,2,4,1,0],\
                [3,4,0,1,2], [3,4,0,2,1], [3,4,1,0,2], [3,4,1,2,0], [3,4,2,0,1], [3,4,2,1,0],\
                [4,0,1,2,3], [4,0,1,3,2], [4,0,2,1,3], [4,0,2,3,1], [4,0,3,1,2], [4,0,3,2,1],\
                [4,1,0,2,3], [4,1,0,3,2], [4,1,2,0,3], [4,1,2,3,0], [4,1,3,0,2], [4,1,3,2,0],\
                [4,2,0,1,3], [4,2,0,3,1], [4,2,1,0,3], [4,2,1,3,0], [4,2,3,0,1], [4,2,3,1,0],\
                [4,3,0,1,2], [4,3,0,2,1], [4,3,1,0,2], [4,3,1,2,0], [4,3,2,0,1], [4,3,2,1,0]    ]

# definicja Strakght or NotStraight graniczna wartosc pomiedzy glowna osia a polosie wkatach np :)
# crossing angles :)
# pora spac, blargh
#####################################################################################################################################################

def MozliwosciWyboruNzK ( N, K ):

    """
    returns all sets of N elements that can be selected from the set of K elements
    """

    import itertools; from itertools import combinations

    Set = range ( K )

    CombinationsI = [ ]

    for combination in combinations ( Set, N ):

        CombinationsI. append ( combination )

    return CombinationsI

# extract all subsets
# 1, 2, 3
# 1, 2, 4
# 1, 2, 5
# 1, 2, 6       

#####################################################################################################################################################

def ListaBezIndexu ( Lista, Index ):

    """
    """

    NowaLista = [ ]

    for N in range( len ( Lista) ):

        if N!= Index:

           NowaLista. append ( Lista [ N ] )

    return NowaLista

#####################################################################################################################################################

def ListaBezIndexow ( Lista, Indeksy ):

    NowaLista = [ ]

    for N in range( len ( Lista) ):

        if N not in Indeksy:

           NowaLista. append ( Lista [ N ] )

    return NowaLista 

#####################################################################################################################################################

def ListaZIndeksami ( Lista, Indeksy ):

    NowaLista = [ ]

    for N in range( len ( Lista) ):

        if N in Indeksy:

           NowaLista. append ( Lista [ N ] )

    return NowaLista 

#####################################################################################################################################################

def PodMatrycaZIndeksami ( Matryca, Indeksy ):

    NowaMatryca = [ ]

    for I in range ( len ( Matryca ) ):

        if I in Indeksy:

           NowaLiniaMatrycy = [ ]

           for J in range ( len ( Matryca [ I ] ) ):

               if J in Indeksy:

                  NowaLiniaMatrycy. append ( Matryca [ I ] [ J ] )

           NowaMatryca. append ( NowaLiniaMatrycy )

    return NowaMatryca

#####################################################################################################################################################

def TouchingNMinusOneSubmatrices ( Matrix ):

    TouchingNMinusOneSubmatricesI = [ ]

    for N in range ( len ( Matrix ) ):
        
        NMinusOneSubmatrixInstance = NMinusOneSubmatrix ( Matrix, MinusOneIndex = N )
        
        if Touching ( NMinusOneSubmatrixInstance ):

           TouchingNMinusOneSubmatricesI. append ( N ) # to jest sztuczka!

    return TouchingNMinusOneSubmatricesI

#####################################################################################################################################################

def NMinusOneSubmatrix ( Matrix, MinusOneIndex ):

    NMinusOneSubmatrixInstance = [ ]

    for I in range ( len ( Matrix ) ):

        if I != MinusOneIndex:

           NMinusOneSubmatrixInstanceRow = [ ]

           for J in range ( len ( Matrix [ I ] ) ):

               if J != MinusOneIndex:

                  NMinusOneSubmatrixInstanceRow. append ( Matrix [ I ] [ J ] )

           NMinusOneSubmatrixInstance. append ( NMinusOneSubmatrixInstanceRow )              

    return NMinusOneSubmatrixInstance

#####################################################################################################################################################

def Touching ( Matrix ):

    for N in range ( len ( Matrix ) ):

        if Matrix [N ].count(0) >= ( len ( Matrix )  ):
#           print 'False'; quit ()
           return False


    return True

#####################################################################################################################################################

def Closed ( Matrix ):

    for Row in Matrix:

        if Row. count (0) >= 2:
# 2 poniewaz sama z soba nie ma kontaktow, nie wiem dlaczego, ale taka umowa
           return False

    return True

#####################################################################################################################################################

def Consecutive ( ListOfIntegersInput ):

    ListOfIntegers = [ int ( Integer ) for Integer in ListOfIntegersInput ]

    for N in range (min ( ListOfIntegers ), max ( ListOfIntegers ) ):

        if N not in ListOfIntegers:

           return False

    return True

#####################################################################################################################################################

def GenerujCiagi ( Dlugosc ): # zawsze tak samo, nie jest to losowe

    Ciagi = [ '' ];

    for N in range ( Dlugosc ):
        WydluzoneCiagi = [ ];

        for Ciag in Ciagi:
            
            for Wartosc in [ '0' , '1' ]:

                WydluzonyCiag = Ciag + Wartosc
                WydluzoneCiagi. append ( WydluzonyCiag )

        Ciagi = [ ]

        for WydluzonyCiag in WydluzoneCiagi:

            Ciagi. append ( WydluzonyCiag )

#    print Ciagi
    return Ciagi

#####################################################################################################################################################

def GenerujPustaMatryce ( Rozmiar ):

    PustaMatryca = [ ]; PustaLinia = [ ];

    for I in range ( Rozmiar ):

        PustaLinia = [ ]

        for J in range ( Rozmiar ):

            PustaLinia. append ( '' )

        PustaMatryca. append ( PustaLinia )

    return PustaMatryca

#########

#####################################################################################################################################################

def GenerujMatryce ( Rozmiar, Ciag ):

#    print Ciag

    Matryca = GenerujPustaMatryce ( Rozmiar );

    for N in range ( Rozmiar ):

        Matryca [ N ] [ N ] = 1

    N = 0

    for I in range ( Rozmiar ):

        for J in range ( I+1, Rozmiar ):
#            print N

            Matryca [ I ] [ J ] = int(Ciag [ N ])
            Matryca [ J ] [ I ] = int(Ciag [ N ])

            N = N + 1
#    print Matryca
    return Matryca

##########################################################

#####################################################################################################################################################

def NumerowaneMozliweTypyMatryc ( Rozmiar ):

    NumerowaneMozliweTypyMatrycI = { }

    MozliweZestawyMatrycKontaktow = GenerujMozliweZestawyMatrycKontaktow ( Rozmiar )

    for N in range ( len ( MozliweZestawyMatrycKontaktow ) ):
        NumerowaneMozliweTypyMatrycI [ N ] = MozliweZestawyMatrycKontaktow [ N ]

    return NumerowaneMozliweTypyMatrycI

########################################################
#####################################################################################################################################################

def GenerujMozliweZestawyMatrycKontaktow ( Rozmiar ):

    ECs = GenerujMozliweMatryce ( Rozmiar )

    ZestawyMatryc = [ ]

    for EC in ECs:

        MMs = GenerujMozliweMatryce ( Rozmiar )

        for MM in MMs:

            ICs = GenerujMozliweMatryce ( Rozmiar )

            for IC in ICs:

                ZestawMatryc = [ EC, MM, IC ]

                ZestawyMatryc. append ( ZestawMatryc )

    return ZestawyMatryc     

##########################################################
#####################################################################################################################################################

def GenerujMozliweMatryce ( Rozmiar ):

    MozliweMatryce = [ ]

    Dlugosc = ( Rozmiar**2 - Rozmiar ) / 2

#    print Dlugosc

    Ciagi = GenerujCiagi ( Dlugosc )

    for Ciag in Ciagi:

        MozliweMatryce. append ( GenerujMatryce ( Rozmiar, Ciag ) )

    return MozliweMatryce

############################
#####################################################################################################################################################

def PoliczCzestoscMatryc ( ZbiorMatryc ):

    MatrycaICzestosc = { }

    MozliweMatryce = GenerujMozliweMatryce ( Rozmiar )

    for Matryca in ZbiorMatryc:

        if Matryca not in MatrycaICzestosc. keys ( ):

           MatrycaICzestosc [ Matryca ] = 1

        else:           

           MatrycaICzestosc [ Matryca ] += 1

    return MatrycaICzestosc

##################
#####################################################################################################################################################

def WykresCzestosciMatryc ( MatrycaICzestosc ):

# i tu jest wlasnie pytanie jak zaprojektowac ten wykres
# typ musi byc dany numerem N in range lista. keys ( )
#
# i musi byc legenda pod spodem, ktory typ oznacza jaka Matryce
# spojrzec w plotting tools

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.mlab as mlab

    fig = plt.figure()
    ax  = fig.add_subplot(111)

    ax.bar ( Ns, Czestosci  )

#    ax.hist(H2Xs,numBins,color='green',alpha=0.8) # musze poczytac wiecej

    plt.savefig(OutputFile ,dpi=100)


#    return
# moze powinienem popracowac teraz nad papierem

####################
# Wymiar = 1
#    1   
 
# Wymiar = 2
#
#     X1
#     1X
#
# Wymiar = 3
#
#
#  X12
#  1X3
#  23X
#
# Wymiar = 4
#
# X123 
# 1X45
# 24X6
# 356X
# Mozna wygenerowac pusta tablice

#####################################################################################################################################################
  
def GeneratePossibleContactPatternMatrices ( N ):

    VariableFields =  (N^2 -N)/2 
# wiec bedziemy przestawiac na kod dwojkowy 

    for I in range ( 2^VariableFields ):

# mozna by to rekurencyjnie
        
        for FieldValue in range ( 2 ): # a wiec zero lub jeden

            print 'Lala'
            
            

# Ciagi [ 1 ] = [ 0, 1 ]
# Ciagi [ 2 ] = [ 00, 01, 

# Ciagi [ N ]

# for Ciag in Ciagi [ N -1 ]:

#     for FieldValue in range ( 2 ):
#         Ciag = FieldValue +  

# przedluz 

# teraz powinienem zrobic te slajsy ktore henri chcial #

# oraz grubosc z slice'a vs liczba CA w slajsie

#############################################################33

