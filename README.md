# cisco_backup_jump_server
python script using Netmiko to  take a cisco config snapshot , via an intermediate jump server

![alt text](https://github.com/markheinemann/cisco_backup_jump_server/blob/main/jump.JPG)


tested in python3.7</br></br>
this script is useful for network engineers when there is a  linux jump server ( jumpbox ) between the user
and the end cisco device, and eg corporate security controls prevent a direct ssh session</br></br>
This script will call devices.txt and take a 'show run' config snapshot of each 
cisco device in the list, writing each device config to a separate .txt file</br></br>
It presumes there maybe different usernames/ passwords for the jump server than vs  end device,
so it will initially prompt the user for all creds</br></br>
it also presumes the user/pass is constant for all end devices</br></br>
Usage</br></br>
create a file " devices.txt " , a device ip address on every new line. see the example in the repo</br></br>
Have ready the creds for:</br></br>
Jump Server IP:</br>
Jump Server Username: </br>
End Cisco Device Username: </br>
End Cisco Exec Password: </br></br>
Known Issues:</br></br>
The RSA key in the jumpbox must match the RSA key in the edn cisco device
if this is not the case, then you may get a keygen error on trying to connect. The solution is to clear the key from the  <b>.ssh/known_hosts</b> file  
An example copmmand would  be  <b>ssh-keygen -R 10.10.10.1</b> where 10.10.10.1 is the ip of the end cisco device


