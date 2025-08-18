#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define KGRN "\x1B[32m"
#define KRED  "\x1B[31m"

int main() {
	srand(time(NULL));
	int randnum = rand() % 3;
	const char *messages[] = {
        	"Knock knock, the one.",
        	"Follow the white rabbit.",
		"Wake up, Neo."
	};
	const char *msg = messages[randnum];
	int randnum2 = rand() % 101;
	if (randnum2 == 2) {
		const char *sussymsg = "Skibidi toilet.";
	 	for (int i = 0; sussymsg[i] != '\0'; i++) {
			printf("%s%c", KRED, sussymsg[i]);
        		fflush(stdout);
        		usleep(300000);
		}
		usleep(200000);
		system("cat /dev/random");
	}
	else {
		for (int i = 0; msg[i] != '\0'; i++) {
			printf("%s%c", KGRN, msg[i]);
        		fflush(stdout);
        		usleep(130000);
    		}
	}
	printf("\n");
	return 0;
}
