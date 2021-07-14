"""
task_2.5 - разбить строку в список по символу

Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить
ее в список по символу ':'
"""

s = '/bin:/usr/bin:/usr/local/bin'

print(s.split(':'))  # ['/bin', '/usr/bin', '/usr/local/bin']
