import csv
import DBManager2

class FileManager2:
    
    def __init__(self, dbm):
        self.dbm = dbm
        self.data = {}
        #self.col_names = []
        #self.rows = []

    def load_csv(self, fn):
        with open(fn) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            car_count = 0
            keys = []
            
            # global col_names
    
            for row in csv_reader:
                if line_count == 0:
                    
                    for i in range(len(row)):
                        keys.append(row[i].replace(' ', '_'))
            
                    # trow = []
                    # for cn in row:
                    #     trow.append(cn.lower().replace(' ', '_'))
                        
                    # self.dbm.col_names = trow
                
                    #print(trow[0], trow[1])
                    line_count += 1
            
                else:
            
                    car_id = row[0]
                    
                    if car_id.isnumeric():
                        
                        car = {}
                        
                        if (len(row) < len(keys)):
                            continue
                        
                        for i in range(len(row)):
                            try:
                                car[keys[i]] = row[i]
                            except (IndexError):
                                print("hit the except at line: ", line_count)
                                pass
                            
                        self.dbm.create(
                            car_id,
                            car['Make'],
                            car['Model'],
                            car['Year'],
                            car['Body_type'],
                            )
                         
                        #self.dbm.rows.append(row)
                
                        car_count += 1
                
                    #if line_count < 10:
                        #print(line_count, row[0], row[1])
                
                    line_count += 1
            
            
            print(f"loaded {car_count} cars from", fn)
    
    
    def save_csv(self, fn):
        length = len(self.dbm.rows)
        
        print("saved", length, "cars to", fn)
        
        with open(fn, 'w', newline='') as outfile:
            
            outfile.write('ID,Make,Model,Year,Body_type\n')
        
            writer = csv.writer(outfile)
        
            for row in self.dbm.rows:
                writer.writerow(row)
            
            pass


if __name__ =="__main__":
    dbm = DBManager2.DBManager2()
    fm = FileManager2(dbm)
    
    dbm.reset()
    
    fm.load_csv("cars.csv")
    
    #fm.save_csv("SAVETEST.csv")
    
    dbm.select("make", "BMW")
    dbm.select("body_type", "Convertible")
    
    fm.save_csv("Select_Save_Test.csv")
    
    dbm.print_selection()
    
    print("GOT TO THE END!!! YAY!!!")