import sys
import EDirect
import itertools


class Fasta:
  """Stores a fasta sequence field and a list of accession numbers
     each of which should reference the same biological sequence field i.e the actual
     fasta element at each accession number should be identical to the 
     sequence field. Hence, list of accession numbers provides non-redundacy."""

  ### Predefined Fields
  self.accessionList = []

  ### Methods
  def __init__(self, fasta):
    accession, self.seq = self.parseFastaElement(fasta)
    self.addAccession(accession)

  def parseFastaElement(self, e):
    """Function takes a string containing a fasta header and biological
       sequence separated by newline characters. 
       Function returns (header, sequence) tuples."""
    lines = e.split('\n')
    hdr = lines.pop(0)
    return (hdr.split(' ')[0], "".join(lines))

  def addAccession(self, a):
    self.accessionList.append(a)
class Pram: """Pram class runs pram algorithm on a single organism and
     stores the resulting data."""

  def __init__(self, organismList):
    pass

  def getKRepeats(self, organism, k):
  """Searches for amino acid repeats of length >= k within the fasta
     protein sequences downloaded for organism. Protein sequences 
     are retrieved from NCBI by querying term organism against
     the protein database. Downloaded sequences are filtered for non-redudancy
     and stored as Fasta: For a redundant fasta (multiple
     fasta elements with different protein accession numbers but identical
     protein sequence), Fasta stores the protein sequence, along with a list of protein 
     accession numbers for each fasta element that referenced the protein sequence."""

    proteinList = self.makeNonRedundant(self.downloadProteins(organism))
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

    # make non redundant fasta 
    dataDump = dataDump.split(">")
    dataDump.pop(0)
    return [Fasta(e) for e in dataDump]

  def makeNonRedundant(self, fastaList):
    # make groups of fasta element, where each group has an identical biological sequence.
    fastaList = itertools.groupby(sorted(fastaList, key=lambda x: x.seq), key=lambda x:x.seq)


def main():
  if len(sys.argv) != 2:
    print("Usage: <exe> <organism name>")
    sys.exit(1)
  p = Pram(sys.argv[1])

if __name__ == "__main__":
  main()
