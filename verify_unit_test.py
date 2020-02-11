from customer import customerList

cl = customerList()
#d = {'fname':'first','lname':'last','email':'email@email.com','password':'password','subscribed':'1',}
#cl.add(d)
#print(cl.data)
'''
cl.set('fname','test')
cl.set('lname','test')
cl.set('email','test')
cl.set('password','test')
cl.set('subscribed','test')
cl.add()
cl.verifyNew()
print(cl.errorlist)
'''

cl.set('fname','a')
cl.set('lname','a')
cl.set('email','a@a.a')
cl.set('password','aaaa')
cl.set('subscribed','True')
cl.add()
cl.verifyNew()
print(cl.errorlist)
