
un playbook de Ansible y la estructura necesaria para realizar un despliegue completo en un único nodo de Kubernetes, desde la instalación de dependencias hasta el lanzamiento de una aplicación.

Este ejemplo crea un clúster de un solo nodo con kubeadm y luego despliega una aplicación.


### create manifiest

```yaml
kubectl apply -f deploy.yaml
kubectl apply -f svc.yaml
kubectl apply -f ingress.yaml
```

```yaml
kubectl -n proyecto-final get all
kubectl -n proyecto-final get svc
kubectl -n proyecto-final get ingress
```

```yaml
kubectl -n proyecto-final describe ingress api-ingress
kubectl -n proyecto-final get endpoints api
kubectl -n proyecto-final logs deploy/api
```

## run
```kubectl commands
kubectl run tester --image=curlimages/curl -it --rm --   sh -lc "curl http://172.20.251.174:80"
kubectl run tester --image=curlimages/curl -it --rm --   sh -lc "curl http://10.0.3.190:5000"


ansible-playbook -i hosts deploy_app.yml --tags "install"

ansible-playbook -i hosts deploy_app.yml

## desplie de los manifiestos de kubernetes con ansible
ansible-playbook -i inventory.ini deploy_app.yml

docker build -t local/miap:1.0
minikube image load local/miapp:1.0

kubectl -n proyecto-final set image deploy/api api=local/miap:1.0 --record
kubectl -n proyecto-final rollout status deply/api
```


kubectl exec -it pod/api-68d7df7fb8-f7gw2 -- bash
kubectl exec -it pod/api-68d7df7fb8-4wqm5 -- bash

## fichero hosts
```yaml
[kubernetes_nodes]
192.168.1.100
```

## install ansible
```yaml
sudo apt install ansible

python3 -m venv .venv
source .venv/bin/activate


pip3 install ansible-lint jinja2
```



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