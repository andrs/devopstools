from flask import Flask, request, jsonify
from celery_app import make_celery
import os, psycopg2

app = Flask(__name__)
celery = make_celery(app)

DB_CONN = {
    "host": "db",
    "dbname": os.getenv("POSTGRES_DB", "labdb"),
    "user": os.getenv("POSTGRES_USER", "labuser"),
    "password": os.getenv("POSTGRES_PASSWORD", "labpass"),
}

def save_result(x, y, result):
    conn = psycopg2.connect(**DB_CONN)
    cur = conn.cursor()
    cur.execute("INSERT INTO resultados (x, y, resultado) VALUES (%s,%s,%s)", (x, y, result))
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    return "Bienvenido a la API Flask de la práctica 3 🚀"

@app.route("/ping")
def ping():
    return jsonify(ok=True)

@celery.task(bind=True)
def add_task(self, x, y):
    r = int(x) + int(y)
    save_result(x, y, r)
    return r

@app.route("/tasks/enqueue")
def enqueue():
    x = request.args.get("x", "0")
    y = request.args.get("y", "0")
    task = add_task.delay(x, y)
    return jsonify(task_id=task.id, status="queued")

@app.route("/tasks/result/<task_id>")
def result(task_id):
    res = celery.AsyncResult(task_id)
    return jsonify(id=task_id, status=res.status, result=res.result if res.ready() else None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)