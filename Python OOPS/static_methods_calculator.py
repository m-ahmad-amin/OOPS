class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

print(Calculator.add(1, 2))
print(Calculator().add(1, 2))