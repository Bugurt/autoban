#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	char *comment = (char *)"Hello, world";

	if (argc == 2) {
		comment = argv[1];
	} else if (argc != 1) {
		cout << "Unexpected args count: " << argc << endl;
	}

	return 0;
}
