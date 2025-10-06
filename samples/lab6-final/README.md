
# dia6 lab real

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
kubectl apply -f 06-api.yaml
kubectl apply -f 07-worker.yaml

# pgAdmin
kubectl apply -f 08-pgadmin.yaml

# Exposición:
# Ingress (recomendado)
kubectl apply -f 09-ingress.yaml
# ...o NodePort:
# kubectl apply -f 09-nodeport-api.yaml
```

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