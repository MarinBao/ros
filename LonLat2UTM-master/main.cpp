#include "utm.h"
#include <iostream>
int main() {
	int ReferenceEllipsoid = 23;
	double Lat = 40.3545;
	double Long = 115.3489;
	double UTMNorthing;
	double UTMEasting;
	char *UTMZone = new char[10];
	LLtoUTM(ReferenceEllipsoid, Lat, Long,
		UTMNorthing, UTMEasting, UTMZone);
	double lat, lon;
	UTMtoLL(ReferenceEllipsoid, UTMNorthing, UTMEasting, UTMZone, lat, lon);
	std::cout << "lat, lon via two transform:" << lat << "," << lon << std::endl;
	return 0;
}