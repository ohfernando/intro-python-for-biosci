import sys
import os


fasta=open(sys.argv[1],"r")
#fasta=open('proteome.fasta',"r")
#listoffastas=['covid.fasta','proteome1.fasta','test.fasta']

countproteins=0
for line in fasta:
    if line[0]=='>':
        countproteins=countproteins+1

proteinostring=str(countproteins)
try:
    print(proteinostring,proteinostring[-3])
    endnumber=int(proteinostring[-3]+proteinostring[-2]+proteinostring[-1])
    endthousand=(int(proteinostring[0:-3])+1)*1000
except IndexError:
    endnumber=proteinostring
    endthousand=1000
fasta.close()

fasta=open(sys.argv[1],"r")
        
newfile=False
parent_dir = os.getcwd()
countmeta=0
count=0
for line in fasta:
    if line[0]=='>':
        if count>1000:
            count=0
            countmeta=countmeta+1
            y=(countmeta*1000)
            if y==endthousand:
                parent_dir_path=str(y-999)+'-' +str(proteinostring)
                pathparent=os.path.join(parent_dir,parent_dir_path)
                os.mkdir(pathparent) 
            else:
                parent_dir_path=str(y-999)+'-' +str(y)
                pathparent=os.path.join(parent_dir,parent_dir_path)
                os.mkdir(pathparent)
        elif newfile==False:
            count=0
            countmeta=countmeta+1
            y=countmeta*1000
            if y==endthousand:
                parent_dir_path=str(y-999)+'-' +str(proteinostring)
                pathparent=os.path.join(parent_dir,parent_dir_path)
                os.mkdir(pathparent) 
            else:
                parent_dir_path=str(y-999)+'-' +str(y)
                pathparent=os.path.join(parent_dir,parent_dir_path)
                os.mkdir(pathparent)
        if newfile!=False:
            newfile.close()
        filename=line.split()[0].split("|")[2]
        directory=filename
        path=os.path.join(pathparent,directory)
        os.mkdir(path)
        filepath=os.path.join(path,filename+'.fasta')
        newfile=open(filepath,'w')
        newfile.write(line)
        count=count+1
        jobpath=os.path.join(path,filename+'.job')
        jobfile=open(jobpath,'w')
        for file in sys.argv[2:]:
        #for item in listoffastas:
            writeline="blastn -db " + filename + " -query " + filepath + " -out results.out"
            jobfile.write(writeline)
        jobfile.close()
    else:
        newfile.write(line)
#folders =0
#for dirnames in os.walk(pathparent):
    #folders += len(dirnames)
#newname=str((countmeta-1)*1000) + '-' + str(folders)
#os.rename(parent_dir_path,newname)
newfile.close()
fasta.close()
