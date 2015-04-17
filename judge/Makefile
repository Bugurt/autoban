CC=g++

CFLAGS=-c -Wall
LDFLAGS=

SOURCES=main.cpp comment.cpp
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
	@rm $(EXECUTABLE)
	@echo Cleaned
	
launch: all post
	@echo Launching..
	$(ECEXUTABLE)
