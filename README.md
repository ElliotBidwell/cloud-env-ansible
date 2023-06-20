# Ansible For ProxMox Cloud Environment
A repo for all files related to using Ansible to automate VM benchmarking in our ProxMox environment.

## Ansible Installation
**1.** If you haven't already, update your Ubuntu.
```r
sudo apt update
```
**2.** Install the common files for software-properties.
```r
sudo apt install software-properties-common
```
**3.** Add the Ansible repository
```r
sudo apt-add-repository --yes --update ppa:ansible/ansible
```
**4.** Install Ansible
```r
sudo apt install ansible
```
**5.** Check your current Ansible version
```r
ansible --version
```

## Important Commands
### Commonly Used Commands
Use to ping each host in an inventory/group.
```r
ansible -i <inventory file path> <inventory group> -m ping --user <remote host username> --ask-pass
```
Use to run a playbook on each host in an inventory/group. `-e <inventory group>` designates a group of hosts within the inventory to run the playbook on.
```r
ansible-playbook <playbook file path> -i <inventory file path> -e <inventory group> --user <remote host username> --ask-pass --ask-become-pass
```

### Arguments/Options Used Above
- `--ask-pass` causes a prompt for the remote host user's password.
* `--ask-become-pass` causes a prompt for the remote host's root password.
* `-m ping` uses the ping module to test the ssh connection with each host.
+
