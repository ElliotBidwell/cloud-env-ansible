# Ansible Benchmark Automation For A ProxMox Cloud Environment
A repo for all files related to using Ansible to automate VM benchmarking in our ProxMox environment.

## Important Resources
A list of useful resources and documentation to help you learn Ansible, Python scripting, etc.
+
* [Detailed YAML syntax documentation](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html#)
* [Using Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- [Ansible command line tools](https://docs.ansible.com/ansible/latest/command_guide/index.html)


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

## Starting SSH Server on Remote Machines
For the remote machines to be accessible, the need to be open to SSH connections. One way to do this is with an OpenSSH server.

**1.** It usually doesn't hurt to update Ubuntu first.
```r
sudo apt update
```

**2.** Another very helpful package is net-tools, which allows you to easily access local IP related info.
```r
sudo apt install net-tools
```

**3.** Install the OpenSSH server package.
```r
sudo apt install openssh-server
```

**4.** Start up the SSH server.
```r
sudo service ssh start
```
To stop or restart the server, replace `start` with `stop` or `restart`, respectively.

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
### Commands Used to Run Benchmarks
To install and run the CoreMark CPU benchmark.
```r
ansible-playbook ./playbooks/coremark-playbook.yml -i ./inventory/hosts --user ansadmin --ask-pass --ask-become-pass
```
To install and run the iperf3 network speed benchmark.
```r
ansible-playbook ./playbooks/iperf3-playbook-2.yml -i ./inventory/hosts --user ansadmin --ask-pass --ask-become-pass
```

### Arguments/Options Used Above
- `--ask-pass` causes a prompt for the remote host user's password.
* `--ask-become-pass` causes a prompt for the remote host's root password.
* `-m ping` uses the ping module to test the ssh connection with each host.
+ `--start-at-task="<task name>"` runs a play or playbook starting at a designated task `<task name>`. Useful for debugging.
