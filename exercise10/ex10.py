import re
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def countfromlist(listworking,listdefs,listout,num):
    count=0
    aastore=listworking[0]
    for i in listdefs:
        templist=listworking[1:]
        index=aastore.index(i)
        for sublist in templist:
            count=count+sublist[index]
    count=count/num
    listout.append(count)

        

#aminoacids=[]
#aminoacids.append(aminoacidst)
hydrophobic=['A','I','L','M','F','V','P','G']
acidic=['D','E']
basic=['A','H','L']
cytosine=['C']
listofthingstoplot=[['cystesines','acids','basic','hydrophobic']]

def docount(a,namelist):
    aminoacids=[['L','I','V','A','M','F','W','P','G','S','N','Q','T','C','Y','D','E','K','R','H']]
    string_without_line_breaks=''
    #fasta=open(a, 'r+')
    fasta=open(sys.argv[a], 'r+')
    for line in fasta:
        if line[0]== ">":
            pass
        else:
            stripped_line = line.rstrip()
            string_without_line_breaks += stripped_line
    fasta.close()
    namelist.append(str(sys.argv[a]))


    #make a list of amino acids in file
    aas_in_file=[]
    new=re.split("",string_without_line_breaks)
    for i in new:
        if i=='':
            pass
        else:
            aas_in_file.append(i)
    countfull=0
    for i in aas_in_file:
        countfull=countfull+1

    templist=[]
    for item in aminoacids[0]:
        count=0
        for aa_f in aas_in_file:
            if item==aa_f:
                count=count+1
        templist.append(count)
    aminoacids.append(templist)

    temporarylist=[]
    countfromlist(aminoacids,cytosine,temporarylist,countfull)
    countfromlist(aminoacids,acidic,temporarylist,countfull)
    countfromlist(aminoacids,basic,temporarylist,countfull)
    countfromlist(aminoacids,hydrophobic,temporarylist,countfull)
    listofthingstoplot.append(temporarylist)

#for i in sys.argv[1:]:
    #docount(i)
namelist=['type_of_aa']
docount(1,namelist)
docount(2,namelist)
print(listofthingstoplot)
#dataframeplot=pd.DataFrame(listofthingstoplot)
tem=dict()
for i in listofthingstoplot:
    index=listofthingstoplot.index(i)
    a=namelist[index]
    tem[a]=i
#do this w range
    

df=pd.DataFrame(tem)
print(df)
#dataframeplot.plot(kind='bar')
#plt.show()
#print(dataframeplot)
#sns.set_theme(style="whitegrid")
#sns.barplot(x="classification", y="count", hue="genre", data=dataframeplot)
df = df.melt(id_vars='type_of_aa', var_name='whichproteome')
sns.catplot(x='type_of_aa', y='value',hue='whichproteome',kind="bar", data=df)
plt.show()


    



