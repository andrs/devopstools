

## ejemplo de llamada
```yaml
localhost ansible_connection=local ansible_become=true ansible_become_method=sudo
(myenv) ubuntu@ip-10-0-10-102:~/dia10$ cat inventory.ini
[web]
localhost ansible_connection=local
(myenv) ubuntu@ip-10-0-10-102:~/dia10$ ansible -i inventory.inc all -m ping
localhost | SUCCESS => {
"ansible_facts": {
"discovered_interpreter_python": "/usr/bin/python3"
},
"changed": false,
"ping": "pong"
}
(myenv) ubuntu@ip-10-0-10-102:~/dia10$ ansible -i inventory.ini all -m ping
localhost | SUCCESS => {
"ansible_facts": {
"discovered_interpreter_python": "/usr/bin/python3"
},
"changed": false,
"ping": "pong"
}
```

netstat -tulnp

ansible -i inventory.inc all -m user -a "name=ubuntu state=present"
ansible -i inventory.inc all -b -m apt -a "name=nginx state=present update_cache=yes"
