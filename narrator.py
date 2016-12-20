#!/usr/bin/env python
import sys
import subprocess
import re

DEBUG = True
QUOTE_CHAR = "'"

def repl(text):
    #Clean up the text
    text = text.strip('\n')
    text = text.replace('-'," ")
    text += " "

    #Run regular expression to capture every other single quote
    #Actual regex is: "\W(.*?)\s"
    capture = "\W" + QUOTE_CHAR + "(.*?)" + QUOTE_CHAR + "\s"
    tokens = re.split(capture, text)
    # if DEBUG:
    #     # print tokens
    #     for p in tokens:
    #         print ">  ", p
    narrator = True
    n_voice = "Alex"
    c_voice = "Samantha"
    voice = n_voice
    for phrase in tokens:
        if(narrator):
            voice = n_voice
        else:
            voice = c_voice
        narrator = not narrator
        if DEBUG:
            print ("{} : {}".format(voice, phrase))
        subprocess.call(["say", "-v" + voice, phrase])
    exit()

def main(argv):
    if(len(argv) is 2):
        repl(argv[1])
    if(sys.stdin):
        repl(''.join([str(x).strip('\n-') for x in sys.stdin]))
    else:
        if(len(argv) != 2):
            print("Usage: narrator [word] \n help for more details")
        elif(argv[1] == "help"):
            print "Format your string like this: narrator 'character' <narrator>"

if __name__ == '__main__':
    main(sys.argv)
