#### borrar images
sudo docker images -a

sudo docker build -t flaskapi:10.0 .

sudo docker run -d --name flaskach10 -p 5000:5000 flaskapi:10.0

#### entrar en un contenedor
sudo sudo docker run -it --name flask flaskapi:2.0 bash

### listar imagenes
sudo docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
flaskapi       5.0       81c36a2b00c4   3 minutes ago    1.12GB

sudo docker tag flaskapi:10.0 andrs/flaskapi:10.0
sudo docker push andrs/flaskapi:10.0
