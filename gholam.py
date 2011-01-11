# coding: utf-8
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

class Gholam(object):
    zaman = ""
    whoBot = ""
    def __init__(self, username, channel):
        self.username = username
        self.channel = channel
        self.pc = 'PRIVMSG ' + self.channel + ' :'
        self.network = "irc.freenode.net"
        self.port = 6667
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.irc.connect((self.network, self.port))
        self.data = self.irc.recv(4096)
        self.irc.send("NICK " + self.username + "\r\n")
        self.irc.send("USER " + self.username + " " + self.username + " " + self.username + " :Python IRC" + "\r\n")
        self.irc.send("JOIN " + self.channel + "\r\n")
    
    # ------------ listen
    
    def listen(self):
        counter = 1
        
        while True:
            print "\nloop: " + strftime("%H:%M:%S", localtime()) + " =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=(" +str(counter) + ")\n"
            
            data = self.irc.recv(4096)
            print "recieve: " + strftime("%H:%M:%S", localtime()) + " (" + repr(data) + ")\n"
            
            if data.find("PING") != -1:
        
                pinger = data.split()[1]
                self.irc.send("PONG " + pinger + "\r\n")
                print "send: " + strftime("%H:%M:%S", localtime()) + "(" + repr("PONG " + pinger + "\r\n") + ")"
                
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
                data = data[data.index("PRIVMSG " + username + " :") + 16:]
                self.irc.send(self.pc + self.whoBot + ", " + data + "\r\n")
        
            elif data.find(self.pc) != -1:
                lod = data.split("!")
                who = lod[0]
                who = who[1:]
                pm = 'PRIVMSG ' + who + ' :'
        
        # -------------- help
        
                if data.find(':!help') != -1:
                    if data.find(username + '!') == -1:
                        self.irc.send(self.pc + who + ", " + "https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands" + "\r\n")
                        print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr("https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands") + ")" 
        
        # ------------- khuruj
        
                elif data.find(":!birun") != -1:
                    irc.send(self.pc + "chashm :(\r\n")
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + "chashm :(\r\n")
                    self.irc.send('QUIT\r\n')
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr('QUIT\r\n')
        
        # ---------------- about
        
                elif data.find(":!about") != -1:
                    self.irc.send(self.pc + who + ', My name is ' + username + ', I was born in 28 December 2010 and I\'m written in python.' + "\r\n")
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', My name is ' + username + ', I was born in 28 December 2010 and I\'m written in python.' + "\r\n") + ")" 
                        
        # --------------- time
                        
                elif data.find(":!time") != -1:
                    self.irc.send(self.pc + who + ', ' + strftime("%H:%M:%S", localtime()) + "\r\n")
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', ' + strftime("%H:%M:%S", localtime()) + "\r\n") + ")"
                
                elif data.find(":!when") != -1:
                    self.irc.send(self.pc + who + ', ' + zaman + "\r\n")
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', ' + zaman + "\r\n") + ")"
                    
                elif data.find(":!date") != -1:
                    tagh = strftime("%Y/%m/%d", localtime()).split("/")
                    taghvim = Calverter().gregorian_to_iranian(int(tagh[0]), int(tagh[1]), int(tagh[2]))
                    year = taghvim[0]
                    month = taghvim[1]
                    day = taghvim[2]
                    wikDay = taghvim[3]
                    self.irc.send(self.pc + who + ', ' + strftime("%a, %Y/%b/%d", localtime()) + " | " + wikDay + " " + day + " " + month + " " + year + "\r\n")
                    print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', ' + strftime("%a, %Y/%b/%d", localtime()) + " | " + wikDay + " " + day + " " + month + " " + year + "\r\n") + ")" 
                    
        # ---------- dot commands
        
                elif data.find(':.') != -1:
                    lod = data.split(":")
                    who = lod[1].split("!")[0]
                    lang = lod[2].split(" ")[0]
                    ebarat = ' '.join(lod[2].split(" ")[1: ])
                    
                    if ebarat.endswith("\r\n"):
                        ebarat = ebarat[:-2]
                        
                    try:
        
        #<GoogleSearch>
                        if data.find(":.web ") != -1:
                            url = "http://www.google.com/search?q=" + ebarat
                            self.irc.send(self.pc + who + ', ' + url.replace(" ", "+") + "\r\n")
                            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', ' + url.replace(" ", "+") + "\r\n") + ")"
                            
                        elif data.find(":.img") != -1:
                            url = "http://www.google.com/images?q=" + ebarat
                            self.irc.send(self.pc + who + ', ' + url.replace(" ", "+") + "\r\n")
                            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', ' + url.replace(" ", "+") + "\r\n") + ")"
                            
                        elif data.find(":.vid") != -1:
                            url = "http://www.google.com/search?q=" + ebarat + "&tbs=vid:1"
                            self.irc.send(self.pc + who + ', ' + url.replace(" ", "+") + "\r\n")
                            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', ' + url.replace(" ", "+") + "\r\n") + ")"
        #</GoogleSearch>
        
        #<ContactWithRobot>
        
                        elif data.find(":.w") != -1:
                            self.irc.send("PRIVMSG la_fen :.w " + ebarat + "\r\n")
                            print "PRIVMSG la_fen :.w " + ebarat + "\r\n"
                            self.whoBot = who
        
                        elif data.find(":.dict") != -1:
                            self.irc.send("PRIVMSG la_fen :.dict " + ebarat + "\r\n")
                            print "PRIVMSG la_fen :.dict " + ebarat + "\r\n"
                            self.whoBot = who
                            
        #</ContactWithRobot>
        
        #<Translate>
                        else:
                            lt = lang[1:3]
                            lf = lang[-2:]
                            self.irc.send(self.pc + who + ', ' + Translator().translate(ebarat, lf, lt).encode("utf-8") + "\r\n")
                            print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', ' + Translator().translate(ebarat, lf, lt).encode("utf-8") + "\r\n") + ")"
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
                                self.irc.send(self.pc + who + ', kheyli bi adabi!!!' + "\r\n")
                                print "send: " + strftime("%H:%M:%S", localtime()) + " (" + repr(self.pc + who + ', kheyli bi adabi!!!' + "\r\n") + ")"
                            except Exception, e:
                                print e
                            break
            counter += 1

username = raw_input("username: ")
channel = raw_input("channel: ")

Gholam(username, channel).listen()