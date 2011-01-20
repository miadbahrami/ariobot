from twisted.web import client
from twisted.internet import reactor
import urllib

class NRE(Exception):
    
    pass

class NRPG(client.HTTPPageGetter):
    
    handleStatus_301 = handleStatus_302 = handleStatus_302 = lambda self: None

class RGCF(client.HTTPClientFactory):
    
    protocol = NRPG
    def page(self, page):
        
        if self.waiting:
            self.waiting = False
            
            if 'location' not in self.response_headers:
                self.deferred.errback(
                    NRE("there wasn't a location header"))
                
            else:
                self.deferred.callback(self.response_headers['location'][0])

def dpaste(data, **kwds):
    kwds['content'] = data
    factory = RGCF('http://dpaste.com/api/v1/', method='POST', postdata=urllib.urlencode(kwds))
    reactor.connectTCP('dpaste.com', 80, factory) #@UndefinedVariable
    return factory.deferred

pp = ""

def res(result):
    global pp
    pp = result

def paste(dd, ll):   
    d = dpaste(dd, language=ll)
    d.addBoth(res)
    return pp