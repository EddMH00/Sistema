#include <iostream>
#include <string>
#include <ctime>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <algorithm> // Se añade la librería para utilizar std::sort(duda)
using namespace std;

// Área de Estructuras
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
    float FI;
    float SDI;
    float CuotaFija;
    float PDpat;
    float PDobr;
    float GPMpat;
    float GMPobr;
    float RT;
    float IVpat;
    float IVobr;
    float GPS;
    float Patron;
    float Obrero;
    float Total;
    int Clase;
    float DiasAguinaldo;
};

struct Finanzas_Proveedor {
    int num_Proveedor;
    string nombre;
    string telefono;
    string compania;
};

struct Finanzas_Cliente {
    int num_Cliente;
    string nombre;
    string telefono;
};

struct Material {
    string Nombre;
    float costoPieza;
    int NumPieza;
    float costoTotal;
};

// Variables Globales
int n;
Material* arr;

// Declaración de funciones
void PedirDatosMateriales();
void OrdenarDatosN(Material* arr, int n);
void OrdenarDatosP(Material* arr, int n);
void OrdenarDatosCT(Material* arr, int n);
void ImprimirTabla(Material* arr, int n);
void PedirDatosEmpleado(Empleados empleados[], int numEmpleados);
void GenerarMatricula(Empleados& empleados);
void GenerarRFC(Empleados& empleados);
void CalcularDiasTrabajados(Empleados empleados[], int numEmpleados);
void ImprimirTablaEmpleados(Empleados empleados[], int numEmpleados);
void Finanzas();
void IngresarProveedores(vector<Finanzas_Proveedor>& listaProveedores);
void IngresarClientes(vector<Finanzas_Cliente>& listaClientes);
void ImprimirTablaFinanzas(const vector<Finanzas_Proveedor>& proveedores, const vector<Finanzas_Cliente>& clientes);
void CalcularUMA(Empleados empleados[], int numEmpleados);
void ImprimirTablaUMA(Empleados empleados[], int numEmpleados);

// Parte Principal del programa
int main() {
    const int MAX_EMPLEADOS = 100;
    Empleados empleado[MAX_EMPLEADOS];
    int numEmpleados = 0;
    int op, op1, op2; // Opciones para Switch Case
    char Respuesta = 'S'; // Condición de inicio del while
    srand(time(0)); // Sembrar la semilla del generador de números aleatorios

    do {
        cout << "1. Recursos Humanos\n2. Produccion\n3. Finanzas\n4. Marketing\n5. Sistemas\n6. Salir" << endl;
        cout << "Seleccione una opción: ";
        cin >> op;

        switch (op) {
            case 1:
                do {
                    cout << "\n1. Ingresar empleado\n2. Mostrar Tabla\n3. Tabla UMA\n4. Salir" << endl;
                    cout << "Seleccione una opción: ";
                    cin >> op1;
                    cin.ignore();

                    switch (op1) {
                        case 1:
                            while (Respuesta == 's' || Respuesta == 'S') {
                                PedirDatosEmpleado(empleado, numEmpleados);
                                numEmpleados++;
                                cout << "¿Desea ingresar otro empleado? (S/N): ";
                                cin >> Respuesta;
                                cin.ignore();
                            }
                            break;
                        case 2:
                            CalcularDiasTrabajados(empleado, numEmpleados);
                            ImprimirTablaEmpleados(empleado, numEmpleados);
                            break;
                        case 3:
                            ImprimirTablaUMA(empleado, numEmpleados);
                            break;
                        case 4:
                            cout << "Saliendo del sistema." << endl;
                            break;
                        default:
                            cout << "Error: Opción no válida." << endl;
                            break;
                    }
                } while (op1 != 4);
                break;
            case 2:
                PedirDatosMateriales();
                cout << "Seleccione cómo desea ordenar los datos: " << endl;
                cout << "1. Nombre\n2. Número de materiales\n3. Costo total" << endl;
                cin >> op2;

                switch (op2) {
                    case 1:
                        OrdenarDatosN(arr, n);
                        break;
                    case 2:
                        OrdenarDatosP(arr, n);
                        break;
                    case 3:
                        OrdenarDatosCT(arr, n);
                        break;
                    default:
                        cout << "Error" << endl;
                        break;
                }

                cout << "Tabla: " << endl;
                ImprimirTabla(arr, n);
                delete[] arr; // Borrar la memoria del arreglo dinámico
                break;
            case 3:
                Finanzas();
                break;
            case 4:
                cout << "Opción para Marketing." << endl; // Por empezar
                break;
            case 5:
                cout << "Opción para Sistemas." << endl; // Por empezar
                break;
            case 6:
                cout << "Salir" << endl;
                break;
            default:
                cout << "Error: Opción no válida." << endl;
        }
    } while (op != 6);

    return 0;
}

