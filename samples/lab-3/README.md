

## 
docker rm -f pg
docker run -d --name pg2 --network app_net -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=labdb -v pgdata:/var/lib/postgresql/data -p 5432:5432 postgres:15

docker exec -it pg2 psql -U postgres -d labdb -c "SELECT * FROM notas;"

docker exec -it pg psql -U postgres -d labdb -c "CREATE TABLE notas(id SERIAL PRIMARY KEY, txt TEXT);"
docker exec -it pg psql -U postgres -d labdb -c "INSERT INTO notas(txt) VALUES ('persistencia ok');"
docker exec -it pg psql -U postgres -d labdb -c "SELECT * FROM notas;"