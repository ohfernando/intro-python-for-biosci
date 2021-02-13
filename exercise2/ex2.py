from numpy import random
from random import randint
import betternumbergenerator as ng
#tempvariables in next line
charisma=1

#still have to do exam

#defines luck
def tryluck(listest):
    luckinput='y'
    if luckinput=='y':
        luck=randint(0,1)
    x=ng.weightedrandom(0,100)
    y=ng.weightedrandom(0,100)
    if x>=y:
        maxres=x
        minres=y
    if x<y:
        maxres=y
        minres=x
    if luck == 0:
        var=minres
    if luck ==1:
        var=maxres
    listest.append(luck)
    listest.append(var)

    
#defines charisma
def charismaexists(charismavar,usevar,listfunc):
    if charismavar==1:
        tempround=round(usevar)
        diff=tempround-usevar
        if diff>0:
            usevar=round(usevar)
        listfunc.append(usevar)

#ifstudentisabsent
def badsleep(var,varlist,sleeplist):
    probgen=random.rand()
    if probgen>0.3:
        var=var
    elif probgen>0.2:
        #midly bas sleep
        var=0.9*var
    else:
        var=0.8*var
    sleeplist.append(probgen)
    varlist.append(var)


effort=ng.weightedrandom(10,15)/10

#blank variables for exercise      
exerciselist=[]
scorelistn=[]
scorelist=[]
#scorelists necessary so local variable inside function is exported globally

#generate a random score for each exercise
for i in range (1,11):
    scoret=[]
    tryluck(scoret)
    score=scoret[1]/10
    charismaexists(charisma,score,scorelistn) #applies charisma factor to score


bslist=[]
for i in scorelistn:
    badsleep(i,scorelist,bslist)


scorelistfinal=[]
for item in scorelist:
    item=item*effort
    if item>10:
        item=10
    scorelistfinal.append(item)
    

for item in scorelistfinal:
    if item>=6:
        pf=1
    else:
        pf=0
    exerciselist.append(pf)
    #make a list of scores for each exercie
print(exerciselist)
exercisetotal=0
for element in exerciselist:
    exercisetotal=exercisetotal+element
#add up the total for each exercise

exam1=[]

tryluck(exam1)
examvar=exam1[1]
exam2=[]
examsleeplist=[]
badsleep(examvar,exam2,examsleeplist)
examscore=exam2[0]/10
examscore=examscore*effort
if examscore>10:
    examscore=10

finalscore=(0.4*examscore)+(exercisetotal*0.6)
print(examscore,exercisetotal)
flist=[]
charismaexists(charisma,finalscore,flist)
gradelist=['A','B','C','D','F']
gradescore=[9,8,7,6,0]
for i in gradescore:
    n=gradescore.index(i)
    if flist[0]>=i:
        print("The letter grade is " + gradelist[n])
        break
print("The final score is " + str(flist[0]))
