
# How to set Up Jenkins with Github and Docker via Web hook for CI/CD

## the repo url is public not credentials not needed

### build docker image and deploy with docker compose


docker run -d --name flaskapi -p 5000:5000 andrs/flaskapi:10.0

sudo docker run --rm -it --cpus="1.0" alpine sh -lc "apk add --no-cache stress-ng && stress-ng --cpu 1 --timeout 600s"

# 4) Levantar el stack

```bash
docker compose up -d
docker compose ps
```



# 🧹 Limpieza

```bash
cd ~/labs/monitoring
docker compose down -v
```

/home/ubuntu/project2/devopstools/parte3-cicd-monitorizacion/grafana/provisioning/dashboards/json

wget -O /home/ubuntu/project2/devopstools/parte3-cicd-monitorizacion/grafana/provisioning/dashboards/json/node-exporter-full.json https://grafana.com/api/dashboards/1860/revisions/33/download || true

``` Descarga (si tienes internet) o crea un placeholder.
/home/ubuntu/project2/devopstools/parte3-cicd-monitorizac 100%[=====================================================================================================================================>] 666.77K  --.-KB/s    in 0.03s

2025-10-07 09:29:06 (25.6 MB/s) - ‘/home/ubuntu/project2/devopstools/parte3-cicd-monitorizacion/grafana/provisioning/dashboards/json/node-exporter-full.json’ saved [682773/682773]

ubuntu@ip-10-0-10-102:~/project2/devopstools/parte3-cicd-monitorizacion/grafana/provisioning/dashboards/json$
ubuntu@ip-10-0-10-102:~/project2/devopstools/parte3-cicd-monitorizacion/grafana/provisioning/dashboards/json$ ls -rlt
total 672
-rw-rw-r-- 1 ubuntu ubuntu    138 Oct  7 08:19 README.md
-rw-rw-r-- 1 ubuntu ubuntu 682773 Oct  7 09:29 node-exporter-full.json
ubuntu@ip-10-0-10-102:~/project2/devopstools/parte3-cicd-monitorizacion/grafana/provisioning/dashboards/json$ cd
```
