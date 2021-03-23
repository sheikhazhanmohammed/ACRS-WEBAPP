import codecs
import secrets
import math
import ctypes
import os
import random


with codecs.open('./static/finalHindiWords.txt', encoding='utf-8') as f:
    hindiWords = f.read()
hindiWords = hindiWords.replace('\r',' ')
hindiWords = hindiWords.replace('\n',' ')
hindiWords = hindiWords.replace('(', ' ')
hindiWords = hindiWords.replace(')', ' ')
hindiWords = hindiWords.replace('<', ' ')
hindiWords = hindiWords.replace('>', ' ')
hindiWords = hindiWords.replace('-', ' ')
hindiWords = hindiWords.replace('.', ' ')
hindiWords = hindiWords.replace(',', ' ')
hindiWords = hindiWords.replace('?', ' ')
hindiWords = hindiWords.replace('  ', ' ')
hindiWords = hindiWords.replace('   ', ' ')
hindiWords = hindiWords.replace('    ', ' ')
hindiWordsList = hindiWords.split(' ')

with codecs.open('./static/finaltamil.txt', encoding='utf-8') as f:
    tamilWords = f.read()
tamilWords = tamilWords.replace('\r',' ')
tamilWords = tamilWords.replace('\n',' ')
tamilWords = tamilWords.replace('(', ' ')
tamilWords = tamilWords.replace(')', ' ')
tamilWords = tamilWords.replace('<', ' ')
tamilWords = tamilWords.replace('>', ' ')
tamilWords = tamilWords.replace('-', ' ')
tamilWords = tamilWords.replace('.', ' ')
tamilWords = tamilWords.replace(',', ' ')
tamilWords = tamilWords.replace('?', ' ')
tamilWords = tamilWords.replace('  ', ' ')
tamilWords = tamilWords.replace('   ', ' ')
tamilWords = tamilWords.replace('    ', ' ')
tamilWordsList = tamilWords.split(' ')

hexadecimalToBinaryDictionary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111"
}

def split(a):
    return [char for char in a]

def convertToBinary(a):
    a = split(a)
    binaryString = ''
    for char in a:
        binaryString = binaryString+hexadecimalToBinaryDictionary[char]
    return binaryString
    
   

def generateChecksum(a):
    b = a[12:16]
    a = a + b
    return a


def splitChecksum(a):
    l = []
    b = 0
    while b<132:
        c = a[b:b+11]
        b = b+11
        l.append(c)
    return l


