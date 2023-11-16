with open( 'wordlist','a') as w:
      for char in  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
          s=""
          for i in range(8):
               s=s+char
          w.write(s+",")
          w.write(s.upper()+",")
      with open("top100.txt",'r') as t:
        for p in t:
            w.write(p+',')