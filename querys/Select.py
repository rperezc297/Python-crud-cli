from db import Database
class Select(Database):
    def Select(self):
      cursor = self.connect().cursor()
      cursor.execute("SELECT id,name FROM users")
      resultados = cursor.fetchall()
      return resultados


    def Close(db,self):
       self.connect().close()
