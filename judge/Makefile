CC=g++

CFLAGS=-c -Wall
LDFLAGS=

SOURCES=comment.cpp lexer.cpp main.cpp
OBJECTS=$(SOURCES:.cpp=.o)

EXECUTABLE=judge

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
	
post:
	@rm -rf *.o

clean: post
	@if [ -a $(EXECUTABLE) ] ; then rm $(EXECUTABLE); fi;
		
	@echo Cleaned
	
launch: all post
	@echo Launching..
	./$(EXECUTABLE)
