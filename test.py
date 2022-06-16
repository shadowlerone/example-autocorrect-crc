from lib2to3.pgen2.tokenize import untokenize
import unittest
import sbh2
import sbh3

class Test_sbh3(unittest.TestCase):
	def test_case1(self):
		self.assertEqual(sbh3.solve("(1+2ε)+(5-3ε)-(-2-8ε)"), "8+7ε")

	def test_case2(self):
		self.assertEqual(sbh3.solve("(7-7ε)*(1+2ε)*(3-5ε)"), "21-14ε")
	
	def test_case3(self):
		self.assertEqual(sbh3.solve("(1+2ε)*(1-2ε)-(1+2ε)*(1-2ε)"), "-2ε")

class Test_sbh2(unittest.TestCase):
	def test_case1(self):
		self.assertEqual(sbh2.solve("x^4 + 20x^3 - 87x^2 - 806x + 3080"), "(x+22)(x+7)(x-4)(x-5)")
	def test_case2(self):
		self.assertEqual(sbh2.solve("x^2 - 169"), "(x+13)(x-13)")
	def test_case3(self):
		self.assertEqual(sbh2.solve("x^3 - 46x^2 + 553x - 1740"), "(x-5)(x-12)(x-29)")

if __name__ == "__main__":
	unittest.main(verbosity=2)
