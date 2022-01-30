#!/usr/bin/python3
# Forrest bicker
# 1/29/22

import sys
import os.path
from typing import List

def get_cookies(lines: List[str], date: str) -> List[str]:
    '''
    given a list of `lines` containing cookie,timestamp pairs, and a `date` (as a string),
    return the cookie that was most active on that date, or most active cookies in the case
    of a tie.
    '''
    # iterate through log file and count the number of times each cookie appears
    cookieCount = {}  # mapping from cookie to number of occurences
    for line in lines:
            cookie, timestamp = line.split(',')
            if timestamp[:10] == date:  # only count cookies from the given date
                if cookie not in cookieCount:
                    cookieCount[cookie] = 0

                cookieCount[cookie] += 1

    # print cookie with most occurences, including those tied for most occurences
    # runs in in O(n) time and O(n) space
    maxOccurences = max(cookieCount.values())
    return [cookie for cookie in cookieCount if cookieCount[cookie] == maxOccurences]

def most_active_cookies_from_file(filepath: str, date: str) -> List[str]:
    '''
    given a `filepath` to a well-formatted log file, and a `date` (as a string),
    return the cookie that was most active on that date, or most active cookies in the case
    of a tie.
    '''
    try:
        with open(filepath, 'r') as f:
            lines = f.read().split('\n')
            assert lines[0] == "cookie,timestamp"  # ensure input file is in correct format
            return get_cookies(lines[1:], date)

    except FileNotFoundError:
        print(f"Specified file at {filepath} not found")
    except AssertionError:
        print("Input file is not in the correct format: header must read cookie,timestamp")

    

if __name__ == "__main__":
    try:
        assert 3 < len(sys.argv) # ensure we have the right number of arguments
        assert sys.argv[2] == "-d" # ensure the 2nd argument is the -d flag
        filepath = sys.argv[1]
        date = sys.argv[3]
    except AssertionError:
        print("Invalid arguments! Usage: ./most_active_cookie <filepath> -d <date>")
            
    for cookie in most_active_cookies_from_file(filepath, date):
        print(cookie)

