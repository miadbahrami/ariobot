from gholamfactory import GholamFactory
from twisted.internet import reactor

if __name__ == "__main__":
    reactor.connectTCP('irc.freenode.net', 6667, GholamFactory("harchi", "gholam_")) #@UndefinedVariable
    reactor.run() #@UndefinedVariable