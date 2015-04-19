#ifndef LEXER_H
#define LEXER_H

#include <vector>
#include <string>

using namespace std;

class Lexer {
public:
	Lexer(string comment);
	~Lexer();

	vector<string> getLexems();

private:
	string mComment;
};

#endif
