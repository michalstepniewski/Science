class TextLines ( list ):

      def WriteToFile ( self, OutputPath ):

          File = open ( OutputPath, 'w' )

          for Line in self:

              File. write ( Line )

          File. flush ( )
          File. close ( )

          return
