# Author: Dan

# Run install.py before hand
import subprocess
import os

pwd = '//home/coremark/'

def run_cmd(command):
    p1 = subprocess.call([command], cwd=pwd)
    results('//home/coremark/run1.log')
    results('//home/coremark/run2.log')

def results(runs):
    print("=======================================")
    print("Results:")
    file = open(runs, 'r')
    for line in file:
        print(line)

run_cmd('make')

