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
        
        int_id = 'lo101'

        loopback_config = f'''
        <config>
			<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
				<intf-items>
					<lb-items>
						<LbRtdIf-list operation="remove">
							<id>{int_id}</id>
						</LbRtdIf-list>
					</lb-items>
				</intf-items>
			</System>
		</config>
        '''
        
        print('Deleting {int_id}...')
        x = m.edit_config(target='running', config=loopback_config)
        print(x)
        

if __name__ == '__main__':
    sys.exit(main())
