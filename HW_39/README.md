# Homework 39

## 1. Прочитать 2-ю главу [Kubernetes in Action](https://github.com/tms-dos17-onl/_sandbox/blob/main/lecture44/kubernetes-in-action.pdf) и повторить приведенные там примеры

```text
Прочитал первую и вторую главу
Ниже прикрепил скрины примеров из книги
```

### 1 пример (Запуск контейнера с образом busybox)

![task1_1](screenshots/task1_1.png)

### 2 пример (создание приложения на NodeJS, написание Dockerfile для него и запуск в Docker)

[app.js приложения из второго примера](book-example/node-js-app/app.js)
[Dockerfile второго примера](book-example/node-js-app/Dockerfile)

![task1_2](screenshots/task1_2.png)

### 3 пример (создание кластера в GKE)

![task1_3](screenshots/task1_3.png)

![Alt text](screenshots/task1_4.png)

### 4 пример (деплой приложения в кластер GKE через cli)

![task1_5](screenshots/task1_5.png)

## 2. Познакомиться с Workload объектами Kubernetes (Pod, ReplicaSet, DaemonSet, Job, CronJob), а также их конфигурацией (Liveness Probe, Resources) путем запуска примеров из [lecture45](https://github.com/tms-dos17-onl/_sandbox/tree/main/lecture45)

### [1-pod.yaml](lecture-examples/1-pod.yaml)

![task2_1](screenshots/task2_1.png)

### [2-namespace.yaml](lecture-examples/2-namespace.yaml)

![task2_2](screenshots/task2_2.png)

### [3-replicaset.yaml](lecture-examples/3-replicaset.yaml)

![task2_3](screenshots/task2_3.png)

### [4-livenessprobe.yaml](lecture-examples/4-livenessprobe.yaml)

![task2_4](screenshots/task2_4.png)

### [5-resources.yaml](lecture-examples/5-resources.yaml)

![task2_5](screenshots/task2_5.png)

### [6-resourcequota.yaml](lecture-examples/6-resourcequota.yaml)

```text
Удалил квоту, чтобы не удалять поды постоянно, а то демонсет не стартовал из-за ограничений
У самого гугла квота на поды 1500 я заметил
```

![task2_6](screenshots/task2_6.png)

### [7-daemonset.yanl](lecture-examples/7-daemonset.yaml)

![task2_7](screenshots/task2_7.png)

### [8-job.yaml](lecture-examples/8-job.yaml)

![task2_8](screenshots/task2_8.png)

### [9-cronjob.yaml](lecture-examples/9-cronjob.yaml)

![task2_9](screenshots/task2_9.png)

### Ниже прикрепил скриншот всех подов и их статусы после запущенных примеров

![kubectlGetPods](screenshots/kubectlGetPods.png)
