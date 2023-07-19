import os
import time

vm_uuid = input("Enter the VM UUID: ")
username = input("Enter the username: ")
ip_address = input("Enter the IP address: ")

os.chdir(r"C:\Program Files\Oracle\VirtualBox")
os.system(f'VBoxManage startvm {vm_uuid} --type headless')
cmd = f'ssh {username}@{ip_address}'

while True:
  result = os.system(cmd)
  if result == -1:
    print('connection closed')
    break
  time.sleep(1)
