import mysql.connector
import random
from typing import List

#Conexion
def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zqw7@r5u&#uZu",
            database="prueba_uno",
            port="3306"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def cerrar_conexion(conexion):
    if conexion:
        conexion.close()
        print("Conexión cerrada.")

def insertar_empleado_mysql(empleado):
    conexion = conectar_mysql()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO empleados (Matricula, Nombre, ApellidoPaterno, ApellidoMaterno, FechaNacimiento, FechaIngreso, Departamento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (empleado.Matricula, empleado.Nombre, empleado.ApellidoPaterno, empleado.ApellidoMaterno, empleado.FechaNacimiento, empleado.FechaIngreso, empleado.Departamento)
            cursor.execute(sql, val)
            conexion.commit()
            print("Empleado insertado en MySQL.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cerrar_conexion(conexion)


# Área de Clases
class Empleados:
    def __init__(self):
        self.Nombre = ""
        self.ApellidoPaterno = ""
        self.ApellidoMaterno = ""
        self.FechaNacimiento = ""
        self.FechaIngreso = ""
        self.DiasTrabajados = 0
        self.Matricula = ""
        self.RFC = ""
        self.Departamento = ""
        self.FI = 0.0
        self.SDI = 0.0
        self.CuotaFija = 0.0
        self.PDpat = 0.0
        self.PDobr = 0.0
        self.GPMpat = 0.0
        self.GMPobr = 0.0
        self.RT = 0.0
        self.IVpat = 0.0
        self.IVobr = 0.0
        self.GPS = 0.0
        self.Patron = 0.0
        self.Obrero = 0.0
        self.Total = 0.0
        self.Clase = 0
        self.DiasAguinaldo = 0.0

def finanzas():
    MAX_PROVEEDORES = 100
    MAX_CLIENTES = 100
    proveedores = [Finanzas_Proveedor() for _ in range(MAX_PROVEEDORES)]
    clientes = [Finanzas_Cliente() for _ in range(MAX_CLIENTES)]
    num_proveedores = 0
    num_clientes = 0
    op1 = 0
    op2 = 0

    while op1 != 3:
        print("\n1. Proveedores\n2. Clientes\n3. Regresar")
        op1 = int(input("Seleccione una opción: "))

        if op1 == 1:
            while op2 != 4:
                print("\n1. Ingresar Proveedor\n2. Mostrar Proveedores\n3. Buscar Proveedor\n4. Regresar")
                op2 = int(input("Seleccione una opción: "))

                if op2 == 1:
                    ingresar_proveedor(proveedores, num_proveedores)
                    num_proveedores += 1
                elif op2 == 2:
                    mostrar_proveedores(proveedores, num_proveedores)
                elif op2 == 3:
                    buscar_proveedor(proveedores, num_proveedores)
                elif op2 == 4:
                    print("Regresando al menú principal.")
                else:
                    print("Error: Opción no válida.")
        elif op1 == 2:
            while op2 != 4:
                print("\n1. Ingresar Cliente\n2. Mostrar Clientes\n3. Buscar Cliente\n4. Regresar")
                op2 = int(input("Seleccione una opción: "))

                if op2 == 1:
                    ingresar_cliente(clientes, num_clientes)
                    num_clientes += 1
                elif op2 == 2:
                    mostrar_clientes(clientes, num_clientes)
                elif op2 == 3:
                    buscar_cliente(clientes, num_clientes)
                elif op2 == 4:
                    print("Regresando al menú principal.")
                else:
                    print("Error: Opción no válida.")
        elif op1 == 3:
            print("Regresando al menú principal.")
        else:
            print("Error: Opción no válida.")

def ingresar_proveedor(proveedores, num_proveedores):
    proveedores[num_proveedores].num_Proveedor = int(input("Ingrese el número del proveedor: "))
    proveedores[num_proveedores].nombre = input("Ingrese el nombre del proveedor: ")
    proveedores[num_proveedores].telefono = input("Ingrese el teléfono del proveedor: ")
    proveedores[num_proveedores].compania = input("Ingrese el nombre de la compañía del proveedor: ")

def mostrar_proveedores(proveedores, num_proveedores):
    print(f"{'Número':<10}{'Nombre':<20}{'Teléfono':<15}{'Compañía':<20}")

    for i in range(num_proveedores):
        print(f"{proveedores[i].num_Proveedor:<10}{proveedores[i].nombre:<20}{proveedores[i].telefono:<15}"
              f"{proveedores[i].compania:<20}")

def buscar_proveedor(proveedores, num_proveedores):
    num = int(input("Ingrese el número del proveedor a buscar: "))
    encontrado = False

    for i in range(num_proveedores):
        if proveedores[i].num_Proveedor == num:
            print(f"Proveedor encontrado:\n"
                  f"Número: {proveedores[i].num_Proveedor}\n"
                  f"Nombre: {proveedores[i].nombre}\n"
                  f"Teléfono: {proveedores[i].telefono}\n"
                  f"Compañía: {proveedores[i].compania}")
            encontrado = True
            break

    if not encontrado:
        print("Proveedor no encontrado.")

def ingresar_cliente(clientes, num_clientes):
    clientes[num_clientes].num_Cliente = int(input("Ingrese el número del cliente: "))
    clientes[num_clientes].nombre = input("Ingrese el nombre del cliente: ")
    clientes[num_clientes].telefono = input("Ingrese el teléfono del cliente: ")

def mostrar_clientes(clientes, num_clientes):
    print(f"{'Número':<10}{'Nombre':<20}{'Teléfono':<15}")

    for i in range(num_clientes):
        print(f"{clientes[i].num_Cliente:<10}{clientes[i].nombre:<20}{clientes[i].telefono:<15}")

def buscar_cliente(clientes, num_clientes):
    num = int(input("Ingrese el número del cliente a buscar: "))
    encontrado = False

    for i in range(num_clientes):
        if clientes[i].num_Cliente == num:
            print(f"Cliente encontrado:\n"
                  f"Número: {clientes[i].num_Cliente}\n"
                  f"Nombre: {clientes[i].nombre}\n"
                  f"Teléfono: {clientes[i].telefono}")
            encontrado = True
            break

    if not encontrado:
        print("Cliente no encontrado.")


class Finanzas_Proveedor:
    def __init__(self):
        self.num_Proveedor = 0
        self.nombre = ""
        self.telefono = ""
        self.compania = ""

class Finanzas_Cliente:
    def __init__(self):
        self.num_Cliente = 0
        self.nombre = ""
        self.telefono = ""

class Material:
    def __init__(self):
        self.Nombre = ""
        self.costoPieza = 0.0
        self.NumPieza = 0
        self.costoTotal = 0.0

# Variables Globales
n = 0
arr = None

# Declaración de funciones
def pedir_datos_materiales():
    global n, arr
    print("Ingresa el número de materiales:")
    n = int(input())
    arr = [Material() for _ in range(n)]

    for i in range(n):
        print(f"[{i}] Ingresa el nombre:")
        arr[i].Nombre = input()
        print("Ingresa el número de material:")
        arr[i].NumPieza = int(input())
        print("Ingresa el costo unitario:")
        arr[i].costoPieza = float(input())
        arr[i].costoTotal = arr[i].costoPieza * arr[i].NumPieza

def ordenar_datos_n(arr):
    arr.sort(key=lambda x: x.Nombre)

def ordenar_datos_p(arr):
    arr.sort(key=lambda x: x.NumPieza)

def ordenar_datos_ct(arr):
    arr.sort(key=lambda x: x.costoTotal)

def imprimir_tabla(arr):
    print(f"{'Numero':<10}{'Nombre':<20}{'Costo/pieza':<15}{'Numero de piezas':<20}{'Costo total':<15}")

    for i, material in enumerate(arr):
        print(f"{i:<10}{material.Nombre:<20}{material.costoPieza:<15}{material.NumPieza:<20}{material.costoTotal:<15}")

def pedir_datos_empleado(empleados, num_empleados):
    empleados[num_empleados].Nombre = input("Ingrese el nombre del empleado: ")
    empleados[num_empleados].ApellidoPaterno = input("Ingrese el apellido paterno del empleado: ")
    empleados[num_empleados].ApellidoMaterno = input("Ingrese el apellido materno del empleado: ")
    empleados[num_empleados].FechaIngreso = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")
    empleados[num_empleados].FechaNacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
    empleados[num_empleados].Departamento = input("Ingrese el departamento del empleado: ")
    print("1. Clase I\t2. Clase II\t3. Clase III\t4. Clase IV")
    empleados[num_empleados].Clase = int(input("Ingrese la Clase del empleado: "))
    generar_matricula(empleados[num_empleados])
    generar_rfc(empleados[num_empleados])

def generar_matricula(empleado):
    empleado.Matricula = str(random.randint(0, 99999)).zfill(5)

def generar_rfc(empleado):
    empleado.RFC = empleado.ApellidoPaterno[:2] + empleado.ApellidoMaterno[:2] + empleado.Nombre[:2] + \
                   empleado.FechaNacimiento[:2] + empleado.FechaNacimiento[3:5] + empleado.FechaNacimiento[8:10]

def calcular_dias_trabajados(empleados, num_empleados):
    from datetime import datetime

    now = datetime.now()
    dia_actual = now.day
    mes_actual = now.month
    anio_actual = now.year

    for i in range(num_empleados):
        dia_ingreso = int(empleados[i].FechaIngreso[:2])
        mes_ingreso = int(empleados[i].FechaIngreso[3:5])
        anio_ingreso = int(empleados[i].FechaIngreso[6:10])

        dias_trabajados = (anio_actual - anio_ingreso) * 365 + (mes_actual - mes_ingreso) * 30 + (dia_actual - dia_ingreso)
        empleados[i].DiasTrabajados = dias_trabajados

def imprimir_tabla_empleados(empleados, num_empleados):
    print(f"{'Matricula':<10}{'Nombre':<20}{'Apellido Paterno':<20}{'Apellido Materno':<20}"
          f"{'RFC':<15}{'Dias Trabajados':<20}{'Departamento':<20}")

    for i in range(num_empleados):
        print(f"{empleados[i].Matricula:<10}{empleados[i].Nombre:<20}{empleados[i].ApellidoPaterno:<20}"
              f"{empleados[i].ApellidoMaterno:<20}{empleados[i].RFC:<15}{empleados[i].DiasTrabajados:<20}"
              f"{empleados[i].Departamento:<20}")

def calcular_uma(empleados, num_empleados):
    dias_anio = 365
    dias_mes = 30
    cuota_fija = 0.204
    uma_2023 = 103.74
    sdi = 183.32
    pdo = 1.5
    pd_pat = 0.007
    pd_obr = 0.0025
    gpm_pat = 0.0105
    gmp_obr = 0.0035
    iv_pat = 0.0175
    iv_obr = 0.00625
    gps = 0.01

    for i in range(num_empleados):
        if empleados[i].DiasTrabajados < 365:
            empleados[i].DiasAguinaldo = (dias_anio / 15) * empleados[i].DiasTrabajados
            empleados[i].FI = (dias_anio + empleados[i].DiasAguinaldo + pdo) / dias_anio
            empleados[i].SDI = empleados[i].FI * sdi
        else:
            empleados[i].FI = (dias_anio + 15 + pdo) / dias_anio
            empleados[i].SDI = empleados[i].FI * sdi

        empleados[i].CuotaFija = cuota_fija * dias_mes * uma_2023
        empleados[i].PDpat = empleados[i].SDI * dias_mes * pd_pat
        empleados[i].PDobr = empleados[i].SDI * dias_mes * pd_obr
        empleados[i].GPMpat = empleados[i].SDI * dias_mes * gpm_pat
        empleados[i].GMPobr = empleados[i].SDI * dias_mes * gmp_obr

        if empleados[i].Clase == 1:
            empleados[i].RT = empleados[i].SDI * dias_mes * (0.54355 / 100)
        elif empleados[i].Clase == 2:
            empleados[i].RT = empleados[i].SDI * dias_mes * (1.13065 / 100)
        elif empleados[i].Clase == 3:
            empleados[i].RT = empleados[i].SDI * dias_mes * (2.5984 / 100)
        elif empleados[i].Clase == 4:
            empleados[i].RT = empleados[i].SDI * dias_mes * (4.65325 / 1400)
        elif empleados[i].Clase == 5:
            empleados[i].RT = empleados[i].SDI * dias_mes * (7.58875 / 100)

        empleados[i].IVpat = empleados[i].SDI * dias_mes * iv_pat
        empleados[i].IVobr = empleados[i].SDI * dias_mes * iv_obr
        empleados[i].GPS = empleados[i].SDI * dias_mes * gps

        empleados[i].Patron = (empleados[i].CuotaFija + empleados[i].PDpat + empleados[i].GPMpat +
                               empleados[i].RT + empleados[i].IVpat + empleados[i].GPS)
        empleados[i].Obrero = empleados[i].PDobr + empleados[i].GMPobr + empleados[i].IVobr

def imprimir_tabla_uma(empleados, num_empleados):
    print(f"{'Matricula':<10}{'Nombre':<20}{'SDI':<20}{'Cuota Fija':<20}"
          f"{'PDpat':<15}{'PDobr':<20}{'GPMpat':<20}{'GPMobr':<10}"
          f"{'RT':<10}{'IVpat':<10}{'IVObr':<10}{'Patron':<10}{'Obrero':<10}")

    for i in range(num_empleados):
        print(f"{empleados[i].Matricula:<10}{empleados[i].Nombre:<20}{empleados[i].SDI:<20}{empleados[i].CuotaFija:<20}"
              f"{empleados[i].PDpat:<15}{empleados[i].PDobr:<20}{empleados[i].GPMpat:<20}{empleados[i].GMPobr:<10}"
              f"{empleados[i].RT:<10}{empleados[i].IVpat:<10}{empleados[i].IVobr:<10}"
              f"{empleados[i].Patron:<10}{empleados[i].Obrero:<10}")

# Parte Principal del programa
def main():
    MAX_EMPLEADOS = 100
    empleado = [Empleados() for _ in range(MAX_EMPLEADOS)]
    num_empleados = 0
    op, op1, op2 = 0, 0, 0  # Opciones para Switch Case
    respuesta = 'S'  # Condición de inicio del while

    while op != 6:
        print("1. Recursos Humanos\n2. Produccion\n3. Finanzas\n4. Marketing\n5. Sistemas\n6. Salir")
        op = int(input("Seleccione una opción: "))

        if op == 1:
            while op1 != 4:
                print("\n1. Ingresar empleado\n2. Mostrar Tabla\n3. Tabla UMA\n4. Salir")
                op1 = int(input("Seleccione una opción: "))

                if op1 == 1:
                    while respuesta == 's' or respuesta == 'S':
                        pedir_datos_empleado(empleado, num_empleados)
                        insertar_empleado_mysql(empleado[num_empleados - 1])  # Insertar el último empleado ingresado
                        num_empleados += 1
                        respuesta = input("¿Desea ingresar otro empleado? (S/N): ")
                elif op1 == 2:
                    calcular_dias_trabajados(empleado, num_empleados)
                    imprimir_tabla_empleados(empleado, num_empleados)
                elif op1 == 3:
                    calcular_uma(empleado, num_empleados)
                    imprimir_tabla_uma(empleado, num_empleados)
                elif op1 == 4:
                    print("Saliendo del sistema.")
                else:
                    print("Error: Opción no válida.")
        elif op == 2:
            pedir_datos_materiales()
            print("Seleccione cómo desea ordenar los datos:")
            print("1. Nombre\n2. Número de materiales\n3. Costo total")
            op2 = int(input())
            if op2 == 1:
                ordenar_datos_n(arr)
            elif op2 == 2:
                ordenar_datos_p(arr)
            elif op2 == 3:
                ordenar_datos_ct(arr)
            else:
                print("Error")
            print("Tabla:")
            imprimir_tabla(arr)
        elif op == 3:
            finanzas()
        elif op == 4:
            print("Opción para Marketing.")  # Por empezar
        elif op == 5:
            print("Opción para Sistemas.")  # Por empezar
        elif op == 6:
            print("Salir")
        else:
            print("Error: Opción no válida.")

if __name__ == "__main__":
    main()
