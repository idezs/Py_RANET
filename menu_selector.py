#!/usr/bin/python3

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import cmd_collector

def json_selector(site):
    if site == "CGH_LLK_PM_AUTOMATION_JUNIPER":
        cmd_collector.cisco_pm_function(site)
    elif site == "CGH_SAIMAI_PM_AUTOMATION_JUNIPER":
        cmd_collector.cisco_pm_function(site)
    else: print("False")