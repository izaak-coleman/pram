import subprocess
import sys

class EDirect:
  """EDirect class is a thin wrapper (just forwards commands) to EDirect:
     a command-line api for E-Utilities."""

  def __init__(self):
    pass

  def getAllProteinsForOrganism(self, query=None, db="ipg", fmt="fasta"):
    """Runs following on command-line:

         esearch -db <db> -query <query> | efetch -format <fmt>

       where args plug into angle brackets and returns ouput from command-line
       as a string. """
    cmd = 'esearch -db ' + db + ' -query "' + query + '" | efetch -format ' + fmt 
    print("Running entrez command: " + cmd)
    result = subprocess.run([cmd], stdout=subprocess.PIPE,shell=True)
    print("Entrez command complete")
    return result.stdout.decode("utf-8")

def main():

  if len(sys.argv) != 2:
    print("Usage: <exe> <species>")
    sys.exit(1)

  # make entrez class
  entrez = EDirect()
  searchResult = entrez.getAllProteinsForOrganism(query=sys.argv[1], db="protein", fmt="fasta")

  searchResult.decode("utf-8").split("\n")

if __name__ == '__main__':
  main()
