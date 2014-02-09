import copy

class Polynomial:
	def __init__(self, coefficients):
		self.coefficients = coefficients
		self.degree = len(coefficients)

	def __call__(self, x):
		result = 0.0
		for exponent in range(self.degree):
			   result += self.coefficients[exponent] * pow(x, exponent)
		return result

  	def __add__(self, other):
		   new_coefficients = Polynomial.sum_coefficients(self.coefficients, other.coefficients)
		   return Polynomial(new_coefficients)

	def __sub__(self, other):
		   negative_other = copy.copy(other.coefficients)
		   for index in range(len(negative_other)):
				 negative_other[index] = -1 * other.coefficients[index]
		   new_coefficients = Polynomial.sum_coefficients(self.coefficients, negative_other)
		   return Polynomial(new_coefficients)

	@staticmethod
	def sum_coefficients(a,b):
		if(len(a) < len(b)):
			c = copy.copy(b)
			for index in range(len(a)):
				c[index] += a[index]
			return c
		else:
			c = copy.copy(a)
			for index in range(len(b)):
				c[index] += b[index]
			return c
