import sys
import sqlite3
from sqlite3 import Error
separador = ("*" * 20) + "\n"

try:
    with sqlite3.connect("BaseDeDatosAlumnos.db") as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS alumno (clave INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS materia (clave_materia INTEGER PRIMARY KEY, nombre TEXT NOT NULL, clave INTEGER NOT NULL, FOREIGN KEY(clave) REFERENCES alumno(clave));") 
        c.execute("CREATE TABLE IF NOT EXISTS calificacion (clave_calificacion INTEGER PRIMARY KEY, valor INTEGER NOT NULL, clave_materia INTEGER, clave INTEGER,FOREIGN KEY (clave_materia) REFERENCES materia(clave_materia) FOREIGN KEY(clave) REFERENCES alumno(clave));")
        print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    conn.close()

print(separador *2)
print ("Selecciona una opción" + " ")
print ("1.- REGISTRAR ALUMNOS")
print ("2.- REGISTRAR MATERIAS")
print ("3.- CAPTURAR CALIFICACIONES")


opcion=int(input("Seleccione la opcion deseada: "))
if opcion == 1:
    c_alumnos=int(input("¿Cuantos alumnos desea registra?: "))
    for i in range (c_alumnos):
        print("Proporcione los datos del alumno, entre la clave 0 (cero) para terminar...")
        campo_clave = int(input("Clave del alumno: "))
        if campo_clave == 0:
            print("!!!!Bye!!!")
        else:
            campo_nombre = input("Nombre del alumno: ")
            try:
                with sqlite3.connect("BaseDeDatosAlumnos.db") as conn:
                    mi_cursor = conn.cursor()
                    valores = {"clave":campo_clave, "nombre":campo_nombre}
                    mi_cursor.execute("INSERT INTO alumno VALUES(:clave,:nombre)", valores)
                    print("*** Registro agregado exitosamente ***")
                    print("")
            except Error as e:
                print (e)
            except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                print("Se concluyó la carga de registros")
                
                continuar = True
if opcion== 2:
    print ("OPCION REGISTRAR MATERIAS SELECCIONADA")
    c_materias=int(input("¿Cuantos materias desea registrar?: "))
    for i in range (c_materias):
        print("Proporcione los datos de la materia, entre la clave 0 (cero) para terminar...")
        campo_clave_materia = int(input("Clave de la materia: "))
        if campo_clave_materia == 0:
            print("BYE")
        else:
            campo_nombre = input("Nombre de la materia: ")
            campo_clave = input("Clave del alumno: ")
        try:
            with sqlite3.connect("BaseDeDatosAlumnos.db") as conn:
                mi_cursor = conn.cursor()
                valores = {"clave_materia":campo_clave_materia, "nombre":campo_nombre, "clave":campo_clave}
                mi_cursor.execute("INSERT INTO materia VALUES(:clave_materia,:nombre,:clave)", valores)
            print("*** Registro agregado exitosamente ***")
            print("")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

if opcion== 3:
    print ("OPCION CAPTURAR CALIFICACIONES SELECCIONADA")
    valores=int(input("¿Cuantos calificaciones desea capturar?: "))
    for i in range (valores):
        print("Proporcione los datos de la calificacion, entre la clave 0 (cero) para terminar...")
        campo_clave_calificacion = int(input("Clave de la calificacion: "))
        if campo_clave_calificacion == 0:
            print("BYE")
        else:
            campo_nombre = input("Calificacion a registrar: ")
            campo_clave_materia = input("Clave de la materia: ")
            campo_clave =input("Clave del alumno: ")
        try:
            with sqlite3.connect("BaseDeDatosAlumnos.db") as conn:
                mi_cursor = conn.cursor()
                valores = {"clave_calificacion":campo_clave_calificacion, "nombre":campo_nombre, "clave":campo_clave_materia, "alumno":campo_clave}
                mi_cursor.execute("INSERT INTO calificacion VALUES(:clave_calificacion,:nombre,:clave,:alumno)", valores)
            print("*** Registro agregado exitosamente ***")
            print("")
        except Error as e:
            print (e)
        except:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

print("Se concluyó la carga de registros")