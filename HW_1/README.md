# Homework 1

## Развернуть две виртуальные машины (Ubuntu, CentOS)

![](screenshots/ubuntuInstall.png)
![](screenshots/centosInstall.png)

### 1. Произвести минимальную настройку (время, локаль, custom motd)

Для установки временной зоны на обеих виртаульных машинах используется команда:

```bash
tzselect
```

Для изменения локализации на английскую используем команды:

Ubuntu

```bash
sudo update-locale LANG=en_US.UTF-8
```

CentOS

```bash
sudo dnf install glibc-langpack-en
localectl set-locale LANG=en_us.utf8
```

Для изменения MOTD мы должны создать или изменить существующий файл ```/etc/motd``` на желаемый нами:

CentOS:

![](screenshots/centosMOTD.png)

Ubuntu:

![](screenshots/ubuntuMOTD.png)

### 2. Определить точную версию ядра

Для определения точной версии ядра используются следующая команда:

Ubuntu и CentOS

```bash
uname -r
```

### 3. Вывести список модулей ядра и записать в файл

Ubuntu и CentOS

```bash
lsmod > kernel_modules.txt
cat kernel_modules.txt
```

1 команда - запись всех модулей ядра в файл. 2 команда - проверка того, что мы записали в файл

### 4. Просмотреть информацию о процессоре и модулях оперативной памяти

