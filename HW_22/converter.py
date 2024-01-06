import argparse
import sys
import json
import xmltodict
import yaml

def main():
    parser = argparse.ArgumentParser(description="Конвертер между форматами XML/JSON/YAML")
    parser.add_argument("--in-format", required=True, help="Формат входного файла")
    parser.add_argument("--in-file", help="Входной файл (если имеется)")
    parser.add_argument("--out-format", required=True, help="Формат выходного файла")
    args = parser.parse_args()
    
    in_format = args.in_format
    in_file = args.in_file
    out_format = args.out_format
    
    if in_file is None:
        data = sys.stdin.read()
    else:
        with open(in_file) as f:
            data = f.read()
    
    if in_format == "xml":
        data = xmltodict.parse(data)
    elif in_format == "json":
        data = json.loads(data)
    elif in_format == "yaml":
        data = yaml.safe_load(data)
    
    if out_format == "xml":
        print(xmltodict.unparse(data))
    elif out_format == "json":
        print(json.dumps(data))
    elif out_format == "yaml":
        print(yaml.safe_dump(data))

if __name__ == "__main__":
    main()
