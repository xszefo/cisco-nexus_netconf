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
        
        for x in m.server_capabilities:
            print(x)

        interface_filter = """
        <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>Lo1</name>
                </interface>
            </interfaces>
        </filter>
        """
        print(m.get_config('running', interface_filter))

if __name__ == '__main__':
    main()
