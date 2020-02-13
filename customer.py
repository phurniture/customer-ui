import pymysql

class customerList:
    def __init__(self):
        self.data = []
        self.tempdata = {}
        self.tn = 'grinnecw_customers'
        self.fnl = ['fname','lname','email','password','subscribed']
        self.pk = 'id'
        self.errorlist = []
        self.conn = None
 
    def connect(self):
        import config
        self.conn = pymysql.connect(host=config.DB['host'], port=config.DB['port'], user=config.DB['user'], passwd=config.DB['passwd'], db=config.DB['db'], autocommit=True)

   
    def add(self):
        self.data.append(self.tempdata)

    def set(self, fn, val):
        if fn in self.fnl:
            self.tempdata[fn] = val
        else:
            print('invalid feild: ' + str(fn))
    
    def update(self,n,fn,val):
        if len(self.data) >= (n+1) and fn in self.fnl:
            self.data[n][fn] = val
        else:
            print('could not set value at row ' + str(n) + ' col ' + str(fn))
    def insert(self,n=0):

        cols = '`,`'.join(self.fnl)
        cols = '`' + cols + '`'
        vals = ('%s,' * len(self.fnl))[:-1]
        tokens = []
        for feildname in self.fnl:
            tokens.append(self.data[n][feildname])
        sql = 'INSERT INTO `' + self.tn + '` ('+ cols + ') VALUES (' + vals + ')'
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        print(sql)
        print(tokens)
        cur.execute(sql,tokens)
        self.data[n][self.pk] = cur.lastrowid

    def delete(self,n=0):
        item = self.data.pop(n)
        self.deleteByID(item[self.pk])

    def deleteByID(self, id):
        sql = 'DELETE FROM `' + self.tn + '` WHERE `' + self.pk + '` = %s;'
        tokens = (id)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql,tokens)


    def verifyNew(self,n=0):
        import re
        if len(self.data[n]['fname']) == 0:
            self.errorlist.append("First name cannont be blank")
       
        if len(self.data[n]['lname']) == 0:
            self.errorlist.append("Last name cannont be blank")
       
        if len(self.data[n]['email']) == 0:
            self.errorlist.append("Email cannont be blank")

        elif re.match('[^@]+@[^@]+\.[^@]+',self.data[n]['email']):
            pass
        else:
            self.errorlist.append("Email address invalid, check for @ and TLD (i.e. .com, .edu, .gov, etc.")

       
        if len(self.data[n]['password']) == 0:
            self.errorlist.append("Password cannont be blank")
        elif len(self.data[n]['password']) < 4:
            self.errorlist.append("Password must be longer than 4 characters")
       
        if len(self.data[n]['subscribed']) == 0:
            self.errorlist.append("Subscription cannont be blank")
        elif self.data[n]['subscribed'] != 'True':
            if self.data[n]['subscribed'] != 'False':
                self.errorlist.append("Subscription must be True or False")

        
        #Add error and validation checking
        #dont forget to call the function to test it
        
        if len(self.errorlist) > 0:
            return False
        else:
            return True
