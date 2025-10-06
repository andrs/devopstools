

(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl -n devops-lab get ingress
NAME          CLASS    HOSTS       ADDRESS   PORTS   AGE
api-ingress   <none>   api.local             80      26s
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$ kubectl -n devops-lab get all
NAME                           READY   STATUS         RESTARTS   AGE
pod/api-647bc7b4cd-25mk7       0/1     Running        0          64s
pod/api-647bc7b4cd-v6v6x       0/1     Running        0          64s
pod/db-69c8cb6574-kvplz        0/1     Pending        0          4m32s
pod/db-init-zwhdr              1/1     Running        0          83s
pod/pgadmin-848dc56c6b-zbvsn   0/1     Running        0          54s
pod/rabbit-6d55ccbfcc-972cw    1/1     Running        0          4m27s
pod/redis-54c8b869c7-779nf     1/1     Running        0          2m54s
pod/worker-b76744d7d-qt5kp     0/1     ErrImagePull   0          59s

NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)              AGE
service/api       ClusterIP   172.20.76.133    <none>        80/TCP               64s
service/db        ClusterIP   172.20.229.2     <none>        5432/TCP             4m32s
service/pgadmin   NodePort    172.20.105.100   <none>        80:30081/TCP         54s
service/rabbit    ClusterIP   172.20.73.247    <none>        5672/TCP,15672/TCP   4m27s
service/redis     ClusterIP   172.20.65.66     <none>        6379/TCP             2m54s

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/api       0/2     2            0           64s
deployment.apps/db        0/1     1            0           4m32s
deployment.apps/pgadmin   0/1     1            0           54s
deployment.apps/rabbit    1/1     1            1           4m27s
deployment.apps/redis     1/1     1            1           2m54s
deployment.apps/worker    0/1     1            0           59s

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/api-647bc7b4cd       2         2         0       64s
replicaset.apps/db-69c8cb6574        1         1         0       4m32s
replicaset.apps/pgadmin-848dc56c6b   1         1         0       54s
replicaset.apps/rabbit-6d55ccbfcc    1         1         1       4m27s
replicaset.apps/redis-54c8b869c7     1         1         1       2m54s
replicaset.apps/worker-b76744d7d     1         1         0       59s

NAME                STATUS    COMPLETIONS   DURATION   AGE
job.batch/db-init   Running   0/1           83s        83s
(myenv) ubuntu@ip-10-0-10-102:~/project2/devopstools/samples/lab6-final$

