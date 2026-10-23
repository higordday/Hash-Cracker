
from argparse import ArgumentParser
from hashlib import sha1, sha224, sha256, sha384, sha512, md5
from threading import Thread
from colorama import Fore, init
from os.path import exists, isfile, basename
from time import sleep
from sys import exit

import os

# ---

if (os.name == 'nt'): init(convert = True)

# ---

VALID_HASH_FORMATS = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'md5']

# ---

hasher = {
    'sha1': locals()['sha1'], 'sha224': locals()['sha224'], 'sha256': locals()['sha256'], 'sha384': locals()['sha384'], 'sha512': locals()['sha512'], 'md5': locals()['md5']
}

# ---

def parser_config():

    parser = ArgumentParser(description = None)

    parser.add_argument('-v', '--hashes', required = True, type = str, help = 'Hashes (Unique, Multiple, Text List)')
    parser.add_argument('-f', '--default-format', type = str, help = 'Default Format')
    parser.add_argument('-w', '--wordlist', required = True, type = str, help = 'Wordlist')

    arguments = parser.parse_args()

    return (
        arguments.hashes, arguments.default_format, arguments.wordlist
    )

# ---

(hashes, default_format, wordlist) = parser_config()

# ---

if ((exists(wordlist) is False) or (isfile(wordlist) is False)):

    exit(f'{Fore.RED}[x Error]{Fore.RESET} Invalid Wordlist File ({basename(wordlist)})')

# ---

if ((default_format) and (default_format.lower() not in VALID_HASH_FORMATS)):

    exit(f'{Fore.RED}[x Error]{Fore.RESET} Invalid Hash Format ({default_format}) - Valid: {", ".join(VALID_HASH_FORMATS)}')

# ---

h = []

if ((exists(hashes) is True) and (isfile(hashes) is True)):
    with open (hashes, 'r', encoding = 'utf-8') as r:

        for item in r.readlines(): h.append(item.strip('\n'))

elif (':' in hashes):

    h = hashes.split(':')

else:

    h.append(hashes)

hashes = h

# ---

class cracker:

    def crack(self, hashed_content, thread_identifier):

        (self.hashed_content, self.thread_identifier) = (hashed_content, thread_identifier)

        print(f'{Fore.BLUE}[*]{Fore.RESET} Trying to crack the following hash: {self.hashed_content}')

        status = False

        with open (wordlist, 'r', encoding = 'utf-8') as r:
            for item in r.readlines():

                striped_wordlist_item = item.strip('\n')

                (found, _format_) = self.test(striped_wordlist_item)

                if (found is False): continue

                status = True

                print(f'{Fore.GREEN}[+ Success]{Fore.RESET} Hash: {self.hashed_content} - Value: {striped_wordlist_item} - Format: {_format_}')

                break

        if (status is False):
            print(f'{Fore.YELLOW}[!]{Fore.RESET} Nothing found ({self.hashed_content})')

    def test(self, wordlist_item):

        hashed_wordlist_item = None

        if (default_format):

            hashed_wordlist_item = hasher[default_format.lower()](wordlist_item.encode('utf-8')).hexdigest()

            if (hashed_wordlist_item == self.hashed_content): return (True, default_format)

        else:
            for hash_format in VALID_HASH_FORMATS:

                hashed_wordlist_item = hasher[hash_format](wordlist_item.encode('utf-8')).hexdigest()

                if (hashed_wordlist_item == self.hashed_content): return (True, hash_format)

        return (False, None)

# ---

if (__name__ == '__main__'):

    cker = cracker()

    thread_identifier = 1

    for hashed_content in hashes:
        Thread(target = cker.crack, args = (hashed_content, thread_identifier,)).start()

        thread_identifier += 1

        sleep(3)