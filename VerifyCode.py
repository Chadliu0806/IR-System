import hashlib
import binascii

def GenerateChecksum(contents):

    if (len(contents) != 0):
        m = hashlib.md5()
        m.update(contents.encode("utf-8"))
        h = m.hexdigest()
        print(h)
        return h
    else:
        return 0

def GenerateCRC32(contents):

    CRC32 = 0
    if (len(contents) != 0):
        CRC32 = binascii.crc32(str.encode(contents), CRC32)
    
    return CRC32    

def Comparison(source, target):
    
    source_len = len(source)
    target_len = len(target)
    
    record = []
    if (source_len == 0 or target_len ==0):
        return False
    elif (source_len != target_len):
        return False
    else:
        print(source)
        print('\n')
        i = 0
        while (i < source_len):
            if (source[i] != target[i]):
                record.append({i, source[i]})
                print('\033[43;31;1m' + target[i] + '\033[0m', end = "")
            else:
                print(target[i], end = '')
            i = i + 1   
        if (len(record) != 0):
            print('\nIncorrect Position:')
            print(record)
            return False
        else:
            return True
        

