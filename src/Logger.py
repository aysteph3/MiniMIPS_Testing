# Copyright (C) 2017 Siavoosh Payandeh Azad, Stephen Oyeniran

import sys
import os
import time


class Logger(object):
    """
    This Class is for redirecting the console messages to a log file...
    """
    def __init__(self, generated_files_folder):
        if os.path.exists(generated_files_folder+'/Console.log'):
            os.remove(generated_files_folder+'/Console.log')
        self.terminal = sys.stdout
        self.log = open(generated_files_folder+'/Console.log', "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass