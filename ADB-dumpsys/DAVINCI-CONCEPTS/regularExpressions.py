__author__ = 'barin.huseyin'

import re


def templateRegularExpression():
    table = set()
    table.add("\b -- boundary between word and non-word ")


def keynotes():
    # REPLACING ANY VALUE IN A STRING
    print re.sub("king$", "not the human", "any string....")


def test_patterns(input, patterns=[]):
    # print "".join(str(i/10 or ' ' for i in range(len(input()))))
    # print "".join(str(i%10 for i in range(len(input()))))
    print input

    for pattern in patterns:
        for match in re.finditer(pattern, input):
            s = match.start()
            e = match.end()
            print 'Between %d and %d  in the input "%s"' % (s, e, input[s:e])
    return


def test():
    text = "This is testing purpose so this is sparta this this"

    patterns = ["this", "that"]

    for pattern in patterns:
        if re.search(pattern, text):
            match = re.search(pattern, text)
            print match.start(), "and ", match.end()
            print 'The string "%s"  in the text "%s" is found %d to %d  so ("%s")' % (
            pattern, text, match.start(), match.end(), text[match.start():match.end()])
            print("hopp", "end=\n\n")

    # multiple matches

    tempText = "ababablksdfalflakjsflaabaababakjalfabababab"

    for match in re.findall("ab", tempText):  #findall returns only substrings from input overlapping pattern.
        print match

    for match in re.finditer("ab", tempText):  #finditer returns   Match instance instead of substring
        s = match.start()
        e = match.end()
        print "the match is ", tempText[s:e]


def test2():
    test_patterns("abbaaabbbbaaaaa", ["ab", "ab*", "+ab+"])


def showRegexResult(s, patterns):
    for patter in patterns:
        print ""


def exercises():
    # replacing string in a
    s = "101 broad"

    print re.sub("road$", "rd.", s)  # yep as you can see, we can want a specific regular expression

    print re.sub("\\broad$", "rd.", s)  # \b


def main():
    # print dir(re.sub)
    # exercises()
    test2()


if __name__ == "__main__": main()