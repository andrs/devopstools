# Deploy a Flask App with PostgreSQL Using Docker Compose

## Step 1: Project Structure
### Set up your project directory and virtual environment
mkdir part1-docker-compose
cd part1-docker-compose
python3 -m venv .venv
source .venv/bin/activate

## Then structure your project like this:
flask-compose-api/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── init.sql
├── docker-compose.yml
└── .venv


## commands
### Build and Run
docker compose up -d

docker compose down

## Add Task:
### task 1
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"description": "Learn Docker Compose"}'

### task 1
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"description": "Complete Project on Docker Compose"}'

### get tasks
http://localhost:5000/tasks

