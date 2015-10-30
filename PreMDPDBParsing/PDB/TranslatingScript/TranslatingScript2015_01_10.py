import sys

AtomNameLexicon = { \

' HB2 ARG': ' HB1 ARG', \
' HB3 ARG': ' HB1 ARG', \
' HG2 ARG': ' HG1 ARG', \
' HG3 ARG': ' HG2 ARG', \
' HD2 ARG': ' HD1 ARG', \
' HD3 ARG': ' HD2 ARG', \


' HB2 ASN': ' HB1 ASN', \
' HB3 ASN': ' HB2 ASN', \

' HB2 ASP': ' HB1 ASP', \
' HB3 ASP': ' HB2 ASP', \

' HB2 CYS': ' HB1 CYS', \
' HB3 CYS': ' HB2 CYS', \
' HG  CYS': ' HG1 CYS', \

' HB2 GLN': ' HB1 GLN', \
' HB3 GLN': ' HB2 GLN', \
' HG2 GLN': ' HG1 GLN', \
' HG3 GLN': ' HG2 GLN', \

' HB2 GLU': ' HB1 GLU', \
' HB3 GLU': ' HB2 GLU', \
' HG2 GLU': ' HG1 GLU', \
' HG3 GLU': ' HG2 GLU', \

' HA2 GLY': ' HA1 GLY', \
' HA3 GLY': ' HA2 GLY', \

' HB2 HSD': ' HB1 HSD', \
' HB3 HSD': ' HB2 HSD', \

' HB2 HSE': ' HB1 HSE', \
' HB3 HSE': ' HB2 HSE', \
 
'HG12 ILE': 'HG11 ILE', \
'HG13 ILE': 'HG12 ILE', \

'HD11 ILE': ' HD1 ILE', \
'HD12 ILE': ' HD2 ILE', \
'HD13 ILE': ' HD3 ILE', \

' HB2 LEU': ' HB1 LEU', \
' HB3 LEU': ' HB2 LEU', \
 
' HB2 LYS': ' HB1 LYS', \
' HB3 LYS': ' HB2 LYS', \

' HG2 LYS': ' HG1 LYS', \
' HG3 LYS': ' HG2 LYS', \

' HD2 LYS': ' HD1 LYS', \
' HD3 LYS': ' HD2 LYS', \
 
' HE2 LYS': ' HE1 LYS', \
' HE3 LYS': ' HE2 LYS', \

' HB2 MET': ' HB1 MET', \
' HB3 MET': ' HB2 MET', \

' HG2 MET': ' HG1 MET', \
' HG3 MET': ' HG2 MET', \

' HB2 PHE': ' HB1 PHE', \
' HB3 PHE': ' HB2 PHE', \

' HB2 PRO': ' HB1 PRO', \
' HB3 PRO': ' HB2 PRO', \
' HG2 PRO': ' HG1 PRO', \
' HG3 PRO': ' HG2 PRO', \
' HD2 PRO': ' HD1 PRO', \
' HD3 PRO': ' HD2 PRO', \

' HB2 SER': ' HB1 SER', \
' HB3 SER': ' HB2 SER', \
' HG  SER': ' HG1 SER', \

' HB2 TRP': ' HB1 TRP', \
' HB3 TRP': ' HB2 TRP', \

' HB2 TYR': ' HB1 TYR', \
' HB3 TYR': ' HB2 TYR', \

}

InFile = open ( sys.argv [1], 'r' )

Lines = InFile. readlines()

InFile. close ()

Bufor = [ ]

for line in Lines:

 if line [12:20] in AtomNameLexicon.keys():

   NewLine = line[:12] + AtomNameLexicon [ line [12:20] ] + line [ 20: ] 

   Bufor. append ( NewLine )

 else: Bufor. append ( line )


OutFile = open( sys.argv [2], 'w' )

for line in Bufor: OutFile. write (line)

OutFile. flush ()
OutFile. close ()


