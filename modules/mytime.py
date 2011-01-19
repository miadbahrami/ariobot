#coding: utf-8
from time import strftime
from calverter import Calverter

def time():
    return strftime("%X")

def miladi():
    return strftime("%Y/%m/%d")

def shamsi():
    lm = miladi().split("/")
    ldate = Calverter().gregorian_to_iranian(int(lm[0]), int(lm[1]), int(lm[2]))[:-1]
    return "/".join(ldate)

def weekday():
    lm = miladi().split("/")
    return Calverter().gregorian_to_iranian(int(lm[0]), int(lm[1]), int(lm[2]))[-1]