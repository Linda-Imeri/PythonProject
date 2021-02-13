import unittest

from my_project import find_ip
from my_project import find_mac

class Testing(unittest.TestCase):
    def test_ip(self):
        file= "C:/Users/LENOVO/Desktop/log1.pcap"
        result = find_ip(file)
        to_test = ['192.168.0.19','108.177.15.189', '52.149.21.60','64.233.184.188']
        self.assertEqual(result, to_test)

    def test_mac(self):
        file= "C:/Users/LENOVO/Desktop/log1.pcap"
        result = find_mac(file)
        to_test = ['08:95:2a:82:a2:bd','84:ef:18:e5:59:de']
        self.assertEqual(result, to_test)

    def test_ip_false(self):
        file= "C:/Users/LENOVO/Desktop/log1.pcap"
        result = find_ip(file)
        to_test = ['192.168.0.19','108.177.15.189', '52.149.21.60']
        self.assertNotEqual(result, to_test)

if __name__ == '__main__':
    unittest.main()