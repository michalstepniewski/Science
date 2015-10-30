################################################################################################

class PdbRecord(object):                                          # any record in PDB file

      def __init__(self, *args, **kwargs):

          self.s = str(*args, **kwargs)

      def Type(self):
#        print self.s[1:(6+1)]

          return self.s[(1-1):(6)]

#######################################################################################################

class HelixRecord(PdbRecord):                                               # HELIX record
   def funkcja():
      print 'lala'

# COLUMNS       DATA TYPE        FIELD        DEFINITION
# --------------------------------------------------------------------
#  1 -  6       Record name      "HELIX "
#  8 - 10       Integer          serNum       Serial number of the helix.
#                                             This starts at 1 and increases
#                                             incrementally.
# 12 - 14       LString(3)       helixID      Helix identifier. In addition
#                                             to a serial number, each helix is
#                                             given an alphanumeric character
#                                             helix identifier.
# 16 - 18       Residue name     initResName  Name of the initial residue.
# 20            Character        initChainID  Chain identifier for the chain
#                                             containing this helix.
# 22 - 25       Integer          initSeqNum   Sequence number of the initial
#                                             residue.
# 26            AChar            initICode    Insertion code of the initial
#                                             residue.
# 28 - 30       Residue name     endResName   Name of the terminal residue of
#                                             the helix.
# 32            Character        endChainID   Chain identifier for the chain
#                                             containing this helix.
# 34 - 37       Integer          endSeqNum    Sequence number of the terminal
#                                             residue.
# 38            AChar            endICode     Insertion code of the terminal
#                                             residue.
# 39 - 40       Integer          helixClass   Helix class (see below).
# 41 - 70       String           comment      Comment about this helix.
# 72 - 76       Integer          length       Length of this helix.






