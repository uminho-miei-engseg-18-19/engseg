#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
        char buf[1024];

        if(argc > 1) {
                strncpy(buf, argv[1], 1023);
                buf[1023] = '\0';
                printf("%s", buf);
        }
}
