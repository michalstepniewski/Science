
# ok, teraz nalezy to przerobic na funkcje

def StackedHistogram ( ):

    import numpy as np
    import pylab as P

#
# The hist() function now has a lot more options
#

#
# first create a single histogram
#

    mu, sigma = 2, 25

# create a new data-set
    x = mu + sigma*P.randn(1000)

    y = mu + sigma*P.randn(1000)

    z = mu + sigma*P.randn(1000)

    print x.T; print len ( x.T )
    print len (x)

# XYZ = horzcat ( X,Y,Z )

    XYZ = np.vstack(( [x, y, z] ))

    print len ( XYZ )

# print XYZ

# print len ( XYZ )

# print len ( XYZ [ 0 ] )

#
# create a histogram by providing the bin edges (unequally spaced)
#

# moze cos takiego zadziala
    P.figure()

# bins = [100,125,150,160,170,180,190,200,210,220,230,240,250,275,300]

    n, bins, patches = P.hist(  XYZ.T, 10, normed=1, histtype='bar'\
    , stacked=True)

# color = ['crimson', 'burlywood', 'chartreuse']

# P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

    P.show()

#
# we can also stack using the step histtype

    P.figure()

    n, bins, patches = P.hist(XYZ.T, 10, histtype='step', stacked=True, fill=True) 

# musimy to wykorzystac, pobawic sie stepem, jesli nie wyjdzie to pokombinowac z barem zeby bar drugi byl naprawde suma pierwszego i drugiego arrayu

    P.show()

#####################################################################################################################################################

StackedHistogram ( )
