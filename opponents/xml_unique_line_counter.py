#!/usr/bin/env python

# To use: python xml_unique_line_counter.py --file C:\file_path_here\GitHub\spni.github.io\opponents\character_name\behaviour.xml
# Verbose: python xml_unique_line_counter.py --file C:\file_path_here\GitHub\spni.github.io\opponents\character_name\behaviour.xml --verbose

# Parser:
# pip install html5lib
# pip install beautifulsoup4


from bs4 import BeautifulSoup
import os
import sys
import getopt
import logging
from collections import Counter

logger = logging.getLogger(os.path.basename(__file__))


def parse(f):

    l_ = []
    with open(f, 'r') as hlr:
        f_ = hlr.read()

    logger.debug("Read file: ******")
    logger.debug(f_)

    logger.debug("Parsing now: ******")
    soup = BeautifulSoup(f_, 'html5lib')
    for c, s in enumerate(soup.find_all('state')):
        text_ = s.text.strip()
        logger.debug('Found text: {}. Count: {}'.format(text_.encode('utf-8'), c))
        l_.append(text_)
    logger.debug('****  Count *****')
    d = dict(Counter(l_))
    ctr = 1

    for k, v in d.iteritems():
        logger.info('{} --> Count: {}, Line count: {}'.format(k.encode('utf-8'), v, ctr))
        ctr += 1
    logger.info('Unique dialogue count: {}'.format(len(d)))


if __name__ == '__main__':
    verbose = None

    log_file = os.path.join(os.path.dirname(__file__),"output.log")
    file_hndlr = logging.FileHandler(log_file)
    logger.addHandler(file_hndlr)
    console = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(console)
    ch = logging.Formatter('[%(levelname)s] %(message)s')
    console.setFormatter(ch)
    file_hndlr.setFormatter(ch)

    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "d:vf:", ["download=", "verbose", "file="])
    for opt, arg in opts:
        if opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-f", "--file"):
            file_ = arg

    if verbose:
        logger.setLevel(logging.getLevelName('DEBUG'))
    else:
        logger.setLevel(logging.getLevelName('INFO'))
    logger.debug('CLI args: {}'.format(opts))
    parse(file_)
