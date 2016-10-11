#!/usr/bin/env python2

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def firstNetwork():

    net = Mininet()
    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    PC = {(i + 1): net.addHost('PC{}'.format(i + 1)) for i in range(4)}

    info( '*** Adding switch\n' )
    switches = {s: net.addSwitch('s{}{}'.format(*s))
                for s in {(1, 4), (2, 4), (3, 4)}}

    info( '*** Creating links\n' )
    for pc, s in {(PC[1], (1, 4)), (PC[2], (2, 4)), (PC[3], (3, 4)),
                  (PC[4], (1, 4)), (PC[4], (2, 4)), (PC[4], (3, 4))}:
        net.addLink(pc, switches[s])


    info( '*** Starting network\n')
    net.start()

    info( '*** Starting xterm on hosts\n' )
    for pc in PC.values():
        pc.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T ' + pc.name + '&')

    for pc in PC.values():
        pc.cmd('ip addr flush')

    info( '*** Running the command line interface\n' )
    CLI( net )

    info( '*** Closing the terminals on the hosts\n' )
    for pc in PC.values():
        pc.cmd("killall xterm")

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    firstNetwork()
