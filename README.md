# ✅ Final Year Project – DevOps Tool Integration Engineer

### ✅ General Aim (usefully tools and commands for me and for anybody)

Students are required to design, implement, and document a database-driven web application. The application must be containerised using Docker, orchestrated with Kubernetes, provisioned with Ansible, and deployed via a CI/CD pipeline using Jenkins.

The project must also include basic security and monitoring.

## comandos utilizados
## pruebas

```This part comes directly from the official website: https://docs.docker.com/engine/install/ubuntu

# Uninstall older versions just in case
sudo apt-get remove docker docker-engine docker.io containerd runc

# Set up the repository
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release

# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# Set up the stable repository

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# to run docker without sudo
sudo usermod -aG docker $USER
````

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

docker run -d -p 8080:80 -v datos_nginx:/usr/share/nginx/html nginx
docker run -d --name web1 -p 8080:80 nginx

docker exec -it web1 bash

docker ps
docker inspect web1

docker rm -f web2

docker volume create webdata
docker run -d --name web2 -p 8080:80 -v webdata:/usr/share/nginx/html nginx

docker exec -it web2 bash -c "echo 'Hola persistente' > /usr/share/nginx/html/index.html"
docker rm -f web2

docker run -d --name web3 -p 8080:80 -v webdata:/usr/share/nginx/html nginx

### delete all images
sudo docker image prune -a

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