from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from netmiko import ConnectHandler
from datetime import datetime
import netmiko
import json
import time
import get_user_pass

#ตัวแปร วัน/เวลา
date = datetime.now()
dts = date.strftime("%d-%m-%Y" + ' ' + "%H-%M-%S")
dt = date.strftime("%d-%m-%Y" + ' ' + "%H-%M")
ts = date.strftime("%d-%m-%Y")

# Get user credential from user input
username, password = get_user_pass.get_credential()

# Get device inventory for netmiko module
# 1. router ip address
# 2. device type
with open('device.json', 'r') as device_file:
    devices = json.load(device_file)

# Define netmiko exception for try/except block to prevent python script from crashing
netmiko_exception = (netmiko.NetMikoAuthenticationException,
                     #netmiko.NetmikoAuthError,
                     #netmiko.NetmikoTimeoutError,
                     netmiko.NetMikoTimeoutException)

# Create ssh connection to each router with for loop
for device in devices:
    # Update/Fill username and password to device inventory before making ssh connection with netmiko
    device["username"] = username
    device["password"] = password
    # Use try/except block to prevent script crash/error from netmiko
    try:
        print("~"*79)
        print("Connecting to device", device["ip"])

        # Create ssh connetion to router with device inventory
        # 1. router ip address
        # 2. device type
        # 3. username
        # 4. password
        connection = netmiko.ConnectHandler(**device)

		#Create File txt to save log
        file = open(dt + ' ' + connection.find_prompt() +'.txt', 'w')
        log = open(dts + ' ' + connection.find_prompt() + '.txt', 'a')
        cmd = ["show env all\n",
        "show ip interface brief\n",
        "show interface status\n",
        "show vlan brief\n",
        "show log\n",
        "show spanning-tree sum\n",
        "show version\n",
        "show processes cpu history\n",
        "show running-config\n"]

        # Send command to router (setting terminal length for entire output - disable pagination (page break))
        connection.send_command("terminal length 0")
        time.sleep(1)

        # Get router prompt and display command to execute on the router
        
        # Send command to router 

        for show in cmd:
            output=connection.send_command(show)
            print(output)
            file.write(connection.find_prompt() + show +"\n" + output + '\n')
            log.write(dts + ' ' + connection.find_prompt() + show + '\n')
        
            
            
        # Closing the ssh connection
        connection.disconnect()

    except netmiko_exception as e:
        # Display failed device and error information to notify the root cause of ssh connection crash
        print("Failed to", device['ip'], e)