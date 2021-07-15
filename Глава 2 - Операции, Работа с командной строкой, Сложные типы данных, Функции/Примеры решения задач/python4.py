users = ['John', 'mIke', 'Mary', 'lian', 'kira']
print(users)

n_users = []

for n_user in users:
    n_users.append(n_user.lower())

print(n_users)

new_users = ['jJy', 'henry', 'jey', 'Kira', 'Mary']

n_new_users = []

for n_new_user in new_users:
    n_new_users.append(n_new_user.lower())

print(n_new_users)

for nnr in n_new_users:
    if nnr in n_users:
        print(nnr + ' you can not join us, incorrect name')
    else:
        print(nnr + ' the name is available')