// Recursos Humanos
void PedirDatosEmpleado(Empleados empleados[], int numEmpleados) {
    cout << "Ingrese el nombre del empleado: ";
    getline(cin, empleados[numEmpleados].Nombre);
    cout << "Ingrese el apellido paterno del empleado: ";
    getline(cin, empleados[numEmpleados].ApellidoPaterno);
    cout << "Ingrese el apellido materno del empleado: ";
    getline(cin, empleados[numEmpleados].ApellidoMaterno);
    cout << "Ingrese la fecha de ingreso (DD/MM/AAAA): ";
    getline(cin, empleados[numEmpleados].FechaIngreso);
    cout << "Ingrese la fecha de nacimiento (DD/MM/AAAA): ";
    getline(cin, empleados[numEmpleados].FechaNacimiento);
    cout << "Ingrese el departamento del empleado: ";
    getline(cin, empleados[numEmpleados].Departamento);
    cout << "1. Clase I\t2. Clase II\t3. Clase III\t4. Clase IV" << endl;
    cout << "Ingrese la Clase del empleado: ";
    cin >> empleados[numEmpleados].Clase;
    GenerarMatricula(empleados[numEmpleados]);
    GenerarRFC(empleados[numEmpleados]);
}

void GenerarMatricula(Empleados& empleados) {
    empleados.Matricula = to_string(rand() % 100000);
}

void GenerarRFC(Empleados& empleados) {
    empleados.RFC = "";
    empleados.RFC += empleados.ApellidoPaterno.substr(0, 2);
    empleados.RFC += empleados.ApellidoMaterno.substr(0, 2);
    empleados.RFC += empleados.Nombre.substr(0, 2);
    empleados.RFC += empleados.FechaNacimiento.substr(0, 2);
    empleados.RFC += empleados.FechaNacimiento.substr(3, 2);
    empleados.RFC += empleados.FechaNacimiento.substr(8, 2);
}

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

        int diasTrabajados = (anioActual - anioIngreso) * 365 + (mesActual - mesIngreso) * 30 + (diaActual - diaIngreso);
        empleados[i].DiasTrabajados = diasTrabajados;
    }
}

void ImprimirTablaEmpleados(Empleados empleados[], int numEmpleados) {
    cout << setw(10) << "Matricula" << setw(20) << "Nombre"
         << setw(20) << "Apellido Paterno" << setw(20) << "Apellido Materno"
         << setw(15) << "RFC" << setw(20) << "Dias Trabajados" << setw(20) << "Departamento" << endl;

    for (int i = 0; i < numEmpleados; ++i) {
        cout << setw(10) << empleados[i].Matricula << setw(20) << empleados[i].Nombre
             << setw(20) << empleados[i].ApellidoPaterno << setw(20) << empleados[i].ApellidoMaterno
             << setw(15) << empleados[i].RFC << setw(20) << empleados[i].DiasTrabajados << setw(20) << empleados[i].Departamento << endl;
    }
}

