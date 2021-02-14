# intro-python-for-biosci
Collection of scripts for evaluation exercises for Biol 282.

Please make sure the following modules are installed: numpy, pandas, matplotlib, seaborn .

Installation instructions for all packages necessary linked at the end of this file 

Each exercise is available in its own subfolder. Please make sure to deposit any files to be used for each script in the specified subfolder. A test file is available in the exercise-specific folder. 

Some of these scripts may take 5-10 minutes to run. I've incuded estimated runtime in scripts which may take longer than a few minutes to run. Please be patient!

Exercise-specific instructions:

Exercise 1: no special notes

Exercise 2: make sure the main file is in the same directory as betternumgenerator.py, then  open betternumgenerator.py before running code

Exercise 3:

Exercise 4: no special notes

Exercise 5: RamachanDraw is necessary. Input PDB identifier in command line as string 

Exercise 6: please note that if you use an organism with a large genome DNA-binding proteins may not be visible due to the density of proteins in graph; if you want to see DNA binding proteins highlighted please make sure to use an organism with less proteins in their genome. The testvisible.fasta file in the directory for that exercise should suit this purpose (please note this is not an actual organism, it's made up of an amalgamation of proteins from different organisms' proteomes).

Exercise 7: ete3 and taxopy are necessary.
The input format should be two taxaIDs in the command line, eg: ex7.py 3702 3712
Please make sure you're connected to the internet when running this script. You might need to delete the file taxdump.tar and associated files in the directory if you get an error when unzipping. 
This script may take 5-10 minutes or more to run due to databases needing to be updated.

Exercise 8: input file should contain coordinates; one set of coordinates per line, latitude and longitude seperated by a space (NOT comma or other character). First coordinate should be the coordinate being triangulated.

Exercise 9: input desired amino acid in command line. format should be: exercisescript.py fastafile.fasta 'A' (where A can be substituted for any other one-letter IUPAC coded amino acid out of the 20 standard amino acids)

Exercise 10: no extra notes

Installation instructions for packages:

ete3: http://etetoolkit.org/download/

matplotlib:

numpy:

pandas:

seaborn:

taxopy: https://pypi.org/project/taxopy/

taxonomy-ranks: https://pypi.org/project/taxonomy-ranks/#description
