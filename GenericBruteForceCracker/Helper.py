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
