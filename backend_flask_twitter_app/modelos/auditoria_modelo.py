from conexion_base_de_datos.conexion import conn

class AuditoriaModel:
    def __init__(self):        
        self.cursor = conn.cursor()

    def get_auditorias(self):
        self.cursor.execute("SELECT * from auditorias")  
        rv = self.cursor.fetchall()
        data = []
        content = {}
        for result in rv:
            content = {
                'auditoria_id': result[0], 
                'user_id': result[1], 
                'fecha': result[2],
                'tweet_id' : result[3],
                'accion' : result[4],
            }
            data.append(content)
            content = {}
        return data

if __name__ == "__main__":    
    am = AuditoriaModel()