import sys
import argparse


parser = argparse.arg

def my_function():
    pass


def main():
    # DEV LIST
    dev_list = ["192.168.1.1", "192.168.1.10"]
    
    
    # COMMAND LIST
    show_commands = [
        'show version',
        'show run'
    ]
    
    # ALL DEV OUTPUT
    all_dev_list = []
    
    # LOOP ALL DEVS
    for dev in dev_list:
        cisco_881 = {
            'device_type': 'cisco_ios',
            'host':   '10.10.10.10',
            'username': 'test',
            'password': 'password',
            'port' : 22,          # optional, defaults to 22
            'secret': 'secret',     # optional, defaults to ''
        }
        
        net_connect = ConnectHandler(**cisco_881)
        output = net_connect.send_command('show ip int brief')
        print(output)
            

if __name__ == "__main__":
    print("Running...")
    main()