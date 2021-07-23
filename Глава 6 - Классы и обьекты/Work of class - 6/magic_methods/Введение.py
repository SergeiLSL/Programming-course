class Test:
    def __add__(self, other):
        return '0_0'


t = Test()
print(t + 2)  # 0_0
# ================================================


class BadStr(str):
    def __add__(self, other):
        return str(self) + str(other)


t = BadStr('some')
print(t + 2)  # some2

# ================================================


class BadStr(str):
    def __add__(self, other):
        return BadStr(str(self) + str(other))


t = BadStr('some')
print(t + 2 + 2)  # some22

# ================================================


class MathObject:  # создает математический объект
    def __init__(self, value):
        self.value = 2

    def __add__(self, other):
        return self.value + other


t = MathObject(0)
print(t + 4)  # 6