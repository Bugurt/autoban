#ifndef COMMENT_H
#define COMMENT_H

#include <string>

using namespace std;

class Comment {
public:
	Comment(char *content);
	~Comment();

	// Returns value form 0 to 1 for getting 'bad' level
	float GetRating();

private:
	// Stores original comment string
	string mComment;
};

#endif
