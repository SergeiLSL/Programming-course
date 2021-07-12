"""
Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить
ее в список по символу ':'
"""
s = '/bin:/usr/bin:/usr/local/bin'

print(s.split(':'))  # ['/bin', '/usr/bin', '/usr/local/bin']
