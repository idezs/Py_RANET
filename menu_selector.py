#!/usr/bin/python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import cmd_collector

def icon_selector(site):
    if site == "PM_CGH_LLK_AUTOMATION_JUNIPER":
        cmd_collector.cisco_pm_function(site)
    elif site == "PM_CGH_SAIMAI_AUTOMATION_JUNIPER":
        cmd_collector.cisco_pm_function(site)
    else: print("False")