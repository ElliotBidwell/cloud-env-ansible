# Ansible Benchmark Automation For A ProxMox Cloud Environment
A repo for all files related to using Ansible to automate VM benchmarking in our ProxMox environment.

## Important Resources
A list of useful resources and documentation to help you learn Ansible, Python scripting, etc.
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
You will need python to be at version 3.5 or later to Ansible to work properly. The latest version of Ubuntu Desktop should
come with it preinstalled

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

### Step 4: Adding the Remote Hosts' IP Addresses and Hostnames to SSH Hosts File and Adding SSH Fingerprints
Another step to making the remote hosts accessible to the controller is to add their hostnames and IP addresses to your Ubuntu hosts file,
and adding each remote host to your list of known hosts.

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
<...>           <...>
<nth-host-ip>   <nth-hostname>
```
Next, you'll need to add each host's to your list of known hosts.
**3.** Connect manually to each remote host using the following command.
```r
ssh <remote-user>@<remote-hostname>
```
Answer yes when it asks if you would like to continue connecting. It will then ask for the password corresponding to `<remote-user>`.
This process adds the ssh fingerprint to the `~/.ssh/known_hosts` file, making it possible for Ansible to connect via SSH as it cannot
perform Host Key checking.

### Step 5: Adding Hostnames to Ansible Inventory File
The final step in making the remote hosts accessible by proxmox is to add the hostnames of each remote host to the Ansible inventory file.

The file is located at `cloud-env-ansible/inventory/hosts`. You'll need to edit several sections.

**1.** Replace the existing hostnames under `[proxmoxbench]` with your own, excluding the localhost IP `127.0.0.1`, which should 
be left as-is.
```
# Group for all ProxMox VM hosts including controller
[proxmoxbench]
ans-remote0
ans-remote1
ans-remote2
127.0.0.1
```
**2.** Replace the existing hostnames under `[proxmoxbench]` with your own.
```
# Group all remote Proxmox VMs
[proxmoxremote]
ans-remote0
ans-remote1
ans-remote2
```
When you are finished, you should have a file that looks something like this, where each hostname in `< >` is replaced by one of
your own.
```
# Group for all ProxMox VM hosts including controller
[proxmoxbench]
<1st-hostname>
<2nd-hostname>
<3rd-hostname>
<...>
<nth-hostname>
127.0.0.1

# Group all remote Proxmox VMs
[proxmoxremote]
<1st-hostname>
<2nd-hostname>
<3rd-hostname>
<...>
<nth-hostname>

# Group for only the local controller
[proxmoxlocal]
127.0.0.1
```

### Step 6: Installing the Suite Using Ansible Plays
**1.** Install the CoreMark CPU benchmark on the remote machines.
```r
ansible-playbook ./playbooks/coremark-install-playbook.yml -i ./inventory/hosts --user <remote-host-user> --ask-pass --ask-become-pass
```
**2.** Install the iperf3 network benchmark on the controller machine.
```r
ansible-playbook ./playbooks/iperf3-local-install-playbook.yml -i ./inventory/hosts --user <remote-host-user> --ask-pass --ask-become-pass
```
**3.** Install the iperf3 network benchmark on the remote machines.
```r
ansible-playbook ./playbooks/iperf3-remote-install-playbook.yml -i ./inventory/hosts --user <remote-host-user> --ask-pass --ask-become-pass
```
**4.** Install Flexible I/O storage benchmark and RAMspeed memory benchmark included in Phoronix on remote machines.
```r
ansible-playbook ./playbooks/phoronix-install-playbook.yml -i ./inventory/hosts --user <remote-host-user --ask-pass --ask-become-pass
```

# Running the Benchmarks

To run the benchmarks, use this command to run their corresponding playbooks.
```r
ansible-playbook <playbook file path> -i <inventory file path> --user <remote host username> --ask-pass --ask-become-pass
```
Existing benchmark playbooks. Each are located in `<path-to-repo>/playbooks` 
* `run-coremark-playbook.yml` for CPU test. Results stored in `/home/<user>/coremark-results` on controller.
* `run-iperf3-playbook.yml` for network test. Results stored in `/home/<user>/iperf-results` on controller.
* `run-fio-playbook.yml` for storage I/O test. Results stored in `/home/<user>/stor-results` on controller.

# Other Useful Commands
Use to ping each host in an inventory/group.
```r
ansible -i <inventory file path> <inventory group> -m ping --user <remote host username> --ask-pass
```

# Useful Command Arguments/Options
* `--ask-pass` causes a prompt for the remote host user's password.
* `--ask-become-pass` causes a prompt for the remote host's root password.
* `-m ping` uses the ping module to test the ssh connection with each host.
* `--start-at-task="<task name>"` runs a play or playbook starting at a designated task `<task name>`. Useful for debugging.

# Implementation
Installation of the benchmarks on remote machines is accomplished with a single playbook for each test. These plays handle the installation of any depenencies including apt packages, pip packages, and repositories as well as the benchmark softwares themselves. Execution and the retrieval of benchmark results are done with another set of playbooks, which store the results in several designated directories on the controller.

## Coremark - CPU
### Installation
Handled by `coremark-install-playbook.yml`

**1.**  Local directory to store results `/home/<user>/coremark-results` is created with the `file` module.

**2.** `build-essential` and `git` packages are installed via the `apt` module.

**3.** [CoreMark github repo](https://github.com/eembc/coremark.git) is cloned into `/tmp`

**4.** Coremark is compiled by running `make`, which is included in `build-essentials`, on the repo using the command module.


### Running
Handled by `run-coremark-playbook.yml`

**1.** User is prompted to name the result files of the new test.

**2.** Remote results directory is created at `/home/<user>/coremark-results` on remote machine.

**3.** Coremark is run by executing `/tmp/coremark/coremark.exe` with `command` module.

**4.** `find` command is executed to search for each of the two resulting files located in their default locations, executing `cp` on each and copying them to the newly created remote directory with new names including appended hostnames, dates, and timestamps.

**5.** New result files are fetched from the remote to the local result directory using the `fetch` module.

## Iperf3 - Network
### Installation
Iperf3 must be installed on both the remotes and the controller so that the controller can host the iperf3 server while the remotes connect as
clients. The local install is handled by `iperf3-local-install-playbook.yml` while the remote install is handled by `iperf3-remote-install-playbook.yml`

**1.**  `iperf3` package is installed with apt module.

**2.**  Local directory `/home/<user>/iperf-results` and remote directory `/home/<user>/iperf3-results` are created with the file module.


### Running
This is done with three different plays within the same playbook, so as to allow separate sets of remote machines to be targeted by separate sets of tasks.

**1.** The first play runs locally on the controller machine. It includes a single task to run a command `that starts the iperf3 server`. This task is run asynchronously, allowing the subsequent tasks/plays to begin while this one continues. This is necessary because the command to run the server continues indefinitely, and thus the task does as well, which would would prevent the tasks that handle the client-side iperf connections from runnning if were not run asynchronously.

**2.** The next play is run on the remote machines. It's first task runs the iperf3 client connection using the `command` module, using the `--logfile` optionfor iperf3 to pipe the results into a log file in `/home/<user>/iperf3-results`. Then, the results are fetched from that directory to `/home/<user>/iperf-results` on the controller. This play is serialized so that it runs for a single remote host at a time, as the iperf3 server can only handle a single client at a time.

**3.** The last play simply runs locally on the controller and executes `killall iperf3` to stop the server and end the playbook.

## Flexible I/O - Storage I/O
### Installation

### Running
