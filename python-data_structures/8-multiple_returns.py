#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
