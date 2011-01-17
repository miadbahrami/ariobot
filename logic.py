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
from translate.translate import Translator
from time import localtime
from time import strftime
from calverter import Calverter
from django.utils.encoding import smart_str

class Gholam(object):
    
    def __init__(self, username, channel, password):
        self.username = smart_str(username)
        self.channel = smart_str(channel)
        self.password = smart_str(password)
        self.pc = 'PRIVMSG %s :' % self.channel
        self.network = "irc.freenode.net"
        self.port = 6667
        self.zaman = ""
        self.whoBot = ""
        self.isFosh = False
        self.send = ""
        self.connect()

    def connect(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.network, self.port))
        self.receive = self.irc.recv(4096)
        self.irc.send("nick %s\r\n" % self.username)
        self.irc.send("user %s %s %s :Python IRC\r\n" % (self.username, self.username, self.username))
        self.irc.send("privmsg nickserv :identify %s\r\n" % self.password)
        self.irc.send("join %s\r\n" % self.channel)
        self.isFosh = False
        
    
    def listen(self):
        print self.receive
        counter = 1
        
        while True:
            
            print "\n%s)-=-=-=-=-=-=-=-\n" % str(counter)
            
            self.receive = self.irc.recv(4096)
            
            print "<receive>\n%s\n</receive>" % repr(self.receive)
                        
            if self.receive:
                
                if self.receive.find("PING") != -1:
                    pinger = self.receive.split()[1]
                    self.send = "PONG %s\r\n" % pinger
                    self.irc.send(self.send)
                
                elif self.receive.find(":%s!~%s" % (self.username, self.username)) != -1 and self.receive.find("JOIN :" + self.channel) != -1:
                    zaman = strftime("%H:%M:%S | %A, %Y/%B/%d", localtime())
            
                elif self.receive.find(":la_fen!~la_fen@") != -1:
                    self.receive = self.receive[self.receive.index("PRIVMSG %s :" % self.username) + 16:]
                    self.send = "%s%s, %s" % (self.pc, self.whoBot, self.receive)
                    self.irc.send(self.send)
            
            #---------------------------

                elif self.receive.find(self.pc) != -1:
                    lod = self.receive.split("!")
                    who = lod[0]
                    who = who[1:]
                    pm = self.pc + who + ', '

            # -------------- help

                    if self.receive.find(":!help") != -1:
                        if self.receive.find(self.username + "!") == -1:
                            self.send = "%shttps://bitbucket.org/aminpy/gholam/issue/1/gholam-commands\r\n" % pm
                            self.irc.send(self.send)
            
            # ------------- khuruj
            
                    elif self.receive.find(":!birun") != -1:
                        self.irc.send(self.pc + "chashm :(\r\n")
                        self.irc.send("QUIT\r\n")
            
            # ---------------- about
            
                    elif self.receive.find(":!about ") != -1:
                        self.send = "%sMy name is %s, I was born in 28 December 2010 and I\'m written in python.\r\n" % (pm, self.username)
                        self.irc.send(self.send)
                            
            # --------------- time
                            
                    elif self.receive.find(":!when ") != -1:
                        self.send = "%s%s\r\n" % (pm, zaman)
                        self.irc.send(self.send)
                        
                    elif self.receive.find(":!date ") != -1:
                        tagh = strftime("%Y/%m/%d", localtime()).split("/")
                        taghvim = Calverter().gregorian_to_iranian(int(tagh[0]), int(tagh[1]), int(tagh[2]))
                        year = taghvim[0]
                        month = taghvim[1]
                        day = taghvim[2]
                        wikDay = taghvim[3]
                        self.send = "%s%s %s %s %s %s ساعت \r\n" % (pm, strftime("%H:%M:%S", localtime()), wikDay, day, month, year)
                        self.irc.send(self.send)
                        
            # ---------- dot commands

                    elif self.receive.find(':.') != -1:
                        lod = self.receive.split(":")
                        who = lod[1].split("!")[0]
                        lang = lod[2].split(" ")[0]
                        ebarat = ' '.join(lod[2].split(" ")[1: ])
                        
                        if ebarat.endswith("\r\n"):
                            ebarat = ebarat[:-2]
                            
                        try:
            
            #<GoogleSearch>
                            if self.receive.find(":.web ") != -1:
                                url = "http://www.google.com/search?q=%s" % ebarat
                                self.send = "%s%s\r\n" % (pm, url.replace(" ", "+"))
                                self.irc.send(self.send)
                                
                            elif self.receive.find(":.img ") != -1:
                                url = "http://www.google.com/images?q=%s" % ebarat
                                self.send = "%s%s\r\n" % (pm, url.replace(" ", "+"))
                                self.irc.send(self.send)
                                
                            elif self.receive.find(":.vid ") != -1:
                                url = "http://www.google.com/search?q=%s&tbs=vid:1" % ebarat
                                self.send = "%s%s\r\n" % (pm, url.replace(" ", "+"))
                                self.irc.send(self.send)
            #</GoogleSearch>
            
            #<ContactWithRobot>
            
                            elif self.receive.find(":.w ") != -1:
                                self.send = "PRIVMSG la_fen :.w %s\r\n" % ebarat
                                self.irc.send(self.send)
                                self.whoBot = who
            
                            elif self.receive.find(":.dict ") != -1:
                                self.send = "PRIVMSG la_fen :.dict %s\r\n" % ebarat
                                self.irc.send(self.send)
                                self.whoBot = who
                                
            #</ContactWithRobot>
    
            #<Translate>
                            else:
                                lt = lang[1:3]
                                lf = lang[-2:]
                                matn = smart_str(Translator().translate(ebarat, lf, lt))
                                self.send = str(pm) + matn + str("\r\n")
                                self.irc.send(self.send)
            #</Translate>
                                
                        except Exception, e:
                            print e
                    
            # <5hit>

                if self.isFosh:
                    for s in foshes.foshes:
                        if self.receive.find(s):
                            if foshes.isFosh(s, self.receive):
                                try:
                                    lod = self.receive.split(":")
                                    who = lod[1].split("!")[0]
                                    self.send = "%skheyli bi adabi!\r\n" % pm
                                    self.irc.send(self.send)
                                except Exception, e:
                                    print e
                                break

                if self.channel != "#5hit":
                    self.isFosh = True
                    
                elif self.receive.find("fuck up") != -1:
                    self.isFosh = True
                    
            # </5hit>
                if self.send:
                    print "\n<send>\n%s\n</send>" % repr(self.send)
                    self.send = ""
                    
                counter += 1

            else:
                self.connect()
