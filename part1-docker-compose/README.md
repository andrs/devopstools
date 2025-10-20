# Deploy a Flask App with PostgreSQL Using Docker Compose
## Postgres and pgAdmin in Docker

### that experiment involves setting up a PostgreSQL instance in Docker, a PGAdmin instance, and app and enabling communication between these two containers.
### access pgadmin cross security way

## Step 1: Project Structure
### Set up your project directory and virtual environment
mkdir part1-docker-compose
cd part1-docker-compose
python3 -m venv .venv
source .venv/bin/activate

## Then structure your project like this:

```yaml
flask-compose-api/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── init.sql
├── docker-compose.yml
└── .venv
```

##  3. Dockerfile → construir imagen miapp:1.0 .
sudo docker build -t app:1.0 .

## commands
### Build and Run
docker compose up -d

docker compose down

## Add Task:
### task 1
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"description": "parte 2 del proyecto final del curso"}'

### task 1
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"description": "parte 2 del proyecto final del curso"}'

### get tasks
http://localhost:5000/tasks

## cambiar puerto
http://localhost:8080/tasks

```yaml
sudo journalctl -u docker.service -n 100 --no-pager
```



``` commands certificates
create TLS certificates 
openssl genrsa -out server.key 2048
openssl req -new -out server.csr -key server.key
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

### Securing PgAdmin
``` Configure TLS to use pgAdmin. 
 
# create a directory in your $HOME that pgadmin docker can use
mkdir /home/ubuntu/docker_volumes/
mkdir /home/ubuntu/docker_volumes/certs/
mkdir /home/ubuntu/docker_volumes/pgadmin/

# copy your certificates in the certs/ directory
cp /path/to/hostname.crt  /home/ubuntu/docker_volumes/certs/
cp /path/to/hostname.key  /home/ubuntu/docker_volumes/certs/

# make both directories owned by the docker id (=5050), run $ docker run -it --rm --entrypoint /usr/bin/id dpage/pgadmin4 to convince yourself

ubuntu@ip-10-0-10-102:~$ sudo docker run -it --rm --entrypoint /usr/bin/id dpage/pgadmin4
uid=5050(pgadmin) gid=0(root) groups=0(root)

so configure

sudo chown -R 5050:5050 /home/ubuntu/Documents/certs
sudo chown -R 5050:5050 /home/ubuntu/Documents/pgadmin


sudo docker run -p 5050:443 \
-v /home/ubuntu/docker_volumes/pgadmin:/var/lib/pgadmin \
-v /home/ubuntu/docker_volumes/certs/certificate.crt:/certs/server.cert \
-v /home/ubuntu/docker_volumes/certs/certificate.key:/certs/server.key \
-v /tmp/servers.json:/pgadmin4/servers.json \
-e 'PGADMIN_DEFAULT_EMAIL=andres@email.com' \
-e 'PGADMIN_DEFAULT_PASSWORD=andres' \
-e 'PGADMIN_ENABLE_TLS=True' \
-d dpage/pgadmin4

Install pgAdmin4

# Pull the image
docker pull dpage/pgadmin4
# Of course you need to replace user@email.com and StrongPassword to your own values
sudo docker run -p 5050:80 -e "PGADMIN_DEFAULT_EMAIL=user@email.com" -e "PGADMIN_DEFAULT_PASSWORD=StrongPassword" -d dpage/pgadmin4

```

curl https://localhost:5050  -k
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/login?next=/">/login?next=/</a>. If not, click the link.

```examples
docker network create my-network
docker run --name my-postgres -p 5433:5432 --network=my-network -v /home/j3/Documents/pg_db:/data -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e TZ=America/New_York  -d postgres:17

docker volume ls

remove images


sudo docker rm -f $(sudo docker ps -a -q)
sudo docker system prune -a

sudo lsof -i :15432

sudo lsof -i :15432
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
docker-pr 137050 root 4u IPv4 575714 0t0 TCP *:5432 (LISTEN)
sudo kill 137050
sudo lsof -i :15432

```