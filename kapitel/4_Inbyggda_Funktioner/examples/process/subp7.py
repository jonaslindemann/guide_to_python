# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:41:59 2018

@author: Jonas Lindemann
"""

import subprocess


def execute_with_output(cmd):

    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True) as p:
        stdout, _ = p.communicate()

        if p.returncode == 0:
            return stdout
        else:
            return None


if __name__ == "__main__":

    output = execute_with_output('dir')

    if output is not None:

        lines = output.split("\n")

        for line in lines:
            print('>' + line)
    else:
        print('Ingen utdata returnerades.')