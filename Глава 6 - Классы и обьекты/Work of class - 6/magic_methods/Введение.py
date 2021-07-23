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
