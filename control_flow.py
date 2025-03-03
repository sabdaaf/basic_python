#<====if statement===>
x = int(input("masukkan angka: "))
if x < 0:
    print('dikit banget')
elif x == 0:
    print('0 banget ini?')
elif x > 0 :
    print('banyak juga yaa')

#<====for statement===>
#measure some string
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {'apple' : 'inactive', 'halrvey' : 'active', 'powder': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(users)

active_users = {}
for user, status in users.items():
    if status == 'active':
         active_users[user] = status
print(active_users)
         

  