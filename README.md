# cisco_backup_jump_server

## Python script using Netmiko to  take a cisco config snapshot , via an intermediate jump server

![alt text](https://github.com/markheinemann/cisco_backup_jump_server/blob/main/jump.JPG)


Tested in python3.7

This script is useful for network engineers when there is a  linux jump server ( jumpbox ) between the user

and the end cisco device, and eg corporate security controls prevent a direct ssh session.

## Installation

Create a virtual environment eg called 'backup'

- `python -m virtualenv backup`

Activate the virtual environment

- `backup\Scripts\activate.bat`

Install Netmiko

- `pip install netmiko`

Verify with `pip list`

## Usage

`python backup_cisco.py`

This script will call __devices.txt__ and take a 'show run' config snapshot of each 

cisco device in the list, writing each device config to a separate .txt file

It presumes there maybe different usernames/ passwords for the jump server vs the  end device,

so it will initially prompt the user for all credentials.

It also presumes the user/pass is constant for all the devices in the txt file



Create a file `devices.txt` , a device ip address on every new line. see the example file in the repo to understand
the format required.Edit this list with your device's ip addresses 

Have ready the creds for:

- Jump Server IP:
- Jump Server Username:
- End Cisco Device Username:
- End Cisco Exec Password:

 getpass will hide the password screen input
 
## Testing 

[You can use the Cisco Modelling Labs Enterprise sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/685f774a-a5d6-4df5-a324-3774217d0e6b?diagramType=Topology)

There is an example lab topology preloaded called "Multi Platform Network". This includes a devbox, some cisco devices and a few linux hosts
 
 
## Known Issues

The RSA key in the jumpbox must match the RSA key in the end cisco device.

If this is not the case, then you may get a keygen error on trying to connect. The solution is to clear the key from the  'ssh/known_hosts' file  

An example command would  be  `ssh-keygen -R 10.10.10.1` where 10.10.10.1 is the ip of the end cisco device

## Authors & Maintainers

Please contact me for any modifications on this script.

## License

This project is licensed to you under the terms of the MIT icense



