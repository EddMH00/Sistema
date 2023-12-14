import random
import datetime
from typing import List

import mysql.connector

class Empleado:
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

class FinanzasProveedor:
    def __init__(self):
        self.num_Proveedor = 0
        self.nombre = ""
        self.telefono = ""
        self.compania = ""

class FinanzasCliente:
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

class Venta:
    def __init__(self):
        self.Producto = ""
        self.Monto = 0.0
        self.FechaVenta = ""

class Usuario:
    def __init__(self):
        self.nombre = ""
        self.rol = ""

class Produccion:
    def __init__(self):
        self.Producto = ""
        self.Cantidad = 0
        self.FechaProduccion = ""

def pedir_datos_empleado(empleados, num_empleados):
    empleado = Empleado()
    empleado.Nombre = input("Ingrese el nombre del empleado: ")
    empleado.ApellidoPaterno = input("Ingrese el apellido paterno del empleado: ")
    empleado.ApellidoMaterno = input("Ingrese el apellido materno del empleado: ")
    empleado.FechaIngreso = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")
    empleado.FechaNacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
    empleado.Departamento = input("Ingrese el departamento del empleado: ")
    print("1. Clase I\t2. Clase II\t3. Clase III\t4. Clase IV")
    empleado.Clase = int(input("Ingrese la Clase del empleado: "))
    generar_matricula(empleado)
    generar_rfc(empleado)
    empleados.append(empleado)

def generar_matricula(empleado):
    empleado.Matricula = str(random.randint(10000, 99999))

def generar_rfc(empleado):
    empleado.RFC = (empleado.ApellidoPaterno[:2] +
                   empleado.ApellidoMaterno[:2] +
                   empleado.Nombre[:2] +
                   empleado.FechaNacimiento[:2] +
                   empleado.FechaNacimiento[3:5] +
                   empleado.FechaNacimiento[8:10])

def calcular_dias_trabajados(empleados):
    now = datetime.datetime.now()
    dia_actual = now.day
    mes_actual = now.month
    anio_actual = now.year

    for empleado in empleados:
        fecha_ingreso = datetime.datetime.strptime(empleado.FechaIngreso, "%d/%m/%Y")
        dias_trabajados = (now - fecha_ingreso).days
        empleado.DiasTrabajados = dias_trabajados

def imprimir_tabla_empleados(empleados):
    print(f"\n{'Matricula':<10}{'Nombre':<20}{'Apellido Paterno':<20}{'Apellido Materno':<20}"
          f"{'RFC':<15}{'Dias Trabajados':<20}{'Departamento':<20}")

    for empleado in empleados:
        print(f"{empleado.Matricula:<10}{empleado.Nombre:<20}{empleado.ApellidoPaterno:<20}{empleado.ApellidoMaterno:<20}"
              f"{empleado.RFC:<15}{empleado.DiasTrabajados:<20}{empleado.Departamento:<20}")
    
    # Conectar a MySQL
    connection = conectar_mysql()
    # Extraer datos de empleados de MySQL y mostrarlos
    mostrar_datos_desde_mysql(connection)
    # Cerrar conexión a MySQL
    cerrar_conexion_mysql(connection)

def calcular_uma(empleados):
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

    for empleado in empleados:
        if empleado.DiasTrabajados < dias_anio:
            empleado.DiasAguinaldo = (dias_anio / 15) * empleado.DiasTrabajados
            empleado.FI = (dias_anio + empleado.DiasAguinaldo + pdo) / dias_anio
            empleado.SDI = empleado.FI * sdi
        else:
            empleado.FI = (dias_anio + 15 + pdo) / dias_anio
            empleado.SDI = empleado.FI * sdi

        empleado.CuotaFija = cuota_fija * dias_mes * uma_2023
        empleado.PDpat = empleado.SDI * dias_mes * pd_pat
        empleado.PDobr = empleado.SDI * dias_mes * pd_obr
        empleado.GPMpat = empleado.SDI * dias_mes * gpm_pat
        empleado.GMPobr = empleado.SDI * dias_mes * gmp_obr

        if empleado.Clase == 1:
            empleado.RT = empleado.SDI * dias_mes * (0.54355 / 100)
        elif empleado.Clase == 2:
            empleado.RT = empleado.SDI * dias_mes * (1.13065 / 100)
        elif empleado.Clase == 3:
            empleado.RT = empleado.SDI * dias_mes * (2.5984 / 100)
        elif empleado.Clase == 4:
            empleado.RT = empleado.SDI * dias_mes * (4.65325 / 1400)
        elif empleado.Clase == 5:
            empleado.RT = empleado.SDI * dias_mes * (7.58875 / 100)

        empleado.IVpat = empleado.SDI * dias_mes * iv_pat
        empleado.IVobr = empleado.SDI * dias_mes * iv_obr
        empleado.GPS = empleado.SDI * dias_mes * gps

        empleado.Patron = (empleado.CuotaFija + empleado.PDpat + empleado.GPMpat +
                           empleado.RT + empleado.IVpat + empleado.GPS)
        empleado.Obrero = empleado.PDobr + empleado.GMPobr + empleado.IVobr

