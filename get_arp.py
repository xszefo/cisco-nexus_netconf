#!/usr/bin/python3

from ncclient import manager
import sys
from lxml import etree

def main():
    # CONSTANTS
    host = 'sbx-nxos-mgmt.cisco.com'
    netconf_port = '10000'
    username = 'admin'
    password = 'Admin_1234!'
    
    print('Connecting to {}...'.format(host))
    with manager.connect(host=host, 
                        port=netconf_port, 
                        username=username, 
                        password=password, 
                        hostkey_verify=False,
                        allow_agent=False,
                        look_for_keys=False,
                        device_params = {'name': 'nexus'}) as m:

        if m.connected: print('Connected')
        

        arp_filter = """
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <arp-items/>
        </System>
        """

        x = m.get(('subtree', arp_filter))
        #print(x)
        xml = x.data_ele
        print(etree.tostring(xml))
        #print(xml.find('.//{http://cisco.com/ns/yang/cisco-nx-os-device}serial').text)
        
if __name__ == '__main__':
    sys.exit(main())
