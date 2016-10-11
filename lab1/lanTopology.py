#!/usr/bin/env python2

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def firstNetwork():

    net = Mininet()
    net.addController( 'c0' )

    PC = {(i + 1): net.addHost('PC{}'.format(i + 1)) for i in range(4)}

    switches = {s: net.addSwitch('s{}{}'.format(*s))
                for s in {(1, 4), (2, 4), (3, 4)}}

    for pc, s in {(PC[1], (1, 4)), (PC[2], (2, 4)), (PC[3], (3, 4)),
                  (PC[4], (1, 4)), (PC[4], (2, 4)), (PC[4], (3, 4))}:
        net.addLink(pc, switches[s])

    info( '*** Starting network\n')
    net.start()

    for pc in PC.values():
        pc.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T ' + pc.name + '&')

#    info( '*** set IP\n' )
#    for pc in PC.values():
#        for intf in pc.intfNames():
#            pc.cmd('ip addr flush dev {}'.format(intf))
#
#    for i, ip, intf in {(1, '10.10.14.{}/24', 'eth0'),
#                         (2, '10.10.24.{}/24', 'eth1'),
#                         (3, '10.10.34.{}/24', 'eth2')}:
#        pc = PC[i]
#        pc_ip = ip.format(i)
#        pc4_ip = ip.format(4)
#        pc.cmd('ip addr add {} dev {}-eth0'.format(pc_ip, pc.name))
#        PC[4].cmd('ip addr add {} dev PC4-{}'.format(pc4_ip, intf))
#
#    for i, ip, intf in {(1, 'fd24:ec43:12ca:c001:14::{}', 'eth0'),
#                        (2, 'fd24:ec43:12ca:c001:24::{}', 'eth1'),
#                        (3, 'fd24:ec43:12ca:c001:34::{}', 'eth2')}:
#        pc = PC[i]
#        pc_ip = ip.format(i)
#        pc4_ip = ip.format(4)
#        pc.cmd('ip -6 addr add {} dev {}-eth0'.format(pc_ip, pc.name))
#        PC[4].cmd('ip -6 addr add {} dev PC4-{}'.format(pc4_ip, intf))

    info('*** up interfaces\n')
    for pc in PC.values():
        for intf in pc.intfNames():
            pc.cmd('ip link set {} up'.format(intf))

    info('*** start cli\n')
    CLI(net)
    for pc in PC.values():
        pc.cmd("killall xterm")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    firstNetwork()
