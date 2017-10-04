# -------------------------------------------------------------------------------------------------------------------
# this is a alpha version. need more work
# writen by Arian Heydari
#
# this program change wrong keyboard language between farsi and english language. for example, It should change
# "hsl lk Hvdk hsj" to farsi like this "اسم من آرین است" and "hi my name is Arian" should remain as what it is.
#
# things that i should add and fix:
#    words list are bad (need better words list)
#    add auto learn new words
# -------------------------------------------------------------------------------------------------------------------

def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        pos = 0
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            pos = midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def lang_exchange(string):
    dict = {
        u'a': u'ش',
        u'b': u'ذ',
        u'c': u'ز',
        u'd': u'ی',
        u'e': u'ث',
        u'f': u'ب',
        u'g': u'ل',
        u'h': u'ا',
        u'i': u'ه',
        u'j': u'ت',
        u'k': u'ن',
        u'l': u'م',
        u'm': u'ئ',
        u'n': u'د',
        u'o': u'خ',
        u'p': u'ح',
        u'q': u'ض',
        u'r': u'ق',
        u's': u'س',
        u't': u'ف',
        u'u': u'ع',
        u'v': u'ر',
        u'w': u'ص',
        u'x': u'ط',
        u'y': u'غ',
        u'z': u'ظ',
        u'A': u'َ',
        u'B': u'إ',
        u'C': u'ژ',
        u'D': u'ِ',
        u'E': u'ٍ',
        u'F': u'ّ',
        u'G': u'ۀ',
        u'H': u'آ',
        u'I': u']',
        u'J': u'ـ',
        u'K': u'«',
        u'L': u'»',
        u'M': u'ء',
        u'N': u'أ',
        u'O': u'[',
        u'P': u'\\',
        u'Q': u'ً',
        u'R': u'ريال',
        u'S': u'ُ',
        u'T': u'،',
        u'U': u',',
        u'V': u'ؤ',
        u'W': u'ٌ',
        u'X': u'ي',
        u'Y': u'؛',
        u'Z': u'ة',
        u';': u'ک',
        u'\'': u'گ',
        u',': u'و',
        u'.': u'.',
        u'/': u'/',
        u'[': u'ج',
        u']': u'چ',
        u'\\': u'پ',
        u':': u':',
        u'"': u'"',
        u'<': u'<',
        u'>': u'>',
        u'?': u'؟',
        u'{': u'}',
        u'}': u'{',
        u'|': u'|',
        u'`': u'÷',
        u'1': u'1',
        u'2': u'2',
        u'3': u'3',
        u'4': u'4',
        u'5': u'5',
        u'6': u'6',
        u'7': u'7',
        u'8': u'8',
        u'9': u'9',
        u'0': u'0',
        u'-': u'-',
        u'=': u'=',
        u'~': u'×',
        u'!': u'!',
        u'@': u'@',
        u'#': u'#',
        u'$': u'$',
        u'%': u'%',
        u'^': u'^',
        u'&': u'&',
        u'*': u'*',
        u'(': u')',
        u')': u'(',
        u'_': u'_',
        u'+': u'+',
        u' ': u' ',
    }
    rdict = {v: k for k, v in dict.items()}
    newString = ''
    for i in range(len(string)):
        if string[i] in dict:
            newString += dict[string[i]]
        elif string[i] in rdict:
            newString += rdict[string[i]]
        else:
            newString += string[i]
    return newString

print("Whait a bit please. loading data...")
# LOAD DATA -------------
enChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', ]
englishWordsFile = open("en.words.txt", 'r')
englishWordsList = englishWordsFile.read().split(',')
englishWordsFile.close()

faChars = [u'ظ', u'ط', u'ز', u'ر', u'ذ', u'د', u'ئ', u'و', u'ش', u'س', u'ی', u'ب', u'ل', u'ا', u'ت', u'ن', u'م', u'ک',
          u'گ', u'ض', u'ص',
          u'ث', u'ق', u'ف', u'غ', u'ع', u'ه', u'خ', u'ح', u'ج', u'چ', u'پ', u'ة', u'ي', u'ژ', u'ؤ', u'إ', u'أ', u'ء',
          u'َ', u'ُ', u'ِ', u'ّ',
          u'ۀ', u'آ', u'ـ', u'«', u'»', u'ً', u'ٌ', u'ٍ', u'ريال', u'،', u'؛', u',', u']', u'[', u'×', ]
farsiWordsFile = open("fa.words.txt", "r", encoding="utf-8")
farsiWordsList = farsiWordsFile.read().split(u',')
farsiWordsFile.close()

# INPUT ---------------
def translate(input_data):
    rowInput = input_data
    splitInput = rowInput.split()
    enWordsNumbers = 0
    faWordsNumbers = 0
    otherWordsNumbers = 0
    allWords = 0
    allChar = 0
    englishChar = 0
    farsiChar = 0
    for x in splitInput:
        allWords += 1
        for i in x:
            allChar += 1
            if i in enChars:
                englishChar += 1
            if i in faChars:
                farsiChar += 1
        if binary_search(farsiWordsList, x):
            faWordsNumbers += 1
        elif binary_search(englishWordsList, x):
            enWordsNumbers += 1
        else:
            otherWordsNumbers += 1
    if farsiChar + englishChar * 2 >= allChar:
        if faWordsNumbers * 20 >= allWords or enWordsNumbers * 20 >= allWords:
            # it is farsi or english
            return rowInput
        else:
            translate_words = lang_exchange(rowInput)
            new_words = 0
            for words in translate_words.split():
                if binary_search(englishWordsList, words) or binary_search(farsiWordsList, words):
                    new_words += 1
            if new_words * 10 > len(translate_words.split()):
                    return translate_words
            return rowInput
    else:
        # it is other language
        print("fuck this sheet")
        return rowInput


print("Done. ready to use ,just type:")
while True:
    print(translate(input()))
