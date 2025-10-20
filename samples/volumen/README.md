# Docker : Uso de contenedores

**Fecha:** Mar 17 sept  
**Duración:** 4 horas

---

##  Objetivos de aprendizaje

- Comprender la **arquitectura Docker**: cliente, daemon, imágenes y contenedores.
- Diferenciar imágenes y contenedores en su ciclo de vida.
- Ejecutar contenedores desde imágenes oficiales.
- Usar volúmenes para **persistir datos** entre ejecuciones.
- Desarrollar seguridad básica en la ejecución de contenedores.

---

## 1. Teoría (1h 30m)

### 1.1 Arquitectura de Docker

- **Cliente (CLI):** ejecuta comandos (`docker run`, `docker build`).
- **Servidor (Docker Daemon):** proceso que crea y gestiona contenedores.
- **REST API:** medio de comunicación entre cliente y daemon.
- **Registry:** almacena imágenes (ej. DockerHub, GitHub Container Registry).

Ejemplo visual (puedes usar en PPT):

```markdown
CLI (usuario) → Docker Daemon → Contenedores
             ↕
           DockerHub
```

---

### 1.2 Imágenes y Contenedores

- **Imagen:** plantilla inmutable que contiene aplicación + dependencias.
- **Contenedor:** instancia en ejecución de una imagen.
- **Ciclo de vida de un contenedor:**
    1. Crear (`docker create`)
    2. Iniciar (`docker start` o `docker run`)
    3. Pausar / detener (`docker stop`, `docker pause`)
    4. Reiniciar (`docker restart`)
    5. Eliminar (`docker rm`)

---

### 1.3 Volúmenes en Docker

- Problema: cuando borramos un contenedor, se pierde su data.
- Solución: **volúmenes**, que permiten persistencia en el host.
- Tipos de almacenamiento:
    - **Volúmenes:** manejados por Docker (`docker volume create`).
    - **Bind mounts:** ruta directa del host al contenedor.
    - **tmpfs:** almacenamiento temporal en memoria.

Ejemplo:

```bash
docker run -d -p 8080:80 -v datos_nginx:/usr/share/nginx/html nginx
```

---

## 2. Laboratorio práctico (2h)

### Paso 1: Comprobar instalación

```bash
docker --version
docker info
```

---

### Paso 2: Ejecutar primer contenedor

`docker run hello-world`

Verifica que Docker funciona y puede descargar imágenes del registry.

---
### Paso 3: Correr Nginx

```bash
docker run -d --name web1 -p 8080:80 nginx
```

- `-d`: modo “detached”.
- `--name`: asigna nombre al contenedor.
- `-p`: mapea puerto 8080 del host → 80 del contenedor.

Abrir navegador en:

```bash
http://localhost:8080
```

Debe aparecer la página por defecto de Nginx.

---

### Paso 4: Inspeccionar contenedor

```bash
docker ps
docker inspect web1
```

- Ver puertos, configuración de red, ID del contenedor.

---

### Paso 5: Probar persistencia sin volumen

1. Entrar al contenedor:

```bash
docker exec -it web1 bash
```

2. Editar página:

```bash
echo "Hola desde Docker" > /usr/share/nginx/html/index.html
```

3. Ver en navegador: `http://localhost:8080`  
   Sale el texto modificado.
4. Eliminar contenedor:

```bash
docker rm -f web1
```

5. Correr nuevo contenedor `nginx` y verificar → **el cambio se perdió**.

---

### Paso 6: Usar volumen para persistencia

1. Crear volumen:

```bash
docker volume create webdata
```

2. Correr contenedor con volumen:

```bash
docker run -d --name web2 -p 8080:80 -v webdata:/usr/share/nginx/html nginx
```

3. Editar archivo persistente:

```bash
docker exec -it web2 bash -c "echo 'Hola persistente' > /usr/share/nginx/html/index.html"
```

4. Ver en navegador: `http://localhost:8080` → “Hola persistente”.
5. Eliminar contenedor:

```bash
docker rm -f web2
```

6. Correr otro contenedor con el mismo volumen:

```bash
docker run -d --name web3 -p 8080:80 -v webdata:/usr/share/nginx/html nginx
```

El cambio persiste gracias al volumen.

---

## 4. Preguntas de repaso (30m)

1. ¿Cuál es la diferencia entre una imagen y un contenedor?
2. ¿Qué comando permite ver todos los contenedores activos?
3. ¿Qué sucede con los datos cuando eliminamos un contenedor sin volumen?
4. ¿Qué tipos de almacenamiento soporta Docker (3 principales)?
5. Escribe el comando para ejecutar un contenedor `nginx` en el puerto 8081 de tu máquina con un volumen llamado `datos`.
6. Explica el ciclo de vida de un contenedor en Docker.