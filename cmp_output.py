#!/usr/bin/python3
import difflib
import filecmp
import time
from datetime import datetime

#Timestamp generate and convert to String
now = datetime.now()
timestamp = datetime.timestamp(now)
date_time = datetime.fromtimestamp(timestamp)
str_date = date_time.strftime("%m-%d-%Y")
str_date_time = date_time.strftime("%m-%d-%Y-%H-%M")
str_dts = date_time.strftime("%m-%d-%Y-%H:%M:%S")

def cmp_files():
    # Definate files and folder for compare
    new_file = "/home/jirasak/pyranet_ws/compare_config_folder/new_run_conf.txt"
    cmp_file = "/home/jirasak/pyranet_ws/compare_config_folder/candidate_run_conf.txt"
    # Compere file size for confirm difference
    compare = filecmp.cmp(new_file, cmp_file, shallow = False)
    print(compare)
    if compare == False:
        # Open and read files
        new_file_rl = open(new_file).readlines()
        cmp_file_rl = open(cmp_file).readlines()
        # Loop read lines check difference
        for line in difflib.unified_diff(
            new_file_rl, cmp_file_rl, fromfile='new_file', tofile='cmp_file'):
            msg_cmp = line
        cmp_log_html = difflib.HtmlDiff().make_file(new_file_rl, cmp_file_rl, new_file, cmp_file)
        gen_html_file = open('cmp_log_' + str_date_time + '.html', 'w')
        gen_html_file.write(cmp_log_html)
        gen_html_file.close()

    else:
        msg_cmp = "New Config and Candidate Config Equal"

    return msg_cmp