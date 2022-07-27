from datetime import datetime
from time import sleep
import serial
import json
import get_user_pass
import time

date = datetime.now()
dts = date.strftime("%d-%m-%Y" + ' ' + "%H-%M-%S")
dt = date.strftime("%d-%m-%Y" + ' ' + "%H-%M")
ts = date.strftime("%d-%m-%Y")

# Print RANET Banner
banner = """      ___           ___           ___           ___                   
     /  /\         /  /\         /  /\         /  /\          ___     
    /  /::\       /  /::\       /  /::|       /  /::\        /__/\    
   /  /:/\:\     /  /:/\:\     /  /:|:|      /  /:/\:\       \  \:\   
  /  /::\ \:\   /  /::\ \:\   /  /:/|:|__   /  /::\ \:\       \__\:\  
 /__/:/\:\_\:\ /__/:/\:\_\:\ /__/:/ |:| /\ /__/:/\:\ \:\      /  /::\ 
 \__\/~|::\/:/ \__\/  \:\/:/ \__\/  |:|/:/ \  \:\ \:\_\/     /  /:/\:\ 
    |  |:|::/       \__\::/      |  |:/:/   \  \:\ \:\      /  /:/__\/
    |  |:|\/        /  /:/       |__|::/     \  \:\_\/     /__/:/     
    |__|:|~        /__/:/        /__/:/       \  \:\       \__\/      
     \__\|         \__\/         \__\/         \__\/     """

print(banner)

# Old Banner
"""print("      ___           ___           ___           ___                   ")
print("     /  /\         /  /\         /  /\         /  /\          ___     ")
print("    /  /::\       /  /::\       /  /::|       /  /::\        /__/\    ")
print("   /  /:/\:\     /  /:/\:\     /  /:|:|      /  /:/\:\       \  \:\   ")
print("  /  /::\ \:\   /  /::\ \:\   /  /:/|:|__   /  /::\ \:\       \__\:\  ")
print(" /__/:/\:\_\:\ /__/:/\:\_\:\ /__/:/ |:| /\ /__/:/\:\ \:\      /  /::\ ")
print(" \__\/~|::\/:/ \__\/  \:\/:/ \__\/  |:|/:/ \  \:\ \:\_\/     /  /:/\:\ ")
print("    |  |:|::/       \__\::/      |  |:/:/   \  \:\ \:\      /  /:/__\/")
print("    |  |:|\/        /  /:/       |__|::/     \  \:\_\/     /__/:/     ")
print("    |__|:|~        /__/:/        /__/:/       \  \:\       \__\/      ")
print("     \__\|         \__\/         \__\/         \__\/     ")"""

# Get user credential from user input
username, password = get_user_pass.get_credential()

# Get device inventory for netmiko module
# 1. router ip address
# 2. device type
with open('device_init.json', 'r') as device_file:
    devices = json.load(device_file)


