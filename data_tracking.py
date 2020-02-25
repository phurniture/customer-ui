from customer import customerList

c = customerList()
c.set('fname','furst')
c.set('lname','lasy')
c.set('email','adres@email.com')
c.set('password','aaa234')
c.set('subscribed','True')
c.add()

##

c.insert()

##

c.data[0]['lname'] = 'newname'
c.insert()
print(c.data)