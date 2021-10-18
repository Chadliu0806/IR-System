import xml.etree.ElementTree as ET
from Regex import getChars, getWords, getSentences, getMatch

def XMLParser(filename, pattern):

    nChars = 0
    nWords = 0
    nSentences = 0
    nPage = 1
    contents = ''

    XMLtree = ET.parse(filename)
    root = XMLtree.getroot()
    # Only process title and abstract content
    for page in root.findall('./PubmedArticle'):
        print (page.tag, page.attrib)
        for node in page.findall('.//Article'):

            nChars = 0
            nWords = 0
            nSentences = 0

            titlenode = node.findtext('./ArticleTitle')
            if (titlenode):
                szTitle = titlenode.title()
                sz = 'Article Title:' + str(nPage) + '-' + szTitle
                #print(sz)
                getMatch(pattern, szTitle)
                nChars += getChars(szTitle)
                nWords += getWords(szTitle)
                nSentences += getSentences(szTitle)
            for nextnode in node.iter(tag='AbstractText'):
                line = ''
                if nextnode.attrib != {}:   # This tag contain the attribute content
                    line = nextnode.attrib['Label'] + ': '
                    
                line = line + ''.join(nextnode.itertext())
                contents = contents + line
                nChars += getChars(line)
                nWords += getWords(line)
                nSentences += getSentences(line)
                if (pattern != ''):
                    getMatch(pattern, line)
                #print(line)
            
            sz = 'Article' + str(nPage) + ' - ' + 'The number of characters in \'XML contents\':' + str(nChars)
            print(sz)
            sz = 'Article' + str(nPage) + ' - ' + 'The number of words in \'XML contents\':' + str(nWords)
            print(sz)
            sz = 'Article' + str(nPage) + ' - ' + 'The number of sentences in \'XML contents\':' + str(nSentences)
            print(sz)

        print ('\n')
        nPage += 1
    return contents
        
    