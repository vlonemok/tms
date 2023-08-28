# Homework 12

## 1. Установить на VM Apache веб-сервер и настроить его на работу с PHP (например, как указано в [инструкции](https://ubuntu.com/server/docs/programming-php)). Поменять порт по умолчанию на 8080. Убедиться, что Apache работает и возвращает страницу с информацией о PHP

```bash
sudo apt update && sudo apt upgrade # Обновляем пакеты
sudo apt install apache2            # Установка Apache сервера
sudo nano /etc/apache2/ports.conf   # Здесь необходимо установить по умолчанию порт Listen 8080
sudo systemctl restart apache2      # Перезапускаем сервис apache2, чтобы применить изменения на сервере
apt install php libapache2-mod-php  # С помощью этого пакета мы подружим Apache и PHP
sudo nano /var/www/html/phpinfo.php # Здесь необходимо написать код для запуска страницы phpinfo
```

После запуска всех команд выше мы можем пройти на ```localhost:8080/phpinfo.php``` и увидеть нашу страницу

![task1](screenshots/task1.png)

## 2. Установить на VM Nginx

```bash
sudo apt install nginx      # Установка nginx
sudo systemctl status nginx # Просмотр статуса сервиса nginx
sudo systemctl start nginx  # Необходимая команда, если сервис nginx не стартанул автоматически
```

![task2](screenshots/task2.png)

![task2_1](screenshots/task2_1.png)

## 3. Скопировать на VM папку <https://github.com/tms-dos17-onl/_sandbox/tree/main/lecture15/react_nginx/build> и настроить Nginx на хостинг этого веб-приложения. Проверить работоспособность приложения путем посещения всех доступных ссылок на главной странице и обновления каждой из страниц в веб-браузере

**Скопированное приложение по пути ```/var/www/homeWork12/html```**

![task3](screenshots/task3.png)

**Создание конфига для сервера**

![task3_0](screenshots/task3_0.png)

**Проверка всех ссылок на работоспособность**

![task3_1](screenshots/task3_1.png)

![task3_2](screenshots/task3_2.png)

![task3_3](screenshots/task3_3.png)

## 4. Скопировать на VM папку <https://github.com/tms-dos17-onl/_sandbox/tree/main/lecture15/api> и запустить Python REST Api приложение согласно инструкции. Проверить работоспособность всех доступных REST Api методов с помощью Swagger

```bash
cd ~/lecture15/api              # Перейти в папку с приложением
pip install -r requirements.txt # Установка пакетов через pip
python3 main.py                 # Запуск приложения с дефолтным портом 5000
```

![task4](screenshots/task4.png)

![task4_1](screenshots/task4_1.png)

![task4_2](screenshots/task4_2.png)

![task4_3](screenshots/task4_3.png)

![task4_4](screenshots/task4_4.png)

![task4_5](screenshots/task4_5.png)

**Так же можно увидеть в логах самого приложения, что все методы отработали и вернули 200 код**

![task4_6](screenshots/task4_6.png)

## 5. Настроить Nginx как Reverse Proxy для Python REST Api приложения из предыдущего пункта. А затем

- Открыть Swagger для веб-приложения через Nginx (http://<NGINX_IP>:<NGINX_PORT>/apidocs).
- Проверить работоспособность всех доступных REST Api методов через Nginx с помощью Swagger. При необходимости поправить конфигурацию Nginx сервера, чтобы все методы работали.
- Для тестирования метода /uploadFile использовать файл размером больше 1MB.
**Использовал PDF файл размером 1.5mb**

![task5_2](screenshots/task5_2.png)
- Вывести в консоль содержимое файла конфигурации Nginx с измененными значениями и комментариями

**Настроенная конфигурация nginx**

![task5](screenshots/task5.png)

**Все методы работают**

![task5_1](screenshots/task5_1.png)
