import sqlite3

class DBManager2:
    
    def __init__(self): #constructor
        # self.data={}
        # self.selection={}
        self.conn = sqlite3.connect('example.db')
        
        self.__execute_query('''CREATE TABLE IF NOT EXISTS cars 
                             (id integer UNIQUE, make text, model text, 
                              year integer, body_type text)''')  
                             
                             
        query = "PRAGMA table_info(cars);"
        infos = self.__execute_query(query)
        self.col_names = [row[1] for row in infos]
        
        self.conditions = []
        self.rows = [] #rows is a list of tuples
        
    
    def create(self, ID, make, model, year, body=""):
        args = (ID, make, model, year, body)
        
        if (args[0].isnumeric()) == False: 
            print("create: invalid parameter(s)")
            return
        
        query = '''INSERT INTO cars (id, make, model, year, body_type)
            VALUES(?, ?, ?, ?, ?);'''
            
        try:
            self.__execute_query(query,tuple(args))
            return("good")
        except sqlite3.IntegrityError as e:
            print(str(e))
            return("bad")
        
    
    def clear_selection(self):
        self.conditions = []
        
    def __check_attr(self, attr):
        if attr in self.col_names:
            return True
        else:
            return False
    
    
    def select(self, attr, val):
        attr = attr.replace('-', '_')
        
        safe = self.__check_attr(attr)
        if not safe:
            return(0, "select: invalid attribute")
            return
        
        self.conditions = []
        self.conditions.append((attr, val))
        
        query = "SELECT * FROM cars WHERE "
        params = []
        
        for x in self.conditions:
            attr = x[0]
            val = x[1]
            
            query += attr + "=? AND "
            
            params += [val]
            
        query += "1"
        
        self.rows = self.__execute_query(query,(val,))
        
        return(1, 'selected ' + str(len(self.rows)) + ' cars with ' + 
                                                       attr + ' ' + val)
        
    def update(self, ID, attr, val):
        safe = self.__check_attr(attr)
        
        if not safe:
            print("update: invalid attribute")
            return
        
        
        #print("updating", ID, attr, val)
        
        query = '''UPDATE cars
            SET {} = ?
            WHERE id = ?'''.format(attr)
            
        self.__execute_query(query,(val, ID))
        
        print("updated {} {} {}".format(ID, attr, val))
           
        
    def delete_car(self, ID):
        
        isThere = self.select_by_id(ID)
        
        if isThere[0] == 1:
        
            query = '''DELETE FROM cars WHERE id = ?'''
        
            self.__execute_query(query,(ID,))
        
            print("deleted car {}".format(ID))
            
        else:
            
            print("delete: car {} not found".format(ID))
            
        pass
            
    
    def get_rows(self):
        return self.rows
    
    def get_col_names(self):
        return self.col_names
            
            
    def print_selection(self):
        
        if self.rows:
            print("selection:")
        else:
            print("print_selection: no selection to print")
            return
        
        for row in self.rows:
            print('\t', row[0])
            
            for i in range(len(row)):
                print('\t\t' +  str(self.col_names[i]) + ':' + str(row[i]))
                
    def get_selection_str(self):
        ret = ""
        
        if not self.rows:
            print("print_selection: no selection to print")
        
        ret = "selection:\n"
        
        for row in self.rows:
            ret += "\t{}\n".format(row[0])
            for i in range(len(row)):
                ret += "\t\t{}:{}\n".format(self.col_names[i], row[i])
                
        print(ret.strip())
            
            
    def select_all(self):
        query = '''SELECT * from cars'''
        
        self.rows = self.__execute_query(query)
        
        print("selected all {} cars".format(len(self.rows)))
        
        
    def select_by_id(self, ID):
        query = '''SELECT * from cars WHERE id = ?'''
        
        params = (ID,)
        
        self.rows = self.__execute_query(query, params)
        
        if not self.rows:
            return(0, "select: car {} not found".format(ID))
            
        else:
            return(1, "selected car {}".format(ID))
            
            
    def reset(self):
        print("reset database")
        self.__execute_query("DROP TABLE IF EXISTS cars")
        self.__init__()
    
    def __del__(self):
        self.conn.close()
        
    
    def __execute_query(self, query, params = None):
        cursor = self.conn.cursor()
        
        if not params:
            cursor.execute(query)
        else:
            cursor.execute(query, params)
            
        rows = cursor.fetchall()
        
        self.conn.commit()
        
        return rows
    
    # def my_filter(self, data, attr, val):
    #     ret = {}
        
    #     for car_id in data:
    #         car = data[car_id]
            
    #         for car_attr in car:
    #             car_val = car[car_attr]
                
    #             if attr == car_attr and val in car_val:
    #                 ret[car_id] = car
                    
    #     return ret
    
    
        
        
        
        