#!/usr/bin/python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
# Import python module to get password (not show password when user is typing) from user
from getpass import getpass

# Create function to get input string from user (Python 2 or Python 3) for example, username
def get_input(prompt=""):
    # Use try/except block to prevent script crash/error
    try:
        # Python 2 use "raw_input" to get input string
        line = raw_input(prompt)
    except:
        # Python 3 use "input" to get input string
        line = input(prompt)
    
    # return input string after execute all line codes within the function
    return line

# Create function to get username and password from user
def get_credential():
    username = get_input("Enter Username for initial all Devices: ")
    password = None
    while not password:
        password = getpass()
        password_verify = getpass("Retype your password for initial all Devices: ")
        
        # If the "password" is not equal to "password_verify", the password is reset to "None"
        # and back to the while loop to let user retype password
        if password != password_verify:
            print("\nPasswords do not match. Try again.\n")
            password = None
    
    # return the username and password after execute all line codes within the function
    return username, password

    # while True:
    #     password = getpass()
    #     password_verify = getpass("Retype your password: ")
    #     if password == password_verify:
    #         break
    #     else:
    #         print("\nPasswords do not match. Try again.\n")
    #         continue
    # return username, password