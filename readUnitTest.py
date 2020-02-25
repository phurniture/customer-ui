from customer import customerList
import time
'''
cl = customerList()
cl.getById(3)
print(cl.data)
'''

'''
cl = customerList()
cl.getAll('fname')
print(cl.data)
'''


cl = customerList()
cl.getById(3)
print(cl.data)
cl.data[0]['fname'] = 'FiRsTnAmE'
cl.update()
