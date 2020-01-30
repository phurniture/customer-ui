from customer import customerList

cl = customerList()
d = {'fname':'first','lname':'last','email':'email@email.com','password':'password','subscribed':'1',}
cl.add(d)
print(cl.data)