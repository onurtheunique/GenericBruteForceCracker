import Library

def formatinput(list):
    lst=[]
    for line in list:
        val=line.find('}')+1
        lst.append(line[val:])
    return lst

def filter(lst):  
    rslt=[]
    for line in  formatinput(lst):
        if line not in rslt:
            rslt.append(line)
    return rslt

def alphabet(Upper:int,Number:str,charset:str,lang:str):
    core=Library.charset(lang)
    if charset!="":
        core =charset.split(',')
    alphabet=[]
    if Upper==1:
        for c in core:
            alphabet.append(c)
    elif Upper==2:
        for c in core:
            alphabet.append(c.upper())
    else :
        for c in core: 
            alphabet.append(c)
            alphabet.append(c.upper())
    if str.upper(Number)=='YES' or str.upper(Number)=='EVET' :
        for i in range(10):
            alphabet.append(str(i))
    return alphabet
def passfileconverter(file:str):
    dictionary={}
    with open( file, 'r') as input_file:
                for record in input_file:
                    (key,hashval) =record.split(":{SHA}")
                    hashval=hashval.replace("\n","")
                    dictionary[hashval]=key
    return dictionary
def patcher():
    with open( 'wordlist','a') as w:
          for char in  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',  'u', 'v', 'w', 'x', 'y', 'z']:
              s=""
              for i in range(8):
                   s=s+char
              w.write(s+"\n")
              w.write(s.upper()+"\n")
          with open("top100.txt",'r') as t:
            for p in t:
                w.write(p)
             

          
        