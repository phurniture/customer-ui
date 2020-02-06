class customerList:
    def __init__(self):
        self.data = []
        self.tempdata = {}
        self.tn = 'customers'
        self.fnl = ['fname','lname','email','password','subscribed']
    
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

        cols = '","'.join(self.fnl)
        cols = '"' + cols + '"'
        vals = ('%s,' * len(self.fnl))[:-1]
        tokens = []
        for feildname in self.fnl:
            tokens.append(self.data[n][feildname])

        sql = 'INSERT INTO `' + self.tn + '` ('+ cols + ') VALUES (' + vals + ')'
        print(sql)
        print(tokens)