from db import Database
class Insert(Database):
    
    def Insert(self,name):
      cone = self.connect()
      cursor = cone.cursor()
      sql = ("INSERT INTO users (id, name) VALUES (%s,%s)")
      value = (None,name)
      cursor.execute(sql,value)
      cone.commit()

      cursor.close()
      cone.close()

      

