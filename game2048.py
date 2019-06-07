#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 05/06/2019 9:43 PM
# @Author  : Fitz Zhang
# @File    : game2048.py
import random
import os
import sys

def initgame(value):
    x=getrandom(value)
    value[x]=4
    y=getrandom(value)
    value[y]=2
    return value

def getrandom(value):
    maplist=[]
    for i in range(0,len(value)-1):
        if value[i]==0:
            maplist.append(i)
    if len(maplist)==0:
        return -1
    else:
        x=random.randint(0,len(maplist)-1)
        return maplist[x]

def upoption(value):
    for i in [0,1,2,3]:
        input=[value[i],value[i+4],value[i+8],value[i+12]]
        output=psort(input)
        value[i], value[i + 4], value[i + 8], value[i + 12]=output[0],output[1],output[2],output[3]
    value[getrandom(value)]=2
    return value

def downoption(value):
    for i in [0,1,2,3]:
        input=[value[i+12],value[i+8],value[i+4],value[i]]
        output=psort(input)
        value[i + 12], value[i + 8], value[i + 4], value[i]=output[0],output[1],output[2],output[3]
    value[getrandom(value)]=2
    return value

def leftoption(value):
    for i in [0,4,8,12]:
        input=[value[i],value[i+1],value[i+2],value[i+3]]
        output=psort(input)
        value[i], value[i + 1], value[i + 2], value[i + 3]=output[0],output[1],output[2],output[3]
    value[getrandom(value)]=2
    return value

def rightoption(value):
    for i in [0,4,8,12]:
        input=[value[i+3],value[i+2],value[i+1],value[i]]
        output=psort(input)
        value[i + 3], value[i + 2], value[i + 1], value[i]=output[0],output[1],output[2],output[3]
    value[getrandom(value)]=2
    return value

def psort(sline):
    j=0
    #print(sline)
    for i in range(0,len(sline)-1):
        if sline[j]==0:
            for k in range(j,len(sline)-1):
                sline[k]=sline[k+1]
            sline[-1]=0
        else:
            j+=1
    j=0
    for i in range(0, len(sline) - 1):
        if sline[j]==sline[j+1]:
            sline[j]=sline[j]*2
            sline[j+1]=0
            for k in range(j+1,len(sline)-1):
                sline[k]=sline[k+1]
            sline[-1]=0
            j+=1
        else:
            j+=1
    #print(sline)
    return sline

def printlist(value):
    os.system('cls')
    for i in [0,4,8,12]:
        print("%s  %s  %s  %s" %(value[i],value[i+1],value[i+2],value[i+3]))

def checkresult(value,target):
    for i in range(0,len(value)):
        if value[i]==target:
            return True
    return False

def play():
    valuelist=[0]*16
    valuelist=initgame(valuelist)
    printlist(valuelist)
    target=32
    flag=True
    while flag:
        option=input()
        #os.system('cls')
        if option=='w':
            valuelist=upoption(valuelist)
            printlist(valuelist)
        elif option=='a':
            valuelist=leftoption(valuelist)
            printlist(valuelist)
        elif option=='s':
            valuelist=downoption(valuelist)
            printlist(valuelist)
        elif option=='d':
            valuelist=rightoption(valuelist)
            printlist(valuelist)
        elif option=='q':
            sys.exit()
        else :
            print('Please use w s a d to play game, thanks')
        if checkresult(valuelist,target):
            flag=False
            print('congulations, you win the gaime')
            sys.exit()


if __name__ == '__main__':
    #test=[2,0,2,4]
    #print(psort(test))
    play()

