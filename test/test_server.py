import unittest
import socket

class TestServer(unittest.TestCase):
	def test_server(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("localhost", 3000))

if __name__ == '__main__':
    unittest.main()