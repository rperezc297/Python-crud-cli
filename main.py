import querys

##Funciones
def insert(name):
    ##Insert
    insert = querys.Insert()
    insert.Insert(name)

def select():    
    ##Select
    select = querys.Select()
    result = select.Select()
    for name in result:
        print(name)

def update(name,id):
    update = querys.Update()
    update.Update(name,id)        

def delete(id):
    delete = querys.Delete()
    delete.Delete(id)

value="y"
while value=="y":
       mensaje = '''
                   1.-Insertar usuario.
                   2.-Consultar usuarios.
                   3.-Actualizar usuarios.
                   4.-Borrar usuarios.  
                 '''
       print(mensaje)
       opcion = int(input("Ingrese una opcion: "))
       
       if opcion==1:
           name = input("Ingrese un nombre: ")
           insert(name)
       
       elif opcion==2:
           select()

       elif opcion==3:
           select()
           id = input("Ingrese el 'id' del usuario a modificar: ") 
           name = input("Nuevo nombre del usuario: ")
           update(name,id)

       elif opcion==4:
           select()
           id = input("Ingrese 'id' del usuario: ")
           delete(id)              
       
       else:
           print("Opcion no valida")
       
       value = input("Desea realizar otro procedimiento (y/n)")
       

# ##Delete
# delete = querys.Delete()
# delete.Delete(db)
