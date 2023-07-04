import psycopg2

conexion = psycopg2.connect(user='postgres', password='root', host='127.0.0.1', port='5432', database='alumnos_bd')

while True:
    try:
        with conexion:
            with conexion.cursor() as cursor:
                id_alumno = input("Ingrese el ID del alumno: ")
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                telefono = input("Ingrese su número telefónico: ")
                mail = input("Ingrese el email: ")
                direccion = input("Ingrese su dirección: ")
                
                sentencia = 'INSERT INTO alumnos (id_alumno, nombre, apellido, telefono, mail, direccion) VALUES (%s, %s, %s, %s, %s, %s)'
                valores = (id_alumno, nombre, apellido, telefono, mail, direccion)
                cursor.execute(sentencia, valores)
                
                registros_insertados = cursor.rowcount
                print(f'Los registros insertados son: {registros_insertados}')
                
        respuesta = input("¿Desea registrar otro alumno? (S/N): ")
        if respuesta.lower() != 's':
            break
    
    except Exception as e:
        print(f'Ocurrió un error: {e}')

conexion.close()


