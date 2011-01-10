#coding: utf-8
##   Copyright (C) 2010-2011 Amin Oruji (aminpy@gmail.com)
##
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2, or (at your option)
##   any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.

import socket
import foshes
from xgoogle.translate import Translator
from time import localtime
from time import strftime
from calverter import Calverter

# --------- connect

username = raw_input("username: ")
channel = raw_input("channel: ")
network = "irc.freenode.net"
port = 6667
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cr = "\r\n"
pc = 'PRIVMSG ' + channel + ' :'
zaman = ""
whoBot = ""

irc.connect((network, port))
data = irc.recv(4096)
print "recieve: " + strftime("%H:%M:%S", localtime()) + " (" + repr(data) + ")\n"

irc.send("NICK " + username + cr)
print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr("NICK " + username + cr) + ")"

irc.send("USER " + username + " " + username + " " + username + " :Python IRC" + cr)
print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr("USER " + username + " " + username + " " + username + " :Python IRC" + cr) + ")"

irc.send("JOIN " + channel + cr)
print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr("JOIN " + channel + cr) + ")"

# ------------ listen

counter = 1

while True:
    print "\nloop: " + strftime("%H:%M:%S", localtime()) + " =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=(" +str(counter) + ")\n"
    
    data = irc.recv(4096)
    print "recieve: " + strftime("%H:%M:%S", localtime()) + " (" + repr(data) + ")\n"
    
    if data.find("PING") != -1:

        pinger = data.split()[1]
        irc.send("PONG " + pinger + cr)
        print "send: " + strftime("%H:%M:%S", localtime()) + "(" + repr("PONG " + pinger + cr) + ")"
        
    if data.find(":" + username + "!~" + username) != -1 and data.find("JOIN :" + channel):
        zaman = strftime("%H:%M:%S | %A, %Y/%B/%d", localtime())

# ----------- welcome

    #elif data.find('JOIN') != -1:
        #lod = data.split("!")
        #who = lod[0]
        #who = who[1:]
        #if data.find(username + '!') == -1:
            #irc.send('PRIVMSG ' + channel + ' :' + who + ', be S.H.I.T (Some Hackers In Town) khosh umadi!\r\n')
            
    if data.find(":la_fen!~la_fen@") != -1:
        if str(data).index("PRIVMSG harchi :"):
            
            irc.send()
        
        
    elif data.find(pc) != -1:
        lod = data.split("!")
        who = lod[0]
        who = who[1:]
        pm = 'PRIVMSG ' + who + ' :'

# -------------- help

        if data.find(':!help') != -1:
            if data.find(username + '!') == -1:
                irc.send(pc + who + ", " + "https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands" + cr)
                print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr("https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands") + ")" 

# ------------- khuruj

        elif data.find(":!birun") != -1:
            irc.send(pc + "chashm :(\r\n")
            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + "chashm :(\r\n")
            irc.send('QUIT\r\n')
            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr('QUIT\r\n')

# ---------------- about

        elif data.find(":!about") != -1:
            irc.send(pc + who + ', My name is ' + username + ', I was born in 28 December 2010 and I\'m written in python.' + cr)
            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', My name is ' + username + ', I was born in 28 December 2010 and I\'m written in python.' + cr) + ")" 
                
# --------------- time
                
        elif data.find(":!time") != -1:
            irc.send(pc + who + ', ' + strftime("%H:%M:%S", localtime()) + cr)
            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', ' + strftime("%H:%M:%S", localtime()) + cr) + ")"
        
        elif data.find(":!when") != -1:
            irc.send(pc + who + ', ' + zaman + cr)
            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', ' + zaman + cr) + ")"
            
        elif data.find(":!date") != -1:
            tagh = strftime("%Y/%m/%d", localtime()).split("/")
            taghvim = Calverter().gregorian_to_iranian(int(tagh[0]), int(tagh[1]), int(tagh[2]))
            year = taghvim[0]
            month = taghvim[1]
            day = taghvim[2]
            wikDay = taghvim[3]
            irc.send(pc + who + ', ' + strftime("%a, %Y/%b/%d", localtime()) + " | " + wikDay + " " + day + " " + month + " " + year + cr)
            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', ' + strftime("%a, %Y/%b/%d", localtime()) + " | " + wikDay + " " + day + " " + month + " " + year + cr) + ")" 
            
# ---------- dot commands

        elif data.find(':.') != -1:
            lod = data.split(":")
            who = lod[1].split("!")[0]
            lang = lod[2].split(" ")[0]
            ebarat = ' '.join(lod[2].split(" ")[1: ])
            
            if ebarat.endswith(cr):
                ebarat = ebarat[:-2]
                
            try:
                
#<GoogleSearch>
                if data.find(":.web ") != -1:
                    url = "http://www.google.com/search?q=" + ebarat
                    irc.send(pc + who + ', ' + url.replace(" ", "+") + cr)
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', ' + url.replace(" ", "+") + cr) + ")"
                    
                elif data.find(":.img") != -1:
                    url = "http://www.google.com/images?q=" + ebarat
                    irc.send(pc + who + ', ' + url.replace(" ", "+") + cr)
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', ' + url.replace(" ", "+") + cr) + ")"
                    
                elif data.find(":.vid") != -1:
                    url = "http://www.google.com/search?q=" + ebarat + "&tbs=vid:1"
                    irc.send(pc + who + ', ' + url.replace(" ", "+") + cr)
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', ' + url.replace(" ", "+") + cr) + ")"
#</GoogleSearch>

#<ContactWithRobot>

                elif data.find(":.w") != -1:
                    irc.send("PRIVMSG la_fen :.w " + ebarat + cr)
                    print "PRIVMSG la_fen :.w " + ebarat + cr
                    who = whoBot

#</ContactWithRobot>

#<Translate>
                else:
                    lt = lang[1:3]
                    lf = lang[-2:]
                    irc.send(pc + who + ', ' + Translator().translate(ebarat, lf, lt).encode("utf-8") + cr)
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', ' + Translator().translate(ebarat, lf, lt).encode("utf-8") + cr) + ")"
#</Translate>                    
                    
            except Exception, e:
                print e


    if counter >= 12:
        for s in foshes.foshes:
            if data.find(s):
                if foshes.isFosh(s, data):
                    try:
                        lod = data.split(":")
                        who = lod[1].split("!")[0]
                        irc.send(pc + who + ', kheyli bi adabi!!!' + cr)
                        print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(pc + who + ', kheyli bi adabi!!!' + cr) + ")"
                    except Exception, e:
                        print e
                    break
    counter += 1
