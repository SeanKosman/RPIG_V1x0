import random
import datetime

def rpigVow():

    phonInvent = []

    #Vowel shapes
    # Y     Triponticular           0   no mid vowels
    # V     Vesticular              1   no categories missing (7 and 8 too)
    # 4     Antidereculum           2   sub high back
    # C     Anticentrodereculum     3   sub mid back
    # |     Vertical                4   a ə or æ e i
    # H     Boxular                 5   sub low
    # >     Trioblong               6   a i o

    vShape = random.randint(0,8)

    '''    
    Vowel shapes
    '''

    if (vShape == 0):

        bottomShape = random.randint(1,4)
        #Bottom Shape
        #1      a
        #2      æ
        #3      ɑ
        #4      æ ɑ
        if bottomShape == 1:
            phonInvent.append("a")
        elif bottomShape == 2:
            phonInvent.append("æ")
        elif bottomShape == 3:
            phonInvent.append("ɑ")
        else:
            phonInvent.extend(["æ","ɑ"])

        phonInvent.append("#")

        schwa = random.randint(1,100)
        if (schwa <= 22):
            phonInvent.append("ə")
            phonInvent.append("#")


        phonInvent.append("i")
        
        frontRound = random.randint(1,100)
        if (frontRound <= 6):
            phonInvent.append("y")

        barredI = random.randint(1,100)
        if (barredI <= 16):
            phonInvent.append("ɨ")

        phonInvent.append("u")

    elif (vShape == 1) or (vShape == 2) or (vShape == 3) or (vShape > 6):
        
        bottomShape = random.randint(1,2)
        #Bottom Shape
        #1      a
        #2      æ ɑ
        if bottomShape == 1:
            phonInvent.append("a")
        else:
            phonInvent.extend(["æ","ɑ"])

        phonInvent.append("#")

        laxHigh = random.randint(-1,2)#Normal mid are lax equivalent
        laxMid = random.randint(-1,2)#Normal mid are lax equivalent
        frontRound = random.randint(1,100)#1 to 6 = both, 7 to 9 = high only, 10 to 11 = mid only, other = not present
        backRound = random.randint(1,100)#Same as above
        
        #Start with e
        if(laxMid > 0):
            if (laxMid == 1):#Just do ɛ
                phonInvent.append("ɛ")
            else:#Do both
                phonInvent.extend(["e","ɛ"])
        else:#Just do e
            phonInvent.append("e")
      
        #ø
        if (frontRound <= 6) or (frontRound == 10 or frontRound == 11):
            if(laxMid > 0):
                if (laxMid == 1):#Just do œ
                    phonInvent.append("œ")
                else:#Do both
                    phonInvent.extend(["ø","œ"])
            else:
                phonInvent.append("ø")

        schwa = random.randint(1,100)
        if (schwa <= 22):
            phonInvent.append("ə")

        if (vShape != 3):    
            #ʌ
            if (backRound <= 6) or (backRound == 10 or backRound == 11):
                if(laxMid > 0):
                    if (laxMid == 1):#Just do ɛ
                        phonInvent.append("ʌ")
                    else:#Do both
                        phonInvent.extend(["ɤ","ʌ"])
                else:
                    phonInvent.append("ɤ")

            #o
            if(laxMid > 0):
                if (laxMid == 1):#Just do ɔ
                    phonInvent.append("ɔ")
                else:#Do both
                    phonInvent.extend(["o","ɔ"])
            else:#Just do o
                phonInvent.append("o")

        phonInvent.append("#")

        #i
        if(laxHigh > 0):
            if (laxHigh == 1):#Just do ɛ
                phonInvent.append("ɪ")
            else:#Do both
                phonInvent.extend(["i","ɪ"])
        else:#Just do e
            phonInvent.append("i")

        #y
        if (frontRound <= 9):
            phonInvent.append("y")

        barredI = random.randint(1,100)
        if (barredI <= 16):
            phonInvent.append("ɨ")

        barredU = random.randint(1,100)
        if (barredU <= 2):
            phonInvent.append("ʉ")

        if (vShape != 2):
            if (backRound <= 9):
                phonInvent.append("ɯ")

            if (laxHigh > 0):
                if (laxHigh == 1):#Just do ʊ
                    phonInvent.append("ʊ")
                else:#Do both
                    phonInvent.extend(["u","ʊ"])
            else:#Just do u
                phonInvent.append("u")

    elif vShape == 4:#Vertical TAKES ONLY LONG
        vertForm = random.randint(0,1)
        if (vertForm):#Ubykh form
            phonInvent.extend(["a","#","ə"])
        else:#Wichita form
            if (random.randint(0,1)):#LOW
                phonInvent.append("a")
            else:
                phonInvent.append("æ")
            phonInvent.append("#")
            if (random.randint(0,1)):#MID
                phonInvent.append("e")
            else:
                phonInvent.append("ɛ")
            phonInvent.append("#")
            if (random.randint(0,1)):#HIGH
                phonInvent.append("i")
            else:
                phonInvent.append("ɪ")
    
    elif vShape == 5:#Boxular TAKES NO SUB ARTIC
        if (random.randint(0,1)):#Tense
            phonInvent.extend(["e","o","#","i","u"])
        else:#Lax
            phonInvent.extend(["ɛ","ɔ","#","ɪ","ʊ"])

    else:#vShape = 6 TAKES NO SUB ARTIC
        phonInvent.extend(["a","#","o","#","i"])

    return phonInvent
    

def printPhonemes(phonInv):#prints out stuff based on if a # is included or not
    
    heightLists = []#stores the phonemes at different vowel heights
    phonAtLvl = ""#stores the phonemes at a certain height
    phonLen = len(phonInv) - 1

    for item in phonInv:
        if item == "#":
            heightLists.append(phonAtLvl)
            phonAtLvl = ""
        elif phonInv.index(item) == phonLen:
            phonAtLvl = phonAtLvl + item
            heightLists.append(phonAtLvl) 
        else:
            phonAtLvl = phonAtLvl + item + "  "

    heightLists.reverse()

    for lvl in heightLists:
        print(lvl, "\t")
    

#main()
start = datetime.datetime.now()
phons = rpigVow()
printPhonemes(phons)
finish = datetime.datetime.now()
print("RPIG VOWEL COMPLETED WITH:   ", finish - start)