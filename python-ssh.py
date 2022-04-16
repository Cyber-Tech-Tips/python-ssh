#!/usr/bin/env python3
import os
import atexit

print('Welcome to ssh python script\n')
print('-------------------------------------\n')

ssh_id = ".ssh/id_rsa"
filename = ".ssh/config"

if os.path.exists(ssh_id):
    print("You have the ssh keys stored in:" )
    os.system("ls -al /home/$USER/.ssh | grep rsa")
else:
    print ("You don't have the RSA ID file, please create a new one\n")
    os.system("ssh-keygen -t rsa")

if not os.path.exists(".ssh"):
    os.makedirs(".ssh")
    print("ssh folder created, because the folder is not yet created\n")

if os.path.exists(filename):
    print("""
**Config File exists**\n
**Now we editing the same Config file**\n
    """)
    config = open(filename, 'a')
else:
    print("**Creating The ssh config File**\n")
    config = open(filename, 'w')


def exit_handler():
    print ('Information Saved\n')


ipaddress_ssh_ports = input("Scan Your network for open ssh, please enter your IP address to scan your network:")
os.system("nmap -v " + ipaddress_ssh_ports + "/24" + "| grep " + " 'ssh'\n")

ipaddress_for_machines = input("Scan Your network for IP Addresses, please enter the IP address to start the scan: ")
os.system("nmap -v " + ipaddress_for_machines + "/24" + "| grep " + " 'port 22'\n")

try:
    while True:
            hostname_regular_user = input("Please insert machine name for the regualr user: ")
            hostname_root_user = input("Please insert the name of the machine for the root user:")
            machine_ip_address = input("Please insert the Hostname of the machine or IP Address: ")
            ssh_port_number = input("Please insert The Port Number. You can Skip with Enter: ")
            machine_regular_user = input("Please insert the regualr machine username: " )
            ssh_copy_id_user = input("Copying the ssh ID to the user's machine. Do you want to continue (y) ")
            ssh_copy_id_root = input("Copying the ssh ID to root. Do you want to continue (y):")
            if hostname_regular_user:
                config.write("Host " + hostname_regular_user)
                config.write("\n")
            if machine_ip_address:
                config.write("Hostname " + machine_ip_address)
                config.write("\n")
            if ssh_port_number: 
                config.write("Port " + ssh_port_number)
                config.write("\n")
            if machine_regular_user:
                config.write("User " + machine_regular_user)
                config.write("\n")
                config.write("\n")
            if hostname_root_user:
                config.write("\n")
                config.write("Host " + hostname_root_user + "\n" + "Hostname " + machine_ip_address + "\n" + ssh_port_number + "\n" + "User " + "root" + "\n")
                config.write("\n")   
            if ssh_copy_id_user:
                    os.system("ssh-copy-id " + machine_regular_user + "@" + machine_ip_address)
            if ssh_copy_id_root:
                    os.system("ssh -t " + machine_regular_user + "@" + machine_ip_address  + " " + " " " 'sudo cp --parents .ssh/authorized_keys /root/' ")    
            print ("Finished and starting with the new machine")
            print ("\n")
            if hostname_regular_user != machine_regular_user:
                config.write("\n")
                config.write("\n")
except KeyboardInterrupt:    
            config.close()
atexit.register(exit_handler)
