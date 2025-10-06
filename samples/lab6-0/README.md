# Día 6 — Kubernetes I: Pods, Deployments, Services

**Duración:** 4 h  
**Objetivos:**

- Entender la **arquitectura** de Kubernetes y sus objetos base.
- Crear apps con **Deployments** (replicasets/pods) y exponerlas con **Services**.
- Operar con `kubectl` (crear, listar, describir, escalar, borrar).
- Empezar buenas prácticas: **labels/selectors**, **probes** y **namespaces**.

---

## 1) Teoría (1h 30m)

### 1.1 Arquitectura (visión rápida)

- **Control Plane**: `kube-apiserver`, `etcd` (estado), `kube-scheduler` (colocación), `controller-manager`.
- **Nodos**: `kubelet` (agente), `kube-proxy` (networking), **runtime** (containerd/Docker).
- **Manifiestos YAML**: deseamos un estado; el plano de control lo **concilia**.

### 1.2 Objetos clave

- **Pod**: unidad mínima de despliegue (1+ contenedores que comparten red/volúmenes).
- **ReplicaSet**: mantiene N réplicas de Pods.
- **Deployment**: gestiona ReplicaSets y **rollouts/rollbacks**.
- **Service**: IP estable y balanceo para Pods (por **label selector**).
    - **ClusterIP** (por defecto, interno), **NodePort** (expone puerto en nodos), **LoadBalancer** (cloud).
- (**Opcional hoy**) **Ingress**: reglas HTTP/HTTPS de entrada (requiere controlador).
- **Namespace**: aislar recursos por equipo/proyecto/ambiente.
- **Labels/Selectors**: metadatos y “pegamento” entre objetos.

### 1.3 Ciclo básico de trabajo

1. Escribes YAML (Deployment/Service).
2. `kubectl apply -f …`
3. Verificas: `kubectl get` / `kubectl describe` / `kubectl logs`.
4. Ajustas (escalar, actualizar imagen), Kubernetes reconcilia.

### 1.4 Probes y Strategy

- **Liveness Probe**: ¿debo reiniciar el contenedor?
- **Readiness Probe**: ¿está listo para recibir tráfico?
- **Startup Probe**: más tiempo en inicios lentos.
- **RollingUpdate** en Deployments (sin downtime controlado).

### 1.5 Redes en K8s (alto nivel)

- Todo Pod obtiene una IP (modelo **CNI**).
- La IP del Pod es **efímera** → usa **Service** para IP estable/nombre DNS.
- DNS interno (CoreDNS): `svcname.namespace.svc.cluster.local`.

---

## 2) Preparación del entorno (10–15 min)

# 1. Herramientas básicas

Primero asegúrate de tener actualizado el sistema:

```bash
sudo apt update && sudo apt upgrade -y
```
Instala utilidades que te harán falta:

```bash
sudo apt install -y curl wget apt-transport-https ca-certificates gnupg lsb-release
```

---

# 2. `kubectl` (cliente de Kubernetes)

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

---

# 3. Elegir el clúster local

Tienes **2 opciones prácticas** para los labs:

### Opción A — **Minikube** (sencilla y recomendada)

1. Instalar dependencias:

```bash
sudo apt install -y conntrack socat
```

2. Descargar Minikube:

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

3. Arrancar el clúster (usando Docker como driver):

```bash
minikube start --driver=docker
```

4. Probar:

   `kubectl get nodes`


---

### Opción B — **kind** (Kubernetes in Docker, más ligero)

1. Instalar:

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

2. Crear cluster:

```bash
kind create cluster --name labk8s
```

3. Verificar:

```bash
kubectl cluster-info --context kind-labk8s
```

---

# 4. (Opcional) Herramientas adicionales

- **Helm** (gestor de paquetes para K8s):

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

- **Lens** o **k9s** (UI para gestionar el cluster):

```bash
sudo snap install kontena-lens --classic   # Lens
sudo snap install k9s --classic            # k9s (CLI)
```


---

# 5. Verificación final

```bash
kubectl create namespace devops-lab
kubectl config set-context --current --namespace=devops-lab
kubectl get ns
```

Si ves `devops-lab` listado, estás listo para aplicar los `yaml` de los labs.

---

📌 **Recomendación para clase**:

- Si quieres algo rápido y que los alumnos repliquen fácil → **Minikube**.

- Si el PC no tiene muchos recursos → **kind**
---

## 3) Laboratorio 1 — Primer Deployment + Service (45–60 min)

### 3.1 Crear un Deployment (nginx)

