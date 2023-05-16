from db import Database
class Delete(Database):
    def Delete(self,id):
      connec = self.connect()
      cursor = connec.cursor()
      sql = "DELETE FROM users WHERE `users`.`id` = %s"
      value = (id,)
      cursor.execute(sql,value)
      connec.commit()

      cursor.close()
      connec.close()

