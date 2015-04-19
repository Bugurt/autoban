#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	char *comment = (char *)"Hello, world";

	// So, there is magic. If I launch it with "./judge"
	// there will be one arg and argv[0] equals to "judge",
	// but if I launch "./judge firstArg" argc == 2 and
	// argv[1] == firstArg. Really strange
	if (argc == 2) {
		comment = argv[1];
	} else if (argc != 1) {
		cout << "Unexpected args count: " << argc << endl;
	}

	return 0;
}
