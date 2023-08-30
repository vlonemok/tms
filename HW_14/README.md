# Homework 14

## 1. Сгенерировать пару ключей/сертификатов (```private.pem``` и ```public.pem```) при помощи ```OpenSSL```

```bash
sudo apt update && sudo apt upgrade
openssl genpkey -algorithm RSA -out private.pem
openssl rsa -in private.pem -pubout -out public.pem
```

С помощью команд выше ключи мы сгенерировали ```private.pem``` и ```public.pem``` ключи

![task1](screenshots/task1.png)

## 2. Создать скрипт ```encrypt.sh```, который считывает стандартный поток ввода, шифрует его при помощи ```public.pem``` через ```OpenSSL``` и выводит в стандартный поток вывода

Код [скрипта](encrypt.sh):

![task2](screenshots/task2.png)

## 3. Создать скрипт ```decrypt.sh```, который считывает стандартный поток ввода, расшифровывает его при помощи ```private.pem``` через ```OpenSSL``` и выводит в стандартный поток вывода

Код [скрипта](decrypt.sh):

![task3](screenshots/task3.png)

## 4. Сгенерировать публичный сертификат ```public-nginx.pem``` для ```private.pem``` через ```OpenSSL```, используя ```<LASTNAME>.io``` в качестве Common Name (CN)

## 5. Настроить Nginx на работу по HTTPS, используя сертификаты из предыдущего задания. Например, чтобы Nginx возвращал домашнюю страницу по HTTPS

## 6. Настроить доверие публичному сертификату в браузере и проверить это

## 7. А теперь открыть домашнюю страницу Nginx по HTTPS через ```curl``` не прибегая к опции ```-k```
