#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import os

def firstNetwork():

    net = Mininet()

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts \n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1/24' )
    h2 = net.addHost( 'h2', ip='10.0.0.2/24' )
    h3 = net.addHost( 'h3', ip='10.0.0.3/31' )
    h4 = net.addHost( 'h4', ip='10.0.1.4/24' )
    PC = {1: h1, 2: h2, 3: h3, 4: h4}

    info( '*** Adding switches\n' )
    s12 = net.addSwitch( 's12' )
    s34 = net.addSwitch( 's34' )

    info( '*** Creating links\n' )
    net.addLink( h1, s12 )
    net.addLink( h2, s12 )
    net.addLink( h3, s34 )
    net.addLink( h4, s34 )
    net.addLink( s12, s34 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Starting xterm on hosts\n' )
    h1.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T h1 &')
    h2.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T h2 &')
    h3.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T h3 &')
    h4.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T h4 &')

    info('*** ovs-ofctl\n')
    os.system('ovs-ofctl add-flow s12 action=flood')
    os.system('ovs-ofctl add-flow s34 action=flood')

    info('*** set IP\n')
    for pc in PC.values():
        for intf in pc.intfNames():
            pc.cmd('ip addr flush dev {}'.format(intf))

    for i in range(1, 4):
        pc = PC[i]
        pc_ip = '10.0.0.{}/24'.format(i)
        pc.cmd('ip addr add {} dev {}-eth0'.format(pc_ip, pc.name))
    PC[4].cmd('ip addr add 10.0.1.4/24 dev {}-eth0'.format(PC[4].name))

    info('*** up interfaces\n')
    for pc in PC.values():
        for intf in pc.intfNames():
            pc.cmd('ip link set {} up'.format(intf))

    info( '*** Running the command line interface\n' )
    CLI( net )

    info( '*** Closing the terminals on the hosts\n' )
    for h in PC:
        h.cmd("killall xterm")

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    firstNetwork()
