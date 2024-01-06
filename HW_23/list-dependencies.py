import argparse
import requests
import json

def main():
    parser = argparse.ArgumentParser(description="Скрипт, генерирующий файл с зависимостями для указанного pip пакета")
    parser.add_argument("--package", required=True, help="Название pip пакета")
    args = parser.parse_args()
    
    package_name = args.package
    
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    
    data = json.loads(response.content)
    
    requirements = data["info"]["requires_dist"]
    
    with open(f"{package_name}.txt", "w") as file:
        for requirement in requirements:
            file.write(f"{requirement}\n")
    
    print(f"Файл с зависимостями создан под названием {package_name}.txt в рабочей директории скрипта")

if __name__ == "__main__":
    main()