void CalcularUMA(Empleados empleados[], int numEmpleados) {
    int DiasAnio = 365, DiasMes = 30;
    float Cuota_Fija = 0.204, UMA2023 = 103.74, SDI = 183.32, PDO = 1.5;
    float PDpat = 0.007, PDobr = 0.0025, GPMpat = 0.0105, GPMobr = 0.0035, IVpat = 0.0175, IVobr = 0.00625, GPS = 0.01;

    for (int i = 0; i < numEmpleados; i++) {
        cout << "Empleado: " << empleados[i].Matricula << " " << empleados[i].Nombre << " " << empleados[i].ApellidoPaterno << endl;

        if (empleados[i].DiasTrabajados < 365) {
            empleados[i].DiasAguinaldo = (DiasAnio / 15) * empleados[i].DiasTrabajados;
            empleados[i].FI = (DiasAnio + empleados[i].DiasAguinaldo + PDO) / DiasAnio;
            empleados[i].SDI = empleados[i].FI * SDI;
        } else {
            empleados[i].FI = (DiasAnio + 15 + PDO) / DiasAnio;
            empleados[i].SDI = empleados[i].FI * SDI;
        }

        empleados[i].CuotaFija = Cuota_Fija * DiasMes * UMA2023;
        empleados[i].PDpat = empleados[i].SDI * DiasMes * PDpat;
        empleados[i].PDobr = empleados[i].SDI * DiasMes * PDobr;
        empleados[i].GPMpat = empleados[i].SDI * DiasMes * GPMpat;
        empleados[i].GMPobr = empleados[i].SDI * DiasMes * GPMobr;

        if (empleados[i].Clase == 1) {
            empleados[i].RT = empleados[i].SDI * DiasMes * (0.54355 / 100);
        } else if (empleados[i].Clase == 2) {
            empleados[i].RT = empleados[i].SDI * DiasMes * (1.13065 / 100);
        } else if (empleados[i].Clase == 3) {
            empleados[i].RT = empleados[i].SDI * DiasMes * (2.5984 / 100);
        } else if (empleados[i].Clase == 4) {
            empleados[i].RT = empleados[i].SDI * DiasMes * (4.65325 / 1400);
        } else if (empleados[i].Clase == 5) {
            empleados[i].RT = empleados[i].SDI * DiasMes * (7.58875 / 100);
        }

        empleados[i].IVpat = empleados[i].SDI * DiasMes * IVpat;
        empleados[i].IVobr = empleados[i].SDI * DiasMes * IVobr;
        empleados[i].GPS = empleados[i].SDI * DiasMes * GPS;

        empleados[i].Patron = empleados[i].CuotaFija + empleados[i].PDpat + empleados[i].GPMpat + empleados[i].RT + empleados[i].IVpat + empleados[i].GPS;
        empleados[i].Obrero = empleados[i].PDobr + empleados[i].GMPobr + empleados[i].IVobr;
    }
}

void ImprimirTablaUMA(Empleados empleados[], int numEmpleados) {
    cout << setw(10) << "Matricula" << setw(20) << "Nombre" << setw(20) << "SDI" << setw(20) << "Cuota Fija"
	     << setw(15) << "PDpat" << setw(20) << "PDobr" << setw(20) << "GPMpat" << setw(10) << "GPMobr"
	     << setw(10) << "RT" << setw(10) << "IVpat" << setw(10) << "IVObr" << setw(10) << "Patron" << setw(10) << "Obrero" << endl;

	for (int i = 0; i < numEmpleados; ++i) {
		cout << setw(10) << empleados[i].Matricula << setw(20) << empleados[i].Nombre << setw(20) << empleados[i].SDI << setw(20) << empleados[i].CuotaFija
		     << setw(15) << empleados[i].PDpat << setw(20) << empleados[i].PDobr << setw(20) << empleados[i].GPMpat << setw(10) << empleados[i].GMPobr
		     << setw(10) << empleados[i].RT << setw(10) << empleados[i].IVpat << setw(10) << empleados[i].IVobr << setw(10) << empleados[i].Patron << setw(10) << empleados[i].Obrero << endl;
	}
}

// Produccion
void PedirDatosMateriales() {
    cout << "Ingresa el número de materiales: " << endl;
    cin >> n;
    arr = new Material[n];
    fflush(stdin);

    for (int i = 0; i < n; i++) {
        cout << "[" << i << "]";
        cout << "Ingresa el nombre: " << endl;
        cin >> arr[i].Nombre;
        cout << "Ingresa el número de material: " << endl;
        cin >> arr[i].NumPieza;
        cout << "Ingresa el costo unitario: " << endl;
        cin >> arr[i].costoPieza;
        arr[i].costoTotal = arr[i].costoPieza * arr[i].NumPieza;
        fflush(stdin);
    }
}

