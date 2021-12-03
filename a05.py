#comment this out before submitting to mimir
# file = open("CSV.txt", 'r')
# def input(prompt=''):
#     print(prompt, end='')
#     return file.readline().strip()

import DBManager2
import FileManager2

class CLI:
    
    def __init__(self, dbm, fm):
        
        self.dbm = dbm
        self.fm = fm
           

    def run_cli(self):
        #global cars
    
        while(1):
            inp = input()
            tokens = inp.split(" ")
            cmd = tokens[0]

            if cmd == "create":
                res = "bad"
                
                if len(tokens) == 6:
                    res = self.dbm.create(
                        tokens[1], tokens[2], tokens[3], 
                        tokens[4], tokens[5])
                    
                elif len(tokens) == 5:
                    res = self.dbm.create(
                        tokens[1], tokens[2], tokens[3], 
                        tokens[4])
                    
                elif len(tokens) < 5:
                    print("create: not enough parameters")
                    
                if res == "good":
                    print("created car with id", tokens[1])
        
            elif cmd == "update":
                self.dbm.update(tokens[1], tokens[2], tokens[3])
        
            elif cmd == "select_all":
                self.dbm.select_all()
            
            elif cmd == "select":
                if len(tokens) < 2:
                    print("select: not enough parameters")
                try:
                    result = self.dbm.select(tokens[1], tokens[2])
                    print(result[1])
                except IndexError:
                    #print("select: invalid attribute")
                    pass
                
            elif cmd == "select_by_id":
                try:
                    result = self.dbm.select_by_id(tokens[1])
                    print(result[1])
                except IndexError:
                    print("cannot select - missing or invalid parameter(s)")
            
            elif cmd == "print_selection":
                self.dbm.print_selection()
                
            elif cmd == "delete":
                self.dbm.delete_car(tokens[1])
        
            elif cmd == "exit":
                break
            
            elif cmd == "load_csv":
                self.fm.load_csv(tokens[1])
                
            elif cmd == "save_csv":
                self.fm.save_csv(tokens[1])
                
            elif cmd == "reset":
                self.dbm.reset()
            
            else:
                print("invalid command") 
        
        
def main():
    dbm = DBManager2.DBManager2()
    fm = FileManager2.FileManager2(dbm)
    
    cli = CLI(dbm, fm)
    cli.run_cli()
    
    
main()



