#include <stdio.h>
#include <unistd.h>
#define KGRN "\x1B[32m"

int main() {
    char msg[] = "Knock knock, the one.";
    for (int i = 0; msg[i] != '\0'; i++) {
        printf("%s%c", KGRN, msg[i]);
        fflush(stdout);
        usleep(80000);
    }
    printf("\n");
    return 0;
}
