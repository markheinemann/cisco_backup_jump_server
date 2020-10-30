# cisco_backup_jump_server
python script using Netmiko to  take a cisco config snapshot , via an intermediate jump server

tested in python3.7</br>
this script is useful when there is a  linux jump server ( jumpbox ) between the user
and the end cisco device, and eg corporate security controls prevent a direct ssh session</br>
This script will call devices.txt and take a 'show run' config snapshot of each 
cisco device in the list, writing each device config to a separate .txt file</br>
It presumes there maybe different usernames/ passwords for the jump server than vs  end device,
so it will initially prompt the user for all creds</br>
it also presumes the user/pass is constant for all end devices
