#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	char *comment = (char *)"None";

	if (argc == 1) {
		comment = argv[0];
	}

	cout << comment << endl;

	return 0;
}
