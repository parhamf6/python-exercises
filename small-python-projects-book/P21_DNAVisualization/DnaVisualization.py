import random,sys,time

pause = 0.2
rows = [
    # 123456789
    '          ##',
    '         #{}-{}#',
    '        #{}---{}#',
    '       #{}-----{}#',
    '      #{}-----{}#',
    '     #{}-----{}#',
    '     #{}-----{}#',
    '      #{}-----{}#',
    '        #{}---{}#',
    '         #{}-{}#',
    '           ##',
    '         #{}-{}#',
    '        #{}---{}#',
    '       #{}-----{}#',
    '      #{}-----{}#',
    '      #{}-----{}#',
    '       #{}-----{}#',
    '        #{}-----{}#',
    '         #{}-----{}#',
    '          #{}---{}#',
    '          #{}-{}#',
    '           ##',
    #123456789
]
try:
    print("Dna visualization")
    print("Ctrl=C to exit")
    rowIndex = 0
    while True:
        rowIndex = rowIndex + 1
        if rowIndex == len(rows):
            rowIndex = 0
        if rowIndex==0 or rowIndex==9:
            print(rows[rowIndex])
            continue
        randomSelection = random.randint(1,4)
        if randomSelection == 1:
            leftNucleotide , RighNucleotide = 'A' , 'T'
        elif randomSelection== 2 :
            leftNucleotide,RighNucleotide = 'T' , 'A'
        elif randomSelection==3:
            leftNucleotide,RighNucleotide = 'C' , 'G'
        elif randomSelection==4:
            leftNucleotide,RighNucleotide = 'G' , 'C'
        print(rows[rowIndex].format(leftNucleotide,RighNucleotide))
        time.sleep(pause)
except KeyboardInterrupt:
    sys.exit()