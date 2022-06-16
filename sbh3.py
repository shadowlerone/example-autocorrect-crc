import re
class Term:
	def __init__(self, i=0, d=0) -> None:
		self.int = int(i)
		self.dual = int(d)
		self.negative = False
	def from_string(t):
		if t.startswith("-"):
			if len(t[1:].split("-")) > 1:
				tt= t[1:].split("-")
				i = -1 * int(tt[0])
				d = -1 * int(tt[1][:-1])
			else:
				tt = t[1:].split("+")
				i = -1 * int(tt[0])
				d = int(tt[1][:-1])
		else:
			if len(t.split("-")) > 1:
				tt= t.split("-")
				i = int(tt[0])
				d = -1 * int(tt[1][:-1])
			else:
				tt = t.split("+")
				i = int(tt[0])
				d = int(tt[1][:-1])

		return Term(i, d)
	def __add__(self, other):
		i = self.int + other.int
		d = self.dual + other.dual
		return Term(i, d)
	def __sub__(self, other):
		i = self.int - other.int
		d = self.dual - other.dual
		return Term(i, d)
	def __mul__(self, other):
		i = self.int * other.int
		d = self.dual* other.int + self.int * other.dual
		return Term(i, d)
	def __str__(self):
		if self.int == 0:
			return f"{self.dual}ε"
		else:
			mod = '+' if self.dual > 0 else ""
			return f"{self.int}{mod}{self.dual}ε"

def solve(operation):
	terms = operation.split(")")
	# terms = [t if t.startswith("+") or t.startswith("(") else t.replace("-","+") for t in terms ]
	terms = [c.split("(") for c in operation.split(")")]
	out = Term.from_string(terms[0][1])
	for idx, t in enumerate(terms):
		# print(t[0])
		try:
			if t[0] == "":
				pass
			elif t[0] == "+":
				out = out + Term.from_string(t[1])
			elif t[0] == "-":
				out = out - Term.from_string(t[1])
			elif t[0] == "*":
				out = out * Term.from_string(t[1])
		except IndexError:
			pass
	return str(out)

if __name__ == "__main__":
	[print(solve(c)) for c in [input() for _ in range(int(input()))]]