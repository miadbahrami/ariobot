from gholamfactory import GholamFactory
from twisted.internet import reactor

if __name__ == "__main__":
    username = raw_input("nickname: ")
    channel = raw_input("channel: ")
    if not username and not channel:
        username = "harchi"
        channel = "harchi"
        
    reactor.connectTCP('irc.freenode.net', 6667, GholamFactory(channel, username)) #@UndefinedVariable
    reactor.run() #@UndefinedVariable