"""
#1
import sqlite3


class Data_base():
    def __init__(self):
        
        self.con = sqlite3.connect("Students.db")
        self.kur = self.con.cursor()
        self.Create()
        
        #for i in range(int(input("nechta: "))):
            #self.insert_into(i + 1, input("Ismi: "), float(input("Stipendiyasi: ")), int(input("kursi: ")))
            #print("")
        
        self.sorov()
        self.con.close()
    
    def Create(self):
            
            self.kur.execute("CREATE TABLE IF NOT EXISTS talaba_hw_12_03 (id NUMERIC, ismi TEXT, step REAL, kurs NUMERIC)")
            self.con.commit()
    
    def insert_into(self, id, ismi, step, kurs):
        self.kur.execute("INSERT INTO talaba_hw_12_03 VALUES(?,?,?)", (id, ismi, step, kurs))
        self.con.commit()
    
    def sorov(self):
        self.kur.execute("SELECT step FROM talaba_hw_12_03 WHERE kurs = 2")
        lt = list(self.kur.fetchall())
        flt = float(0)
        print("\n===== 1 - SO'ROV =====\n")
        for i in range(len(lt)):
            flt += float(*lt[i])
        print(flt, "\n")
        self.kur.execute("SELECT * FROM talaba_hw_12_03 ORDER BY kurs DESC")
        lt = list(self.kur.fetchall())
        print("\n===== 2 - SO'ROV =====\n")
        for i in range(len(lt)):
            lt1 = list(lt[i])
            if len(lt1[1]) >= 5:
                print(*lt1)


ob = Data_base()            
"""


"""
#2

import sqlite3


class Data_base():
    def __init__(self):
        
        self.con = sqlite3.connect("Aeroport.db")
        self.kur = self.con.cursor()
        self.Create()
        
        #for i in range(int(input("nechta: "))):
            #self.insert_into(i + 1, input("Type: "), input("Date: "), input("Uchish shaxri: "), input("Qo'nish shaxri: "), input("Uchish vaqti: "))
            #print("")
        
        a = int(input("qaysi so'rovni tanlaysiz\n"))
        if a == 1:
            self.sorov1()
        elif a == 2:    
            self.sorov2()
        self.con.close()
    
    def Create(self):
            
            self.kur.execute("CREATE TABLE IF NOT EXISTS aeroport_hw_12_03 (id INTEGER, type TEXT, date TEXT, uchish_sh TEXT, qonish_sh TEXT, uchish_vaqti TEXT)")
            self.con.commit()
    
    def insert_into(self, id, type, date, uchish_sh, qonish_sh, uchish_vaqti):
        self.kur.execute("INSERT INTO aeroport_hw_12_03 VALUES(?, ?, ?, ?, ?, ?)", (id, type, date, uchish_sh, qonish_sh, uchish_vaqti))
        self.con.commit()
    
    def sorov1(self):
        self.kur.execute("SELECT * FROM aeroport_hw_12_03")
        lt = list(self.kur.fetchall())
        for i in range(len(lt)):
            lt1 = list(lt[i][2])
            if int(lt1[3]) == 0 and (int(lt1[4]) == 6 or int(lt1[4]) == 7 or int(lt1[4]) == 8):
                print(*lt[i])
    
    def sorov2(self):
        self.kur.execute("SELECT * FROM aeroport_hw_12_03")
        lt = list(self.kur.fetchall())
        for i in range(len(lt)):
            lt1 = list(lt[i][5])
            if lt1[0] == '0' and lt1[1] == '2' and str(lt[i][4]) == 'Toshkent':
                self.delete(int(lt[i][0]))
                
     
    def delete(self, id):
        self.kur.execute("DELETE FROM aeroport_hw_12_03 WHERE id = (?)", (id,))
        self.con.commit()
                
                
ob = Data_base()            
"""



