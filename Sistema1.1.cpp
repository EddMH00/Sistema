#include <iostream>
#include <string>
#include <ctime>
#include <iomanip>
#include <vector>
#include <cstdlib>
using namespace std;
//area de Estructuras
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
//variables Globales
int n;
Material *arr;
// Declaración de funciones
void PedirDatos();
void OrdenarDatosN(Material *arr, int n);
void OrdenarDatosP(Material *arr, int n);
void OrdenarDatosCT(Material *arr, int n);
void imprimirTabla(Material *arr, int n);
void Pedir_Datos(Empleados empleados[], int numEmpleados);
void GenerarMatricula(Empleados &empleados);
void GenerarRFC(Empleados &empleados);
void CalcularDiasTrabajados(Empleados empleados[], int numEmpleados);
void ImprimirTabla(Empleados empleados[], int numEmpleados);
void Finanzas();
void Finanzas_proveedores(vector<Finanzas_Proveedor>& listaProveedores);
void Finanzas_clientes(vector<Finanzas_Cliente>& listaClientes);
void Finanzas_imprimir_tabla(const vector<Finanzas_Proveedor>& proveedores, const vector<Finanzas_Cliente>& clientes);
void CalculoUMA(Empleados empleados[], int numEmpleados);
void TablaUMA(Empleados empleados[], int numEmpleados);
//Parte Principal del programa
int main() {
	const int MAX_EMPLEADOS = 100;
	Empleados empleado[MAX_EMPLEADOS];
	int numEmpleados = 0;
	int op, op1, op2;//opciones para Switch Case:
	char Respuesta = 'S'; // condicion de inicio del while
	srand(time(0)); // Sembrar la semilla del generador de números aleatorios
	do {//condicion de cumplimiento
		cout << "1. Recursos Humanos\n2. Produccion\n3. Finanzas\n4. Marketing\n5. Sistemas\n6. Salir" << endl;
		cout << "Seleccione una opción: ";
		cin >> op;
		//primer switch para ingresar a los departamentos
		switch (op) {
			case 1:
				do {
					cout << "\n1. Ingresar usuario\n2. Mostrar Tabla\n3. Tabla UMA \n4. Salir" << endl;
					cout << "Seleccione una opción: ";
					cin >> op1;
					cin.ignore(); // Limpiar el buffer del teclado
					//switch para Recursos humanos
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
							TablaUMA(empleado, numEmpleados);
							break;
						case 4:
							cout << "Saliendo del sistema." << endl;
							break;
						default:
							cout << "Error: Opción no válida." << endl;
							break;
					}
				} while (op1 != 4); //condicion para continuaro salir del programa
				break;
			case 2:
				PedirDatos();
				cout<<"Seleccione como desea ordenar los datos: "<<endl;
				cout<<"1.Nombre\n "<<"2.Numero de materiales\n"<<"3.Costo total"<<endl;
				cin>>op2;
				switch(op2) {
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
						cout<<"Error"<<endl;
						break;
				}
				cout<<"tabla: "<<endl;
				imprimirTabla(arr, n);
				delete[] arr;//borrar la memeoria del arreglo Dinamico
				break;
			case 3: //Area de Finanzas
				Finanzas();
				break;
			case 4:
				cout << "Opción para Marketing." << endl;//Por empezar
				break;
			case 5:
				cout << "Opción para Sistemas." << endl;//Por empezar
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
//Recursos Humanos
// Pedir Datos De empleado
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
	cout << "1. Clase I\t2. Clase II\t3.Clase III\t4. Clase IV"<<endl;
	cout << "Ingrese la Clase del empleado: ";
	cin>>empleados[numEmpleados].Clase;
	GenerarMatricula(empleados[numEmpleados]);
	GenerarRFC(empleados[numEmpleados]);
}
//Generar matricula de forma aleatoria
void GenerarMatricula(Empleados &empleados) {
	empleados.Matricula = to_string(rand() % 100000);
}
//Generar RFC con los datos de los empleados
void GenerarRFC(Empleados &empleados) {
	empleados.RFC = "";
	empleados.RFC += empleados.ApellidoPaterno.substr(0, 2);
	empleados.RFC += empleados.ApellidoMaterno.substr(0, 2);
	empleados.RFC += empleados.Nombre.substr(0, 2);
	empleados.RFC += empleados.FechaNacimiento.substr(0, 2);
	empleados.RFC += empleados.FechaNacimiento.substr(3, 2);
	empleados.RFC += empleados.FechaNacimiento.substr(8, 2);
}
//Dias Trabajdos de los empleadoas desde la fecha de inicio
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
//Tabla de Empleados
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
//Finanzas
//Funcion Principal de Finanzas
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
//ingresar datos de proveedores
void Finanzas_proveedores(vector<Finanzas_Proveedor>& listaProveedores) {
	int num_proveedores;
	cout << "¿Cuántos proveedores desea ingresar?: ";
	cin >> num_proveedores;
	srand(time(0));
	for (int i = 0; i < num_proveedores;) {
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
//Ingresar datos de clientes
void Finanzas_clientes(vector<Finanzas_Cliente>& listaClientes) {
	int num_Clientes;
	cout << "¿Cuántos clientes desea ingresar?: ";
	cin >> num_Clientes;
	srand(time(0));
	for (int i = 0; i <
	        num_Clientes; i++) {
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
//Tabla de finanzas
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
//Recursos Humanos
//Calculo UMA
void CalculoUMA(Empleados empleados[], int numEmpleados) {
	int DiasAnio = 365, DiasMes = 30;
	float Cuota_Fija=0.204, UMA2023 = 103.74, SDI = 183.32, PDO = 1.5;
	float PDpat=0.007, PDobr=0.0025, GPMpat=0.0105, GPMobr=0.0035, IVpat = 0.0175, IVobr=0.00625, GPS = 0.01;
	for(int i = 0; i<numEmpleados; i++) {
		cout<<"Empleado: "<<empleados[i].Matricula<< " " <<empleados[i].Nombre<<" "<<empleados[i].ApellidoPaterno[i]<<endl;
		if(empleados[i].DiasTrabajados<365) {
			empleados[i].DiasAguinaldo = (DiasAnio/15)*empleados[i].DiasTrabajados;
			empleados[i].FI = (DiasAnio + empleados[i].DiasAguinaldo + PDO)/DiasAnio;
			empleados[i].SDI =  empleados[i].FI * SDI;
			empleados[i].CuotaFija = Cuota_Fija * DiasMes * UMA2023;
			empleados[i].PDpat = empleados[i].SDI * DiasMes * PDpat;
			empleados[i].PDobr = empleados[i].SDI * DiasMes * PDobr;
			empleados[i].GPMpat = empleados[i].SDI * DiasMes * GPMpat;
			empleados[i].GMPobr = empleados[i].SDI * DiasMes * GPMobr;
			if(empleados[i].Clase == 1) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (0.54355/100);
			} else if(empleados[i].Clase == 2) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (1.13065/100);
			} else if(empleados[i].Clase == 3) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (2.59840/100);
			} else if(empleados[i].Clase == 4) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (4.65325/1400);
			} else if(empleados[i].Clase == 5) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (7.58875/100);
			}
			empleados[i].IVpat = empleados[i].SDI * DiasMes * IVpat;
			empleados[i].IVobr = empleados[i].SDI * DiasMes * IVobr;
			empleados[i].GPS = empleados[i].SDI * DiasMes * GPS;
			empleados[i].Patron = empleados[i].CuotaFija + empleados[i].PDpat + empleados[i].GPMpat + empleados[i].RT + empleados[i].IVpat + empleados[i].GPS;
			empleados[i].Obrero = empleados[i].PDobr + empleados[i].GMPobr + empleados[i].IVobr;
		} else {
			empleados[i].FI = (DiasAnio + 15 + PDO)/DiasAnio;
			empleados[i].SDI =  empleados[i].FI * SDI;
			empleados[i].CuotaFija = Cuota_Fija * DiasMes * UMA2023;
			empleados[i].PDpat = empleados[i].SDI * DiasMes * PDpat;
			empleados[i].PDobr = empleados[i].SDI * DiasMes * PDobr;
			empleados[i].GPMpat = empleados[i].SDI * DiasMes * GPMpat;
			empleados[i].GMPobr = empleados[i].SDI * DiasMes * GPMobr;
			if(empleados[i].Clase == 1) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (0.54355/100);
			} else if(empleados[i].Clase == 2) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (1.13065/100);
			} else if(empleados[i].Clase == 3) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (2.59840/100);
			} else if(empleados[i].Clase == 4) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (4.65325/1400);
			} else if(empleados[i].Clase == 5) {
				empleados[i].RT = empleados[i].SDI * DiasMes * (7.58875/100);
			}
			empleados[i].IVpat = empleados[i].SDI * DiasMes * IVpat;
			empleados[i].IVobr = empleados[i].SDI * DiasMes * IVobr;
			empleados[i].GPS = empleados[i].SDI * DiasMes * GPS;
			empleados[i].Patron = empleados[i].CuotaFija + empleados[i].PDpat + empleados[i].GPMpat + empleados[i].RT + empleados[i].IVpat + empleados[i].GPS;
			empleados[i].Obrero = empleados[i].PDobr + empleados[i].GMPobr + empleados[i].IVobr;
		}
	}
}
//Imprimir Tabla UMA
void TablaUMA(Empleados empleados[], int numEmpleados) {
	cout << setw(10) << "Matricula" << setw(20) << "Nombre" << setw(20) << "SDI" << setw(20) << "Cuota Fija"
	     << setw(15) << "PDpat" << setw(20) << "PDobr" << setw(20) << "GPMpat" << setw(10) << "GPMobr"
	     << setw(10) << "RT" << setw(10) << "IVpat" << setw(10) << "IVObr" << setw(10) << "Patron" << setw(10) << "Obrero" << endl;

	for (int i = 0; i < numEmpleados; ++i) {
		cout << setw(10) << empleados[i].Matricula << setw(20) << empleados[i].Nombre << setw(20) << empleados[i].SDI << setw(20) << empleados[i].CuotaFija
		     << setw(15) << empleados[i].PDpat << setw(20) << empleados[i].PDobr << setw(20) << empleados[i].GPMpat << setw(10) << empleados[i].GMPobr
		     << setw(10) << empleados[i].RT << setw(10) << empleados[i].IVpat << setw(10) << empleados[i].IVobr << setw(10) << empleados[i].Patron << setw(10) << empleados[i].Obrero << endl;
	}
}
//Produccion
//Pedir Datos
void PedirDatos() {
	cout<<"ingresa el numero de materiales:"<<endl;
	cin>>n;
	arr = new Material[n];
	fflush(stdin);
	for (int i=0; i<n; i++) {
		cout<<"["<<i<<"]";
		cout<<"ingresa el nombre: "<<endl;
		cin>> arr[i].Nombre;
		cout<<"ingresa el numero de material: "<<endl;
		cin>> arr[i].NumPieza;
		cout<<"ingresa el costo unitario: "<<endl;
		cin>>arr[i].costoPieza;
		arr[i].costoTotal=arr[i].costoPieza*arr[i].NumPieza;
		fflush(stdin);
	}
}
//ordenar por nombre
void OrdenarDatosN(Material *arr, int n) {
	for(int i=0; i<n-1; i++) {
		for(int j=0; j<n-i-1; j++) {
			if(arr[j].Nombre > arr[j+1].Nombre) {
				Material aux = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = aux;
			}
		}
	}
}
//ordenar por numero de piezas
void OrdenarDatosP(Material *arr, int n) {
	for(int i=0; i<n-1; i++) {
		for(int j=0; j<n-i-1; j++) {
			if(arr[j].NumPieza > arr[j+1].NumPieza) {
				Material aux = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = aux;
			}
		}
	}
}
//ordenar datos por costo total
void OrdenarDatosCT(Material *arr, int n) {
	for(int i=0; i<n-1; i++) {
		for(int j=0; j<n-i-1; j++) {
			if(arr[j].costoTotal > arr[j+1].costoTotal) {
				Material aux = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = aux;
			}
		}
	}
}
//arreglar tabla
void imprimirTabla(Material *arr, int n) {
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
