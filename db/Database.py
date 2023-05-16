#sudo apt install python3-pip
#pip3 install mysql-connector-python
import mysql.connector

class Database:
    def connect(self):
       self.conexion = mysql.connector.connect(host="localhost",user="root",password="123456",database="python")
       return self.conexion

        
        


