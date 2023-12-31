# -*- coding: utf-8 -*-
from asyncio.windows_events import NULL
from genericpath import isfile
import itertools
from math import fabs
import Art
import time
import os 
from Helper import alphabet, passfileconverter
import Library
from hashlib import sha1 
import base64 
from glob import glob

def Wordlister(Lenght:int,Upper:int,Number:str,charset:str,lang:str,vers:int):
    s_time=time.time()
    charlist=alphabet(Upper,Number,charset,lang) 
    lib=Library.strings(lang)
    if vers==1:    
        for i in range(Lenght):
            if i==0:
               with open( 'wordlist','w') as f:
                f.write(','.join(charlist))
            else:
                print(lib["wordliststatus"]%i)
                with open( 'temp.txt','w') as t: 
                    with open( 'wordlist','r') as f:
                        for s in f.read().split(','):
                            if s!="":
                                for c in charlist:
                                    t.write((str(s)+str(c))+',')
                    print(lib["donein"]%str(time.time()-s_time))            
                os.remove('wordlist')
                os.rename('temp.txt','wordlist')
    elif vers==2:
        with open( 'wordlist','w') as f:
            permutations=itertools.product(charlist,repeat=Lenght)
            for p in permutations:
                f.writelines(''.join(p)+"\n")    
            print(lib["donein"]%str(time.time()-s_time))            
    cost= (time.time()-s_time)
    print(lib["wordlistended"]%(str(Lenght),str(cost)))        
def uroboros(Lenght:int,Upper:int,Number:str,charset:str,lang:str,name:str):
    s_time=time.time()
    charlist=alphabet(Upper,Number,charset,lang) 
    lib=Library.strings(lang)
    solved=[]
    with open( 'wordlist','w') as f:
            permutations=itertools.product(charlist,repeat=Lenght)
            for p in permutations:
                forged=forge(p,s_time,name)
                if forged.count()>0:
                    for res in forged:
                        solved.append(res)     
    cost= (time.time()-s_time)
    print(lib["wordlistended"]%(str(Lenght),str(cost)))  
    with open( 'solved','w') as s:
              s.write(','.join(solved))
def forge(candidate:str,stime:str,target,lang:str):
    lib=Library.strings(lang)
    if "\n" in candidate:
        candidate=candidate.replace("\n",'')
    crypted=base64.b64encode(sha1(candidate.encode()).digest()).decode()
    for key,value in target.items():                        
        if crypted==key:
            cost=time.time()-stime
            with open ("cracked.txt","a") as cr:
                cr.write(key+candidate+':'+str(cost)+"\n")
                print(lib["found"])

def BruteForcer(target:str,lang:str):
    lib=Library.strings(lang)
    targets=passfileconverter(target)    
    filesready=True
    path=os.getcwd()+"\\Wordlists\\"
    trycount=0
    while filesready:
        worlists=glob(path)
        if len(worlists)>0:
            filesready=False
        else:
            print(lib['fnf'])
            input()
    files=os.listdir(path)
    s_time=time.time()   
    for file in files:               
        with open ((path+file),'r') as wordlist:
           print(lib["workingonfile"]%(file))
           for candidate in wordlist.read().split(","):
            forge(candidate,s_time,targets,lang) 
            trycount=trycount+1
    print(lib["Cc"]%(str(time.time()-s_time),str(trycount)))
    
def langselector():
       flg=True
       while flg:
           rslt=input("Chose prefered language/Dil Tercihinizi yapınız (Turk/Eng)\n")
           if rslt.upper()=="ENG" or rslt.upper()=="TURK":
               flg=False
       return rslt
       
def main():
    Art.Oppening()
    lang=langselector()
    lib=Library.strings(lang)
    stat=True
    while stat:    
        job=int(input(lib['jobs']))
        if job==1 or job==3:
            getl=True
            while getl:
                l=int(input(lib['lenght']))
                if l>0:
                    getl=False
            getu=True
            while getu:      
                u=int(input(lib['updown']))
                if u>0:
                    getu=False
            getn=True
            while getn:
                n=str(input(lib['numbers']) )  
                if n!="":
                    getn=False
            if job==1:
                getmvl=True
                while getmvl:
                    v=int(input(lib["wlv"]))  
                    if v==1 or v==2:
                        getmvl=False                  
            cs=str(input(lib["charlist"]) ) 
            if job==1:
                Wordlister(l,u,n,cs,lang,v)
            if job==3:
                getkeys=True
                while getkeys:
                    name=str(input(lib['fileloc']))
                    if name!="":
                        getkeys=False
                uroboros(l,u,n,cs,lang,name)
                
        elif job==2:
            getkeys=True
            while getkeys:
                name=str(input(lib['fileloc']))
                if name!="" and os.path.isfile("/"+name)!=True:        
                    getkeys=False
            BruteForcer(name,lang)
            
        elif job==0:
            print(lib['force'])
            Art.yoda()
            stat=False
            break
            
main()
    