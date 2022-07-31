import netmiko
import json
import time
import get_user_pass
from datetime import datetime

#Timestamp generate and convert to String
now = datetime.now()
timestamp = datetime.timestamp(now)
date_time = datetime.fromtimestamp(timestamp)
str_date = date_time.strftime("%m-%d-%Y")
str_date_time = date_time.strftime("%m-%d-%Y-%H-%M")
str_dts = date_time.strftime("%m-%d-%Y-%H:%M:%S")

def cmd_pm():
    username, password = get_user_pass.get_credential()

# Get device inventory for netmiko module
# 1. router ip address
# 2. device type
with open('devices_no_credential.json', 'r') as device_file:
    devices = json.load(device_file)

# Define netmiko exception for try/except block to prevent python script from crashing
netmiko_exception = (netmiko.NetMikoAuthenticationException,
                     netmiko.NetmikoAuthError,
                     netmiko.NetmikoTimeoutError,
                     netmiko.NetMikoTimeoutException)

# Create ssh connection to each router with for loop
for device in devices:
    # Update/Fill username and password to device inventory before making ssh connection with netmiko
    device["ranetadmin"] = username
    device["!1Q2w3e4r5t!"] = password
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

        # Send command to router (setting terminal length for entire output - disable pagination (page break))
        connection.send_command("terminal length 0")
        time.sleep(1)

        # Get router prompt and display command to execute on the router
        print("\n" + connection.find_prompt() + "show cdp neighbor")

        # Send command to router 
        print(connection.send_command("show cdp neighbor") + "\n")

        # Closing the ssh connection
        connection.disconnect()

    except netmiko_exception as e:
        # Display failed device and error information to notify the root cause of ssh connection crash
        print("Failed to", device['ip'], e)