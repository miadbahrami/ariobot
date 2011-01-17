from twisted.words.protocols import irc
from translate.translate import Translator

class Gholam(irc.IRCClient):

    def _get_nickname(self):
        return self.factory.nickname
    
    nickname = property(_get_nickname)

    def signedOn(self):
        self.join(self.factory.channel)
        print "Ba id e %s be server vasl shodam." % (self.nickname,)

    def joined(self, channel):
        print "Raftam tu %s." % (channel,)

    def privmsg(self, user, channel, msg):
        if channel[0] == "#":
            id = user.split("!")[0]
            ebarat = msg[5:]
            print "%s: %s" % (id, msg,)
            
            if msg == "!help":
                self.send = "%s, https://bitbucket.org/aminpy/gholam/issue/1/gholam-commands" % id
                self.msg(channel, self.send)
                
            elif msg == "!about":
                self.send = "%s, My name is Gholam, I was born in 28 December 2010 and I'm written in python." % id
                self.msg(channel, self.send)

            elif msg.startswith(".web "):
                url = "http://www.google.com/search?q=%s" % ebarat
                self.send = "%s, %s" % (id, url.replace(" ", "+"))
                self.msg(channel, self.send)

            elif msg.startswith(".img "):
                url = "http://www.google.com/images?q=%s" % ebarat
                self.send = "%s, %s" % (id, url.replace(" ", "+"))
                self.msg(channel, self.send)

            elif msg.startswith(".vid "):
                url = "http://www.google.com/search?q=%s&tbs=vid:1" % ebarat
                self.send = "%s, %s" % (id, url.replace(" ", "+"))
                self.msg(channel, self.send)
                
            elif msg.startswith(".") and msg[5] == " ":
                msg = msg.split(" ")[0]
                lt = msg[1:3]
                lf = msg[-2:]
                matn = Translator().translate(ebarat, lf, lt).encode("utf-8")
                self.send = "%s, %s" % (id, matn)
                self.msg(channel, self.send)

            print "%s: %s" % (self.nickname, self.send)
