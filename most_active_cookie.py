#!/usr/bin/python3
# Forrest bicker
# 1/29/22

import sys
from typing import List

from matplotlib.pyplot import get

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
    maxOccurences = max(cookieCount.values()) if cookieCount else 0
    return [cookie for cookie in cookieCount if cookieCount[cookie] == maxOccurences]

def most_active_cookies_from_file(filepath: str, date: str) -> List[str]:
    '''
    given a `filepath` to a well-formatted log file, and a `date` (as a string),
    return the cookie that was most active on that date, or most active cookies in the case
    of a tie.
    '''
    input_lines = read_lines(filepath)
    return get_cookies(input_lines, date)
        
def most_active_cookies_from_file_multipath(filepaths: List[str], date: str) -> List[str]:
    '''
    given a `filepath` to a well-formatted log file, and a `date` (as a string),
    return the cookie that was most active on that date, or most active cookies in the case
    of a tie.
    '''
    all_lines = []
    for file in filepaths:
        all_lines += read_lines(file)
    return get_cookies(all_lines, date)


def read_lines(filepath: str):
    with open(filepath, 'r') as f:
        try:
            lines = f.read().split('\n')
            assert lines[0] == "cookie,timestamp"  # ensure input file is in correct format
            return lines[1:]
        except FileNotFoundError:
            print(f"Specified file at {filepath} not found")
        except AssertionError:
            print("Input file is not in the correct format: header must read cookie,timestamp")

def get_input():
    try:
        assert 3 < len(sys.argv)  # ensure we have the right number of arguments
        assert sys.argv[2] == "-d"  # ensure the 2nd argument is the -d flag
        filepath = sys.argv[1]
        date = sys.argv[3]
        return filepath, date
    except AssertionError:
        print("Invalid arguments! Usage: ./most_active_cookie <filepath> -d <date>")

if __name__ == "__main__":
    filepath, date = get_input()
    for cookie in most_active_cookies_from_file_multipath():

        # for cookie in most_active_cookies_from_file_multipath(['test\\test_cookies_1.csv', 'test\\test_cookies_2.csv', 'test\\test_cookies_3.csv'], '2018-12-09'):
        print(cookie)
