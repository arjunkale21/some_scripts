# some_scripts
(Some general purpose scripts) 

# 1) vbox_ssh.py (script to connect virtual box vm through ssh.)

* Each and every VM in the virtual box has an unique UUID to which we can get to using: cmd : VBoxManage list vms.
* O/P of the above prompt would be name of the vm and their corresponding UUIDs.
* Out of which select and copy the specefic UUID for required VM.
* Also make sure you have username and IP address for the said VM.
* We can look for IP at Files >> Tools >> Network Manager.
* Hardcode these parameters into the code if you want to connect to a fix VM.
  
    