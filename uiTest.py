from customer import customerList

info = ''
c = customerList()
info = input('enter your first name: ')
c.set('fname', info)

info = input('enter your last name: ')
c.set('lname', info)

info = input('enter your email: ')
c.set('email', info)

info = input('enter your password: ')
c.set('password', info)

info = input('enter your true if you are subscribed or false otherwise: ')
c.set('subscribed', info)

c.add()

print(c.data)

if c.verifyNew():
    c.insert()
    print(c.data)
else:
    print(c.errorlist)

print(c.data)

'''
for fn in c.fnl:
    var = input('enter ' + fn + '\n')
    c.set(fn,var)
c.add()
c.insert()
print(c.data)
'''