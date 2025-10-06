
un playbook de Ansible y la estructura necesaria para realizar un despliegue completo en un único nodo de Kubernetes, desde la instalación de dependencias hasta el lanzamiento de una aplicación.

Este ejemplo crea un clúster de un solo nodo con kubeadm y luego despliega una aplicación.


## Estructura de Archivos
Para organizar el proyecto de forma limpia y escalable, te recomiendo la siguiente estructura de carpetas y archivos:

ansible_k8s/
├── roles/
│   └── kubernetes_node_setup/
│       └── tasks/
│           └── main.yml
├── files/
│   └── app-deployment.yml
├── inventory.ini
└── deploy_k8s_app.yml


