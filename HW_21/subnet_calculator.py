import ipaddress
import argparse

def calculate_subnet(ip_address, cidr_mask):
    try:
        network = ipaddress.IPv4Network(f"{ip_address}/{cidr_mask}", strict=False)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    print(f"Адрес подсети: {network.network_address}")
    print(f"Маска подсети: {network.netmask}")
    print(f"IP первого хоста: {network.network_address + 1}")
    print(f"IP последнего хоста: {network.broadcast_address - 1}")
    print(f"Широковещательный адрес: {network.broadcast_address}")
    
    first_octet = int(network.network_address.exploded.split('.')[0])
    
    if 0 <= first_octet <= 127:
        print("Класс подсети: A")
    elif 128 <= first_octet <= 191:
        print("Класс подсети: B")
    elif 192 <= first_octet <= 223:
        print("Класс подсети: C")
    elif 224 <= first_octet <= 239:
        print("Класс подсети: D")
    elif 240 <= first_octet <= 255:
        print("Класс подсети: E")
    else:
        print("Класс подсети: Неизвестная")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Калькулятор подсетей")
    parser.add_argument("--ip", required=True, help="IP адрес в формате")
    parser.add_argument("--cidr-mask", required=True, help="Маска подсети в формате CIDR")

    args = parser.parse_args()

    calculate_subnet(args.ip, args.cidr_mask)
