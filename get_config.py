#!/usr/bin/python3

from ncclient import manager


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
                        device_params = {'name': 'nexus'}) as m:

        if m.connected: print('Connected')
        
        for x in dir(m):
            print(x)

if __name__ == '__main__':
    main()
