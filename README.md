# Ansible Benchmark Automation For A ProxMox Cloud Environment
A repo for all files related to using Ansible to automate VM benchmarking in our ProxMox environment.

## Important Resources
A list of useful resources and documentation to help you learn Ansible, Python scripting, etc.
+
* [Detailed YAML syntax documentation](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html#)
* [Using Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
* [Ansible command line tools](https://docs.ansible.com/ansible/latest/command_guide/index.html)

## Installing the Automated Benchmark Suite

### Step 1: Installing Git and Cloning the Repository
You'll need to clone this repository on the machine you've chosen to be the Ansible controller. To do this you need to have git installed. 

**1.** If you haven't already, update your Ubuntu.
```r
sudo apt update
```
**2.** Install git through the command line
```r
sudo apt-get install git-all
```
**3.** Clone this repository.
```r
git clone https://github.com/ElliotBidwell/cloud-env-ansible.git
```

### Step 2: Ansible Installation
Next, you'll need Ansible installed on the controller.

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

### Step 3: Starting SSH Server on Remote Machines
For the remote machines to be accessible, they need to be open to SSH connections. One way to do this is with an OpenSSH server.

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

### Step 4: Adding the Remote Hosts' IP Addresses to Your List of Known SSH Hosts
Another step to making the remote hosts accessible to the controller is to add their hostnames and IP addresses to your Ubuntu Hosts file.

**1.** The hosts file is located at `/etc/hosts`. It can be accessed for editing via the following command.
```r
sudo nano /etc/hosts
```
**2.** At the top of the file you will see a 2-column list of IP addresses next to their corresponding hostnames as shown below. 
Add the IPs and hostnames of each of your remote host machines where `<host-ip>` and `<hostname>` are shown. Take care to make
the formatting and spacing consistent with each item in the list.
```
127.0.0.1       localhost
127.0.1.1       ansible-primary
<1st-host-ip>   <1st-hostname>
<2nd-host-ip>   <2nd-hostname>
and so on...
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
### Commands Used to Run Benchmarks
To install and run the CoreMark CPU benchmark.
```r
ansible-playbook ./playbooks/coremark-playbook.yml -i ./inventory/hosts --user ansadmin --ask-pass --ask-become-pass
```
To install and run the iperf3 network speed benchmark.
```r
ansible-playbook ./playbooks/iperf3-playbook.yml -i ./inventory/hosts --user ansadmin --ask-pass --ask-become-pass
```

### Arguments/Options Used Above
- `--ask-pass` causes a prompt for the remote host user's password.
* `--ask-become-pass` causes a prompt for the remote host's root password.
* `-m ping` uses the ping module to test the ssh connection with each host.
+ `--start-at-task="<task name>"` runs a play or playbook starting at a designated task `<task name>`. Useful for debugging.
