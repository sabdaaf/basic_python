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

#<====range function===>
list(range(5, 10))
print(list(range(5,10)))

print(list(range(0, 10, 3)))# range 0<x<=10 dengan step 3, naik 3 tiap hitungan

a = ['saya','suka','bermain','free4talk']
for i in range(len(a)):
    print(a[i])

print('=======')
for i in range(5):
    print(i+1)

print('=======')
print(sum(range(6)))

print('=======')
f4t = ['halrvey','apple','powder','yukari','k','boo-la','cha-bi']
for i in range(len(f4t)):
    print(f4t[i])


  