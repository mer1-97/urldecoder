#!python3
#-*- coding: utf-8 -*-

"""
URL Decoder
Usage : python urldecoder.py [-h] or [-c] "string"
Options :
    -h      Print this help
    -c      Decode the string, copy to clipboard
"""

import sys
import subprocess
import urllib.parse

from time import sleep

def check_option(r_args):
    args = r_args
    copy = False

    if len(r_args) == 0:
        print(__doc__)
        sys.exit(1)

    for arg in r_args:
        if arg == '-c':
            copy = True
            args.remove('-c')      
        elif arg == '-h':
            print(__doc__)
            sys.exit(1)
    
    return copy, args

def url_decode(string):
    return urllib.parse.unquote(string, encoding='utf-8')

def string_copy(string):
    return subprocess.run(['clip.exe'], input=string.strip().encode('utf-16le'), check=True)

def main():
    copy, arg = check_option(sys.argv[1:])

    result = url_decode(arg[0])
    print('')
    if copy:
        string_copy(result)
        print('[+] Copy to clipboard done...')

    print('[!] Decode URL is.. {}'.format(result))

if __name__ == '__main__':
    main()
