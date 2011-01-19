from modules.mytime import weekday
from modules.mytime import shamsi
from time import strftime

def withoutPhrase(msg, channel, id):
    msgDic = {
        "!help":  "%s, https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands" % id,
        "!about": "%s, My name is Gholam, I was born in 28 December 2010 and I'm written in python." % id,
        "!date": "%s, %s - %s" % (id, weekday(), shamsi()),
        "!time": "%s, %s" % (id, strftime("%X")),
        "!author": "%s, Amin Oruji - aminpy@gmail.com" % id 
    }
    
    return msgDic.get(msg)