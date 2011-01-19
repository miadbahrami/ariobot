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

from twisted.words.protocols import irc
from modules.translate import Translator
from modules.wiktionary import wikt
from other import withoutPhrase
from time import strftime

class Gholam(irc.IRCClient):
    isChannel = False

    def _get_nickname(self):
        return self.factory.nickname
    
    nickname = property(_get_nickname)

    def signedOn(self):
        self.join(self.factory.channel)
        print "%s - ba nick e %s be server vasl shodam." % (strftime("%X"), self.nickname,)

    def joined(self, channel):
        self.isChannel = True
        self.channel = channel
        print "%s - Raftam tu %s." % (strftime("%X"), channel,)
        
    def left(self):
        print "left shodam :D"
        
    def pong(self):
        print "pong :D:D"
        
    def userRenamed(self, oldname, newname): 
        self.msg(self.channel, "%s, shakh shodi nick avaz mikoni?!" % newname)
        

    def privmsg(self, user, channel, msg):
        if self.isChannel:
            id = user.split("!")[0]
            if channel[0] == "#":
                ebarat = msg[5:]
                send = ""
                print "%s - %s: %s" % (strftime("%X"), id, msg,)

# without phrase commands              
                if msg.startswith("!"):
                    send = withoutPhrase(msg, channel, id)
                    self.msg(channel, send)
                    
# ping bot
                elif msg.startswith("%s, " % self.nickname) or msg.startswith("%s: " % self.nickname):
                    send = "help -> https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands"
                    self.msg(id, send)

# with phrase commands
                elif msg.startswith("."):
                    if msg.startswith(".web "):
                        url = "http://www.google.com/search?q=%s" % ebarat
                        send = "%s, %s" % (id, url.replace(" ", "+"))
                        self.msg(channel, send)
    
                    elif msg.startswith(".w "):
                        msg = msg.split()[1]
                        send = "%s, %s" % (id, wikt(msg))
                        self.msg(channel, send)
                        
                    elif msg.startswith(".img "):
                        url = "http://www.google.com/images?q=%s" % ebarat
                        send = "%s, %s" % (id, url.replace(" ", "+"))
                        self.msg(channel, send)
        
                    elif msg.startswith(".vid "):
                        url = "http://www.google.com/search?q=%s&tbs=vid:1" % ebarat
                        send = "%s, %s" % (id, url.replace(" ", "+"))
                        self.msg(channel, send)
                        
# Google Translate
                    elif msg.startswith(".") and msg[5] == " ":
                        msg = msg.split(" ")[0]
                        lt = msg[1:3]
                        lf = msg[-2:]
                        matn = Translator().translate(ebarat, lf, lt).encode("utf-8")
                        send = "%s, %s" % (id, matn)
                        self.msg(channel, send)
    
                if send:
                    print "%s - %s: %s" % (strftime("%X"), self.nickname, send)

            else:
                print "%s - %s: >%s<, %s" % (strftime("%X"), id, self.nickname, msg)
                send = "https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands"
                if id != "ChanServ" and id != "NickServ":
                    self.msg(id, send)
                    print "%s - %s: >%s<, %s" % (strftime("%X"), self.nickname, id, send)