def imprimir_tabla_uma(empleados):
    print(f"\n{'Matricula':<10}{'Nombre':<20}{'SDI':<20}{'Cuota Fija':<20}"
          f"{'PDpat':<15}{'PDobr':<20}{'GPMpat':<20}{'GMPobr':<10}"
          f"{'RT':<10}{'IVpat':<10}{'IVobr':<10}{'GPS':<10}{'Patron':<10}{'Obrero':<10}")

    for empleado in empleados:
        print(f"{empleado.Matricula:<10}{empleado.Nombre:<20}{empleado.SDI:<20}{empleado.CuotaFija:<20}"
              f"{empleado.PDpat:<15}{empleado.PDobr:<20}{empleado.GPMpat:<20}{empleado.GMPobr:<10}"
              f"{empleado.RT:<10}{empleado.IVpat:<10}{empleado.IVobr:<10}{empleado.GPS:<10}"
              f"{empleado.Patron:<10}{empleado.Obrero:<10}")

def pedir_datos_materiales():
    n = int(input("Ingresa el número de materiales: "))
    arr = []

    for i in range(n):
        material = Material()
        print(f"[{i}]")
        material.Nombre = input("Ingresa el nombre: ")
        material.NumPieza = int(input("Ingresa el número de material: "))
        material.costoPieza = float(input("Ingresa el costo unitario: "))
        material.costoTotal = material.costoPieza * material.NumPieza
        arr.append(material)

    return arr

def ordenar_datos_n(arr):
    arr.sort(key=lambda x: x.Nombre)

def ordenar_datos_p(arr):
    arr.sort(key=lambda x: x.NumPieza)

def ordenar_datos_ct(arr):
    arr.sort(key=lambda x: x.costoTotal)

def imprimir_tabla(arr):
    print(f"\n{'Numero':<10}{'Nombre':<20}{'Costo/pieza':<15}"
          f"{'Numero de piezas':<20}{'Costo total':<15}")

    for i, material in enumerate(arr):
        print(f"{i:<10}{material.Nombre:<20}{material.costoPieza:<15}"
              f"{material.NumPieza:<20}{material.costoTotal:<15}")

def ingresar_proveedores(lista_proveedores):
    num_proveedores = int(input("Ingrese el número de proveedores: "))

    for i in range(num_proveedores):
        proveedor = FinanzasProveedor()
        print(f"Proveedor #{i + 1}:")
        proveedor.num_Proveedor = random.randint(10000, 99999)
        print(f"Número de proveedor: {proveedor.num_Proveedor}")
        proveedor.nombre = input("Nombre: ")
        proveedor.telefono = input("Teléfono: ")
        proveedor.compania = input("Compañía: ")

        lista_proveedores.append(proveedor)

def ingresar_clientes(lista_clientes):
    num_clientes = int(input("Ingrese el número de clientes: "))

    for i in range(num_clientes):
        cliente = FinanzasCliente()
        print(f"Cliente #{i + 1}:")
        cliente.num_Cliente = random.randint(10000, 99999)
        print(f"Número de Cliente: {cliente.num_Cliente}")
        cliente.nombre = input("Nombre: ")
        cliente.telefono = input("Teléfono: ")

        lista_clientes.append(cliente)

def imprimir_tabla_finanzas(proveedores, clientes):
    print("\nTabla de Proveedores:")
    print(f"{'Número':<20}{'Nombre':<20}{'Teléfono':<20}{'Compañía':<20}")

    for proveedor in proveedores:
        print(f"{proveedor.num_Proveedor:<20}{proveedor.nombre:<20}{proveedor.telefono:<20}{proveedor.compania:<20}")

    print("\nTabla de Clientes:")
    print(f"{'Número':<20}{'Nombre':<20}{'Teléfono':<20}")

    for cliente in clientes:
        print(f"{cliente.num_Cliente:<20}{cliente.nombre:<20}{cliente.telefono:<20}")

