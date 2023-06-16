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
Use to run a playbook on each host in an inventory/group.
```r
ansible-playbook -i <inventory file path> <inventory group> <playbook file path> --user <remote host username> --ask-pass --ask-become-pass
```

### Arguments/Options Used Above
- `-i <inventory file path> <inventory group>` designates an inventory group of hosts in the selected inventory file to run a playbook against. Leave `<inventory group>` blank to run the playbook against every host in the file.
* `--ask-pass` causes a prompt for the remote host user's password.
* `-m ping` pings each host.
* ``
*
+
