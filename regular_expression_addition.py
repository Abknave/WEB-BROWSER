sentence="hello 2 all of you 44"
import re

def sumnums(sentence):
     result=0
     regex=re.findall("[0-9]+",sentence)
     for i in regex:
         result+=int(i)
     return result
    
print sumnums(sentence)