def pedir_datos_venta(ventas, num_ventas):
    venta = Venta()
    venta.Producto = input("Ingrese el nombre del producto: ")
    venta.Monto = float(input("Ingrese el monto de la venta: "))
    venta.FechaVenta = input("Ingrese la fecha de la venta (AAAA-MM-DD): ")
    ventas.append(venta)

def marketing(min_ventas, max_ventas, ventas):
    menu_marketing = 0

    while menu_marketing != 3:
        print("\nMarketing\n1.- Registrar venta\n2.- Mostrar ventas\n3.- Salir")
        menu_marketing = int(input("Seleccione una opción: "))

        if menu_marketing == 1:
            # Registrar venta
            if len(ventas) < max_ventas:
                pedir_datos_venta(ventas, len(ventas))
                print("Venta registrada exitosamente.")
            else:
                print("Se alcanzó el número máximo de ventas permitidas.")
        elif menu_marketing == 2:
            # Mostrar ventas
            print("\nVentas registradas:")
            # Conectar a MySQL
            connection = conectar_mysql()
            mostrar_datos_ventas_desde_mysql(connection)
            # Cerrar conexión a MySQL
            cerrar_conexion_mysql(connection)
            
        elif menu_marketing == 3:
            print("Saliendo del departamento de Marketing.")
            # Conectar a MySQL
            connection = conectar_mysql()
            # Exportar datos de ventas a MySQL
            exportar_ventas_a_mysql(ventas, connection)
            # Cerrar conexión a MySQL
            cerrar_conexion_mysql(connection)
        else:
            print("Error: Opción no válida.")


def pedir_datos_usuario(usuarios, num_usuarios):
    usuario = Usuario()
    usuario.nombre = input("Ingrese el nombre del usuario: ")
    usuario.rol = input("Ingrese el rol del usuario: ")
    usuarios.append(usuario)

def area_sistemas(lista_usuarios):
    op_sistemas = 0

    while op_sistemas != 3:
        print("\nSistemas\n1. Ingresar usuarios\n2. Mostrar usuarios\n3. Salir")
        op_sistemas = int(input("Seleccione una opción: "))

        if op_sistemas == 1:
            # Ingresar usuarios
            num_usuarios = int(input("Ingrese el número de usuarios a registrar: "))
            for _ in range(num_usuarios):
                pedir_datos_usuario(lista_usuarios, len(lista_usuarios))

            print("Usuarios registrados exitosamente.")
        elif op_sistemas == 2:
            # Mostrar usuarios
            print("\nLista de Usuarios:")
            # Conectar a MySQL
            connection = conectar_mysql()
            mostrar_datos_usuarios_desde_mysql(connection)
            # Cerrar conexión a MySQL
            cerrar_conexion_mysql(connection)
            
        elif op_sistemas == 3:
            print("Saliendo del departamento de Sistemas.")
            # Conectar a MySQL
            connection = conectar_mysql()
            # Exportar datos de usuarios a MySQL
            exportar_usuarios_a_mysql(lista_usuarios, connection)
            # Cerrar conexión a MySQL
            cerrar_conexion_mysql(connection)
        else:
            print("Error: Opción no válida.")


def pedir_datos_produccion(produccion, num_producciones):
    produccion_item = Produccion()
    produccion_item.Producto = input("Ingrese el nombre del producto: ")
    produccion_item.Cantidad = int(input("Ingrese la cantidad producida: "))
    produccion_item.FechaProduccion = input("Ingrese la fecha de producción (AAAA-MM-DD): ")
    produccion.append(produccion_item)

