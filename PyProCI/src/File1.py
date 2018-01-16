import unittest

class Trav(unittest.TestCase):
	def setUp(self):
		print ('inside set up file')
		
	def setUp_2(self):
		print ('inside set up 2 file')
		
	def setUp_3(self):
		print ('inside set up 3 file')
		
if __name__=="__main__":
	unittest.main()