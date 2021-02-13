import unittest

from regex_app import find_ip
from regex_app import find_mac

class Testing(unittest.TestCase):
    def test_ip(self):
        file= "log1.pcap"
        result = find_ip(file)
        to_test = ['192.168.20.70','74.125.131.27']
        self.assertEqual(result, to_test)

    def test_mac(self):
        file= "log1.pcap"
        result = find_mac(file)
        to_test = ['00:1f:29:5e:4d:26','00:50:56:bb:3a:a0']
        self.assertEqual(result, to_test)

    def test_ip_false(self):
        file= "log1.pcap"
        result = find_ip(file)
        to_test = ['192.168.20.19','108.177.15.189', '52.149.21.60']
        self.assertNotEqual(result, to_test)

if __name__ == '__main__':
    unittest.main()