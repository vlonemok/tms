import ipaddress
import unittest
from subnet_calculator import calculate_subnet

class TestCalculateSubnet(unittest.TestCase):
    
    def test_calculate_subnet_1(self):
        ip_address = "192.168.0.1"
        cidr_mask = "24"
        
        network = ipaddress.IPv4Network(f"{ip_address}/{cidr_mask}", strict=False)
        
        self.assertEqual(str(network.network_address), "192.168.0.0")
        self.assertEqual(str(network.netmask), "255.255.255.0")
        self.assertEqual(str(network.network_address + 1), "192.168.0.1")
        self.assertEqual(str(network.broadcast_address - 1), "192.168.0.254")
        self.assertEqual(str(network.broadcast_address), "192.168.0.255")
        
        first_octet = int(network.network_address.exploded.split('.')[0])
        self.assertEqual(first_octet, 192)
        
    def test_calculate_subnet_2(self):
        ip_address = "10.0.0.1"
        cidr_mask = "24"

        network = ipaddress.IPv4Network(f"{ip_address}/{cidr_mask}", strict=False)

        self.assertEqual(str(network.network_address), "10.0.0.0")
        self.assertEqual(str(network.netmask), "255.255.255.0")
        self.assertEqual(str(network.network_address + 1), "10.0.0.1")
        self.assertEqual(str(network.broadcast_address - 1), "10.0.0.254")
        self.assertEqual(str(network.broadcast_address), "10.0.0.255")

        first_octet = int(network.network_address.exploded.split('.')[0])

        self.assertEqual(first_octet, 10)