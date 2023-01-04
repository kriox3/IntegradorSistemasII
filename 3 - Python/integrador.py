import sqlite3
import click
import traceback
import sys


def clrscr():
    click.clear()


def menuppal():
    print()
    print("====================")
    print("== MENU PRINCIPAL ==")
    print("====================")
    print()
    print("1. Gestion de Institutos")
    print("2. Gestion de Carreras")
    print("3. Gestion de Estudiantes")
    print("4. Gestion de Cursadas")
    print()
    opcionprincipal = input("Digite un numero para continuar: ")
    if opcionprincipal == "1":
        menuInstitutos()
    elif opcionprincipal == "2":
        menuCarreras()
    elif opcionprincipal == "3":
        menuEstudiantes()
    elif opcionprincipal == "4":
        menuCursadas()
    else:
        print()


""" menu institutos """


def menuInstitutos():
    clrscr()
    print()
    print("=====================")
    print("== MENU INSTITUTOS ==")
    print("=====================")
    print()
    print("1. Alta de Instituto")
    print("2. Modificar Instituto")
    print("3. Baja de Instituto")
    print("4. Listar los Institutos")
    print("---------------------")
    print("5. Volver a Menu Principal")
    print()
    opcion = input("Digite un numero para continuar: ")
    if opcion == "1":
        altaInstitutos()
    elif opcion == "2":
        modInstitutos()
    elif opcion == "3":
        bajaInstitutos()
    elif opcion == "4":
        listaInstitutos()
    elif opcion == "5":
        clrscr()
        menuppal()
    else:
        print()