**deploy-nginx.yaml**

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-nginx
  labels:
    app: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web
      tier: frontend
  template:
    metadata:
      labels:
        app: web
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 3
          periodSeconds: 5
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 10
```

Aplicar y verificar:

```bash
kubectl apply -f deploy-nginx.yaml
kubectl get deploy,rs,pods -l app=web
kubectl describe deploy web-nginx
```

### 3.2 Exponer con Service (NodePort)

**svc-nginx.yaml**

```bash
apiVersion: v1
kind: Service
metadata:
  name: web-svc
  labels:
    app: web
spec:
  type: NodePort
  selector:
    app: web
    tier: frontend
  ports:
  - name: http
    port: 80
    targetPort: 80
    nodePort: 30080  # opcional; si lo omites, K8s elige uno
```

Aplicar y probar:

```bash
kubectl apply -f svc-nginx.yaml
kubectl get svc web-svc
```

- **Minikube**:

```bash
minikube service web-svc --url
# abre URL o curl a la URL retornada
```

- **kind / Docker Desktop**: usa IP del nodo y `:30080`.

```bash
kubectl get nodes -o wide
curl http://<NODE-IP>:30080/
```

### 3.3 Escalar, actualizar y rollback

```bash
# Escalar réplicas
kubectl scale deploy web-nginx --replicas=4
kubectl get pods -l app=web -o wide

# Actualizar imagen
kubectl set image deploy/web-nginx nginx=nginx:1.25.2
kubectl rollout status deploy/web-nginx

# Historial y rollback
kubectl rollout history deploy/web-nginx
kubectl rollout undo deploy/web-nginx
```

---

## 4) Laboratorio 2 — App de 2 capas (API + Redis) (45 min)

### 4.1 API Python + Redis (ClusterIP interno)

**api-redis-deploy.yaml**

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 2
  selector:
    matchLabels: { app: api }
  template:
    metadata:
      labels: { app: api }
    spec:
      containers:
      - name: api
        image: ghcr.io/tsl-edu/flask-echo:latest # o tu imagen del día 4
        ports:
        - containerPort: 5000
        env:
        - name: REDIS_HOST
          value: redis
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
spec:
  replicas: 1
  selector:
    matchLabels: { app: redis }
  template:
    metadata:
      labels: { app: redis }
    spec:
      containers:
      - name: redis
        image: redis:7
        ports:
        - containerPort: 6379
```

**api-redis-svc.yaml**

```bash
apiVersion: v1
kind: Service
metadata:
  name: api-svc
spec:
  selector: { app: api }
  ports:
  - port: 80
    targetPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: redis
spec:
  selector: { app: redis }
  ports:
  - port: 6379
    targetPort: 6379
```

Aplicar y probar dentro del clúster:

```bash
kubectl apply -f api-redis-deploy.yaml
kubectl apply -f api-redis-svc.yaml
kubectl get all -l app=api
kubectl get svc api-svc

# Prueba interna desde un pod temporal
kubectl run curl --image=curlimages/curl -it --rm -- \
  sh -lc 'curl -s http://api-svc/ && echo'
```

> Si quieres exponer la API hacia fuera: crea un Service `NodePort` para `api-svc` o instala un **Ingress Controller** (más propio de Día 7).

---

## 5) Notas de instructor

- Remarcar **labels/selector**: si no coinciden, el Service no enruta.
- **Probes**: ver cómo `readiness` controla si entra en el balanceo.
- Cambiar réplicas y mostrar Pods en **nodos distintos** (si hay varios).
- `kubectl explain <recurso>` es oro para el examen y el día a día.

---

## 6) Troubleshooting (rápido)

- **Pods pendientes (Pending)**: no hay recursos o `imagePull` falló → `kubectl describe pod`.
- **CrashLoopBackOff**: error en contenedor → `kubectl logs <pod> -c <container>`.
- **Service no responde**:
    - Ver `selector` vs `labels`.
    - `kubectl get endpoints <svc>` (¿hay IPs?).
    - Probar desde dentro: `kubectl run curl … curl http://svc:port/`.
- **Minikube URL**: si NodePort no abre, usa `minikube service <svc> --url`.

---

## 7) Limpieza

```bash
kubectl delete -f svc-nginx.yaml -f deploy-nginx.yaml
kubectl delete -f api-redis-svc.yaml -f api-redis-deploy.yaml
# (opcional) borrar namespace:
# kubectl delete ns devops-lab
```

---

## 8) Preguntas de repaso (30 min)

1. ¿Qué diferencia hay entre **Pod**, **ReplicaSet** y **Deployment**?
2. ¿Para qué sirve un **Service** y qué tipos conoces?
3. ¿Cómo escalar un Deployment a 5 réplicas?
4. ¿Qué hace una **readinessProbe** vs una **livenessProbe**?
5. ¿Cómo expones un servicio hacia fuera en un clúster local?
6. ¿Qué comando muestra el historial de despliegues y cómo haces **rollback**?