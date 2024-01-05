# Homework 22

## 1. Реализовать конвертер между XML/JSON/YAML форматами, который считывает файл, переданный через аргумент ```--in-file``` или же из стандартного потока ввода, и его формат ```--in-format```, и выводит в стандартный поток вывода содержимое файла в формате, переданном через аргумент ```--out-format```

Для реализации скрипта рекомендуется использовать следующие пакеты/модули:

- [xmltodict](https://pypi.org/project/xmltodict/)
- [json](https://docs.python.org/3/library/json.html)
- [PyYAML](https://pypi.org/project/PyYAML/)

Описание аргументов командной строки скрипта:

```./converter.py --in-format {xml|json|yaml} [--in-file <IN_FILE>] --out-format {xml|json|yaml}```
