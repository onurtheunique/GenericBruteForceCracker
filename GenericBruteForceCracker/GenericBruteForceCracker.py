# -*- coding: utf-8 -*-
from genericpath import isfile
import itertools
from math import fabs
import Art
import time
import os 
from Helper import alphabet, passfileconverter
import Library
from hashlib import sha1 
from base64 import b64encode 

"""
def Wordlister(Lenght:int,Upper:int,Number:str,charset:str,lang:str):
    s_time=time.time()
    charlist=alphabet(Upper,Number,charset,lang) 
    lib=Library.strings(lang)
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

    cost= (time.time()-s_time)
    print(lib["wordlistended"]%(str(Lenght),str(cost)))
"""

def Wordlister(Lenght:int,Upper:int,Number:str,charset:str,lang:str):
    s_time=time.time()
    charlist=alphabet(Upper,Number,charset,lang) 
    lib=Library.strings(lang)
    with open( 'wordlist','w') as f:
        permutations=list(itertools.permutations(charlist,Lenght))
        for p in permutations:
            f.writelines(''.join(p)+"\n")    
        print(lib["donein"]%str(time.time()-s_time))            
    cost= (time.time()-s_time)
    print(lib["wordlistended"]%(str(Lenght),str(cost)))


def BruteForcer(target:str,lang:str):
    lib=Library.strings(lang)
    if os.path.isfile(target)!=True:
        print(lib['terminated'])
    else:
        targetdictionary=passfileconverter(target)
        
    if os.path.isfile("wordlist")!=True:
        print(lib['fnf'])
        
    solved={}
    
    with open("wordlist","r") as wlist:
        s_time=time.time()        
        for candidate in wlist.read().split(','):
            crypted=b64encode(sha1(candidate.encode()).digest()).decode()
            if crypted in solved.keys():
                break
            """ V1
            with open( target, 'r') as input_file:
                for record in input_file:
                    (key,hashval) =record.split(":{SHA}")
                    hashval=hashval.replace("\n","")
            """
            for key,value in targetdictionary.items():                        
                    if crypted==key:
                        cost= (time.time()-s_time)
                        del targetdictionary[key]
                        solved[crypted]=lib["record"]%(key,candidate,str(cost))
                        print(lib["found"])
                        break       
        print(lib["Cc"]) 
        with open ("cracked.txt","w") as cr:
            for key,value in solved.items():             
                cr.writelines(key+':'+value)
    

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
        if job==1:
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
            getcs=True
            cs=str(input(lib['charlist']) )  

            Wordlister(l,u,n,cs,lang)
        elif job==2:
            getkeys=True
            while getkeys:
                name=str(input(lib['fileloc']))
                if name!="":
                    getkeys=False
            BruteForcer(name,lang)
        elif job==0:
            print(lib['force'])
            Art.Tux()
            stat=False
            break
            
main()
    