from modules.mytime import weekday
from modules.mytime import shamsi
from time import strftime
from modules.dpaste import paste
import sys

def withoutPhrase(msg, channel, id):
    
    msgDic = {
        "!help":  "%s, %s" % (id, "%splain/" % pasteIt()),
        "!about": "%s, My name is Gholam, I was born in 28 December 2010 and I'm written in python." % id,
        "!date": "%s, %s - %s" % (id, weekday(), shamsi()),
        "!time": "%s, %s" % (id, strftime("%X")),
        "!author": "%s, Amin Oruji - aminpy@gmail.com" % id 
    }
    
    
    return msgDic.get(msg)

def pasteIt():
    f = open("%s/help.txt" % sys.path[0], "r")
    data = f.read()
    f.close() 
    return paste(data, "Python")
    