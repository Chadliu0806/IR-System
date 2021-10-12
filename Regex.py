import re

def getChars(sz):
    nChars = 0
    for ch in sz:
        if ord(ch) <= 127:          # only process standard ASCII
            nChars = nChars + 1
    return nChars

def getWords(sz):
    return len((sz.encode(encoding='ascii', errors='ignore')).split())

def getSentences(sz):
    # regular expression string come from network paper
    szSentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sz)
    return len(szSentences)

def getMatch(pattern, sz):   
  
    filter = '(.{0,20})(' + pattern + ')(.{0,20})' 
   
    match = re.findall(filter, sz)
    if (match):
        for element in match:   # more than one comparison data may be found in each line
            if (element):
                print(element)
      
