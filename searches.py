#!/usr/bin/env python3.6

import re


def matching_lines(keyword, decoded_html):
    """Return a list of lines in the string that contain a match of keyword."""
    return [line for line in decoded_html.splitlines() if keyword in line]


def keyword_found(keyword, string, ignore_case):
    """Return True if keyword is found in the html file, which is a string."""
    #return keyword in decoded_html_string
    if ignore_case:
        return isinstance(re.search(r'.*{}.*'.format(keyword), string, re.IGNORECASE).string, str)
    return isinstance(re.search(r'.*{}.*'.format(keyword), string).string, str)


def keyword(keyword, string, ignore_case):
    """Returns a regex match object if found.
    This can be used to extract the match for further analysis.
    """
    if ignore_case:
        return re.search(r'.*{}.*'.format(keyword), string, re.IGNORECASE)
    return re.search(r'.*{}.*'.format(keyword), string)


def tag(keyword, string, ignore_case=False):
    """Return the span of the enclosing tag containing the keyword if a match.."""
    if ignore_case:
        return re.search(r'.*(?P<tag>\<.*{}.*\>)'.format(keyword),
                         string, re.IGNORECASE).group('tag')
    return re.search(r'.*(?P<tag>\<.*{}.*\>)'.format(keyword), string).group('tag')


if __name__ == '__main__':
    pass
