#!/usr/bin/env python

import json

data = None
with open("current_run_info.json") as fobj:
    data = json.loads(fobj.read())

user = data['user']
host1 = data['vm1']
host1 = data['vm2']
key = data['keyfile']

result = """{0} ansible_ssh_host={1} ansible_ssh_user={2} ansible_ssh_private_key_file={3}
{4} ansible_ssh_host={5} ansible_ssh_user={6} ansible_ssh_private_key_file={7}""".format("atomic-test.example.com",host1,user,key,"atomic-test2.example.com",host2,user,key)
with open("atomic-host-tests/inventory", "w") as fobj:
    fobj.write(result)

