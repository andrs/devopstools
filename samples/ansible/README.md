
---

## Objetivos

- Comprender la automatización de configuraciones con Ansible.
- Trabajar con inventarios, playbooks, variables y plantillas.
- Usar módulos para gestionar usuarios, paquetes y servicios.
- Aplicar seguridad con `ansible-vault`.

---

## 1. – Fundamentos de Ansible (1h)

### 1.1 ¿Qué es Ansible?

- Herramienta de **automatización de TI** → instalación, configuración, despliegues.
- Sin agentes → se conecta por **SSH**.
- Declarativo → se define “estado deseado” en vez de comandos imperativos.

### 1.2 Arquitectura

- **Control Node**: máquina con Ansible instalado
- **Managed Nodes**: máquinas a configurar.
- **Inventario**: lista de nodos (`/etc/ansible/hosts` o `.ini/.yaml`).
- **Playbook**: conjunto de tareas en YAML.
- **Módulos**: acciones (`user`, `apt`, `service`, `template`, etc.).

### 1.3 Ventajas

- Fácil de usar (YAML).
- Idempotencia → aplicar varias veces no rompe nada.
- Integración con DevOps (Docker, K8s, CI/CD).

---

```instalacion de ansible 
install ansible-link

1328  pip3 install ansible-link jinja2
pipx list
```

```ini
[web]
localhost ansible_connection=local
```

```bash
ansible -i inventory.ini all -m ping
```


### Paso 3: Comandos ad-hoc

- Crear usuario:

```bash
ansible -i inventory.ini all -m user -a "name=devops state=present"
```

- Instalar paquete:

```bash


```

---

## 3. Laboratorio 2 – Playbook básico

Ejecutar:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

Comprobar:

```bash
curl http://localhost
```

## resultado
```
ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/ansible$ curl http://localhost
<html>
<head><title>DevOps con Puppet</title></head>
<body style="font-family:sans-serif">
  <h1>¡Hola Andrés desde Puppet!. Usando anchor command</h1>
  <p>Estado deseado aplicado con <strong>puppet apply</strong>.</p>
</body>
</html>
ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/ansible$
```