def altaInstitutos():
    try:
        cursor = sqliteConnection.cursor()

        clrscr()
        print("Agregando nuevo Instituto: ")
        print()
        nombreInstituto = input("Nombre: ")
        cueInstituto = input("CUE: ")
        direccionInstituto = input("Direccion: ")
        telefonoInstituto = input("Telefono: ")
        webInstituto = input("Web: ")
        print()

        sqlite_insert_query = """INSERT INTO instituto
                          ( nombre, cue, direccion, telefono, web)  VALUES  ('"""+nombreInstituto+"', '"+cueInstituto+"', '"+direccionInstituto+"', '"+telefonoInstituto+"', '"+webInstituto+"')"

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Agregado Correctamente ",
          cursor.rowcount)
        cursor.close()

        menuInstitutos()


    except sqlite3.Error as error:
        print("Error al agregar datos")
        print("Clase de Excepcion: ", error.__class__)
        print("La Excepcion es", error.args)
        print('Imprimiendo detalles: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        print()


def modInstitutos():
    try:
        try:
            cursor = sqliteConnection.cursor()
            clrscr()
            print("Modificando Instituto: ")
            print()
            sqlite_cuenta = """SELECT count(*) from instituto"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Institutos disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT * from instituto"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCarreras()
        finally:
            print()

        print("De los anteriores, digite solo el id del instituto:")
        instituto_idInstituto = input("Id Instituto: ")
        nombreInstituto = input("Nuevo Nombre: ")
        cueInstituto = input("Nuevo CUE: ")
        direccionInstituto = input("Nueva Direccion: ")
        telefonoInstituto = input("Nuevo Telefono: ")
        webInstituto = input("Nueva Web: ")
        print()


        cursor = sqliteConnection.cursor()
        sqlite_update_query = """Update instituto set nombre = ?, cue = ?, direccion = ?, telefono = ?, web = ? where id = ?"""
        columnValues = (nombreInstituto, cueInstituto, direccionInstituto, telefonoInstituto, webInstituto, instituto_idInstituto)
        cursor.execute(sqlite_update_query, columnValues)
        sqliteConnection.commit()
        print("Registro Actualizado ")
        cursor.close()

        menuInstitutos()

    except sqlite3.Error as error:
        print("Fallo Actualizar tabla", error)
    finally:
        print()


def bajaInstitutos():
    print()


def listaInstitutos():
    try:
        cursor = sqliteConnection.cursor()
        clrscr()
        print("Listando Institutos: ")
        print()
        sqlite_cuenta = """SELECT count(*) from instituto"""
        cursor.execute(sqlite_cuenta)
        totalRows = cursor.fetchone()
        total = totalRows[0]
        print("Institutos disponibles:  ", total)
        cursor.close()

        cursor = sqliteConnection.cursor()
        sqlite_lista = """SELECT * from instituto"""
        cursor.execute(sqlite_lista)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()

    except sqlite3.Error as error:
        print("Error a leer datos de la tabla ", error)
        menuInstitutos()
    finally:
        print()
    
    input("Presione cualquier tecla para volver... ")
    menuInstitutos()


""" menu carreras """


def menuCarreras():
    clrscr()
    print()
    print("===================")
    print("== MENU CARRERAS ==")
    print("===================")
    print()
    print("1. Alta de Carrera")
    print("2. Modificar Carrera")
    print("3. Baja de Carrera")
    print("4. Listar las Carreras")
    print("-------------------")
    print("5. Volver a Menu Principal")
    print()
    opcion = input("Digite un numero para continuar: ")
    if opcion == "1":
        altaCarreras()
    elif opcion == "2":
        modCarreras()
    elif opcion == "3":
        bajaCarreras()
    elif opcion == "4":
        listaCarreras()
    elif opcion == "5":
        clrscr()
        menuppal()
    else:
        print()


def altaCarreras():
    try:
        clrscr()
        print("Agregando nueva Carrera: ")
        print()


        try:
            cursor = sqliteConnection.cursor()

            sqlite_cuenta = """SELECT count(*) from instituto"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Institutos disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT id, nombre from instituto"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCursadas()
        finally:
            print()
        
        print("De los anteriores, digite solo el id del instituto:")
        instituto_idCarrera = input("Id Instituto: ")
        codigoCarrera = input("Codigo: ")
        nombreCarrera = input("Nombre: ")
        resolucionCarrera = input("Resolucion: ")
        duracionCarrera = input("Duracion: ")
        activoCarrera = input("Activo (1- activo | 0- inactivo): ")
        print()

        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO carrera
                          ( instituto_id, codigo, nombre, resolucion, duracion, activo)  VALUES  ('"""+instituto_idCarrera+"', '"+codigoCarrera+"', '"+nombreCarrera+"', '"+resolucionCarrera+"', '"+duracionCarrera+"', '"+activoCarrera+"')"

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Agregado Correctamente ",
          cursor.rowcount)
        cursor.close()

        menuCarreras()


    except sqlite3.Error as error:
        print("Error al agregar datos")
        print("Clase de Excepcion: ", error.__class__)
        print("La Excepcion es", error.args)
        print('Imprimiendo detalles: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        print()


def modCarreras():
    try:
        try:
            cursor = sqliteConnection.cursor()
            clrscr()
            print("Modificando Carrera: ")
            print()
            sqlite_cuenta = """SELECT count(*) from carrera"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Carreras disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT * from carrera"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCarreras()
        finally:
            print()

        print("De los anteriores, digite solo el id de la carrera:")
        carrera_idCarrera = input("Id Carrera: ")

        try:
            cursor = sqliteConnection.cursor()

            sqlite_cuenta = """SELECT count(*) from instituto"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Institutos disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT id, nombre from instituto"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCarreras()
        finally:
            print()
        
        print("De los anteriores, digite solo el id del instituto:")
        instituto_idCarrera = input("Nuevo Id Instituto: ")
        codigoCarrera = input("Nuevo Codigo: ")
        nombreCarrera = input("Nuevo Nombre: ")
        resolucionCarrera = input("Nueva Resolucion: ")
        duracionCarrera = input("Nuevo Duracion: ")
        activoCarrera = input("Nuevo Estado de Activo (1- activo | 0- inactivo): ")
        print()


        cursor = sqliteConnection.cursor()
        sqlite_update_query = """Update carrera set instituto_id = ?, codigo = ?, nombre = ?, resolucion = ?, duracion = ?, activo = ? where id = ?"""
        columnValues = (instituto_idCarrera, codigoCarrera, nombreCarrera, resolucionCarrera, duracionCarrera, activoCarrera, carrera_idCarrera)
        cursor.execute(sqlite_update_query, columnValues)
        sqliteConnection.commit()
        print("Registro Actualizado ")
        cursor.close()

        menuCarreras()

    except sqlite3.Error as error:
        print("Fallo Actualizar tabla", error)
    finally:
        print()


def bajaCarreras():
    print()


def listaCarreras():
    try:
        cursor = sqliteConnection.cursor()
        clrscr()
        print("Listando Carreras: ")
        print()
        sqlite_cuenta = """SELECT count(*) from carrera"""
        cursor.execute(sqlite_cuenta)
        totalRows = cursor.fetchone()
        total = totalRows[0]
        print("Carreras disponibles:  ", total)
        cursor.close()

        cursor = sqliteConnection.cursor()
        sqlite_lista = """SELECT * from carrera"""
        cursor.execute(sqlite_lista)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()

    except sqlite3.Error as error:
        print("Error a leer datos de la tabla ", error)
        menuCarreras()
    finally:
        print()
    
    input("Presione cualquier tecla para volver... ")
    menuCarreras()


""" menu estudiantes """


def menuEstudiantes():
    clrscr()
    print()
    print("======================")
    print("== MENU ESTUDIANTES ==")
    print("======================")
    print()
    print("1. Alta de Estudiante")
    print("2. Modificar Estudiante")
    print("3. Baja de Estudiante")
    print("4. Listar los Estudiantes")
    print("----------------------")
    print("5. Volver a Menu Principal")
    print()
    opcion = input("Digite un numero para continuar: ")
    if opcion == "1":
        altaEstudiantes()
    elif opcion == "2":
        modEstudiantes()
    elif opcion == "3":
        bajaEstudiantes()
    elif opcion == "4":
        listaEstudiantes()
    elif opcion == "5":
        clrscr()
        menuppal()
    else:
        print()


def altaEstudiantes():
    try:
        cursor = sqliteConnection.cursor()

        clrscr()
        print("Agregando nuevo Estudiante: ")
        print()
        apellidoEstudiante = input("Apelido: ")
        nombreEstudiante = input("Nombre: ")
        dniEstudiante = input("Dni: ")
        fecha_nacimientoEstudiante = input("Fecha Nacimiento: ")
        foto_dniEstudiante = input("Foto DNI: ")
        foto_secundarioEstudiante = input("Foto Secundario: ")
        telefonoEstudiante = input("Telefono: ")
        emailEstudiante = input("Email: ")
        print()

        sqlite_insert_query = """INSERT INTO estudiante
                          ( apellido, nombre, dni, fecha_nacimiento, foto_dni, foto_secundario, telefono, email)  VALUES  ('"""+apellidoEstudiante+"', '"+nombreEstudiante+"', '"+dniEstudiante+"', '"+fecha_nacimientoEstudiante+"', '"+foto_dniEstudiante+"', '"+foto_secundarioEstudiante+"', '"+telefonoEstudiante+"', '"+emailEstudiante+"')"

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Agregado Correctamente ",
          cursor.rowcount)
        cursor.close()

        menuEstudiantes()


    except sqlite3.Error as error:
        print("Error al agregar datos")
        print("Clase de Excepcion: ", error.__class__)
        print("La Excepcion es", error.args)
        print('Imprimiendo detalles: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        print()


def modEstudiantes():
    try:
        try:
            cursor = sqliteConnection.cursor()
            clrscr()
            print("Modificando Estudiante: ")
            print()
            sqlite_cuenta = """SELECT count(*) from estudiante"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Estudiantes disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT * from estudiante"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuEstudiantes()
        finally:
            print()

        print("De los anteriores, digite solo el id del Estudiante:")
        estudiante_idEstudiante = input("Id Estudiante: ")

        apellidoEstudiante = input("Nuevo Apelido: ")
        nombreEstudiante = input("Nuevo Nombre: ")
        dniEstudiante = input("Nuevo Dni: ")
        fecha_nacimientoEstudiante = input("Nueva Fecha Nacimiento: ")
        foto_dniEstudiante = input("Nueva Foto DNI: ")
        foto_secundarioEstudiante = input("Nueva Foto Secundario: ")
        telefonoEstudiante = input("Nuevo Telefono: ")
        emailEstudiante = input("Nuevo Email: ")
        print()


        cursor = sqliteConnection.cursor()
        sqlite_update_query = """Update estudiante set apellido = ?, nombre = ?, dni = ?, fecha_nacimiento = ?, foto_dni = ?, foto_secundario = ?, telefono = ?, email = ? where id = ?"""
        columnValues = (apellidoEstudiante, nombreEstudiante, dniEstudiante, fecha_nacimientoEstudiante, foto_dniEstudiante, foto_secundarioEstudiante, telefonoEstudiante, emailEstudiante, estudiante_idEstudiante)
        cursor.execute(sqlite_update_query, columnValues)
        sqliteConnection.commit()
        print("Registro Actualizado ")
        cursor.close()

        menuEstudiantes()

    except sqlite3.Error as error:
        print("Fallo Actualizar tabla", error)
    finally:
        print()


def bajaEstudiantes():
    try:
        try:
            cursor = sqliteConnection.cursor()
            clrscr()
            print("Borrando Estudiante: ")
            print()
            sqlite_cuenta = """SELECT count(*) from estudiante"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Estudiantes disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT * from estudiante"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuEstudiantes()
        finally:
            print()

        print("De los anteriores, digite solo el id de la Estudiante:")
        estudiante_Id = input("Id Estudiante: ")

        cursor = sqliteConnection.cursor()

        try:
            cursor = sqliteConnection.cursor()
            sqlite_cuenta = """SELECT count(*) from cursada where estudiante_id="""+estudiante_Id
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            total = totalRows[0]
            print("Estudiantes disponibles:  ", total)
            cursor.close()

            if total > 0:
                print("TIENE REGISTRO no puede eliminar")
            else:
                print("Puede borrar")

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuEstudiantes()
        finally:
            print()

        
        #sqlite_update_query = """Delete from estudiante where id = ?"""
        #columnValues = (estudiante_Id)
        #cursor.execute(sqlite_update_query, columnValues)
        #sqliteConnection.commit()
        #print("Registro Borrado ")
        
        cursor.close()

        menuEstudiantes()

    except sqlite3.Error as error:
        print("Fallo Actualizar tabla", error)
    finally:
        print()


def listaEstudiantes():
    try:
        cursor = sqliteConnection.cursor()
        clrscr()
        print("Listando Estudiantes: ")
        print()
        sqlite_cuenta = """SELECT count(*) from estudiante"""
        cursor.execute(sqlite_cuenta)
        totalRows = cursor.fetchone()
        total = totalRows[0]
        print("Estudiantes disponibles:  ", total)
        cursor.close()

        cursor = sqliteConnection.cursor()
        sqlite_lista = """SELECT * from estudiante"""
        cursor.execute(sqlite_lista)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()

    except sqlite3.Error as error:
        print("Error a leer datos de la tabla ", error)
        menuEstudiantes()
    finally:
        print()
    
    input("Presione cualquier tecla para volver... ")
    menuEstudiantes()


""" menu cursadas """


def menuCursadas():
    clrscr()
    print()
    print("===================")
    print("== MENU CURSADAS ==")
    print("===================")
    print()
    print("1. Alta de Cursada")
    print("2. Modificar Cursada")
    print("3. Baja de Cursada")
    print("4. Listar los Cursada")
    print("-------------------")
    print("5. Volver a Menu Principal")
    print()
    opcion = input("Digite un numero para continuar: ")
    if opcion == "1":
        altaCursadas()
    elif opcion == "2":
        modCursadas()
    elif opcion == "3":
        bajaCursadas()
    elif opcion == "4":
        listaCursadas()
    elif opcion == "5":
        clrscr()
        menuppal()
    else:
        print()


def altaCursadas():
    try:
        clrscr()
        print("Agregando nueva Cursada: ")
        print()


        try:
            cursor = sqliteConnection.cursor()

            sqlite_cuenta = """SELECT count(*) from estudiante"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Estudiantes disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT id, apellido, nombre, dni from estudiante"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCursadas()
        finally:
            print()
        
        print("De los anteriores, digite solo el id del estudiante:")
        estudiante_idCursada = input("Id Estudiante: ")

        try:
            cursor = sqliteConnection.cursor()

            sqlite_cuenta = """SELECT count(*) from carrera WHERE activo=1"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Carreras disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT id, nombre, resolucion from carrera WHERE activo=1"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCursadas()
        finally:
            print()

        print("De los anteriores, digite solo el id de la carrera:")
        carrera_idCursada = input("Id Carrera: ")
        fecha_inscripcionCursada = input("Fecha Inscripcion: ")
        actualCursada = input("Es Carrera Actual (1- Si | 0- No): ")
        finalizadaCursada = input("Finalizada (1- Si | 0- No): ")
        print()

        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO cursada
                          ( estudiante_id, carrera_id, fecha_inscripcion, actual, finalizada)  VALUES  ('"""+estudiante_idCursada+"', '"+carrera_idCursada+"', '"+fecha_inscripcionCursada+"', '"+actualCursada+"', '"+finalizadaCursada+"')"

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Agregado Correctamente ",
          cursor.rowcount)
        cursor.close()

        menuCursadas()


    except sqlite3.Error as error:
        print("Error al agregar datos")
        print("Clase de Excepcion: ", error.__class__)
        print("La Excepcion es", error.args)
        print('Imprimiendo detalles: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        print()


def modCursadas():
    try:
        try:
            cursor = sqliteConnection.cursor()
            clrscr()
            print("Modificando Cursada: ")
            print()
            sqlite_cuenta = """SELECT count(*) from cursada"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Cursadas disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT * from cursada"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCursadas()
        finally:
            print()

        print("De los anteriores, digite solo el id de la Cursada:")
        cursada_idCursada = input("Id Cursada: ")

        try:
            cursor = sqliteConnection.cursor()

            sqlite_cuenta = """SELECT count(*) from estudiante"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Estudiantes disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT id, apellido, nombre, dni from estudiante"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCursadas()
        finally:
            print()
        
        print("De los anteriores, digite solo el id del estudiante:")
        estudiante_idCursada = input("Id Estudiante: ")

        try:
            cursor = sqliteConnection.cursor()

            sqlite_cuenta = """SELECT count(*) from carrera WHERE activo=1"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Carreras disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT id, nombre, resolucion from carrera WHERE activo=1"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCursadas()
        finally:
            print()

        print("De los anteriores, digite solo el id de la carrera:")
        carrera_idCursada = input("Nueva Id Carrera: ")
        fecha_inscripcionCursada = input("Nueva Fecha Inscripcion: ")
        actualCursada = input("Nuevo estado en Carrera Actual (1- Si | 0- No): ")
        finalizadaCursada = input("Nuevo estado de Finalizacion (1- Si | 0- No): ")
        print()


        cursor = sqliteConnection.cursor()
        sqlite_update_query = """Update cursada set estudiante_id = ?, carrera_id = ?, fecha_inscripcion = ?, actual = ?, finalizada = ? where id = ?"""
        columnValues = (estudiante_idCursada, carrera_idCursada, fecha_inscripcionCursada, actualCursada, finalizadaCursada, cursada_idCursada)
        cursor.execute(sqlite_update_query, columnValues)
        sqliteConnection.commit()
        print("Registro Actualizado ")
        cursor.close()

        menuCursadas()

    except sqlite3.Error as error:
        print("Fallo Actualizar tabla", error)
    finally:
        print()


def bajaCursadas():
    try:
        try:
            cursor = sqliteConnection.cursor()
            clrscr()
            print("Borrando Cursada: ")
            print()
            sqlite_cuenta = """SELECT count(*) from cursada"""
            cursor.execute(sqlite_cuenta)
            totalRows = cursor.fetchone()
            total = totalRows[0]
            print("Cursadas disponibles:  ", total)
            cursor.close()

            cursor = sqliteConnection.cursor()
            sqlite_lista = """SELECT * from cursada"""
            cursor.execute(sqlite_lista)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()

        except sqlite3.Error as error:
            print("Error a leer datos de la tabla ", error)
            menuCursadas()
        finally:
            print()

        print("De los anteriores, digite solo el id de la Cursada:")
        cursada_idCursada = input("Id Cursada: ")

        cursor = sqliteConnection.cursor()
        sqlite_update_query = """Delete from cursada where id = ?"""
        columnValues = (cursada_idCursada)
        cursor.execute(sqlite_update_query, columnValues)
        sqliteConnection.commit()
        print("Registro Borrado ")
        cursor.close()

        menuCursadas()

    except sqlite3.Error as error:
        print("Fallo Actualizar tabla", error)
    finally:
        print()


def listaCursadas():
    try:
        cursor = sqliteConnection.cursor()
        clrscr()
        print("Listando Cursadas: ")
        print()
        sqlite_cuenta = """SELECT count(*) from cursada"""
        cursor.execute(sqlite_cuenta)
        totalRows = cursor.fetchone()
        total = totalRows[0]
        print("Cursadas disponibles:  ", total)
        cursor.close()

        cursor = sqliteConnection.cursor()
        sqlite_lista = """SELECT * from cursada"""
        cursor.execute(sqlite_lista)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()

    except sqlite3.Error as error:
        print("Error a leer datos de la tabla ", error)
        menuCursadas()
    finally:
        print()
    
    input("Presione cualquier tecla para volver... ")
    menuCursadas()


""" fin de los menu """

try:
    from colorama import Fore, init
    from colorama import Style, init
    init()
    print(Fore.GREEN + "Cargando recursos...")

    sqliteConnection = sqlite3.connect('integrador.db')
    cursor = sqliteConnection.cursor()
    clrscr()
    print(Style.BRIGHT + "          __                         ")
    print("     ...-'  |`.           .-''-.     ")
    print(".--. |      |  |        .' .-.  )    ")
    print("|__| ....   |  |       / .'  / /     ")
    print(".--.   -|   |  |      (_/   / /      ")
    print("|  |    |   |  |           / /       ")
    print("|  | ...'   `--'          / /        ")
    print("|  | |         |`.       . '         ")
    print("|  | ` --------\ |      / /    _.-') ")
    print("|__|  `---------'     .' '  _.'.-''  ")
    print("                     /  /.-'_.'      ")
    print("                    /    _.'         ")
    print("                   ( _.-'            ")

    print("Bienvenido al Proyecto Integrador")
    print("Carreras Vs Cursadas v1.0 con conexion sqlite3")
    print(Style.RESET_ALL + Fore.GREEN)

    """ sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close() """

    menuppal()


except sqlite3.Error as error:
    print("Error conectando a la base de datos", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("Conexion Cerrada")
