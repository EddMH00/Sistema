#include<iostream>
#include<cstdlib>
#include<ctime>
#include<string>

using namespace std;

//structura de datos de empleado
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
};

//Generar Matricula
void GenerarMatricula(Empleados &empleados){
	srand(time(0));
	empleados.Matricula = to_string(rand() % 10000 + 10000);
}

//Generar RFC
void GenerarRFC(Empleados &empleados){
	empleados.RFC = "";
	empleados.RFC = empleados.RFC + empleados.ApellidoPaterno.substr(0,2);
	empleados.RFC = empleados.RFC + empleados.ApellidoMaterno.substr(0,2);
	empleados.RFC = empleados.RFC + empleados.Nombre.substr(0,2);
	empleados.RFC = empleados.RFC + empleados.FechaNacimiento.substr(0,2);
	empleados.RFC = empleados.RFC + empleados.FechaNacimiento.substr(3,2);
	empleados.RFC = empleados.RFC + empleados.FechaNacimiento.substr(6,2);
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
        int diasTrabajados = 0;
        diasTrabajados = (anioActual - anioIngreso) * 365 + (mesActual - mesIngreso) * 30 + (diaActual - diaIngreso);
        empleados[i].DiasTrabajados = diasTrabajados;
    }
}

int main(){
	const int MAX_EMPLEADOS = 100;
	Empleados empleado[MAX_EMPLEADOS];
	int numEmpleados = 0;
	
}
