import time
from netmiko import ConnectHandler, redispatch
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
from getpass import getpass

# tested in python3.7
# this script is useful when there is a  linux jump server ( jumpbox ) between the user
# and the end cisco device, and eg corporate security controls prevent a direct ssh session
# this script will call devices.txt and take a 'show run' config snapshot of each 
# cisco device in the list, writing each device config to a separate .txt file
# it presumes there maybe different usernames/ passwords for the jump server than the end device
# so it will initially prompt the user for all creds
# it also presumes the user/pass is constant for all end devices

# user input
terminal = input("Jump Server IP: ")
username = input("Jump Server Username: ")
password = getpass("Jump Server Exec Password: ")
username2 = input("End Cisco Device Username: ")
secret = getpass("End Cisco Exec Password: ")
# jump server dictionary
ssh_device = {

    'device_type': 'terminal_server',
    'ip': terminal,
    'username': username,
    'password': password,
    'secret': secret,
    'port': 22,
}
# open device list and split
devices = open('devices.txt', 'r')
devices = devices.read()
devices = devices.strip().splitlines()
# connect to jumpbox for each device
for device in devices:
    try:
        print('-' * 79)
        print('connecting to device', device)
        net_connect = ConnectHandler(**ssh_device)
        print ("SSH prompt: {}".format(net_connect.find_prompt()))
        net_connect.write_channel(
            "ssh -o StrictHostKeyChecking=no -l " + username2 + " " + device + '\n')
        time.sleep(2)
        output = net_connect.read_channel()
        print(output)
        if 'ssword' in output:
            net_connect.write_channel(secret + '\r\n')
            time.sleep(2)
            output = net_connect.read_channel()
            # Did we successfully login
        net_connect.write_channel('\r\n')
        time.sleep(2)
        print(output)
        # connect to the end device
        redispatch(net_connect, device_type='cisco_ios')
        net_connect.enable()
        hostname = net_connect.send_command('show run | inc hostname')
        # generate txt file
        hostname.split(" ")
        col1, col2 = hostname.split(" ")
        filename = col2 + '.txt'
        filename = (filename.replace("\n", " "))
        print(filename)
        showrun = net_connect.send_command('show run')
        log_file = open(filename, "a")   # in append mode
        log_file.write(showrun)
        net_connect.disconnect()
# error controls
    except ValueError:
        print('authentication failed to ', device)
        continue
    except NetMikoTimeoutException:
        print('device not reachable', device)
        continue
    except NetMikoAuthenticationException:
        print('auth failure', device)
        continue
