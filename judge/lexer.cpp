#include "lexer.h"
#include <locale>

using namespace std;

Lexer::Lexer(string comment) {
	this->mComment = comment;
}

Lexer::~Lexer() { }

vector<string> Lexer::getLexems() {
	locale loc;
	vector<string> res(0);

	string newLexem("");

	for (string::iterator it = mComment.begin(); it != mComment.end(); it++) {
		// Is it alphabetic character add letter to word
		if (isalpha(*it, loc)) {
			newLexem += *it;
		} else if (newLexem.size()) { //It isn't alphabetic char and word isn't empty
			res.push_back(newLexem);

			newLexem = string("");
		}
	}

	if (newLexem.size()) {
		res.push_back(newLexem);
	}

	return res;
}
