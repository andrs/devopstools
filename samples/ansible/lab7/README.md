
## **Dos “nodos” de práctica en Docker con SSH**

> Útil si quieres que practiquen contra “remotos” reales, sin levantar VMs.

### 7.1 Crear dos contenedores Ubuntu con SSH

```bash
# Red y dos contenedores con puertos SSH diferentes
docker network create ansinet || true
docker run -d --name node1 --hostname node1 --network ansinet -p 2221:22 ubuntu:22.04 sleep infinity
docker run -d --name node2 --hostname node2 --network ansinet -p 2222:22 ubuntu:22.04 sleep infinity

# Instalar openssh-server y crear usuario 'ansible' con clave pública
for n in node1 node2; do
  docker exec -it $n bash -lc 'apt-get update && apt-get install -y openssh-server sudo && mkdir -p /run/sshd'
  docker exec -it $n bash -lc 'useradd -m -s /bin/bash ansible && echo "ansible ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ansible'
  PUB=$(cat ~/.ssh/id_rsa.pub)
  docker exec -it $n bash -lc "mkdir -p ~ansible/.ssh && echo '$PUB' > ~ansible/.ssh/authorized_keys && chown -R ansible:ansible ~ansible/.ssh && chmod 600 ~ansible/.ssh/authorized_keys"
  docker exec -it $n bash -lc '/usr/sbin/sshd -D &'   # lanza el SSHD
done

```

### 7.2 Inventario SSH

`inventory-ssh.ini`

```ini
[web]
node1 ansible_host=127.0.0.1 ansible_port=2221 ansible_user=ansible ansible_ssh_private_key_file=~/.ssh/id_rsa
node2 ansible_host=127.0.0.1 ansible_port=2222 ansible_user=ansible ansible_ssh_private_key_file=~/.ssh/id_rsa
```

Prueba:

```bash
ansible -i inventory-ssh.ini web -m ping
ansible -i inventory-ssh.ini web -b -m apt -a "name=nginx state=present update_cache=yes"
```

> Si ves `Permission denied (publickey)`, revisa que tu `~/.ssh/id_rsa.pub` haya quedado en `~ansible/.ssh/authorized_keys` dentro de cada contenedor.

**Limpieza (opcional):**

```bash
docker rm -f node1 node2
docker network rm ansinet
```

---

# Validación rápida (checklist)

- `ansible --version` ✅
- `ansible -i inventory.ini all -m ping` ✅
- `ansible-playbook -i inventory.ini playbook.yml` ✅ (Nginx responde 200)
- `ansible-playbook -i inventory.ini site.yml` ✅ (template + handler)
- `ansible-playbook -i inventory.ini roles.yml` ✅ (role funcionando)
- `ansible-playbook -i inventory.ini vault-demo.yml --ask-vault-pass` ✅ (muestra secretos)
- (Opcional SSH) `ansible -i inventory-ssh.ini web -m ping` ✅
- 