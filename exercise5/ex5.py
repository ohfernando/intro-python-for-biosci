from RamachanDraw import fetch, phi_psi, plot
import sys

# PDB id to be downloaded
PDV_id=sys.argv[1]

# Drawing the Ramachandran plot
plot(fetch(PDB_id))
