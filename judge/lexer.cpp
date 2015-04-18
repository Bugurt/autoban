#include "lexer.h"

using namespace std;

Lexer::Lexer(string comment) {
	this->mComment = comment;
	this->mCurrentPosition = 0;
}

Lexer::~Lexer() { }

vector<string> GetLexems() {

}
