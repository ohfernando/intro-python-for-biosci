#for this module please provide command line argument as name of test file and one-letter AA sequence, eg test.py 'A'


import sys
import re
import numpy as np
import pandas as pd
#fasta=open(sys.argv[1], 'r')
#can be sys.argv[1] is aminoacid sys.argv[2] is sequence
string_without_line_breaks=''
aminoacids=[['L','I','V','A','M','F','W','P','G','S','N','Q','T','C','Y','D','E','K','R','H']]
string_without_line_breaks=''
namelist=[]
#fasta=open('proteome.fasta','r+')
#templist=np.array([])
#aas_in_file=np.array([])
templist=[]
aas_in_file=[]
new=''
aminoacid=sys.argv[2]
fasta=open(sys.argv[1],'r+')
for line in fasta:
    try:
        if line[0]== ">":
            #np.concatenate(aas_in_file,templist)
            namelist.append(line.split()[0].split("|")[2])
            if templist==[]:
                pass
            else:
                aas_in_file.append(templist)
            templist=[]

        else:
            stripped_line=''
            stripped_line = line.rstrip()
            new=re.split("",stripped_line)
            for i in new:
                if i=='':
                    pass
                else:
                    templist.append(i)
    except MemoryError:
        print('error, please restart program')
fasta.close()
aas_in_file.append(templist)

countlist=[]
for sublist in aas_in_file:
    count=0
    for item in sublist:
        if item==aminoacid:
            count=count+1
    countlist.append(count)

print(countlist)
print(namelist)
percentiles=np.percentile(countlist,[20,80])
countp=0

for item in percentiles:
    if countp==0:
        percentilelist1=[]
        a=len(countlist)
        for index in range(0,a):
            element=countlist[index]
            if element<=item:
                percentilelist1.append(namelist[index])
        print("The 20th percentile is", end=' ')
        print(percentilelist1)
        countp=countp+1
    else:
        percentilelist2=[]
        a=len(countlist)
        for index in range(0,a):
            element=countlist[index]
            if element>=item:
                percentilelist2.append(namelist[index])
        print("The 80th percentile is", end=' ')
        print(percentilelist2)
        countp=countp+1

countarray=np.array(countlist)
print(countarray)
sortedarr=np.sort(countarray)
long=0
short=0
for i in countarray:
    if i>=percentiles[1]:
        long=long+i
    else:
        short=short+i
if short>long:
    print('The top 20% have less of the amino acid than the shorter 80%')
elif long>short:
    print('The top 20% have more of the amino acid than the shorter 80%')
else:
    print('both chains have equal counts of the amino acid')

            
