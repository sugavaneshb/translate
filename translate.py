#! /usr/bin/python

'''
This is a command line tool to use google translate to translate words from terminal
'''
import sys, urllib2

DEFAULT_TARGET_LANG="en"
target_lang=DEFAULT_TARGET_LANG
source_lang="auto"

opener = urllib2.build_opener()
opener.addheaders=[('User-agent', 'Mozilla/5.0')]


def translate(text):
    length=len(text)
    translate_text=" ".join(text)
    print "The text to be translated..",translate_text
    url_part2 = translate_text.replace(" ", "%20")
    url_part1="http://translate.google.com/translate_a/t?client=t&text="
    url_part3="&hl=en&sl=en&tl=ta&ie=UTF-8&oe=UTF-8&multires=1&otf=2&ssel=0&tsel=0&sc=1"
    print("Fetching results from Google Translate...\n.\n.")
    fetchurl=url_part1 + url_part2 + url_part3
    op=opener.open(fetchurl).read()
    print op.split(',')[0][3:]
    #print op.split(',')[0]


if __name__ == '__main__':
    #print 'Enter the string to be translated',
    length=len(sys.argv)
    if length == 1:
        print("We need a string to translate.. Try translate.py --help")
    elif length == 2:
        if sys.argv[1] == '--help':
            print('Syntax: translate.py [<string to be translated>] [<Source Language>] [<Target language>]\n if source missing, use auto \n if target missing use DEFAULT_TARGET_LANG=en')
            sys.exit()
      # else:
      #     translate(sys.argv[1])
    elif length == 3:
        source_lang = sys.argv[2]
    else:
        source_lang = sys.argv[2]
        target_lang = sys.argv[3]
    translate(sys.argv[1:])
