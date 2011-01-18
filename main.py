from gholamfactory import GholamFactory
from twisted.internet import reactor

if __name__ == "__main__":
#    username = raw_input("id: ")
#    channel = raw_input("ch: ")
    reactor.connectTCP('irc.freenode.net', 6667, GholamFactory("harchi", "harchi")) #@UndefinedVariable
    reactor.run() #@UndefinedVariable