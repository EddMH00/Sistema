#include<iostream>
#include<cstdlib>
#include<ctime>
#include<string>
#include <iomanip>
using namespace std;
//Esctructura de Datos de Usuario
struct Empleados {
    string Nombre;
    string ApellidoPaterno;
    string ApellidoMaterno;
    string FechaNacimiento;
    string FechaIngreso;
    int DiasTrabajados;
    string Matricula;
    string RFC;
    string Departamento;
};
//Crear numero Matricula de forma aleatoria
void GenerarMatricula(Empleados &empleados) {
    srand(time(0));
    empleados.Matricula = to_string(rand() % 10000);//crea un numero aleatorio entre 0 y 100000 y Se almacena en un arreglo
}
//Crear RFC
void GenerarRFC(Empleados &empleados) {
    empleados.RFC = "";//Asegurar que la cadena esta vacia
    empleados.RFC += empleados.ApellidoPaterno.substr(0, 2);
    empleados.RFC += empleados.ApellidoMaterno.substr(0, 2);
    empleados.RFC += empleados.Nombre.substr(0, 2);
    empleados.RFC += empleados.FechaNacimiento.substr(0, 2);
    empleados.RFC += empleados.FechaNacimiento.substr(3, 2);
    empleados.RFC += empleados.FechaNacimiento.substr(6, 2);
}
//Dias Trabajdos
void CalcularDiasTrabajados(Empleados empleados[], int numEmpleados) {
    time_t now = time(0);
    tm* fechaActual = localtime(&now);
    int diaActual = fechaActual->tm_mday;
    int mesActual = fechaActual->tm_mon + 1;
    int anioActual = fechaActual->tm_year + 1900;

    for (int i = 0; i < numEmpleados; ++i) {
        int diaIngreso = stoi(empleados[i].FechaIngreso.substr(0, 2));
        int mesIngreso = stoi(empleados[i].FechaIngreso.substr(3, 2));
        int anioIngreso = stoi(empleados[i].FechaIngreso.substr(6, 4));
        int diasTrabajados = 0;
        diasTrabajados = (anioActual - anioIngreso) * 365 + (mesActual - mesIngreso) * 30 + (diaActual - diaIngreso);
        empleados[i].DiasTrabajados = diasTrabajados;
    }
}
//imprimir Tabla
void ImprimirTabla(Empleados empleados[], int numEmpleados) {
    cout << setw(10) << "Matricula" << setw(20) << "Nombre"
         << setw(20) << "Apellido Paterno" << setw(20) << "Apellido Materno" 
         << setw(15) << "RFC" << setw(20) << "Dias Trabajados" << setw(20) << "Departamento" << endl;

    for (int i = 0; i < numEmpleados; ++i) {
        cout << setw(10) << empleados[i].Matricula << setw(20) << empleados[i].Nombre
             << setw(20) << empleados[i].ApellidoPaterno << setw(20) << empleados[i].ApellidoMaterno
             << setw(15) << empleados[i].RFC << setw(20) << empleados[i].DiasTrabajados << setw(20) << empleados[i].Departamento << endl;
    }
}

int main() {
    const int MAX_EMPLEADOS = 100;
    Empleados empleado[MAX_EMPLEADOS];
    int numEmpleados = 0;
    int op, op1;

    do {
        cout << "1. Recursos Humanos \n2. Produccion \n3. Finanzas \n4. Salir" << endl;
        cin >> op;

        switch (op) {
            case 1:
                do {
                    cout << "1. Ingresar usuario \n2. Mostrar Tabla \n3. Salir" << endl;
                    cin >> op1; fflush(stdin);
                    switch (op1) {
                        case 1:
                            char Respuesta = 'S';
                            fflush(stdin); // Limpiar el buffer del teclado
                            while (Respuesta == 's' || Respuesta == 'S') {
                                cout << "Ingrese el nombre del empleado: ";
                                getline(cin, empleado[numEmpleados].Nombre);
                                cout << "Ingrese el apellido paterno del empleado: ";
                                getline(cin, empleado[numEmpleados].ApellidoPaterno);
                                cout << "Ingrese el apellido materno del empleado: ";
                                getline(cin, empleado[numEmpleados].ApellidoMaterno);
                                cout << "Ingrese la fecha de ingreso (DD/MM/AAAA): ";
                                getline(cin, empleado[numEmpleados].FechaIngreso);
                                cout << "Ingrese la fecha de nacimiento (DD/MM/YYYY): ";
                                getline(cin, empleado[numEmpleados].FechaNacimiento);
                                cout << "Ingrese el departamento del empleado: ";
                                getline(cin, empleado[numEmpleados].Departamento);
                                GenerarMatricula(empleado[numEmpleados]);
                                GenerarRFC(empleado[numEmpleados]);
                                numEmpleados++;
                                cout << "¿Desea ingresar otro empleado? (S/N): ";
                                cin >> Respuesta;
                                fflush(stdin); // Limpiar el buffer del teclado
                            }
                            break;
                        case 2:
                            ImprimirTabla(empleado[], numEmpleados);
                            break;
                        case 3:
                            cout << "Saliendo del sistema." << endl;
                            break;
                        default:
                            cout << "Error: Opción no válida." << endl;
                            break;
                    }
                } while (op1 != 3);
                break;
            case 2:
                cout << "Opción para Producción." << endl;
                break;
            case 3:
                cout << "Opción para Finanzas." << endl;
                break;
            case 4:
                cout << "Opcion para Marketing" << endl;
                break;
            case 5:
            	cout<<"Opcion para Sistemas" <<endl;
            	break;
            case 6:
            	cout << "Salir" << endl;
            default:
                cout << "Error: Opción no válida." << endl;
        }
    } while (op != 6);

    return 0;
}
