import random

def load_words(WORDLIST_FILENAME):
       print ("Loading word list from file...")
       wordlist = list()
       # 'with' can automate finish 'open' and 'close' file
       with open(WORDLIST_FILENAME) as f:
            # fetch one line each time, include '\n'
            for line in f:
                # strip '\n', then append it to wordlist
                wordlist.append(line.rstrip('\n'))
       print (" ", len(wordlist)), "words loaded."
       return wordlist

wordlist = load_words('wordlst.txt')




def generateMnemonic (mnemLength) :

    nemMnem = []
    i = 0;

    if mnemLength == 12 or mnemLength == 24:
        while i < mnemLength:
            nemMnem.append(random.choice(wordlist))
            i = i+1

    mnemonic = ' '.join(nemMnem)
    return mnemonic
    # lists words divided by 'space'



mnemonic = generateMnemonic(12)