#conectar a mysql
def conectar_mysql():
    # Modifica estos valores según la configuración de tu base de datos
    config = {
        'user': 'root',
        'password': 'z',
        'host': 'localhost',
        'database': 'prueba_dos',
        'raise_on_warnings': True
    }

    try:
        connection = mysql.connector.connect(**config)
        print("Conexión a MySQL exitosa.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def cerrar_conexion_mysql(connection):
    if connection:
        connection.close()
        print("Conexión a MySQL cerrada.")

def exportar_empleados_a_mysql(empleados, connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    for empleado in empleados:
        sql = """INSERT INTO empleados (Matricula, Nombre, ApellidoPaterno, ApellidoMaterno, 
                 FechaNacimiento, FechaIngreso, DiasTrabajados, RFC, Departamento, Clase, SDI)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        data = (empleado.Matricula, empleado.Nombre, empleado.ApellidoPaterno, empleado.ApellidoMaterno,
                empleado.FechaNacimiento, empleado.FechaIngreso, empleado.DiasTrabajados, empleado.RFC,
                empleado.Departamento, empleado.Clase, empleado.SDI)

        cursor.execute(sql, data)

    connection.commit()
    cursor.close()

    print("Datos de empleados exportados a MySQL correctamente.")

#Extraer datos
def mostrar_datos_desde_mysql(connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    # Consulta para obtener todos los empleados desde la base de datos
    sql = "SELECT * FROM empleados"
    cursor.execute(sql)

    # Mostrar la información obtenida
    print("\nDatos de empleados extraídos desde MySQL:")
    for row in cursor.fetchall():
        print(row)

    cursor.close()

#Exporta datos en materiales de mysql
def exportar_materiales_a_mysql(materiales, connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    for material in materiales:
        sql = """INSERT INTO materiales (Nombre, costoPieza, NumPieza, costoTotal)
                 VALUES (%s, %s, %s, %s)"""

        data = (material.Nombre, material.costoPieza, material.NumPieza, material.costoTotal)

        cursor.execute(sql, data)

    connection.commit()
    cursor.close()

    print("Datos de materiales exportados a MySQL correctamente.")

def mostrar_datos_materiales_desde_mysql(connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    # Consulta para obtener todos los materiales desde la base de datos
    sql = "SELECT * FROM materiales"
    cursor.execute(sql)

    # Mostrar la información obtenida
    print("\nDatos de materiales extraídos desde MySQL:")
    for row in cursor.fetchall():
        print(row)

    cursor.close()

#Mysql produccion
def exportar_produccion_a_mysql(produccion, connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    for item in produccion:
        sql = """INSERT INTO produccion (Producto, Cantidad, FechaProduccion)
                 VALUES (%s, %s, %s)"""

        data = (item.Producto, item.Cantidad, item.FechaProduccion)

        cursor.execute(sql, data)

    connection.commit()
    cursor.close()

    print("Datos de producción exportados a MySQL correctamente.")

def mostrar_datos_produccion_desde_mysql(connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    # Consulta para obtener todos los registros de producción desde la base de datos
    sql = "SELECT * FROM produccion"
    cursor.execute(sql)

    # Mostrar la información obtenida
    print("\nDatos de producción extraídos desde MySQL:")
    for row in cursor.fetchall():
        print(row)

    cursor.close()

#Mysql marketing
def exportar_ventas_a_mysql(ventas, connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    for venta in ventas:
        sql = """INSERT INTO marketing (Producto, Monto, FechaVenta)
                 VALUES (%s, %s, %s)"""

        data = (venta.Producto, venta.Monto, venta.FechaVenta)

        cursor.execute(sql, data)

    connection.commit()
    cursor.close()

    print("Datos de ventas exportados a MySQL correctamente.")

def mostrar_datos_ventas_desde_mysql(connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    # Consulta para obtener todos los registros de ventas desde la base de datos
    sql = "SELECT * FROM marketing"
    cursor.execute(sql)

    # Mostrar la información obtenida
    print("\nDatos de ventas extraídos desde MySQL:")
    for row in cursor.fetchall():
        print(row)

    cursor.close()

#Mysql sistemas
def exportar_usuarios_a_mysql(usuarios, connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    for usuario in usuarios:
        sql = """INSERT INTO usuarios (Nombre, Rol)
                 VALUES (%s, %s)"""

        data = (usuario.nombre, usuario.rol)

        cursor.execute(sql, data)

    connection.commit()
    cursor.close()

    print("Datos de usuarios exportados a MySQL correctamente.")

def mostrar_datos_usuarios_desde_mysql(connection):
    if not connection:
        print("Error: No se pudo conectar a MySQL.")
        return

    cursor = connection.cursor()

    # Consulta para obtener todos los registros de usuarios desde la base de datos
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)

    # Mostrar la información obtenida
    print("\nDatos de usuarios extraídos desde MySQL:")
    for row in cursor.fetchall():
        print(row)

    cursor.close()


#Codigo principal
def main():
    empleados = []
    materiales = []
    proveedores = []
    clientes = []
    ventas = []
    usuarios = []
    produccion = []

    menu_principal = 0

    while menu_principal != 6:
        print("\nMenú Principal\n1. Departamento de Recursos Humanos\n2. Departamento de Finanzas"
              "\n3. Departamento de Producción\n4. Departamento de Marketing\n5. Departamento de Sistemas\n6. Salir")
        menu_principal = int(input("Seleccione una opción: "))

        if menu_principal == 1:
            # Departamento de Recursos Humanos
            print("\nDepartamento de Recursos Humanos")
            op_rrhh = 0

            while op_rrhh != 5:
                print("\n1.- Ingresar empleado\n2.- Calcular días trabajados\n"
                      "3.- Imprimir tabla de empleados\n4.- Calcular UMA\n5.- Salir")
                op_rrhh = int(input("Seleccione una opción: "))

                if op_rrhh == 1:
                    # Ingresar empleado
                    pedir_datos_empleado(empleados, len(empleados))
                    print("Empleado registrado exitosamente.")
                elif op_rrhh == 2:
                    # Calcular días trabajados
                    calcular_dias_trabajados(empleados)
                    print("Días trabajados calculados exitosamente.")
                elif op_rrhh == 3:
                    # Imprimir tabla de empleados
                    imprimir_tabla_empleados(empleados)
                elif op_rrhh == 4:
                    # Calcular UMA
                    calcular_uma(empleados)
                    imprimir_tabla_uma(empleados)
                elif op_rrhh == 5:
                    print("Saliendo del Departamento de Recursos Humanos.")
                    # Conectar a MySQL
                    connection = conectar_mysql()
                    # Exportar datos de empleados a MySQL
                    exportar_empleados_a_mysql(empleados, connection)
                    # Cerrar conexión a MySQL
                    cerrar_conexion_mysql(connection)

                else:
                    print("Error: Opción no válida.")
        elif menu_principal == 2:
            # Departamento de Finanzas
            print("\nDepartamento de Finanzas")
            op_finanzas = 0

            while op_finanzas != 4:
                print("\n1.- Ingresar materiales\n2.- Ordenar materiales\n"
                      "3.- Imprimir tabla de materiales\n4.- Salir")
                op_finanzas = int(input("Seleccione una opción: "))

                if op_finanzas == 1:
                    # Ingresar materiales
                    materiales = pedir_datos_materiales()
                elif op_finanzas == 2:
                    # Ordenar materiales
                    print("\nOrdenar materiales\n1.- Por nombre\n2.- Por número de piezas\n"
                          "3.- Por costo total")
                    op_ordenar = int(input("Seleccione una opción: "))

                    if op_ordenar == 1:
                        ordenar_datos_n(materiales)
                    elif op_ordenar == 2:
                        ordenar_datos_p(materiales)
                    elif op_ordenar == 3:
                        ordenar_datos_ct(materiales)
                    else:
                        print("Error: Opción no válida.")
                elif op_finanzas == 3:
                    # Imprimir tabla de materiales
                    imprimir_tabla(materiales)
                    # Conectar a MySQL
                    connection = conectar_mysql()
                    mostrar_datos_materiales_desde_mysql(connection)
                    # Cerrar conexión a MySQL
                    cerrar_conexion_mysql(connection)
                elif op_finanzas == 4:
                    print("Saliendo del Departamento de Finanzas.")
                    # Conectar a MySQL
                    connection = conectar_mysql()
                    exportar_materiales_a_mysql(materiales, connection)
                    # Cerrar conexión a MySQL
                    cerrar_conexion_mysql(connection)
                else:
                    print("Error: Opción no válida.")
        elif menu_principal == 3:
            # Departamento de Producción
            print("\nDepartamento de Producción")
            op_produccion = 0

            while op_produccion != 3:
                print("\n1.- Ingresar producción\n2.- Imprimir tabla de producción\n"
                      "3.- Salir")
                op_produccion = int(input("Seleccione una opción: "))

                if op_produccion == 1:
                    # Ingresar producción
                    pedir_datos_produccion(produccion, len(produccion))
                    print("Producción registrada exitosamente.")
                elif op_produccion == 2:
                    # Imprimir tabla de producción
                    # (Esto mostrará tanto los datos en memoria como los almacenados en MySQL)
                    connection = conectar_mysql()
                    mostrar_datos_produccion_desde_mysql(connection)
                    cerrar_conexion_mysql(connection)
                elif op_produccion == 3:
                    print("Saliendo del Departamento de Producción.")
                    # Exportar producción a MySQL
                    connection = conectar_mysql()
                    exportar_produccion_a_mysql(produccion, connection)
                    cerrar_conexion_mysql(connection)
                else:
                    print("Error: Opción no válida.")

        elif menu_principal == 4:
            # Departamento de Marketing
            print("\nDepartamento de Marketing")
            marketing(3, 10, ventas)
        elif menu_principal == 5:
            # Departamento de Sistemas
            print("\nDepartamento de Sistemas")
            area_sistemas(usuarios)
        elif menu_principal == 6:
            print("Saliendo del sistema.")
        else:
            print("Error: Opción no válida.")

if __name__ == "__main__":
    main()