#<====if statement===>
x = int(input("masukkan angka: "))
if x < 0:
    print('dikit banget')
elif x == 0:
    print('0 banget ini?')
elif x > 0 :
    print('banyak juga yaa')

print("/n")
#<====for statement===>
#measure some string
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
print("/n")

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
print("/n")

#<====range function===>
list(range(5, 10))
print(list(range(5,10)))
print(list(range(0, 10, 3)))# range 0<x<=10 dengan step 3, naik 3 tiap hitungan
print("/n")

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


#<====basic looping===>
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
print('===hayoo apa bedanya===')
    
for i in range(1,5):
    for j in range(1,5):
        print(j,i)
print('======')
 
for i in range(1,5): #1,2,3,4
    for j in range(1,i): #1,2,3 karena i = 4 
        print(i,j)
print('======')

#<====break and continue statement===>   
#wahh ini gimana njirr
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

  