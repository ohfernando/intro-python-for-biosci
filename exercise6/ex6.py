from Bio.SeqUtils.ProtParam import ProteinAnalysis
import re
import sys
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

fasta=open(sys.argv[1], 'r+')
#fasta=open('proteome.fasta', 'r+')

def fileappend(list1,string1):
    if string1!='':
        list1.append(string1)
        string1=''
        return string1

def whichfile(dnabinding,aas_in_file_dnabinding,aas_in_file,string_without_line_breaks):
    if dnabinding==True:
        string_without_line_breaks=fileappend(aas_in_file_dnabinding,string_without_line_breaks)
    elif dnabinding==False:
        string_without_line_breaks=fileappend(aas_in_file,string_without_line_breaks)


def analysis(listofaas,outlist):
    for prot in listofaas:
        exc=0
        try:
            templist=[]
            p=ProteinAnalysis(prot)
            templist.append(p.molecular_weight())
            templist.append(p.instability_index())
            templist.append(p.isoelectric_point())
            outlist.append(templist)
        except ValueError:
            exc=exc+1
        except KeyError:
            exc=exc+1
            
def dictfordf(listin,dictin):
    for i in range(0,3):
        templistn=[]
        for sublist in listin:
            templistn.append(sublist[i])
        a=listofindices[i]
        dictin[a]=templistn
    

aas_in_file=[]
aas_in_file_dnabinding=[]
string_without_line_breaks=''
count=0
for line in fasta:
    if line[0]== ">":
        try:
            a=line.index("DNA-binding")
            dnabinding=True
        except ValueError:
            dnabinding=False
        if dnabinding==True:
            if string_without_line_breaks!='':
                aas_in_file_dnabinding.append(string_without_line_breaks)
                string_without_line_breaks=''
        elif dnabinding==False:
            if string_without_line_breaks!='':
                aas_in_file.append(string_without_line_breaks)
                string_without_line_breaks=''
    else:
        stripped_line = line.rstrip()
        string_without_line_breaks += stripped_line
        
if dnabinding==True:
     if string_without_line_breaks!='':
        aas_in_file_dnabinding.append(string_without_line_breaks)
elif dnabinding==False:
    if string_without_line_breaks!='':
        aas_in_file_dnabinding.append(string_without_line_breaks)

fasta.close()

listweach=[]
listweachdnabinding=[]
exc=0

analysis(aas_in_file_dnabinding,listweachdnabinding)
analysis(aas_in_file,listweach)


#if exc!=0:
    #print(str(exc)+"proteins not plotted due to noncanonical amino acids")
#X,U,O raisexception
    
listofindices=['molweight','instindex','isopt']
dictforfr={}
dictforfrdnabinding={}

dictfordf(listweachdnabinding,dictforfrdnabinding)
dictfordf(listweach,dictforfr)

df1=pd.DataFrame(dictforfr)
df2=pd.DataFrame(dictforfrdnabinding)

#dna binding protein jus tin name
#plot those in different colors



sns.set(style = "darkgrid")


fig = plt.figure()
sns.set_color_codes('bright')
ax = fig.add_subplot(111, projection = '3d')

for curr_df, c in zip((df1, df2), ('k', 'y')):
    ax.scatter(*curr_df[['molweight', 'instindex', 'isopt']].values.T, color=c)

ax.set_xlabel("Molecular Weight")
ax.set_ylabel("Instability Index")
ax.set_zlabel("Isoelectric Point")

plt.show()
    
