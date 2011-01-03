#encoding: utf-8

import socket
from xgoogle.translate import Translator

username = "s-h-i-t"
channel = "#harchi"
network = 'irc.freenode.net'
port = 6667
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

irc.connect((network, port))

print irc.recv(4096)

irc.send('NICK ' + username + '\r\n')
irc.send('USER ' + username + " " + username + " " + username + ' :Python IRC\r\n')
irc.send('JOIN ' + channel + '\r\n')

counter = 1

while True:

    data = irc.recv(4096)
    if data.find('PING') != -1:
        irc.send('PONG ' + data.split()[1] + '\r\n')

    elif data.find('PRIVMSG ' + channel) != -1:

# ---------- Translate

        if data.find(':.') != -1:
            lod = data.split(":")
            who = lod[1].split("!")[0]
            lang = lod[2].split(" ")[0]
            ebarat = ' '.join(lod[2].split(" ")[1: ])
            if ebarat.endswith("\r\n"):
                ebarat = ebarat[:-2]

                be = lang[-2:]
                az = lang[1:3]
                irc.send('PRIVMSG ' + channel + ' :' + who + ', ' + Translator().translate(ebarat, be, az) + '\r\n')
                print Translator().translate(ebarat, be, az)


    print data
    print str(counter) + ")=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
    counter += 1


