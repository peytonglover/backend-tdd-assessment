#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "???"

import argparse
import sys

def to_upper(text):
    result = text.upper()
    return result

def to_lower(text):
    result = text.lower()
    return result

def to_title(text):
    result = text.title()
    return result

def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    # your code here
    parser = argparse.ArgumentParser(description='Perform transformation on input text.')
    
    parser.add_argument('-u', '--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true', help='convert text to titlecase')
    parser.add_argument('text', help='text to be manipulated')
    return parser 

def main(args):
    """Implementation of echo"""
    # your code here
    parser = create_parser()
    ns = parser.parse_args(args)
    
    _upper = ns.upper
    _lower = ns.lower
    _title = ns.title
    text = ns.text
    
    if _upper:
        to_upper(text)
    elif _lower:
        to_lower(text)
    elif _title:
        to_title(text)

    
    return


if __name__ == '__main__':
    main(sys.argv[1:])
