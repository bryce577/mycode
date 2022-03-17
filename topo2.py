#!/usr/bin/python3
"""Alta3 Research | Custom topology example

   Two directly connected switches plus a host for each switch:

      host --- switch --- switch --- host

   Adding the 'topos' dict with a key/value pair to generate our newly defined
   topology enables one to pass in '--topo=mytopo' from the command line.
   """

from mininet.topo import Topo

class NewTopo( Topo ):
       "Simple topology example."

       def __init__( self ):
           "Create custom topo."

           # Initialize topology
           Topo.__init__( self )

           # Add hosts and switches
           middleSwitch = self.addSwitch ( 's1' )
           leftHost = self.addHost( 'h1' )  # create the obj leftHost and give it the visable name h1
           rightHost = self.addHost( 'h4' )
           leftSwitch = self.addSwitch( 's2' ) # create the obj leftSwitch and give it the visable name s3
           rightSwitch = self.addSwitch( 's3' )
           h6 = self.addHost ( 'h6' )
           h5 = self.addHost ( 'h5' )
           h2 = self.addHost ( 'h2' )
           h3 = self.addHost ( 'h3' )

           # Add links
           self.addLink( leftHost, leftSwitch )
           self.addLink( leftSwitch, middleSwitch )
           self.addLink( rightSwitch, middleSwitch )
           self.addLink( rightSwitch, rightHost )
           self.addLink( h2, leftSwitch )
           self.addLink( h3, rightSwitch )
           self.addLink( h6, middleSwitch )
           self.addLink( h5, middleSwitch )


topos = { 'newtopo': ( lambda: NewTopo() ) }

