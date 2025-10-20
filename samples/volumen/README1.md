#  Día 5 – Docker Compose y Swarm

**Fecha:** Jue 19 sept  
**Duración:** 4 horas

---

##  Objetivos de aprendizaje

- Comprender qué es **Docker Compose** y su utilidad para aplicaciones multicontenedor.
- Crear y ejecutar stacks con archivos `docker-compose.yml`.
- Usar variables y escalado de servicios.
- Introducir conceptos de **Docker Swarm** (cluster, servicios, stacks, secretos).
- Implementar un laboratorio práctico con Flask + Mongo + Nginx en Compose y Swarm.

---

## 1. Teoría (1h 30m)

### 1.1 ¿Qué es Docker Compose?

- Herramienta para definir y correr aplicaciones multicontenedor.
- Se configura con un archivo `docker-compose.yml`.
- Permite:
    - Definir servicios, redes y volúmenes.
    - Escalar servicios fácilmente.
    - Ejecutar todo con un solo comando:
```bash
docker-compose up -d
```

---

### 1.2 Sintaxis básica de `docker-compose.yml`

Ejemplo mínimo:

```bash
version: "3.9"
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  db:
    image: mongo
    volumes:
      - mongodata:/data/db
volumes:
  mongodata:
```

---

### 1.3 Escalado de servicios

- Para levantar varias réplicas:

```bash
docker-compose up -d --scale web=3
```

- Balanceo básico entre instancias (solo con Compose).

---

### 1.4 Introducción a Docker Swarm

- **Swarm** = orquestador nativo de Docker.
- Convierte múltiples nodos en un **cluster**.
- Conceptos clave:
    - **Manager/Worker**: roles en el cluster.
    - **Services**: definición de contenedores gestionados por Swarm.
    - **Stacks**: colecciones de servicios definidos en un Compose file.
    - **Secrets**: gestión segura de credenciales.

Inicializar Swarm:

```bash
docker swarm init
```

Crear servicio:

```bash
docker service create --name web -p 8080:80 nginx
```

Escalar servicio:

```bash
docker service scale web=3
```

---

## 2. Laboratorio práctico (2h)

### Paso 1: Crear `docker-compose.yml`

```bash
version: "3.9"
services:
  flask:
    build: ./flaskapp
    ports:
      - "5000:5000"
    networks:
      - appnet
    depends_on:
      - mongo

  mongo:
    image: mongo
    volumes:
      - mongodata:/data/db
    networks:
      - appnet

  nginx:
    image: nginx
    ports:
      - "8080:80"
    networks:
      - appnet

volumes:
  mongodata:

networks:
  appnet:
```

Carpeta `flaskapp/` contiene el `Dockerfile` y la app Flask del **día 4**.

---

### Paso 2: Levantar stack en Compose

```bash
docker-compose up -d
docker-compose ps
```

Probar:

- `http://localhost:5000` → Flask.
- `http://localhost:8080` → Nginx.

---

### Paso 3: Escalar servicio Flask

```bash
docker-compose up -d --scale flask=3
docker ps
```

Verás varias réplicas de Flask levantadas.

---

### Paso 4: Iniciar Docker Swarm

```bash
docker swarm init
```

---

### Paso 5: Deploy stack en Swarm

```bash
docker stack deploy -c docker-compose.yml mystack
docker stack services mystack
```

---

### Paso 6: Escalar servicio en Swarm

```bash
docker service scale mystack_flask=5
```

---

### Paso 7: Usar secretos (Swarm)

1. Crear secreto:

```bash
echo "clave_supersecreta" | docker secret create mongo_pass -
```

2. Montarlo en el contenedor:

```bash
services:
  mongo:
    image: mongo
    secrets:
      - mongo_pass
secrets:
  mongo_pass:
    external: true
```

---

## 3. Preguntas de repaso (30m)

1. ¿Qué comando levanta todos los servicios definidos en un `docker-compose.yml`?
2. ¿Cómo escalas el servicio `web` a 4 réplicas en Compose?
3. ¿Cuál es la diferencia entre un **Service** en Compose y en Swarm?
4. ¿Qué comando inicializa un cluster de Swarm?
5. Escribe la definición básica de un servicio `redis` con volumen persistente en Compose

