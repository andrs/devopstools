# devopstools

python application.py

export HOSTNAME=localhost

export HOSTNAME=172.26.0.3


export USERNAME=andres
export PASSWORD=andres
export PORT=5432
export DB_NAME=andresdb



## pruebas
docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=andres@domain.com -e PGADMIN_DEFAULT_PASSWORD=andres -d dpage/pgadmin4

# borrar imagenes
sudo docker rm -f $(sudo docker ps -a -q)

sudo docker build -t app:2.0 .

# prueba de execución
sudo sudo docker run -it --name flask app:1.0 bash

sudo docker exec -it flask bash

# postgres
## acceso cliente psql
psql -U andres -d andresdb

# list rows (empty for now)
SELECT * FROM user;

## comandos
netstat -tulnp
mkdir -p grafana/provisioning/{datasource,dashboards}
sudo docker compose up -d
sudo docker compose down


python3 -m venv runtime
source ./runtime/bin/activate


sudo docker run --rm  -it --cpus="1.0" alpine sh  -ls
sudo docker run --rm -it --cpus="1.0" alpine sh -lc "apk add --no-cache stress-ng && stress-ng --cpu 1 --timeout 600s"


sudo docker compose up -d
sudo docker compose up -d
sudo docker compose ps


http://localhost:8888/login?next=/

## emoticons
⚠⚠⚠⚠⚠

⚠️ (Emoji): This is the emoji version of the warning sign, often used in digital communication to convey caution or importance.

❗ (Exclamation Mark Emoji): A red exclamation mark, also used to indicate importance, urgency, or a warning.

❗️ (Heavy Exclamation Mark Symbol): A more formal, heavier version of the exclamation mark.

⛔ (No Entry Sign): Used to prohibit entry or indicate something is forbidden.

🛑 (Stop Sign): Indicates a full stop is required.

🚫 (No Symbol / Prohibited Sign): Often used over another symbol to indicate "no," "not allowed," or "prohibited" (e.g., 🚭 No Smoking).

❌ (Cross Mark / Multiplication X): Can be used to indicate something is wrong, incorrect, or to mark a deletion.

✅ (Check Mark): The opposite of a warning, indicates something is correct, approved, or done.

ℹ️ (Information Emoji): An "i" in a circle, used to denote information.

➡️ (Right Arrow Emoji): Often used to point to important information or the next step.

➡️ (Rightwards Arrow): A standard arrow symbol.

➕ (Plus Sign): Can indicate addition, positive, or "more."

➖ (Minus Sign): Can indicate subtraction, negative, or "less."

❓ (Question Mark Emoji): Used to ask a question or indicate uncertainty.

❔ (White Question Mark Ornament): A stylistic question mark.

❓ (Black Question Mark Ornament): Another stylistic question mark.

💡 (Light Bulb Emoji): Often represents an idea, solution, or insight.

🔔 (Bell Emoji): Can indicate a notification or alert.

🚨 (Police Car Light Emoji): Used to indicate an emergency or urgent situation.

🔥 (Fire Emoji): Can represent fire, but also something "lit" or "hot" (trendy).

⚡ (High Voltage Sign / Lightning Bolt): Often signifies electricity, power, or speed.

☣️ (Biohazard Sign): Indicates biological hazard.

☢️ (Radioactive Sign): Indicates radioactive material.

💀 (Skull and Crossbones): Universal symbol for poison or death.