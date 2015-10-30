import sys

#S169	F166	Y184	Y176	S179	F263	T177	F182	H181	K171	S185	Q170	R168	E172	Q188	G173	S180	Y187	F189	L174	H175
#23	28	29	30	31	33	33	37	39	40	40	45	47	50	54	55	58	60	70	90	100




#czyli dla kazdego aminokwasu obliczyc, przez jaki okres czasu 
# jest on w zakresie
# w najprostszym zakresie po prostu w jakim procencie klatek

##########################################################################

def AACloserThanThreshold (AA, Threshold):

    Distance = float ( AA. split () [-1] )

    if Distance <= Threshold:

       return True

    else: return False

##########################################################################

def AAFramesPercentLexicon (Frames, Threshold):

    AAFramesPercentLexiconI = {}

    for Frame in Frames:

        for AALine in Frame:

            AA = AALine[:10]
            Distance = float ( AALine. split () [-1] )

            if Distance <= float(Threshold):
               print Distance; print Threshold

               if AA in AAFramesPercentLexiconI. keys():

                  AAFramesPercentLexiconI[AA] += 1.0

               else:

                  AAFramesPercentLexiconI [AA] = 1.0

    NoFrames = float( len (Frames) )


    AAFramesPercentLexicon2I = {}

    for AA in AAFramesPercentLexiconI. keys ():

        AAPercent = (AAFramesPercentLexiconI[AA]/NoFrames) * 100.0

        AAFramesPercentLexicon2I [AA] = AAPercent

    print AAFramesPercentLexiconI                 
    print AAFramesPercentLexicon2I
    return AAFramesPercentLexicon2I

##########################################################################

def SplitLinesIntoFrames (Lines):

    Frames =[]; Frame =[]

    for Line in Lines:

        if Line[:5]== 'TITLE':

           Frames. append (Frame)
           Frame = []

        else:

           Frame. append (Line)

    return Frames[1:]

##########################################################################

def OutputAAFramesPercentLexicon (AAFramesPercentLexiconI, OutFilePath):

    OutFile = open (OutFilePath, 'w')
    
    for AA in AAFramesPercentLexiconI. keys ():

        Line = AA +' '+ str(AAFramesPercentLexiconI [ AA ]) + '\n'

        OutFile. write ( Line )

    OutFile. flush ()
    OutFile. close ()

    return

##########################################################################

def Main (InFilePath, OutFilePath, Threshold):

    InFile  = open (InFilePath, 'r')
    InLines = InFile. readlines ()
    InFile. close ()

    Frames = SplitLinesIntoFrames (InLines)

    AAFramesPercentLexiconI = AAFramesPercentLexicon (Frames, Threshold)

    OutputAAFramesPercentLexicon (AAFramesPercentLexiconI, OutFilePath)

    return

##########################################################################

Main (sys.argv[1], sys.argv[2], sys.argv[3])
