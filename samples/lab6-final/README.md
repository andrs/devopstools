
# DIA6 LAB REAL NOT AI

# Ejecución

```yaml
# Namespace
kubectl apply -f 00-namespace.yaml

# Config & Secret
kubectl apply -f 01-config-secrets.yaml

# Infra
kubectl apply -f 02-postgres.yaml
kubectl apply -f 04-rabbit.yaml
kubectl apply -f 05-redis.yaml

# Inicializa DB
kubectl apply -f 03-db-init-job.yaml
kubectl -n devops-lab get jobs

# App + Worker
kubectl apply -f 03-api.yaml
kubectl apply -f 07-worker.yaml

# pgAdmin
kubectl apply -f 08-pgadmin.yaml

# Exposición:
# Ingress (recomendado)
kubectl apply -f 04-ingress.yaml
# ...o NodePort:
# kubectl apply -f 09-nodeport-api.yaml
```

kubectl exec -it -n devops-lab pod/api-68d7df7fb8-4mqhr  -- bash

**Comprobar**

```yaml
kubectl -n devops-lab get all
kubectl -n devops-lab get svc
kubectl -n devops-lab get ingress
```

**Acceso**

- **API**
    - Con Ingress: `http://api.local/` (o `curl http://api.local/`)
    - Con NodePort: `curl http://<NODE-IP>:30080/`
- **Encolar tarea**:  
  `curl "http://api.local/tasks/enqueue?x=7&y=5"`
- **Consultar resultado** (sustituye `<ID>`):  
  `curl "http://api.local/tasks/result/<ID>"`
- **pgAdmin**: `http://<NODE-IP>:30081`
    - Conectar a `db:5432`, user `labuser`, pass `labpass`, DB `labdb`.
- **Rabbit UI** (exponer con minikube service o un NodePort si quieres).

---

# Troubleshooting rápido

- **API 502/404 (Ingress)**
    - `kubectl -n devops-lab describe ingress api-ingress`
    - `kubectl -n devops-lab get endpoints api` (¿tiene IPs?)
    - `kubectl -n devops-lab logs deploy/api`
- **Worker no consume tareas**
    - `kubectl -n devops-lab logs deploy/worker`
    - ¿Rabbit listo? `kubectl -n devops-lab logs deploy/rabbit`
    - Revisar `CELERY_BROKER_URL`/`CELERY_RESULT_BACKEND` en pods (`kubectl -n devops-lab exec -it <pod> -- env | grep CELERY`)
- **DB Init Job falla**
    - `kubectl -n devops-lab logs job/db-init`
    - Asegura que Service `db` resuelve y que el secret tiene credenciales.
- **Permisos de almacenamiento**
    - Ver `kubectl -n devops-lab describe pvc pgdata`
    - En kind/minikube suele haber `default` StorageClass; si no, crea una temporal.

## endpoints
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$  kubectl -n devops-lab get endpoints api
NAME   ENDPOINTS                         AGE
api    10.0.3.201:5000,10.0.4.109:5000   2m42s
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$


## logs
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl -n devops-lab get all
NAME                           READY   STATUS             RESTARTS   AGE
pod/api-68d7df7fb8-4mqhr       1/1     Running            0          41s
pod/api-68d7df7fb8-xlvd8       1/1     Running            0          41s
pod/db-69c8cb6574-kvplz        0/1     Pending            0          16m
pod/db-init-zwhdr              1/1     Running            0          13m
pod/pgadmin-848dc56c6b-zbvsn   1/1     Running            0          13m
pod/rabbit-6d55ccbfcc-972cw    1/1     Running            0          16m
pod/redis-54c8b869c7-779nf     1/1     Running            0          15m
pod/worker-b76744d7d-qt5kp     0/1     ImagePullBackOff   0          13m

NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)              AGE
service/api       ClusterIP   172.20.239.122   <none>        80/TCP               41s
service/db        ClusterIP   172.20.229.2     <none>        5432/TCP             16m
service/pgadmin   NodePort    172.20.105.100   <none>        80:30081/TCP         13m
service/rabbit    ClusterIP   172.20.73.247    <none>        5672/TCP,15672/TCP   16m
service/redis     ClusterIP   172.20.65.66     <none>        6379/TCP             15m

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/api       2/2     2            2           41s
deployment.apps/db        0/1     1            0           16m
deployment.apps/pgadmin   1/1     1            1           13m
deployment.apps/rabbit    1/1     1            1           16m
deployment.apps/redis     1/1     1            1           15m
deployment.apps/worker    0/1     1            0           13m

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/api-68d7df7fb8       2         2         2       41s
replicaset.apps/db-69c8cb6574        1         1         0       16m
replicaset.apps/pgadmin-848dc56c6b   1         1         1       13m
replicaset.apps/rabbit-6d55ccbfcc    1         1         1       16m
replicaset.apps/redis-54c8b869c7     1         1         1       15m
replicaset.apps/worker-b76744d7d     1         1         0       13m

NAME                STATUS    COMPLETIONS   DURATION   AGE
job.batch/db-init   Running   0/1           13m        13m
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl exec -it pod/api-68d7df7fb8-4mqhr  -- bash
Error from server (NotFound): pods "api-68d7df7fb8-4mqhr" not found
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl exec -it -n devops-lab pod/api-68d7df7fb8-4mqhr  -- bash
root@api-68d7df7fb8-4mqhr:/app# curl 172.20.239.122
Bienvenido a la API Flask de la práctica 3 🚀root@api-68d7df7fb8-4mqhr:/app#
root@api-68d7df7fb8-4mqhr:/app#
root@api-68d7df7fb8-4mqhr:/app# exit
exit
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl -n devops-lab get all^C
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ curl 172.20.105.100:30081
^C
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl -n devops-lab get endpoints api
NAME   ENDPOINTS                         AGE
api    10.0.3.201:5000,10.0.4.109:5000   2m42s
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ curl 10.0.3.201:5000
^C
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl exec -it -n devops-lab pod/api-68d7df7fb8-4mqhr  -- bash
root@api-68d7df7fb8-4mqhr:/app# curl 10.0.3.201:5000
Bienvenido a la API Flask de la práctica 3 🚀root@api-68d7df7fb8-4mqhr:/app#
root@api-68d7df7fb8-4mqhr:/app#
