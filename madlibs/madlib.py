#madlib.py - this program acts like a traditional madlib program
#NOTE:
#Point storyFile variable to .txt on your machine
#Point newStoryFile to .txt on your machine

import re

#TODO - read the text file and grab string
storyFile = open('/Users/obrown/Documents/automate/madlibs/story.txt')
madlibMode = storyFile.read()
storyFile.close()

#string to list to make editing easier
stringToList = madlibMode.split()


#adding a regex for diff scenarios (aka punctuation)
posRegex = re.compile(r'.*ADJECTIVE|VERB|ADVERB|NOUN.*', re.I)
punctRegex = re.compile(r'\.|,')

hasPunct = False

#checks anywhere ADJ, VERB, NOUN, ADV appears
for current in range(len(stringToList)):
    if posRegex.search(stringToList[current]) != None:

        #check for punctuation if the regex finds something with punct
        #replace it with with a space in order for it to go to the next space
        if punctRegex.search(stringToList[current]) != None:

            #LEARN - I need to replace the subbed word, I didn't tell it to
            #do that, which is why it would do what I wanted.
            removedPunct = punctRegex.sub(r'',stringToList[current])
            stringToList[current] = removedPunct

            #a trigger to replace punctuation
            hasPunct = True
                       
        #ask user to change the word
        #adjective shows stuup, prompt user and ask for new word. rewrite
        print('Enter ' + stringToList[current].lower() + ': ')
        stringToList[current] = input()

        #replace the punctuation in the madlibbed word,
        #NOT COMPLETE - since it only does periods
        if hasPunct == True:
            stringToList[current] = stringToList[current] + '.'
            hasPunct = False
            

#take modified list and rejoin it to string
madlibbedMode = ' '.join(stringToList)


#create new file and open it in write mode
#write the now joined string from the list
#close the new story file
newStoryFile = open('story-complete.txt', 'w')
newStoryFile.write(madlibbedMode)
newStoryFile.close()


