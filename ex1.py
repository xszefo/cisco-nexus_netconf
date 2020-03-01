#!/usr/bin/python3

from ncclient import manager


def main():
    # CONSTANTS
    host = 'sbx-nxos-mgmt.cisco.com'
    netconf_port = '8181'
    username = 'admin'
    password = 'Admin_1234!'

    with manager.connect(host=host, 
                        port=netconf_port, 
                        username=username, 
                        password=password, 
                        hostkey_verify=False) as m:

        print(m.connected)

    
if __name__ == '__main__':
    main()
