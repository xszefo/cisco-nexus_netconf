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
                        allow_agent=False,
                        look_for_keys=False,
                        device_params = {'name': 'nexus'}) as m:

        if m.connected: print('Connected')
        
        for x in m.server_capabilities:
            print(x)

        interface_filter = """
        <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>Loopback1</name>
                </interface>
            </interfaces>
        </filter>
        """


        hostname_filter = '''
                          <show xmlns="http://www.cisco.com/nxos:1.0">
                              <hostname>
                              </hostname>
                          </show>
                          '''

        x = m.get_config('running', interface_filter)
        #x = m.get(('subtree', hostname_filter))
        print('test')
        print(x)

if __name__ == '__main__':
    main()
