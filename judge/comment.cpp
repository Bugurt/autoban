#include "comment.h"

Comment::Comment(char* comment) {
	this->mComment = string(comment);
}

Comment::~Comment() { }

float Comment::GetRating() {

	return 1.0f;
}
