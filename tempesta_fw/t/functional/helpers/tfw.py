#!/usr/bin/env python

"""
Helpers for interacting with Tempesta FW (start/stop, configure, etc). 
"""

import os
import subprocess
import sys

from . import teardown

__author__ = 'NatSys Lab'
__copyright__ = 'Copyright (C) 2012-2014 NatSys Lab. (info@natsys-lab.com).'
__license__ = 'GPL2'

_functest_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
_tempesta_dir = os.path.normpath(os.path.join(_functest_dir, '../../../'))

def start():
    _sh("SYNC_SOCKET=./sync_socket TDB=./tempesta_db ./tempesta.sh start")

def stop():
    _sh("./tempesta.sh stop")

def _sh(command):
    return subprocess.check_output(command, shell=True, cwd=_tempesta_dir)

def _is_started():
    return (0 == subprocess.call("lsmod | grep -q tempesta", shell=True))

def _stop_if_started():
    if (_is_started()):
        stop()

# Ensure we start and stop in a pristine environment.
assert (not _is_started())
# The teardown line is commented-out because we have the issue:
#   #10 -Oops on shutdown
# At this point it is not solved and Tempesta FW simply can't be stopped.
# TODO: un-comment it after the issue is fixed.
#teardown.register(_stop_if_started)
