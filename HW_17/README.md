# Homework 17

## Реализовать Ansible playbook, который

### 1. Устанавливает LAMP стэк на VM при помощи ролей

- [Apache](https://galaxy.ansible.com/ui/standalone/roles/geerlingguy/apache/)
- [MySQL](https://galaxy.ansible.com/ui/standalone/roles/geerlingguy/mysql/)
- [PHP](https://galaxy.ansible.com/ui/standalone/roles/geerlingguy/php/)

```bash
ansible-galaxy install geerlingguy.apache geerlingguy.mysql geerlingguy.php geerlingguy.memcached
ansible-galaxy list
```

![task1](screenshots/task1.png)

### 2. (**) Устанавливает memcached сервис на VM при помощи [роли](https://galaxy.ansible.com/ui/standalone/roles/geerlingguy/memcached/)

### 3. Перенести логику по установке приложения [https://github.com/qyjohn/simple-lamp](simple-lamp) в Ansible роль

```bash
ansible-playbook -i hosts -K simple-lamp-roles.yml
```

![task3_1](screenshots/task3_1.png)

![task3_2](screenshots/task3_2.png)

![task3](screenshots/task3.png)

### 4. Создать Pull Request (PR) содержащий Ansible playbook и разработанную роль/роли