# Serial connect comport
for device in devices:
    # Fill username and password to device inventory making initial configuration
    device["username"] = username
    device["password"] = password
    
    # Connection serial to devices
    serial_port = serial.Serial(device["comport"], baudrate=9600, timeout=None, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, xonxoff=False)
    
    log = open(dts + ' ' + device["hostname"] + '.txt', 'a')

    # Send "CTRL+C" to Serial x2
    serial_port.write(b'\x03'), sleep(.5)
    serial_port.write(b'\x03'), sleep(.5)

    # Print Serial Connect Prompt
    print("~"*79 + "\n")
    print("Connecting to Serial Comport", serial_port.name)
    print("\n" + "~"*79)

    # Start command initial devices
    # Send cmd ("enable", "conf t")


    serial_port.write("\n".encode('utf-8')), sleep(.5)
    log.write(dts + device["hostname"] + "enable\n")
    serial_port.write("enable\n".encode('utf-8')), sleep(.5)
    log.write(dts + device["hostname"] + "terminal len 0\n")
    serial_port.write("terminal len 0\n".encode('utf-8')), sleep(.5)
    log.write(dts + device["hostname"] + "config terminal\n")
    serial_port.write("config terminal\n".encode('utf-8')), sleep(.5)
    print(serial_port.read(serial_port.inWaiting()).decode('utf-8'))

    # Send cmd "hostname"
    cmd_host = ("hostname " + device["hostname"] + "\n")
    log.write(dts + device["hostname"] + cmd_host + "\n")
    serial_port.write(cmd_host.encode('utf-8')), sleep(.5)
    print(serial_port.read(serial_port.inWaiting()).decode('utf-8'))

    # Send cmd "ip domain-name"
    cmd_domain = ("ip domain-name " + device["domain"] + "\n")
    log.write(dts + device["hostname"] + cmd_domain + "\n")
    serial_port.write(cmd_domain.encode('utf-8')), sleep(.5)
    print(serial_port.read(serial_port.inWaiting()).decode('utf-8'))

    # Send cmd "Key Gen SSH"
    serial_port.write("crypto key gen rsa\n".encode('utf-8')), sleep(5)
    log.write(dts + device["hostname"] + "crypto key gen rsa\n")
    output = (serial_port.read(serial_port.inWaiting()).decode('utf-8'))

    # Check Condition existing key
    if output.rfind("replace") != -1:
        serial_port.write("yes\n".encode('utf-8')), sleep(3)
        serial_port.write("1024\n".encode('utf-8')), sleep(5)
        log.write(dts + device["hostname"] + "yes\n")
        log.write(dts + device["hostname"] + "1024\n")
    else: 
        serial_port.write("1024\n".encode('utf-8')), sleep(5)
        log.write(dts + device["hostname"] + "1024\n")
    
    # Send command ssh version 2
    serial_port.write("ip ssh version 2\n".encode('utf-8')), sleep(5)
    log.write(dts + device["hostname"] + "ip ssh version 2\n")


    # Send cmd "Username Password From get_user_pass"
    cmd_userpass = ("username " + username + " " + "privilege 15 " + "secret " + password + "\n")
    log.write(dts + device["hostname"] + cmd_userpass + "\n")
    serial_port.write(cmd_userpass.encode('utf-8')), sleep(.5)

    # Send config line vty 
    log.write(dts + device["hostname"] + "line vty 0 4\n")
    serial_port.write("line vty 0 4\n".encode('utf-8')), sleep(.5)
    log.write(dts + device["hostname"] + "login local\n")
    serial_port.write("login local\n".encode('utf-8')), sleep(.5)
    log.write(dts + device["hostname"] + "transport input ssh\n")
    serial_port.write("transport input ssh\n".encode('utf-8')), sleep(.5)

    serial_port.write("exit\n".encode('utf-8')), sleep(.5)
    serial_port.write("\n".encode('utf-8')), sleep(.5)

    # Send config interface VLAN
    log.write(dts + device["hostname"] + "interface vlan 1\n")
    serial_port.write("interface vlan 1\n".encode('utf-8')), sleep(.5)
    cmd_ip = ("ip address " + device["ip"] + " " + device["subnet"] + "\n")
    log.write(dts + device["hostname"] + cmd_ip +"\n")
    serial_port.write(cmd_ip.encode('utf-8')), sleep(5)
    serial_port.write("end\n".encode('utf-8')), sleep(.5)
    
    # Send command save running-config to startup-config
    serial_port.write(b'\x03'), sleep(.5)
    log.write(dts + device["hostname"] +"copy run start\n")
    serial_port.write("copy run start\n".encode('utf-8')), sleep(.5)
    serial_port.write("\n".encode('utf-8')), sleep(.5)

    print(serial_port.read(serial_port.inWaiting()).decode('utf-8'))
    #Close connect serial alway
    serial_port.close()
    print(serial_port.is_open)


