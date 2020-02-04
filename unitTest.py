from customer import customerList

cl = customerList()
#d = {'fname':'first','lname':'last','email':'email@email.com','password':'password','subscribed':'1',}
#cl.add(d)
#print(cl.data)
cl.set('fname','first')
cl.set('lname','last')
cl.set('lastname','last')
cl.set('email','address@email.com')
cl.add()
cl.add()
#print(cl.data)

print(cl.data)
print(cl.data[0])
cl.update(0,'email','gov@email.gov')
cl.update(0,'e_mail','gov@email.gov')
print(cl.data)
