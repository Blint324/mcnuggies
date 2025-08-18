#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define KGRN "\x1B[32m"

int main() {
    srand(time(NULL));
    int randnum = rand() % 3;
    const char *messages[] = {
        "Knock knock, the one.",
        "Follow the white rabbit.",
        "Wake up, Neo."
    };
    const char *msg = messages[randnum];
    for (int i = 0; msg[i] != '\0'; i++) {
        printf("%s%c", KGRN, msg[i]);
        fflush(stdout);
        usleep(130000);
    }
    printf("\n");
    return 0;
}
