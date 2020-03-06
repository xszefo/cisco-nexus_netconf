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
        

        vlan_filter = """
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <vlanTable-items>
                <vlan-items>
                    <VlanEntry-list/>
                </vlan-items>
            </vlanTable-items>
        </System>
        """


        vlan_filter = """
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <stp-items>
                <inst-items>
                    <vlan-items>
                        <Vlan-list/>
                    </vlan-items>
                </inst-items>
            </stp-items>
        </System>
        """
        x = m.get(('subtree', vlan_filter))
        print(x)
        #xml = x.data_ele
        #print(xml)
        #print(etree.tostring(xml))

        
if __name__ == '__main__':
    sys.exit(main())
