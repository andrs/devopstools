
### build flaskapi:1.0 image
docker build -t flaskapi:1.0 .

## borrar contenedores
sudo docker rm -f $(sudo docker ps -a -q)

#### borrar images
sudo docker images -a

sudo docker build -t flaskapi:3.0 .

sudo docker run -d --name flaskach -p 5000:5000 flaskapi:3.0

sudo docker run -d --name flaskacha -p 5000:5000 flaskapi:3.0

#### entrar en un contenedor
sudo sudo docker run -it --name flask flaskapi:2.0 bash


(myenv) ubuntu@ip-10-0-10-102:~/lab1/img$ sudo docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
flaskapi       5.0       81c36a2b00c4   3 minutes ago    1.12GB

(myenv) ubuntu@ip-10-0-10-102:~/lab1/img$ sudo docker tag flaskapi:5.0 andrs/flaskapi:5.0
(myenv) ubuntu@ip-10-0-10-102:~/lab1/img$ sudo docker push andrs/flaskapi:5.0
