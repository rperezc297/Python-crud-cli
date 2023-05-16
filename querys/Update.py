from db import Database
class Update(Database):
    
    def Update(self,name,id):
      cone = self.connect()
      cursor = cone.cursor()
      sql = ("update users set name=%s where id=%s")
      value = (name,id,)
      cursor.execute(sql,value)
      cone.commit()

      cursor.close()
      cone.close()

      

