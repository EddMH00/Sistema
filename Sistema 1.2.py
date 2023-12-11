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

class Usuario:
    def __init__(self):
        self.nombre = ""
        self.rol = ""

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

def marketing(min_ventas, max_ventas, ventas):
    menu_marketing = 0

    while menu_marketing != 3:
        print("\nMarketing\n1.- Registrar venta\n2.- Mostrar ventas\n3.- Salir")
        menu_marketing = int(input("Seleccione una opción: "))

        if menu_marketing == 1:
            # Registrar venta
            if len(ventas) < max_ventas:
                nueva_venta = Venta()
                nueva_venta.Producto = input("Ingrese el nombre del producto: ")
                nueva_venta.Monto = float(input("Ingrese el monto de la venta: "))

                ventas.append(nueva_venta)
                print("Venta registrada exitosamente.")
            else:
                print("Se alcanzó el número máximo de ventas permitidas.")
        elif menu_marketing == 2:
            # Mostrar ventas
            if len(ventas) >= min_ventas:
                print("\nVentas registradas:")
                for venta in ventas:
                    print(f"Producto: {venta.Producto}, Monto: {venta.Monto}")
            else:
                print(f"Se requiere un mínimo de {min_ventas} ventas para mostrar el historial.")
        elif menu_marketing == 3:
            print("Saliendo del departamento de Marketing.")
        else:
            print("Error: Opción no válida.")

def area_sistemas(lista_usuarios):
    op_sistemas = 0

    while op_sistemas != 3:
        print("\nSistemas\n1. Ingresar usuarios\n2. Mostrar usuarios\n3. Salir")
        op_sistemas = int(input("Seleccione una opción: "))

        if op_sistemas == 1:
            # Ingresar usuarios
            num_usuarios = int(input("Ingrese el número de usuarios a registrar: "))
            for _ in range(num_usuarios):
                usuario = Usuario()
                usuario.nombre = input("Ingrese el nombre del usuario: ")
                usuario.rol = input("Ingrese el rol del usuario: ")
                lista_usuarios.append(usuario)

            print("Usuarios registrados exitosamente.")
        elif op_sistemas == 2:
            # Mostrar usuarios
            if lista_usuarios:
                print("\nLista de Usuarios:")
                for usuario in lista_usuarios:
                    print(f"Nombre: {usuario.nombre}, Rol: {usuario.rol}")
            else:
                print("No hay usuarios registrados.")
        elif op_sistemas == 3:
            print("Saliendo del departamento de Sistemas.")
        else:
            print("Error: Opción no válida.")

#conectar a mysql
def conectar_mysql():
    # Modifica estos valores según la configuración de tu base de datos
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'nombre_de_tu_base_de_datos',
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

#Codigo principal
def main():
    empleados = []
    materiales = []
    proveedores = []
    clientes = []
    ventas = []
    usuarios = []

    menu_principal = 0

    while menu_principal != 7:
        print("\nMenú Principal\n1. Departamento de Recursos Humanos\n2. Departamento de Finanzas"
              "\n3. Departamento de Producción\n4. Departamento de Compras\n5. Departamento de Ventas"
              "\n6. Departamento de Sistemas\n7. Salir")
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
                elif op_finanzas == 4:
                    print("Saliendo del Departamento de Finanzas.")
                else:
                    print("Error: Opción no válida.")
        elif menu_principal == 3:
            # Departamento de Producción
            print("\nDepartamento de Producción")
            print("Funcionalidad no implementada.")
        elif menu_principal == 4:
            # Departamento de Compras
            print("\nDepartamento de Compras")
            print("Funcionalidad no implementada.")
        elif menu_principal == 5:
            # Departamento de Ventas
            print("\nDepartamento de Ventas")
            marketing(3, 10, ventas)
        elif menu_principal == 6:
            # Departamento de Sistemas
            print("\nDepartamento de Sistemas")
            area_sistemas(usuarios)
        elif menu_principal == 7:
            print("Saliendo del sistema.")
        else:
            print("Error: Opción no válida.")
    
    # Conectar a MySQL
    connection = conectar_mysql()

    # Exportar datos de empleados a MySQL
    exportar_empleados_a_mysql(empleados, connection)

    # Cerrar conexión a MySQL
    cerrar_conexion_mysql(connection)

if __name__ == "__main__":
    main()