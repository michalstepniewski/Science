def RozbiciaNaDwa ( Set, N ): # dwa sety # tylko ze nie moze byc N musi byc Set

    import itertools; from itertools import combinations

#    Set = range ( K ); 

    CombinationsI = [ ]; Rozbicia = [ ]; Combination = [ ]

    for combination in combinations ( Set, N ):

        Combination = [ ]
        for Element in combination: Combination. append ( Element )        

        Reszta = [ ]

        for Item in Set:

            if Item not in Combination:

               Reszta. append ( Item )

        Rozbicie = [ Combination, Reszta ]


        Rozbicia. append ( Rozbicie )

    return Rozbicia

#####################################################################################################################################################

def RozbiciaNaDwaZNakladaniem ( Set, N, Nakladanie ): # dwa sety # tylko ze nie moze byc N musi byc Set

    import itertools; from itertools import combinations

#    Set = range ( K ); 

    CombinationsI = [ ]; Rozbicia = [ ]; Combination = [ ]

    for combination in combinations ( Set, N ):

        Combination = [ ]

        for Element in combination: Combination. append ( Element )

        for niewreszcie in combinations ( Combination, ( N - Nakladanie  )  ): 

            NieWReszcie = [ ]

            for Element in niewreszcie: NieWReszcie. append ( Element )

            Reszta = [ ]

            for Item in Set:

               if Item not in NieWReszcie:

                  Reszta. append ( Item )

            Rozbicie = [ Combination, Reszta ]


            Rozbicia. append ( Rozbicie )

    return Rozbicia

#####################################################################################################################################################

def Rozbicia( Zbior, Rzedy):

    NoweRozbicia = [ ]

    if Rzedy == []:
        return [ [ [], Zbior ] ] # najpierw jest reszta a potem jest zbior
    else:

        for Rozbicie in Rozbicia (Zbior, Rzedy [1:] ): # rozbicia nizszego poziomu ze zbiorem i reszta
#            print Rozbicie

            for RozbicieNaDwaI in RozbiciaNaDwa ( Rozbicie[-1], Rzedy [0] ): # rozbijamy Zbior jest w jedynce
#                print RozbicieNaDwaI 

#                NoweRozbicie = RozbicieNaDwaI [ 0 ] # tym razem rozbicie na trzy
#                print NoweRozbicie # to co juz rozbite
                NoweRozbicie = [ ]

                for Element in Rozbicie [ :-1 ]:
                    NoweRozbicie.append ( Element)
                
                NoweRozbicie.append ( RozbicieNaDwaI [ 0 ] )
                NoweRozbicie.append ( RozbicieNaDwaI [ 1 ] )
#                    NoweRozbicie. append ( Element )
                NoweRozbicia. append ( NoweRozbicie )
        return NoweRozbicia

#####################################################################################################################################################


def RozbiciaZNakladaniem ( Zbior, Rzedy, Nakladanie ):

    NoweRozbicia = [ ]

    if Rzedy == []: # problem polega chyba w ostatnim zbiorze
        return [ [ [], Zbior ] ] # najpierw jest reszta a potem jest zbior
    else:

        for Rozbicie in RozbiciaZNakladaniem (Zbior, Rzedy [1:], Nakladanie ): # rozbicia nizszego poziomu ze zbiorem i reszta
#            print Rozbicie

            for RozbicieNaDwaI in RozbiciaNaDwaZNakladaniem ( Rozbicie[-1], Rzedy [0], Nakladanie ): # rozbijamy Zbior jest w jedynce
#                print RozbicieNaDwaI 

#                NoweRozbicie = RozbicieNaDwaI [ 0 ] # tym razem rozbicie na trzy
#                print NoweRozbicie # to co juz rozbite
                NoweRozbicie = [ ]

                for Element in Rozbicie [ :-1 ]:
                    NoweRozbicie.append ( Element)
                
                NoweRozbicie.append ( RozbicieNaDwaI [ 0 ] )
                NoweRozbicie.append ( RozbicieNaDwaI [ 1 ] )
#                    NoweRozbicie. append ( Element )
                NoweRozbicia. append ( NoweRozbicie )
        return NoweRozbicia


#####################################################################################################################################################

def SformatowaneRozbicia ( Zbior, Rzedy):

    RozbiciaI = [ ]

    NiesformatowaneRozbicia = Rozbicia( Zbior, Rzedy)

    for RozbicieI in NiesformatowaneRozbicia:
        RozbiciaI. append ( RozbicieI[1:] )

    return RozbiciaI

Zbior = range ( 7 )

# print Rozbicia ( Zbior, [])

# print SformatowaneRozbicia ( Zbior, [3,2]) [ 0 ]

#####################################################################################################################################################

def SformatowaneRozbiciaZNakladaniem ( Zbior, Rzedy, Nakladanie):

    RozbiciaI = [ ]

    NiesformatowaneRozbiciaZNakladaniem = RozbiciaZNakladaniem( Zbior, Rzedy, Nakladanie)

    for RozbicieI in NiesformatowaneRozbiciaZNakladaniem:
        RozbiciaI. append ( RozbicieI[1:] )

    return RozbiciaI


#####################################################################################################################################################

# print Rozbicia( Zbior, [2, 2] )
# print RozbiciaNaDwa ( Zbior, 2 )
#    print RozbiciaNaDwa ( Zbior, 2 )

#####################################################################################################################################################
#################################################### Rozbicie Na Dwa Z Nakladaniem ##################################################################
# Rozbicie na Dwa z Nakladaniem jeden ze z Combination wybieramy N-1 elementow, ktore nie beda w Reszcie ############################################
#####################################################################################################################################################

Set = range ( 7 )
N   = 3
Nakladanie = 1

# print RozbiciaNaDwaZNakladaniem ( Set, N, Nakladanie )

Zbior = range ( 9 )
Rzedy = [ 2, 3, 2 ]
Nakladanie = 2

print SformatowaneRozbiciaZNakladaniem ( Zbior, Rzedy, Nakladanie ) [ 6 ]

###### wszystko dziala dla rozbicia tylko dla pierwszego rozbicia na dwa, potem nie ma nakladania, musze przesledzic co sie dzieje ##################


