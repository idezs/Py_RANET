#!/usr/bin/python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import cmd_collector

def icon_selector(site):
    if site == "PM_AUTOMATION_CISCO_1":
        cmd_collector.cisco_pm_function(site)
    elif site == "PM_AUTOMATION_CISCO_2":
        cmd_collector.cisco_pm_function(site)
    else: print("False")
