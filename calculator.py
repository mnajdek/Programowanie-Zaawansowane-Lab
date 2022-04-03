import numpy as np

class Calculator:
    def _change_list_to_np_array(self, a):
        if isinstance(a, list):
            return np.array(a)
        return a

    def add(self, a, b):
        a = self._change_list_to_np_array(a)
        b = self._change_list_to_np_array(b)
        return a + b

    def substract(self, a, b):
        a = self._change_list_to_np_array(a)
        b = self._change_list_to_np_array(b)
        return a - b

    def multiply(self, a, b):
        a = self._change_list_to_np_array(a)
        b = self._change_list_to_np_array(b)
        return a * b

    def divide(self, a, b):
        a = self._change_list_to_np_array(a)
        b = self._change_list_to_np_array(b)
        return a / b

    def sqrt(self, a):
        a = self._change_list_to_np_array(a)
        return np.sqrt(a)

    def log(self, a):
        a = self._change_list_to_np_array(a)
        return np.log(a)

c = Calculator()
a=9
b=3
print(c.add(a,b))
print(c.substract(a,b))
print(c.multiply(a,b))
print(c.divide(a,b))
print(c.sqrt(a))
print(c.log(a))