def binaryToDecimalInteger(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def binaryToDecimal(a):
    l = []
    for b in a:
        b = int(b)
        c = binaryToDecimalInteger(b)
        l.append(c)
    return l

def wordGenerator(entropy, language):
    if(entropy=='NA' or entropy=='na'):
        entropy = secrets.token_hex(32)
        binaryOutput = convertToBinary(entropy)
        checksum = generateChecksum(binaryOutput)
        final = splitChecksum(checksum)
        finalList = binaryToDecimal(final)
        wordList = []
        for i in finalList:
            if(language=='Hindi'):
                wordList.append(hindiWordsList[i])
            else:
                wordList.append(tamilWordsList[i])
    else:
        binaryOutput = convertToBinary(entropy)
        checksum = generateChecksum(binaryOutput)
        final = splitChecksum(checksum)
        finalList = binaryToDecimal(final)
        wordList = []
        for i in finalList:
            if(language=='Hindi'):
                wordList.append(hindiWordsList[i])
            else:
                wordList.append(tamilWordsList[i])
    return wordList, finalList

BinSoln = None
ExpSoln = None

def count(x, y):
    res = 0
    y = str(y)
    for i in x:
        if i==y:
            res += 1
    return res

def pad(x, bits):
    diff = bits - len(x)
    if diff==0:
        return x
    elif diff<0:
        return x[:64]
    for i in range(diff):
        x = '0' + x
    return x
    

def toCharArray(x):
    return [i for i in x]


def tc(n):
    nbits = n.bit_length() + 1
    return f"{n & ((1 << nbits) - 1):0{nbits}b}"

def getBestSolution(x, y, z, selectedRegisters, expLen, bits):
    #print('In muta')
    xx = ['|', '&', '^' ];
    yy = [' ', '~'];
    zz = selectedRegisters
    Finalx = x.copy()
    Finaly = y.copy()
    Finalz = z.copy()
    Condition = False; 
    ExpSoln, BinSoln = None, None
    
    for i in range(len(xx)):
        for j in range(len(yy)):
            for k in range(len(zz)):
                for l in range(20):
                    Finalx[l] = xx[i];
                    Finaly[l] = yy[j];
                    Finalz[l] = zz[k];
                    Exp = yy[0] + zz[0] + xx[0] + yy[1] + zz[1]
                    for jj in range(2, expLen):
                        Exp += Finalx[jj] +  Finaly[jj] + Finalz[jj];
                    try:
                        num = tc(eval(Exp))
                    except:
                        continue
                    checkNumber = pad(num, bits)
                    Zero = count(checkNumber, 0)
                    One = count(checkNumber, 1)
                    if(Zero == One):
                        ExpSoln = Exp
                        BinSoln = checkNumber
                        Condition = True
                        break
                if Condition:
                    break
            if Condition:
                    break
        if Condition:
                    break
    #print(Finalz)
    return Condition, ExpSoln, BinSoln
            
                                       
def SRFG(
#         A = 84351354321321353,\
#         B = 358432165132132110,\
#         C = 91651454651451321,\
#         D = 58132132132158132,\
#         E = 98432513651321536,\
        \
        selectedRegisters = ['A', 'B', 'C', 'D'],\
        Registers = "AAAAABBBBBCCCCCDDDDD",\
        Operations = "||||||||&&&&&&&&^^^^^^^^",\
        Negations = "~~~~~~~~~~~          ",\
        expLen = 10,\
        bits = 64):
        
#     A = 84351354321321353
#     B = 358432165132132110
#     C = 91651454651451321
#     D = 58132132132158132
#     E = 98432513651321536
    A = random.randrange(10**16, 10**17)
    B = random.randrange(10**16, 10**17)
    C = random.randrange(10**16, 10**17)
    D = random.randrange(10**16, 10**17)
    ExpSoln, BinSoln = None, None
    x = toCharArray(Operations)
    y = toCharArray(Negations)
    z = toCharArray(Registers)
    random.shuffle(x)
    random.shuffle(z)
    
    for i in range(1,1001):
              
        #print('In eval')
        random.shuffle(x)
        random.shuffle(z)
        random.shuffle(y)
        #print(z)
        Exp = ''
        
        Exp += y[0] + z[0] + x[0] + y[1] + z[1]
        
        for j in range(2,expLen):
            Exp += x[j] + y[j] + z[j]
        
        try:
            num = tc(eval(Exp))
        except:
            continue
            
        
        checkNumber = pad(num, bits)
        #print(Exp, checkNumber)
        Zero = count(checkNumber, 0)
        One = count(checkNumber, 1)
        
        if(Zero == One):
            ExpSoln = Exp
            BinSoln = checkNumber
            return Exp, BinSoln
            break
        
        elif i==999:
            return None, None
            break
        
        if (Zero > bits/2 - bits / 8 and Zero < bits / 2 + bits / 8):
            condn, ExpSoln, BinSoln = getBestSolution(x, y, z, selectedRegisters, expLen, bits)
            if condn:
              return ExpSoln, BinSoln
            
                
def pad_new(x, bits):
    diff = bits - len(x)
    if diff==0:
        return x
    elif diff<0:
        return x[:bits]
    for i in range(diff):
        x = str(random.randrange(0,2)) + x
    return x
    


def applySRFG(mnem_phrase):
    s = pad(mnem_phrase, (len(mnem_phrase)//4 + 1) * 4)
    l = len(s)
    x = len(s)//4
    # print(x)
    a = int(s[:x], 2)
    b = int(s[x:2*x], 2)
    c = int(s[2*x:3*x], 2)
    d = int(s[3*x:], 2)
    rf = SRFG()[0]
#     print(a, b, c, d)
    seed = ''
    for i in range(1, 9):
        A = int(pad(bin(a)[2:],64), 2)
        B = int(pad(bin(b)[2:],64), 2)
        C = int(pad(bin(c)[2:],64), 2)
        D = int(pad(bin(d)[2:],64), 2)
        ans = bin(eval(rf))
    #     print(len(ans))
        if ans[0] == '-':
            ans = ans[3:]
            ans = pad_new(ans,64)
        else:
            ans = ans[2:]
            ans = pad_new(ans,64)
        seed += ans
#     print(seed) 
    for i in range(2047):
        seed = pad(seed, (len(s)//4 + 1) * 4)
        #     print(seed)
        l = len(seed)
        x = len(seed)//4
        #     print(x)
        a = int(seed[:x], 2) 
        d = int(seed[x:2*x], 2) 
        c = int(seed[2*x:3*x], 2) 
        d = int(seed[3*x:], 2) 
        #     print(a, b, c, d)
        seed = ''
        for i in range(1, 9):
            A = int(pad(bin(a)[2:],64), 2)
            B = int(pad(bin(b)[2:],64), 2)
            C = int(pad(bin(c)[2:],64), 2)
            D = int(pad(bin(d)[2:],64), 2)
            ans = bin(eval(rf))
        #         print(len(ans))
            if ans[0] == '-':
                ans = ans[3:]
                ans = pad_new(ans,64)
            else:
                ans = ans[2:]
                ans = pad_new(ans,64)
            seed += ans
    return seed

def cocktail(data):
#     print(len(str(data)))
    data = pad(str(data), 155)
    data = data.encode('utf-8')
    test = ctypes.CDLL('lib.so')    
    test.cocktail.argtypes = [ctypes.c_char_p]
    test.cocktail(data)
    file = open('hash.txt')
    x = file.read().lower()
    file.close()
#     os.remove('hash.txt')
    del test
    return x
                       
           
def hmacCocktail(seed):
    k = 0x426974636f696e2073656564
    opad = 0x5c5c5c5c5c5c5c5c5c5c5c5c
    ipad = 0x363636363636363636363636
    m = int(seed, 16)
    a1 = k ^ opad
    a2 =  int(cocktail(k^ipad), 16)
    a3 = m
    arg = a1 | a2 | a3
#     print(arg)
#     print(m)
    hash = cocktail(arg)
#     print(hash)
    mpk = hex(int(hash[:64], 16))
    mcc = hex(int(hash[64:], 16))
    return mpk, mcc        
        
        
def getBinMnemPhrase(word_list_indices):
    mp = ''
    for index in word_list_indices:
        mp += pad(bin(index)[2:],11)
    return mp
              
def G2R(word_list_indices): 
    #Generate binary mnemonic phrase
    mnem_phrase = getBinMnemPhrase(word_list_indices)
    #Get root seed
    seed = applySRFG(mnem_phrase)
    #Get private key and chain code
    privKey,cCode = hmacCocktail(seed) 
    return (hex(int(seed,2)),privKey,cCode)    