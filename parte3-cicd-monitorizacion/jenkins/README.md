## Instación de Jenkins using Docker Compose

```yaml
docker build -t devopstools-jenkins .
sudo docker compose up -d

# para ver la clave
sudo docker compose logs


```

## Removing Jenkins
# remove all docker compose objects
docker compose down --volumes --rmi all 