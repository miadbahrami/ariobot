#coding: utf-8
from time import strftime
from calverter import Calverter

def shamsi():
    lm = strftime("%Y/%m/%d").split("/")
    ldate = Calverter().gregorian_to_iranian(int(lm[0]), int(lm[1]), int(lm[2]))[:-1]
    return "/".join(ldate)

def weekday():
    lm = strftime("%Y/%m/%d").split("/")
    return Calverter().gregorian_to_iranian(int(lm[0]), int(lm[1]), int(lm[2]))[-1]