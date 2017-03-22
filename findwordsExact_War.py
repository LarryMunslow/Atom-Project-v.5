# This program will search input text content and count the words that match
# positive and negative word lists

#
# open the postive and negative list files and store the data into a structure.
# The list will need to store the word and a count field. The count field is
# always a positive number.
# imports
import sys
import matplotlib as mpl
import re


#

# data structures and classes
# wordElement class.
class WordElement():
    "Stores word and count"
    def __init__(self, word, n):
        self.word = word
        self.count = n

    def __iter__(self):
        return iter(self.word)

    def increment_count(self):
        self.count +=1



# store for WarEvent words with count
War_word_count = []

#
# end of data structure definitions
#
def exact_match(phrase, word):
    b = r'(\s|^|$)'
    return re.match(b + word + b, phrase)

# variable to hold positive words and count field

# debug lines below to show word in lists
#for i in range(0,3):
#    print "%d: %s" % (i, negative_word_count[i].word)


# read War.rtf
pf = open('War.rtf')
# loop reading each line
for i, line in enumerate(pf):
    data = line.strip()
    War_word_count.append(WordElement(data, 0))

# search for a string
#searchfile('content.rtf', 'This')
pcontent = open('content.txt', 'rt')

# look for positive words first
#[findwrd(obj, line) for x, obj in enumerate(positive_word_count) for line
# in pcontent]
for line in pcontent:
    sentence_words = line.split()
    for wrd in sentence_words:
        wrd = wrd.strip('.,!?:;()_-')
        wrd = wrd.lower()
        #print "{0}".format(wrd)


        for newobj1 in War_word_count:
            if exact_match(wrd, newobj1.word) != None:
                newobj1.increment_count()



for obj in War_word_count:
    if obj.count > 0:
        print "{0}".format(obj.word)
        print "{0}".format(obj.count)


War_total_count = 0

for obj in War_word_count:
    War_total_count += obj.count

print " Total War count is {0}".format(War_total_count)


#plot stuff
