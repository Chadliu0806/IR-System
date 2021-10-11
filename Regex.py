import re

def getChars(sz):
    nChars = 0
    for ascii in sz:
        if ord(ascii) < 128:
            nChars = nChars + 1
    return nChars

def getWords(sz):
    return len((sz.encode(encoding='ascii', errors='ignore')).split())

def getSentences(sz):
    szSentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sz)
    return len(szSentences)

def getMatch(pattern, sz):   
  
    filter = '(.{0,20})(' + pattern + ')(.{0,20})' 
   
    match = re.findall(filter, sz)
    if (match):
        for element in match:
            if (element):
                print(element)
      
