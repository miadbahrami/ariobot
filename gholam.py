import socket
import foshes
from xgoogle.translate import Translator

# --------- connect

username = raw_input("username: ")
channel = raw_input("channel: ")
network = "irc.freenode.net"
port = 6667
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cr = "\r\n"
pc = 'PRIVMSG ' + channel + ' :'

irc.connect((network, port))

print irc.recv(4096)

irc.send("NICK " + username + cr)
irc.send("USER " + username + " " + username + " " + username + " :Python IRC" + cr)
irc.send("JOIN " + channel + cr)

# ------------ listen

counter = 1

while True:

    data = irc.recv(4096)
    
    if data.find('PING') != -1:

        pinger = data.split()[1]
        irc.send('PONG ' + pinger + cr)
        print 'PONG ' + pinger + cr
        
# ----------- welcome

    #elif data.find('JOIN') != -1:
        #lod = data.split("!")
        #who = lod[0]
        #who = who[1:]
        #if data.find(username + '!') == -1:
            #irc.send('PRIVMSG ' + channel + ' :' + who + ', be S.H.I.T (Some Hackers In Town) khosh umadi!\r\n')
            
    elif data.find(pc) != -1:
        lod = data.split("!")
        who = lod[0]
        who = who[1:]
        pm = 'PRIVMSG ' + who + ' :'

# -------------- help

        if data.find(':!help') != -1:
            if data.find(username + '!') == -1:
                irc.send(pm + "+----------------Menu---------------+" + cr)
                irc.send(pm + "| !help ~> Command List             |" + cr)
                irc.send(pm + "| !about ~> About Me                |" + cr)
                irc.send(pm + "| .w phrase ~> Wikipedia Search     |" + cr)
                irc.send(pm + "|-----------------------------------|" + cr)
                irc.send(pm + "|           --Translate--           |" + cr)
                irc.send(pm + "| en = english, fa = persian and ...|" + cr)
                irc.send(pm + "|    ---------examples----------    |" + cr)
                irc.send(pm + "| .enfa phrase ~> English to Farsi  |" + cr)
                irc.send(pm + "| .faen phrase ~> Farsi to English  |" + cr)
                irc.send(pm + "| .defa phrase ~> German to Farsi   |" + cr)
                irc.send(pm + "| .fade phrase ~> Farsi to German   |" + cr)
                irc.send(pm + "|               ...                 |" + cr)
                irc.send(pm + "+-----------------------------------+" + cr)

# ------------- khuruj

        elif data.find("!birun") != -1:
            irc.send(pc + "chashm :(\r\n")
            irc.send('QUIT\r\n')

# ---------------- about

        elif data.find(":!about") != -1:
            if data.find(username + "!") == -1:
                irc.send(pc + who + ', My name is ' + username + ', I was born in 28 December 2010 and I\'m written in python.' + cr)

# ---------- Translate

        elif data.find(':.') != -1:
            lod = data.split(":")
            who = lod[1].split("!")[0]
            lang = lod[2].split(" ")[0]
            
            ebarat = ' '.join(lod[2].split(" ")[1: ])
            if ebarat.endswith(cr):
                ebarat = ebarat[:-2]
            try:
                lt = lang[1:3]
                lf = lang[-2:]
                irc.send(pc + who + ', ' + Translator().translate(ebarat, lf, lt).encode("utf-8") + cr)
                    
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
                        irc.send(pc + who + ', kheyli bi adabi!!!' + cr)
                    except Exception, e:
                        print e
                    break

    print data
    print str(counter) + ")=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
    counter += 1
