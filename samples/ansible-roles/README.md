
# Roles - buena práctica para organizar


### Estructura clave:
```yaml
roles/webserver/
├── tasks/main.yml
├── templates/index.html.j2
└── defaults/main.yml
```

```yaml
Playbook que invoca el role es: roles.yml
```

#### ejecutar
ansible-playbook -i inventory.ini roles.yml