void OrdenarDatosN(Material* arr, int n) {
    sort(arr, arr + n, [](const Material& a, const Material& b) {
        return a.Nombre < b.Nombre;
    });
}

void OrdenarDatosP(Material* arr, int n) {
    sort(arr, arr + n, [](const Material& a, const Material& b) {
        return a.NumPieza < b.NumPieza;
    });
}

void OrdenarDatosCT(Material* arr, int n) {
    sort(arr, arr + n, [](const Material& a, const Material& b) {
        return a.costoTotal < b.costoTotal;
    });
}

void ImprimirTabla(Material* arr, int n) {
    cout << setw(10) << "Numero"
         << setw(20) << "Nombre"
         << setw(15) << "Costo/pieza"
         << setw(20) << "Numero de piezas"
         << setw(15) << "Costo total" << endl;

    for (int i = 0; i < n; i++) {
        cout << setw(10) << i
             << setw(20) << arr[i].Nombre
             << setw(15) << arr[i].costoPieza
             << setw(20) << arr[i].NumPieza
             << setw(15) << arr[i].costoTotal << endl;
    }
}

// Finanzas
void Finanzas() {
    int menu_Finanzas;
    vector<Finanzas_Proveedor> listaProveedores;
    vector<Finanzas_Cliente> listaClientes;

    do {
        cout << "\nFinanzas\n1.- Proveedores\n2.- Clientes\n3.- Imprimir tabla\n4.- Salir\n";
        cin >> menu_Finanzas;

        switch (menu_Finanzas) {
            case 1:
                IngresarProveedores(listaProveedores);
                break;
            case 2
            	:
                IngresarClientes(listaClientes);
                break;
            case 3:
                ImprimirTablaFinanzas(listaProveedores, listaClientes);
                break;
            case 4:
                cout << "Saliendo de Finanzas." << endl;
                break;
            default:
                cout << "Error: Opción no válida." << endl;
                break;
        }
    } while (menu_Finanzas != 4);
}

void IngresarProveedores(vector<Finanzas_Proveedor>& listaProveedores) {
    int numProveedores;
    cout << "Ingrese el número de proveedores: ";
    cin >> numProveedores;

    for (int i = 0; i < numProveedores; ++i) {
        Finanzas_Proveedor proveedor;
        cout << "Proveedor #" << i + 1 << ":" << endl;
        cout << "Número de proveedor: ";
        cin >> proveedor.num_Proveedor;
        cout << "Nombre: ";
        cin >> proveedor.nombre;
        cout << "Teléfono: ";
        cin >> proveedor.telefono;
        cout << "Compañía: ";
        cin >> proveedor.compania;

        listaProveedores.push_back(proveedor);
    }
}

void IngresarClientes(vector<Finanzas_Cliente>& listaClientes) {
    int numClientes;
    cout << "Ingrese el número de clientes: ";
    cin >> numClientes;

    for (int i = 0; i < numClientes; ++i) {
        Finanzas_Cliente cliente;
        cout << "Cliente #" << i + 1 << ":" << endl;
        cout << "Número de cliente: ";
        cin >> cliente.num_Cliente;
        cout << "Nombre: ";
        cin >> cliente.nombre;
        cout << "Teléfono: ";
        cin >> cliente.telefono;

        listaClientes.push_back(cliente);
    }
}

void ImprimirTablaFinanzas(const vector<Finanzas_Proveedor>& proveedores, const vector<Finanzas_Cliente>& clientes) {
    cout << "\nTabla de Proveedores:" << endl;
    cout << setw(20) << "Número" << setw(20) << "Nombre" << setw(20) << "Teléfono" << setw(20) << "Compañía" << endl;

    for (const auto& proveedor : proveedores) {
        cout << setw(20) << proveedor.num_Proveedor << setw(20) << proveedor.nombre << setw(20) << proveedor.telefono << setw(20) << proveedor.compania << endl;
    }

    cout << "\nTabla de Clientes:" << endl;
    cout << setw(20) << "Número" << setw(20) << "Nombre" << setw(20) << "Teléfono" << endl;

    for (const auto& cliente : clientes) {
        cout << setw(20) << cliente.num_Cliente << setw(20) << cliente.nombre << setw(20) << cliente.telefono << endl;
    }
}