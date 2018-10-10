import sys
import EDirect

class Pram:
    """Pram class runs pram algorithm on a single organism and
       stores the resulting data."""

    def __init__(self, organism):
      self.proteinList = self.downloadProteins(organism)
      # Handle duplicate sequences. If duplicate, store same sequence
      # And simply group together headers
      print('\n'.join([(hdr+'\n'+fa) for hdr,fa in self.proteinList]))

    def downloadProteins(self, organism):
      """Uses EDirect class to download protein sequences (fasta format)
         for organism. Each fasta element is converted to (header, sequence)
         tuple and tuples are returned in a list."""
     
      # Download from NCBI
      entrez = EDirect.EDirect()
      dataDump = entrez.getAllProteinsForOrganism(query=organism, db="protein",fmt="fasta")

      # make tuples
      dataDump = dataDump.split(">")
      dataDump.pop(0)
      return [self.makeFastaTuple(e) for e in dataDump]

    def makeFastaTuple(self, e):
      """Function takes a string containing a fasta header and biological
         sequence separated by newline characters. 
         Function returns (header, sequence) tuples."""
      lines = e.split('\n')
      hdr = lines.pop(0)
      return (hdr.split(' ')[0], "".join(lines))

def main():
  if len(sys.argv) != 2:
    print("Usage: <exe> <organism name>")
    sys.exit(1)
  p = Pram(sys.argv[1])

if __name__ == "__main__":
  main()
