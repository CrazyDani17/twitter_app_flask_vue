from conexion_base_de_datos.conexion import conn

class UserModel:
    def __init__(self):        
        self.cursor = conn.cursor()

    def user_login(self, user_name, password):
        params = {
            'user_name' : user_name,
            'password' : password
        }
        query = """SELECT user_id from users where user_name = %(user_name)s and password = %(password)s"""
        self.cursor.execute(query, params)
        user_id = self.cursor.fetchone()
        if user_id:
            data = {
                'user_id': user_id[0],
                'estado' : "True",
            }
        else:
            data = {
                'user_id': None,
                'estado' : "False",
            }
        return data

    def get_user(self, id):
        params = {'id' : id}    
        self.cursor.execute("SELECT * from users where user_id=%(id)s", params)                
        rv = self.cursor.fetchall()
        data = []
        content = {}
        for result in rv:
            content = {
                'user_id': result[5], 
                'user_name': result[0], 
                'password': result[1],
                'nombre_completo' : result[2],
                'email' : result[3],
                'tipo_de_usuario' : result[4],
            }
            data.append(content)
            content = {}
        return data

    def get_users(self):
        self.cursor.execute("SELECT * from users")  
        rv = self.cursor.fetchall()
        data = []
        content = {}
        for result in rv:
            content = {
                'user_id': result[5], 
                'user_name': result[0],
                'password': result[1],
                'nombre_completo' : result[2],
                'email' : result[3],
                'tipo_de_usuario' : result[4],
            }
            data.append(content)
            content = {}
        return data

    def create_user(self, user_name, password, nombre_completo, email, tipo_de_usuario):
        params = {
            'user_name' : user_name,
            'password' : password,
            'nombre_completo' : nombre_completo,
            'email' : email,
            'tipo_de_usuario' : tipo_de_usuario
        }
        query = """insert into users (user_name, password, nombre_completo, email, tipo_de_usuario) 
         values (%(user_name)s, %(password)s, %(nombre_completo)s, %(email)s, %(tipo_de_usuario)s) RETURNING user_id"""    
        cursor = self.cursor.execute(query, params)
        id_of_new_row = self.cursor.fetchone()[0]
        conn.commit()  

        data = {
            'user_id': id_of_new_row,
            'user_name': params['user_name'],
            'password': params['password'],
            'nombre_completo': params['nombre_completo'],
            'email': params['email'],
            'tipo_de_usuario': params['tipo_de_usuario']
        }
        return data

    def delete_user(self, id):
        params = {'id' : id}      
        query = """delete from users where user_id = %(id)s RETURNING user_id"""    
        self.cursor.execute(query, params)
        conn.commit()

        user_id = self.cursor.fetchone()
        if user_id:
            data = {
                'user_id': user_id[0],
                'eliminado' : "True",
            }
        else:
            data = {
                'user_id': id,
                'eliminado' : "False",
            }
        return data

    def update_user(self, id, user_name, password, nombre_completo, email, tipo_de_usuario):
        params = {
            'user_id' : id,
            'user_name' : user_name,
            'password' : password,
            'nombre_completo' : nombre_completo,
            'email' : email,
            'tipo_de_usuario' : tipo_de_usuario
        }
        query = """UPDATE users SET user_name = %(user_name)s, password = %(password)s, nombre_completo = %(nombre_completo)s, email = %(email)s, tipo_de_usuario = %(tipo_de_usuario)s WHERE user_id = %(user_id)s"""    
        cursor = self.cursor.execute(query, params)
        conn.commit()   

        data = {
            'user_id': id,
            'user_name': params['user_name'],
            'password': params['password'],
            'nombre_completo': params['nombre_completo'],
            'email': params['email'],
            'tipo_de_usuario': params['tipo_de_usuario']
        }
        return data

if __name__ == "__main__":    
    um = UserModel()