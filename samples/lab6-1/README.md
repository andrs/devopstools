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
curl http://<NODE-IP>:30080/     # en kind o Docker Desktop

# Prueba interna desde pod
kubectl run curl --image=curlimages/curl -it --rm --   sh -lc 'curl -s http://api-svc/ && echo'

sudo docker run --rm  -it --cpus="1.0" alpine sh  -ls