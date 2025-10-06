# Práctica de Repaso (Día 1 – Día 8)

## Objetivos

- Reforzar los conceptos clave de DevOps.
- Practicar control de versiones con Git.
- Construir y ejecutar contenedores Docker.
- Probar persistencia y redes.
- Desplegar una app sencilla en Kubernetes.
- Usar Vagrant para crear una VM y provisionarla.

---

## Parte 1 – DevOps y Git (Día 1-3)

1. **Crear un repo local**

```bash
mkdir repaso-devops && cd repaso-devops
git init
```

2. **Crear app Flask mínima**  
   Archivo `app.py`:

```bash
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Repaso DevOps  - Día 1 a 8"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

3. **Commit inicial**

```bash
git add app.py
git commit -m "App Flask inicial"
```

---

## Parte 2 – Docker (Día 3-4)

1. **Dockerfile**

```bash
FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
```

2. **Construir y correr**

```bash
docker build -t repaso-flask:1.0 .
docker run -d --name repaso -p 5000:5000 repaso-flask:1.0
curl http://localhost:5000
```

3. **Persistencia con volumen**

```bash
docker run -d --name repaso-vol -p 5001:5000 \
  -v datos_repaso:/app/data repaso-flask:1.0
```

---

## Parte 3 – Docker Compose (Día 5)

Archivo `docker-compose.yml`:

```bash
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8080:5000"
    volumes:
      - datos_repaso:/app/data
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: labuser
      POSTGRES_PASSWORD: labpass
      POSTGRES_DB: labdb
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  datos_repaso:
  pgdata:
```

Levantar:

```bash
docker compose up -d
curl http://localhost:8080

```

---

## Parte 4 – Kubernetes básico (Día 6-7)

1. **Namespace**

```bash
kubectl create namespace repaso
kubectl config set-context --current --namespace=repaso
```

2. **Deployment + Service**  
   `repaso-deploy.yaml`:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: repaso-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: repaso
  template:
    metadata:
      labels:
        app: repaso
    spec:
      containers:
      - name: flask
        image: repaso-flask:1.0
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: repaso-svc
spec:
  selector:
    app: repaso
  ports:
  - port: 80
    targetPort: 5000
  type: NodePort
```

    Aplicar:

 ```bash
 kubectl apply -f repaso-deploy.yaml
minikube service repaso-svc --url -n repaso
 ```

3. **Test de Service Discovery**

```bash
kubectl run tester --image=curlimages/curl -n repaso -it --rm -- \
  sh -lc "curl http://repaso-svc"
```

---

## Parte 5 – Vagrant (Día 8)

1. **Carpeta**

```bash
mkdir ~/repaso-vagrant && cd ~/repaso-vagrant
```

2. **Vagrantfile**

```bash
 Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "forwarded_port", guest: 80, host: 8082
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -y
    apt-get install -y apache2
    echo 'Repaso DevOps con Vagrant' > /var/www/html/index.html
    systemctl enable --now apache2
  SHELL
end
```

3. **Levantar**

```bash
vagrant up --provider=virtualbox
vagrant ssh -c "curl -s http://localhost"
```

4. **Validar en navegador**  
   [http://localhost:8082](http://localhost:8082)

## Preguntas de repaso

1. ¿Qué diferencia hay entre un contenedor y una VM?
2. ¿Cómo persistes datos en Docker?
3. ¿Qué resuelve el Service Discovery en Kubernetes?
4. ¿Qué hace el provisionamiento en Vagrant?
5. ¿Qué comando inicializa un repositorio Git?