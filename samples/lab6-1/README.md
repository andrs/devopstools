### aws eks update-kubeconfig --name public-endpoint-cluster

kubectl create namespace devops-lab
kubectl config set-context --current --namespace=devops-lab

# Aplicar manifests
kubectl apply -f deploy-nginx.yaml
kubectl apply -f svc-nginx.yaml
kubectl apply -f api-redis-deploy.yaml
kubectl apply -f api-redis-svc.yaml


kubectl get all
kubectl describe svc web-svc
kubectl rollout status deploy web-nginx

# Escalar
kubectl scale deploy web-nginx --replicas=4
kubectl get pods -l app=web


# Probar acceso
curl http://172.20.71.31:30080/     # en kind o Docker Desktop

# Prueba interna desde pod
kubectl run curl --image=curlimages/curl -it --rm --   sh -lc 'curl -s http://api-svc/ && echo'

sudo docker run --rm  -it --cpus="1.0" alpine sh  -ls


## resultado del servicio
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-1$ kubectl describe svc web-svc
Name:                     web-svc
Namespace:                default
Labels:                   app=web
Annotations:              <none>
Selector:                 app=web,tier=frontend
Type:                     NodePort
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       172.20.71.31
IPs:                      172.20.71.31
Port:                     http  80/TCP
TargetPort:               80/TCP
NodePort:                 http  30080/TCP
Endpoints:                10.0.4.36:80,10.0.3.65:80,10.0.4.182:80 + 1 more...
Session Affinity:         None
External Traffic Policy:  Cluster
Internal Traffic Policy:  Cluster
Events:                   <none>
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-1$


#### entrar en un pod i probar la ip del servicio
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-1$ kubectl exec -it pod/api-58b5c9f9fc-ls2vz -- bash
root@api-58b5c9f9fc-ls2vz:/app#
root@api-58b5c9f9fc-ls2vz:/app# curl
curl: try 'curl --help' or 'curl --manual' for more information
root@api-58b5c9f9fc-ls2vz:/app# curl http://172.20.71.31
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@api-58b5c9f9fc-ls2vz:/app#
root@api-58b5c9f9fc-ls2vz:/app#


#### 
command terminated with exit code 127
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-1$ kubectl get pods -l app=web
NAME                         READY   STATUS    RESTARTS   AGE
web-nginx-7bf8bc65c6-2clrj   1/1     Running   0          5m
web-nginx-7bf8bc65c6-7x2kk   1/1     Running   0          67m
web-nginx-7bf8bc65c6-mw95v   1/1     Running   0          67m
web-nginx-7bf8bc65c6-tg9bq   1/1     Running   0          5m
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-1$
