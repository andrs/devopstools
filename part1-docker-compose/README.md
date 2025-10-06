# Deploy a Flask App with PostgreSQL Using Docker Compose

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



