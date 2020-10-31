# cisco_backup_jump_server

## python script using Netmiko to  take a cisco config snapshot , via an intermediate jump server

![alt text](https://github.com/markheinemann/cisco_backup_jump_server/blob/main/jump.JPG)


tested in python3.7

this script is useful for network engineers when there is a  linux jump server ( jumpbox ) between the user

and the end cisco device, and eg corporate security controls prevent a direct ssh session

This script will call `devices.txt` and take a 'show run' config snapshot of each 

cisco device in the list, writing each device config to a separate .txt file

It presumes there maybe different usernames/ passwords for the jump server than vs  end device,

so it will initially prompt the user for all creds

it also presumes the user/pass is constant for all end devices

## Usage

create a file `devices.txt` , a device ip address on every new line. see the example file in the repo to undertstand
the format required.Edit this list with your device's ip addresses 

Have ready the creds for:

- Jump Server IP:
- Jump Server Username:
- End Cisco Device Username:
- End Cisco Exec Password:

 getpass will hide the password screen input
 
## Known Issues

The RSA key in the jumpbox must match the RSA key in the end cisco device

if this is not the case, then you may get a keygen error on trying to connect. The solution is to clear the key from the  'ssh/known_hosts' file  

An example command would  be  `ssh-keygen -R 10.10.10.1` where 10.10.10.1 is the ip of the end cisco device


