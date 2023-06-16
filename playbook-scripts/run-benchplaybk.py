# Author: Elliot

import subprocess
import os

def run_playbooks(dirs):
    # This script's file path
    script_filepath = os.path.dirname(__file__)
    # Path to playbooks
    play_path = script_filepath + "/../playbooks/"
    inv_option = "-i"
    # Path to inventory files
    inv_path = script_filepath + "/../inventory/"
    # Inventory file name
    inv_file = "hosts" # In the future, be able to pass in file name as argument
    # Inventory group
    inv_group = "localVMsElliot" # Not used yet
    # User option
    user_option = "--user"
    # Host user
    user = "ebidwell" # In the future, be able to user name as argument
    # User ask password option
    user_pass_opt = "--ask-pass"
    # Sudo ask password option
    sudo_pass_opt = "--ask-become-pass"
    
    for playbook in dirs:
        print(f'Executing playbook {playbook}')
        subprocess.run(["ansible-playbook", play_path + playbook, inv_option, inv_path + inv_file, user_option, user, user_pass_opt, sudo_pass_opt])
        

playbookdirs = ['run-coremark.yml']
run_playbooks(playbookdirs)

    
