from backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

################### Actividad ################################
    def get_actividad(self, ID_Actividad):    
        params = {'ID_Actividad' : ID_Actividad}      
        rv = self.mysql_pool.execute("SELECT * from actividad where ID_Actividad=%(ID_Actividad)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'ID_Actividad': result[0], 'nombre': result[1], 'descripcion': result[2], 'fechaInicio': result[3], 'fechaFin': result[4], 'enlaceReunion': result[5], 'isProtocolar': result[6], 'isPonencia': result[7], 'isPanel': result[8], 'isConcurso': result[9], 'bases': result[10]}
            data.append(content)
            content = {}
        return data

    def get_actividads(self):  
        rv = self.mysql_pool.execute("SELECT * from actividad")  
        data = []
        content = {}
        for result in rv:
            content = {'ID_Actividad': result[0], 'nombre': result[1], 'descripcion': result[2], 'fechaInicio': result[3], 'fechaFin': result[4], 'enlaceReunion': result[5], 'isProtocolar': result[6], 'isPonencia': result[7], 'isPanel': result[8], 'isConcurso': result[9], 'bases': result[10]}
            data.append(content)
            content = {}
        return data

    def add_actividad(self, nombre, descripcion, fechaInicio, fechaFin, enlaceReunion, isProtocolar, isPonencia, isPanel, isConcurso, bases):
        params = {
            'nombre' : nombre,
            'descripcion' : descripcion,
            'fechaInicio' : fechaInicio,
            'fechaFin' : fechaFin,
            'enlaceReunion' : enlaceReunion,
            'isProtocolar' : isProtocolar,
            'isPonencia' : isPonencia,
            'isPanel' : isPanel,
            'isConcurso' : isConcurso,
            'bases' : bases
        }  
        query = """insert into actividad (nombre, descripcion, fechaInicio, fechaFin, enlaceReunion, isProtocolar, isPonencia, isPanel, isConcurso, bases)
            values (%(nombre)s, %(descripcion)s, %(fechaInicio)s, %(fechaFin)s, %(enlaceReunion)s, %(isProtocolar)s, %(isPonencia)s, %(isPanel)s, %(isConcurso)s, %(bases)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'ID_Actividad': cursor.lastrowid, 'nombre': nombre, 'descripcion': descripcion, 'fechaInicio': fechaInicio, 'fechaFin': fechaFin, 'enlaceReunion': enlaceReunion, 'isProtocolar': isProtocolar, 'isPonencia': isPonencia, 'isPanel': isPanel, 'isConcurso': isConcurso, 'bases': bases}
        return data

    def delete_actividad(self, ID_Actividad):    
        params = {'ID_Actividad' : ID_Actividad}      
        query = """delete from actividad where ID_Actividad = %(ID_Actividad)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_actividad(1))
    #print(tm.get_actividads())
    print(tm.delete_actividad(67))
    print(tm.get_actividads())
    #print(tm.create_actividad('prueba 10', 'desde python'))