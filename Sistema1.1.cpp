#include <iostream>
#include <string>
#include <ctime>
#include <iomanip>
#include <vector>
#include <cstdlib>
using namespace std;
struct Empleados{
	string Nombre;
	string ApellidoPaterno;
	string ApellidoMaterno;
	string FechaNacimiento;
	string FechaIngreso;
	int DiasTrabajados;
	string Matricula;
	string RFC;
	string Departamento;
	float PDO;
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
	int clase;
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
// Declaración de funciones
void Pedir_Datos(Empleados empleados[], int numEmpleados);
void GenerarMatricula(Empleados &empleados);
void GenerarRFC(Empleados &empleados);
void CalcularDiasTrabajados(Empleados empleados[], int numEmpleados);
void ImprimirTabla(Empleados empleados[], int numEmpleados);
void Finanzas();
void Finanzas_proveedores(vector<Finanzas_Proveedor>& listaProveedores);
void Finanzas_clientes(vector<Finanzas_Cliente>& listaClientes);
void Finanzas_imprimir_tabla(const vector<Finanzas_Proveedor>& proveedores, const vector<Finanzas_Cliente>& clientes);
int main() {
	const int MAX_EMPLEADOS = 100;
	Empleados empleado[MAX_EMPLEADOS];
	int numEmpleados = 0;
	int op, op1;
	char Respuesta = 'S';
	srand(time(0)); // Sembrar la semilla del generador de números aleatorios
	do {
		cout << "1. Recursos Humanos\n2. Produccion\n3. Finanzas\n4. Marketing\n5. Sistemas\n6. Salir" << endl;
		cout << "Seleccione una opción: ";
		cin >> op;
		switch (op) {
			case 1:
				do {
					cout << "\n1. Ingresar usuario\n2. Mostrar Tabla\n3. Salir" << endl;
					cout << "Seleccione una opción: ";
					cin >> op1;
					cin.ignore(); // Limpiar el buffer del teclado
					switch (op1) {
						case 1:
							while (Respuesta == 's' || Respuesta == 'S') {
								Pedir_Datos(empleado, numEmpleados);
								numEmpleados++;
								cout << "¿Desea ingresar otro empleado? (S/N): ";
								cin >> Respuesta;
								cin.ignore(); // Limpiar el buffer del teclado
							}
							break;
						case 2:
							CalcularDiasTrabajados(empleado, numEmpleados);
							ImprimirTabla(empleado, numEmpleados);
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
				Finanzas();
				break;
			case 4:
				cout << "Opción para Marketing." << endl;
				break;
			case 5:
				cout << "Opción para Sistemas." << endl;
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
// Resto de las funciones

void Pedir_Datos(Empleados empleados[], int numEmpleados) {
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
	GenerarMatricula(empleados[numEmpleados]);
	GenerarRFC(empleados[numEmpleados]);
}
void GenerarMatricula(Empleados &empleados) {
	empleados.Matricula = to_string(rand() % 100000);
}
void GenerarRFC(Empleados &empleados) {
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
void Finanzas() {
	int menu_Finanzas;
	vector<Finanzas_Proveedor> listaProveedores;
	vector<Finanzas_Cliente> listaClientes;
	do {
		cout << "\nFinanzas\n1.- Proveedores\n2.- Clientes\n3.- Imprimir tabla\n4.- Salir\n";
		cin >> menu_Finanzas;

		switch (menu_Finanzas) {
			case 1:
				Finanzas_proveedores(listaProveedores);
				break;
			case 2:
				Finanzas_clientes(listaClientes);
				break;
			case 3:
				Finanzas_imprimir_tabla(listaProveedores, listaClientes);
				break;
			case 4:
				cout << "Saliendo de Finanzas";
				break;
			default:
				cout << "Introduzca una opción válida";
				break;
		}
	} while (menu_Finanzas != 4);
}
void Finanzas_proveedores(vector<Finanzas_Proveedor>& listaProveedores) {
	int num_proveedores;
	cout << "¿Cuántos proveedores desea ingresar?: ";
	cin >> num_proveedores;

	srand(time(0));

	for (int i = 0; i < num_proveedores; i++) {
		Finanzas_Proveedor proveedor;
		proveedor.num_Proveedor = rand() % 90000 + 10000;

		cout << "Nombre: ";
		cin.ignore();
		getline(cin, proveedor.nombre);

		cout << "Telefono: ";
		getline(cin, proveedor.telefono);

		cout << "Compañía: ";
		getline(cin, proveedor.compania);

		listaProveedores.push_back(proveedor);
	}
}
void Finanzas_clientes(vector<Finanzas_Cliente>& listaClientes) {
	int num_Clientes;
	cout << "¿Cuántos clientes desea ingresar?: ";
	cin >> num_Clientes;

	srand(time(0));

	for (int i = 0; i < num_Clientes; i++) {
		Finanzas_Cliente cliente;
		cliente.num_Cliente = rand() % 90000 + 10000;

		cout << "Nombre: ";
		cin.ignore();
		getline(cin, cliente.nombre);

		cout << "Telefono: ";
		getline(cin, cliente.telefono);

		listaClientes.push_back(cliente);
	}
}
void Finanzas_imprimir_tabla(const vector<Finanzas_Proveedor>& proveedores, const vector<Finanzas_Cliente>& clientes) {
	cout << "\nDatos de los proveedores ingresados:\n";
	for (int i = 0; i < proveedores.size(); i++) {
		cout << "Proveedor " << i + 1 << ":\n";
		cout << "No proveedor: " << proveedores[i].num_Proveedor << "\n";
		cout << "Nombre: " << proveedores[i].nombre << "\n";
		cout << "Telefono: " << proveedores[i].telefono << "\n";
		cout << "Compañía: " << proveedores[i].compania << "\n\n";
	}
	cout << "\nDatos de los clientes ingresados:\n";
	for (int i = 0; i < clientes.size(); i++) {
		cout << "Cliente " << i + 1 << ":\n";
		cout << "No cliente: " << clientes[i].num_Cliente << "\n";
		cout << "Nombre: " << clientes[i].nombre << "\n";
		cout << "Telefono: " << clientes[i].telefono << "\n";
	}
}
