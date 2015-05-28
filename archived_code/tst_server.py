import Pyro4
import tst

t = tst.TernarySearchTree()
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(t)
ns.register("tst.server", uri)

print "Ready."
daemon.requestLoop()