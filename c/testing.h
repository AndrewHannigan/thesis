#ifndef TESTING_H
#define TESTING_H

int dTest(int N, int d_upper, int d_interval, char *file_name);

int bigTest(int N, int d, char *file_name);

int hopcroftTest(int N, int d, char *file_name);

void basicLaurens(int N, int d, int runForever);

void basicHopcroft(int N, int d, int runForever);

int basicLaurensPersist(int N, int d, char *file_name, FILE *graphFile);

char *getInput(char *prompt, char *userInput, int max);

#endif

