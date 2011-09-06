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
from time import strftime
from modules.dpaste import paste
#import sys
import os
from modules.mytime import shamsi, weekday

class Gholam(irc.IRCClient):
    help = ""
    isChannel = False

    def _get_nickname(self):
        return self.factory.nickname

    nickname = property(_get_nickname)

    def signedOn(self):
        self.join(self.factory.channel)
        # raf'e khali budan be ellate inke run ghable in mozu run shode
        self.pasteIt()
        print "%s-ba nick e %s be server vasl shodam." % (strftime("%X"),
                                                          self.nickname,)

    def joined(self, channel):
        self.pasteIt()
        self.isChannel = True
        self.channel = channel
        print "%s-Raftam tu %s." % (strftime("%X"), channel,)

    def left(self):
        print "left shodam :D"

    def userJoined(self, user, channel):
        print "%s-%s Joined to %s." % (strftime("%X"), user, channel)

    def userLeft(self, user, channel):
        print "%s-%s left %s." % (strftime("%X"), user, channel)

    def userQuit(self, user, quitMessage):
        print "%s-%s has quit (%s)." % (strftime("%X"), user, quitMessage)

    def userRenamed(self, oldname, newname):
        print "%s-%s changed nick to %s." % (strftime("%X"), oldname, newname)

    def privmsg(self, user, channel, msg):

        if not self.help and self.pasteIt():
            self.help = "%splain/" % self.pasteIt()

        if self.isChannel:
            id = user.split("!")[0]
            if channel[0] == "#":
                ebarat = msg[5:]
                send = ""
                print "%s-%s: %s" % (strftime("%X"), id, msg,)

# without phrase commands              
                if msg.startswith("!"):
                    send = self.withoutPhrase(msg, channel, id)
                    self.msg(channel, send)

# ping bot
                elif msg.startswith("%s, " % self.nickname) or msg.startswith("%s: " % self.nickname) or " %s " % self.nickname in msg:
                    send = self.help
                    self.msg(id, send)
                    print "%s-%s: >%s<, %s" % (strftime("%X"), self.nickname, id, send)
                    send = ""

# with phrase commands
                elif msg.startswith("."):

# Google Translate
                    if msg.startswith(".") and msg[5] == " ":
                        msg = msg.split(" ")[0]
                        lt = msg[1:3]
                        lf = msg[-2:]
                        matn = Translator().translate(ebarat, lf, lt).encode("utf-8")
                        send = "%s, %s" % (id, matn)
                        self.msg(channel, send)

                    elif msg.startswith(".web "):
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

                if send:
                    print "%s-%s: %s" % (strftime("%X"), self.nickname, send)

            else:
                print "%s-%s: >%s<, %s" % (strftime("%X"), id, self.nickname, msg)
                send = self.help
                if id != "ChanServ" and id != "NickServ":
                    self.msg(id, send)
                    print "%s-%s: >%s<, %s" % (strftime("%X"), self.nickname, id, send)

    def pasteIt(self):
#        f = open("%s/help.txt" % sys.path[0], "r")
        f = open(os.path.join(os.path.dirname(__file__), 'help.txt').replace('\\', '/'), "r")
        data = f.read()
        f.close()
        return paste(data, "Python")

    def withoutPhrase(self, msg, channel, id):
        msgDic = {
            "!help":  "%s, %s" % (id, self.help),
            "!about": "%s, My name is Gholam, I was born in 28 December 2010 and I'm written in python." % id,
            "!date": "%s, %s - %s" % (id, weekday(), shamsi()),
            "!time": "%s, %s" % (id, strftime("%X")),
            "!author": "%s, Amin Oruji - aminpy@gmail.com" % id
        }

        return msgDic.get(msg)
