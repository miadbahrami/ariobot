import socket
import foshes
from xgoogle.search import GoogleSearch, SearchError
from xgoogle.translate import Translator

# --------- connect

username = raw_input("username: ")
channel = raw_input("channel: ")
network = 'irc.freenode.net'
port = 6667
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

irc.connect((network, port))

print irc.recv(4096)

irc.send('NICK ' + username + '\r\n')
irc.send('USER ' + username + " " + username + " " + username + ' :Python IRC\r\n')
irc.send('JOIN ' + channel + '\r\n')

# ------------ listen

counter = 1

while True:

    data = irc.recv(4096)
    
    if data.find('PING') != -1:
        
        pinger = data.split()[1]
        irc.send('PONG ' + pinger + '\r\n')
        print 'PONG ' + pinger + '\r\n'
        
# ----------- welcome

    #elif data.find('JOIN') != -1:
        #lod = data.split("!")
        #who = lod[0]
        #who = who[1:]
        #if data.find(username + '!') == -1:
            #irc.send('PRIVMSG ' + channel + ' :' + who + ', be S.H.I.T (Some Hackers In Town) khosh umadi!\r\n')
            
    elif data.find(" PRIVMSG " + channel + " :") != -1:
        if data.find(" PRIVMSG " + channel + " :" + username) != -1:
            pass

        else:
            
# -------------- help

            if data.find(':!help') != -1:
                lod = data.split("!")
                who = lod[0]
                who = who[1:]
                if data.find(username + '!') == -1:
                    irc.send('PRIVMSG ' + who + ' :+----------------Menu---------------+\r\n')
                    irc.send('PRIVMSG ' + who + ' :| !help ~> Command List             |\r\n')
                    irc.send('PRIVMSG ' + who + ' :| !about ~> About Me                |\r\n')
                    irc.send('PRIVMSG ' + who + ' :| .w phrase ~> Wikipedia Search     |\r\n')
                    irc.send('PRIVMSG ' + who + ' :|-----------------------------------|\r\n')
                    irc.send('PRIVMSG ' + who + ' :|           --Translate--           |\r\n')
                    irc.send('PRIVMSG ' + who + ' :| en = english, fa = persian and ...|\r\n')
                    irc.send('PRIVMSG ' + who + ' :|    ---------examples----------    |\r\n')
                    irc.send('PRIVMSG ' + who + ' :| .enfa phrase ~> English to Farsi  |\r\n')
                    irc.send('PRIVMSG ' + who + ' :| .faen phrase ~> Farsi to English  |\r\n')
                    irc.send('PRIVMSG ' + who + ' :| .defa phrase ~> German to Farsi   |\r\n')
                    irc.send('PRIVMSG ' + who + ' :| .fade phrase ~> Farsi to German   |\r\n')
                    irc.send('PRIVMSG ' + who + ' :|               ...                 |\r\n')
                    irc.send('PRIVMSG ' + who + ' :+-----------------------------------+\r\n')


# ------------- khuruj

            elif data.find('!birun') != -1:
                irc.send('PRIVMSG ' + channel + ' :chashm :(\r\n')
                irc.send('QUIT\r\n')

# ---------------- about

            elif data.find(':!about') != -1:
                lod = data.split("!")
                who = lod[0]
                who = who[1:]
                if data.find(username + '!') == -1:
                    irc.send('PRIVMSG ' + channel + ' :' + who + ', My name is ' + username + ', I was born in 28 December 2010 and I\'m written in python.\r\n')

# ---------- Translate

            elif data.find(':.') != -1:
                lod = data.split(":")
                who = lod[1].split("!")[0]
                lang = lod[2].split(" ")[0]
                ebarat = ' '.join(lod[2].split(" ")[1: ])
                if ebarat.endswith("\r\n"):
                    ebarat = ebarat[:-2]
                try:
                    if lang == ".w":
                        try:
                            gs = GoogleSearch(ebarat + " wikipedia")
                            gs.results_per_page = 5
                            results = gs.get_results()
                            for res in results:
                                if "http://en.wikipedia.org" in res.url.encode("utf8") or "http://fa.wikipedia.org" in res.url.encode("utf8"):
                                    irc.send('PRIVMSG ' + channel + ' :' + who + ', ' + res.url.encode("utf8") + '\r\n')
                                    break
                        except SearchError, e:
                            print "Search failed: %s" % e
                            
                    else:
                        lt = lang[1:3]
                        lf = lang[-2:]
                        irc.send('PRIVMSG ' + channel + ' :' + who + ', ' + Translator().translate(ebarat, lf, lt).encode("utf-8") + '\r\n')
                        
                except Exception, e:
                    print e

# ------------- ping username

    if counter >= 12:
        for s in foshes.foshes:
            if data.find(s):
                if foshes.isFosh(s, data):
                    try:
                        lod = data.split(":")
                        who = lod[1].split("!")[0]
                        irc.send('PRIVMSG ' + channel + ' :' + who + ', kheyli bi adabi!!!\r\n')
                    except Exception, e:
                        print e
                    break

    print data
    print str(counter) + ")=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
    counter += 1
